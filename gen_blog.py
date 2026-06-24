#!/usr/bin/env python3
"""
Blog generator for the Lawn & Land site.

SINGLE SOURCE OF TRUTH: _blog.json (post metadata + featured image + optional podcast video).
Generates, from the current resources/blog/index.html as the structural template:
  - the paginated blog index            -> /resources/blog/  + /resources/blog/page/N/
  - one hub page per category           -> /resources/blog/category/<slug>/
  - stamps each article's hero media     -> real <img>, or a click-to-play episode video (podcasts)

To add an article: create its article file, add an entry to _blog.json, run:
    python3 gen_blog.py && python3 build.py
Don't hand-edit the generated index / category / pagination pages.
"""
import json, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
PROD = "https://lawnandlandmarketing.com"   # schema uses production domain
STAGE = "https://new.lawnlab.dev"           # canonicals point to staging until launch flip

def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f: return f.read()
def write(p, s):
    full = os.path.join(ROOT, p); os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f: f.write(s)
def H(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")

data = json.load(open(os.path.join(ROOT, "_blog.json"), encoding="utf-8"))
PPP = data["postsPerPage"]; POSTS = data["posts"]; FEAT = data["featured"]; CATS = data["categories"]

FILTERS = """    <div class="blog-filters">
      <button class="blog-filter is-active" data-cat="all">All</button>
      <button class="blog-filter" data-cat="growth-stories">Client Stories</button>
      <button class="blog-filter" data-cat="seo">SEO</button>
      <button class="blog-filter" data-cat="ads-social">Ads &amp; Social</button>
      <button class="blog-filter" data-cat="strategy">Strategy</button>
    </div>"""

PAGINATION_CSS = """
    .blog-pagination{display:flex;align-items:center;justify-content:center;gap:18px;margin:40px auto 6px;font-family:var(--font-l);}
    .blog-pagination a{display:inline-flex;align-items:center;gap:6px;padding:10px 18px;border-radius:999px;border:1px solid var(--card-bd);color:#fff;background:var(--card-bg);font-size:14px;transition:border-color .2s,color .2s;}
    .blog-pagination a:hover{border-color:var(--lime);color:var(--lime);}
    .blog-pagination .blog-page-num{color:var(--muted);font-size:13px;letter-spacing:.04em;}
    .blog-cat-intro{max-width:680px;margin:0 0 6px;color:var(--body);font-size:17px;}
    .blog-cat-back{display:inline-flex;align-items:center;gap:6px;font-family:var(--font-l);font-size:13px;color:var(--muted);margin-bottom:18px;}
    .blog-cat-back:hover{color:var(--lime);}
"""

VID_CSS = """
    .article-hero-img.blog-video{position:relative;cursor:pointer;height:420px;}
    .article-hero-img.blog-video .blog-video-play{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:76px;height:76px;border-radius:50%;background:rgba(7,16,10,.6);border:2px solid rgba(255,255,255,.88);display:flex;align-items:center;justify-content:center;transition:background .2s,transform .2s;}
    .article-hero-img.blog-video:hover .blog-video-play{background:var(--lime);transform:translate(-50%,-50%) scale(1.06);}
    .article-hero-img.blog-video .blog-video-play::after{content:"";margin-left:6px;border-style:solid;border-width:13px 0 13px 22px;border-color:transparent transparent transparent #fff;}
    .article-hero-img.blog-video:hover .blog-video-play::after{border-left-color:#07100a;}
"""

def card(p):
    return ('      <a href="/resources/blog/%s/" class="blog-card" data-cat="%s">\n'
            '        <div class="blog-card-img"><img src="%s" alt="%s" loading="lazy" width="400" height="225"></div>\n'
            '        <div class="blog-card-body">\n'
            '          <span class="blog-card-cat">%s</span>\n'
            '          <h3 class="blog-card-title">%s</h3>\n'
            '          <p class="blog-card-excerpt">%s</p>\n'
            '          <div class="blog-card-meta">\n'
            '            <span class="blog-card-author"><img class="blog-card-avatar" src="/assets/images/matt-author.jpg" alt="" loading="lazy">Matt Foreman</span>\n'
            '            <span class="blog-card-date">%s</span>\n'
            '          </div>\n'
            '        </div>\n'
            '      </a>') % (p["slug"], p["cat"], p["image"], H(p["imageAlt"]), H(p["badge"]),
                            H(p["title"]), H(p["excerpt"]), H(p["dateDisplay"]))

def fcard(f):
    return ('      <a href="%s" class="blog-card" data-cat="%s">\n'
            '        <div class="blog-card-img"><img src="%s" alt="%s" loading="lazy" width="400" height="225"></div>\n'
            '        <div class="blog-card-body">\n'
            '          <span class="blog-card-cat">%s</span>\n'
            '          <h3 class="blog-card-title">%s</h3>\n'
            '          <p class="blog-card-excerpt">%s</p>\n'
            '          <div class="blog-card-meta"><span class="blog-card-cta">%s &rarr;</span></div>\n'
            '        </div>\n'
            '      </a>') % (f["url"], f["cat"], f["image"], H(f["imageAlt"]), H(f["badge"]),
                            H(f["title"]), H(f["excerpt"]), H(f["cta"]))

def pagination(cur, total, baseurl):
    if total <= 1: return ""
    out = ['    <nav class="blog-pagination" aria-label="Blog pages">']
    if cur > 1:
        prev = baseurl if cur == 2 else "%spage/%d/" % (baseurl, cur-1)
        out.append('      <a rel="prev" href="%s">&larr; Newer</a>' % prev)
    out.append('      <span class="blog-page-num">Page %d of %d</span>' % (cur, total))
    if cur < total:
        out.append('      <a rel="next" href="%spage/%d/">Older &rarr;</a>' % (baseurl, cur+1))
    out.append('    </nav>')
    return "\n".join(out)

def section(cards_html, pag_html, lead_html, intro_html=""):
    return ('<section class="blog-index">\n%s\n%s    <div class="blog-grid">\n%s\n    </div>\n%s\n  </section>'
            % (lead_html, intro_html, cards_html, pag_html))

SEC_RE = re.compile(r'<section class="blog-index">.*?</section>', re.S)
def put_section(htmltext, sec): return SEC_RE.sub(lambda m: sec, htmltext, count=1)

def inject(htmltext, css): return htmltext.replace("  </style>", css + "  </style>", 1)

def set_meta(htmltext, title, desc, canon):
    t, d = H(title), H(desc)
    rep = [(r'<title>.*?</title>', '<title>%s</title>' % t),
           (r'(<meta name="description" content=")[^"]*', r'\g<1>'+d),
           (r'(<meta property="og:description" content=")[^"]*', r'\g<1>'+d),
           (r'(<meta name="twitter:description" content=")[^"]*', r'\g<1>'+d),
           (r'(<meta property="og:title" content=")[^"]*', r'\g<1>'+t),
           (r'(<meta name="twitter:title" content=")[^"]*', r'\g<1>'+t),
           (r'(<link rel="canonical" href=")[^"]*', r'\g<1>'+canon),
           (r'(<meta property="og:url" content=")[^"]*', r'\g<1>'+canon)]
    for pat, sub in rep:
        htmltext = re.sub(pat, sub, htmltext, count=1, flags=re.S)
    return htmltext

LD_RE = re.compile(r'<script type="application/ld\+json">\{"@context"[^\n]*?"@type":"(?:Blog|CollectionPage)".*?</script>', re.S)
def set_schema(htmltext, obj):
    s = '<script type="application/ld+json">%s</script>' % json.dumps(obj, ensure_ascii=False)
    return LD_RE.sub(lambda m: s, htmltext, count=1)

def blog_schema(page_posts):
    bp = [{"@type":"BlogPosting","@id":"%s/resources/blog/%s/"%(PROD,p["slug"]),"headline":p["title"],
           "url":"%s/resources/blog/%s/"%(PROD,p["slug"]),"datePublished":p["datePublished"],
           "author":{"@id":"%s/#matt-foreman"%PROD}} for p in page_posts]
    return {"@context":"https://schema.org","@type":"Blog","@id":"%s/resources/blog/#blog"%PROD,
            "name":"Lawn & Land Marketing Blog",
            "description":"Practical, first-hand marketing insight for green-industry companies: SEO, paid ads, websites, and the systems that turn search into booked work.",
            "url":"%s/resources/blog/"%PROD,"inLanguage":"en-US","publisher":{"@id":"%s/#organization"%PROD},"blogPost":bp}

def cat_schema(cat):
    return {"@context":"https://schema.org","@type":"CollectionPage",
            "@id":"%s/resources/blog/category/%s/#collection"%(PROD,cat["slug"]),
            "name":cat["title"],"description":cat["metaDesc"],
            "url":"%s/resources/blog/category/%s/"%(PROD,cat["slug"]),
            "isPartOf":{"@id":"%s/resources/blog/#blog"%PROD},"publisher":{"@id":"%s/#organization"%PROD}}

def set_cat_hero(htmltext, cat):
    htmltext = htmltext.replace('<div class="hero-kicker">Blog</div>',
                                '<div class="hero-kicker">%s</div>' % H(cat["label"]), 1)
    htmltext = htmltext.replace('<h1>Sharp takes and practical growth advice for the green industry.</h1>',
                                '<h1>%s</h1>' % H(cat["title"]), 1)
    htmltext = htmltext.replace('<p>No fluff, no filler. Just real marketing insight from the team that builds growth machines for green-industry companies every day.</p>',
                                '<p>%s</p>' % H(cat["intro"]), 1)
    htmltext = htmltext.replace('<div class="crumbs"><a href="/">Home</a><span>/</span><span>Resources</span><span>/</span><span>Blog</span></div>',
                                '<div class="crumbs"><a href="/">Home</a><span>/</span><a href="/resources/blog/">Blog</a><span>/</span><span>%s</span></div>' % H(cat["label"]), 1)
    return htmltext

def video_figure(p):
    vid, alt, img = p["video"], H(p["imageAlt"]), p["image"]
    fig = ('<figure class="article-hero-img blog-video" data-yt="' + vid + '" role="button" tabindex="0" aria-label="Play the Mow Money, Mow Problems episode">'
           '<img src="' + img + '" alt="' + alt + '" loading="eager" width="1280" height="720" style="width:100%;height:420px;object-fit:cover;display:block;">'
           '<span class="blog-video-play" aria-hidden="true"></span></figure>')
    js = ('<script>(function(){var f=document.currentScript.previousElementSibling;function go(){'
          'f.innerHTML=\'<iframe src="https://www.youtube-nocookie.com/embed/' + vid + '?autoplay=1&rel=0" '
          'title="Mow Money, Mow Problems episode" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" '
          'allowfullscreen style="position:absolute;inset:0;width:100%;height:100%;border:0;"></iframe>\';}'
          'f.addEventListener("click",go);f.addEventListener("keydown",function(e){if(e.key==="Enter"||e.key===" "){e.preventDefault();go();}});})();</script>')
    return fig + js

HERO_FIG_RE = re.compile(r'<figure class="article-hero-img">.*?</figure>', re.S)

def main():
    base = inject(read("resources/blog/index.html"), PAGINATION_CSS)
    pages = 0; cat_pages = 0; stamped = 0

    # ---- main paginated index ----
    total = max(1, (len(POSTS) + PPP - 1) // PPP)
    for i in range(total):
        pg = i + 1
        pp = POSTS[i*PPP:(i+1)*PPP]
        cards = ([fcard(f) for f in FEAT] if pg == 1 else []) + [card(p) for p in pp]
        sec = section("\n".join(cards), pagination(pg, total, "/resources/blog/"), FILTERS)
        h = put_section(base, sec)
        if pg == 1:
            title = "Blog: Landscaping Marketing Insights | Lawn & Land Marketing"
            desc = "Sharp takes and practical growth advice for green industry owners. SEO, ads, websites, automation, from the team that does it daily."
            canon = "%s/resources/blog/" % STAGE
        else:
            title = "Blog: Landscaping Marketing Insights (Page %d) | Lawn & Land Marketing" % pg
            desc = "More green-industry marketing insight from Lawn & Land Marketing. Page %d of the blog." % pg
            canon = "%s/resources/blog/page/%d/" % (STAGE, pg)
        h = set_meta(h, title, desc, canon)
        h = set_schema(h, blog_schema(pp))
        write("resources/blog/index.html" if pg == 1 else "resources/blog/page/%d/index.html" % pg, h)
        pages += 1

    # ---- category hub pages ----
    for cat in CATS:
        cp = [p for p in POSTS if p["cat"] == cat["slug"]]
        ctot = max(1, (len(cp) + PPP - 1) // PPP)
        for i in range(ctot):
            pg = i + 1
            pp = cp[i*PPP:(i+1)*PPP]
            base_url = "/resources/blog/category/%s/" % cat["slug"]
            back = '    <a class="blog-cat-back" href="/resources/blog/">&larr; All articles</a>'
            intro = '    <p class="blog-cat-intro">%s</p>\n' % H(cat["intro"])
            sec = section("\n".join(card(p) for p in pp), pagination(pg, ctot, base_url), back, intro)
            h = put_section(base, sec)
            h = set_cat_hero(h, cat)
            title = "%s | Lawn & Land Marketing" % cat["title"] + ("" if pg == 1 else " (Page %d)" % pg)
            canon = (STAGE + base_url) if pg == 1 else "%s%spage/%d/" % (STAGE, base_url, pg)
            h = set_meta(h, title, cat["metaDesc"], canon)
            h = set_schema(h, cat_schema(cat))
            write("resources/blog/category/%s/index.html" % cat["slug"] if pg == 1
                  else "resources/blog/category/%s/page/%d/index.html" % (cat["slug"], pg), h)
            cat_pages += 1

    # ---- stamp article hero media ----
    for p in POSTS:
        path = "resources/blog/%s/index.html" % p["slug"]
        if not os.path.exists(os.path.join(ROOT, path)): continue
        h = read(path)
        media = video_figure(p) if p["video"] else (
            '<figure class="article-hero-img"><img src="%s" alt="%s" loading="eager" width="1200" height="630" style="width:100%%;height:420px;object-fit:cover;display:block;"></figure>'
            % (p["image"], H(p["imageAlt"])))
        h2 = HERO_FIG_RE.sub(lambda m: media, h, count=1)
        if p["video"] and ".article-hero-img.blog-video{" not in h2:
            h2 = inject(h2, VID_CSS)
        if h2 != h:
            write(path, h2); stamped += 1

    # ---- author page: list ALL of Matt's articles (every post is attributed to him) ----
    auth_path = "author/matt-foreman/index.html"
    if os.path.exists(os.path.join(ROOT, auth_path)):
        ah = read(auth_path)
        cards_html = "\n".join(
            ('      <a href="/resources/blog/%s/" class="blog-card">\n'
             '        <img class="blog-card-img" src="%s" alt="%s" loading="lazy" width="400" height="225">\n'
             '        <div class="blog-card-body"><span class="blog-card-cat">%s</span><h3 class="blog-card-title">%s</h3><div class="blog-card-date">%s</div></div>\n'
             '      </a>') % (p["slug"], p["image"], H(p["imageAlt"]), H(p["badge"]), H(p["title"]), H(p["dateDisplay"]))
            for p in POSTS)
        sec = ('<section class="author-articles">\n'
               '    <div class="author-articles-head">\n'
               '      <h2>Articles by Matt Foreman</h2>\n'
               '      <a href="/resources/blog/">View all on the blog &rarr;</a>\n'
               '    </div>\n'
               '    <div class="blog-grid">\n' + cards_html + '\n    </div>\n  </section>')
        ah = re.sub(r'<section class="author-articles">.*?</section>', lambda m: sec, ah, count=1, flags=re.S)
        write(auth_path, ah)
        print("author page: %d articles listed" % len(POSTS))

    print("index pages: %d | category pages: %d | articles stamped: %d" % (pages, cat_pages, stamped))

if __name__ == "__main__":
    main()
