#!/usr/bin/env python3
"""Generate migrated blog pages from the live WordPress archive and audit CSV.

This is intentionally deterministic. It does not invent a full rewrite for each
post; it applies the migration quality layer consistently: clean static HTML,
answer-first summary, author/EEAT, FAQ schema, related links, sitemap entries,
and old /blog/ redirects.
"""
from __future__ import annotations

import csv
import html
import json
import os
import re
import shutil
import subprocess
import urllib.request
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from urllib.parse import urldefrag

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
BLOG_DIR = ROOT / "resources" / "blog"
AUDIT_CSV = Path("/opt/koga/.openclaw/workspace/tmp/lawn-land-blog-migration-audit-2026-06-22.csv")
WP_API = "https://lawnandlandmarketing.com/wp-json/wp/v2/posts?per_page=100&page=1&_fields=id,date,modified,slug,link,title,excerpt,content,status"
SITE = "https://lawnandlandmarketing.com"
NEW_BLOG_BASE = "/resources/blog/"
DEFAULT_IMAGE = "/assets/images/blog/qualified-landscaping-leads.jpg"


SCRAP_REDIRECT_TARGETS = {
    "4-essential-lawn-care-tips-for-guest-bloggers": "lawn-care-blogging-and-guest-posting",
    "why-are-seo-tactics-vital-for-lawn-care-blogs": "lawn-care-blogging-and-guest-posting",
    "what-drives-success-in-garden-care-video-ads": "video-marketing-for-lawn-and-garden-services",
    "what-are-top-mobile-marketing-tactics-for-landscapers": "website-design-for-landscaping-businesses",
    "guide-to-crm-adoption-for-lawn-care-companies": "online-customer-relationship-management-for-lawn-care",
    "creating-engaging-seo-content-for-gardeners": "lawn-care-blogging-and-guest-posting",
    "6-key-mobile-responsive-design-tips-for-landscapers": "website-design-for-landscaping-businesses",
    "5-best-social-networks-for-landscapers-success": "social-media-strategies-for-landscapers",
    "why-should-landscapers-prioritize-online-reputation": "managing-lawn-service-reviews-online-reputation-tips",
    "why-should-landscapers-invest-in-digital-analytics": "digital-analytics-for-landscaping-services-analytics-for-landscaping-success",
    "why-choose-video-marketing-for-landscaping-success": "video-marketing-for-lawn-and-garden-services",
    "whats-your-email-edge-for-lawn-care-success": "creative-email-newsletter-strategies-for-landscapers",
    "what-are-top-social-media-strategies-for-landscapers": "social-media-strategies-for-landscapers",
    "what-are-top-content-strategies-for-landscapers": "content-marketing-for-lawn-care-businesses",
    "top-mobile-marketing-tips-for-landscapers": "website-design-for-landscaping-businesses",
    "top-digital-branding-tips-for-landscapers": "digital-branding-for-lawn-care-professionals",
    "11-budget-friendly-lawn-care-seo-tips": "lawn-landscaping-local-seo",
    "mobile-marketing-for-landscape-services": "website-design-for-landscaping-businesses",
    "7-easy-steps-to-dominate-local-seo-for-your-landscaping-business": "lawn-landscaping-local-seo",
    "the-importance-of-seo-for-your-lawn-care-and-landscape-business": "lawn-landscaping-local-seo",
}

LEGACY_ROUTE_MAP = {
    "/solutions/": "/marketing-services/",
    "/solutions/websites/": "/marketing-services/website-design/",
    "/solutions/local-seo/": "/marketing-services/local-seo/",
    "/solutions/reputation-management/": "/marketing-services/reputation-management/",
    "/solutions/lead-nurturing/": "/marketing-services/automation/",
    "/solutions/paid-ads/": "/marketing-services/google-ads/",
    "/solutions/content-marketing/": "/resources/blog/content-marketing-for-lawn-care-businesses/",
    "/precision-case-study/": "/case-studies/precision/",
    "/schedule/": "/get-started/book-strategy-call/",
}


@dataclass
class Post:
    slug: str
    title: str
    excerpt: str
    content_html: str
    date: str
    modified: str
    action: str
    notes: str
    clicks16: int
    imps16: int
    clicks90: int
    imps90: int

    @property
    def new_path(self) -> str:
        return f"{NEW_BLOG_BASE}{self.slug}/"

    @property
    def new_url(self) -> str:
        return f"{SITE}{self.new_path}"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def strip_trailing_ws(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.splitlines()) + "\n"


def clean_text(raw: str) -> str:
    text = BeautifulSoup(raw or "", "html.parser").get_text(" ")
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def esc(text: str) -> str:
    return html.escape(text or "", quote=True)


def canonical_old_url(url: str) -> str:
    u = urldefrag(url)[0]
    return u if u.endswith("/") else u + "/"


def load_audit() -> dict[str, dict[str, str]]:
    rows = {}
    with AUDIT_CSV.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            slug = canonical_old_url(row["URL"]).rstrip("/").split("/")[-1]
            rows[slug] = row
    return rows


def fetch_posts() -> list[dict]:
    req = urllib.request.Request(WP_API, headers={"User-Agent": "Lawn & Land migration generator"})
    with urllib.request.urlopen(req, timeout=45) as response:
        return json.load(response)


def post_category(title: str, slug: str) -> str:
    hay = f"{title} {slug}".lower()
    if "story teaches" in hay or "growth" in hay and any(x in hay for x in ["alex", "trevor", "johnny", "couri", "luke", "bob", "mark", "pat", "chad", "dustin", "brandon", "brian", "grant", "scott", "nate", "cameron"]):
        return "Client Stories"
    if "seo" in hay or "local search" in hay:
        return "SEO"
    if "google ads" in hay or "ppc" in hay or "pay-per-click" in hay:
        return "Paid Ads"
    if "website" in hay or "web design" in hay:
        return "Website Design"
    if "crm" in hay or "automation" in hay or "lead nurturing" in hay:
        return "CRM & Automation"
    if "review" in hay or "reputation" in hay:
        return "Reputation"
    if "email" in hay or "newsletter" in hay:
        return "Email Marketing"
    if "social" in hay or "video" in hay or "$20 marketing" in hay:
        return "Social & Video"
    if "ai" in hay:
        return "AI"
    return "Digital Marketing"


def category_url(category: str) -> str:
    mapping = {
        "SEO": "/marketing-services/local-seo/",
        "Paid Ads": "/marketing-services/google-ads/",
        "Website Design": "/marketing-services/website-design/",
        "CRM & Automation": "/marketing-services/automation/",
        "Reputation": "/marketing-services/reputation-management/",
        "AI": "/marketing-services/your-ai-partner/",
        "Client Stories": "/resources/mow-money-mow-problems-podcast/",
    }
    return mapping.get(category, "/marketing-services/")


def normalize_href(href: str) -> str:
    if href.startswith("https://lawnandlandmarketing.com/"):
        href = href.replace("https://lawnandlandmarketing.com", "")
    if href in LEGACY_ROUTE_MAP:
        return LEGACY_ROUTE_MAP[href]
    blog_match = re.match(r"^/blog/([^/#?]+)/?$", href)
    if blog_match:
        slug = blog_match.group(1)
        target = SCRAP_REDIRECT_TARGETS.get(slug, slug)
        return f"{NEW_BLOG_BASE}{target}/"
    return href


def topic_summary(post: Post, category: str) -> tuple[str, list[str]]:
    title = post.title.rstrip(".")
    summary = post.excerpt or f"{title} gives lawn and landscape operators a clearer way to evaluate the next marketing move."
    summary = summary.rstrip(".") + "."
    if category == "SEO":
        bullets = [
            "Clarify the service, location, buyer intent, and proof on the page before chasing more traffic.",
            "Use headings, FAQs, internal links, and schema so Google and AI tools can extract the answer cleanly.",
            "Track qualified calls and booked work, not rankings alone.",
        ]
    elif category == "Paid Ads":
        bullets = [
            "Start with lead quality, budget discipline, conversion tracking, and a strong landing page.",
            "Separate urgent buyer intent from research traffic so the campaign does not pay for bad-fit clicks.",
            "Review search terms, negatives, and follow-up speed before blaming the platform.",
        ]
    elif category == "Website Design":
        bullets = [
            "Make service fit, proof, location, and next step obvious above the fold.",
            "Design for booked estimates, not just visual polish.",
            "Use fast mobile pages, trust signals, and clear internal paths to high-value services.",
        ]
    elif category == "CRM & Automation":
        bullets = [
            "A CRM should keep every lead, estimate, review request, and follow-up from falling through the cracks.",
            "The useful automation is simple: faster response, cleaner pipeline stages, and consistent reminders.",
            "Measure response time, booked appointments, close rate, and missed opportunities.",
        ]
    elif category == "Reputation":
        bullets = [
            "Reviews help buyers choose and help local search engines understand trust.",
            "The best system asks at the right moment, makes the request easy, and responds like a real operator.",
            "No incentives, gating, or fake review shortcuts. That is how you create a future mess.",
        ]
    elif category == "Email Marketing":
        bullets = [
            "Email works when it is tied to seasonal timing, service reminders, and actual customer intent.",
            "Send useful reminders, project ideas, review/referral prompts, and reactivation campaigns.",
            "Keep the list clean and the next step obvious.",
        ]
    elif category == "Social & Video":
        bullets = [
            "Document real work: before/after, walkthroughs, jobsite decisions, and finished results.",
            "Use short, specific posts that show proof instead of generic brand noise.",
            "Measure whether social content supports trust, retargeting, referrals, and estimate requests.",
        ]
    elif category == "Client Stories":
        bullets = [
            "Use the operator story as proof, not celebrity content.",
            "Pull out the business lesson, the marketing takeaway, and the execution detail a landscaper can apply.",
            "Connect the story back to positioning, proof, follow-up, local search, and the sales process.",
        ]
    else:
        bullets = [
            "Start with the business problem, not the channel.",
            "Make the advice specific to lawn and landscape operators.",
            "Tie every recommendation back to qualified demand, booked work, and follow-up.",
        ]
    return summary, bullets


def clean_body_html(raw: str) -> tuple[str, list[tuple[str, str]]]:
    soup = BeautifulSoup(raw or "", "html.parser")
    allowed = {"p", "h2", "h3", "ul", "ol", "li", "strong", "em", "a", "blockquote"}
    body_parts: list[str] = []
    headings: list[tuple[str, str]] = []

    def clean_node(node):
        if getattr(node, "name", None) is None:
            return html.escape(str(node))
        if node.name not in allowed:
            return "".join(clean_node(c) for c in node.children)
        tag = soup.new_tag(node.name)
        if node.name == "a" and node.get("href"):
            tag["href"] = normalize_href(node["href"])
        for child in node.children:
            tag.append(BeautifulSoup(clean_node(child), "html.parser"))
        return str(tag)

    for node in soup.find_all(["p", "h2", "h3", "ul", "ol", "blockquote"], recursive=False):
        text = clean_text(str(node))
        if not text:
            continue
        if node.name in {"h2", "h3"}:
            hid = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:72] or "section"
            if node.name == "h2":
                headings.append((hid, text))
            node["id"] = hid
            body_parts.append(str(node))
        else:
            body_parts.append(clean_node(node))

    if not body_parts:
        fallback = clean_text(raw)
        if fallback:
            body_parts.append(f"<p>{esc(fallback)}</p>")
    return "\n".join(body_parts), headings[:8]


def make_faq(post: Post, category: str) -> list[tuple[str, str]]:
    if category == "SEO":
        return [
            ("What matters most for landscaping SEO now?", "Specificity. A useful page should make the service, service area, buyer intent, proof, and next step clear enough for both people and search systems to understand."),
            ("Should landscaping companies optimize for AI search?", "Yes, but not by chasing tricks. Use answer-first sections, clear headings, helpful FAQs, schema, author signals, and real examples so AI tools can extract accurate answers."),
            ("What should we measure besides rankings?", "Track qualified calls, form fills, booked estimates, lead quality, close rate, and whether the search traffic matches the services and locations the company wants to grow."),
        ]
    if category == "Paid Ads":
        return [
            ("What makes landscaping ads waste money?", "Weak tracking, broad keywords, poor landing pages, slow follow-up, and campaigns aimed at volume instead of qualified estimate requests."),
            ("How should a landscaping company judge paid ads?", "Judge campaigns by booked estimates, lead quality, cost per qualified opportunity, and closed work, not raw lead count alone."),
        ]
    if category == "Website Design":
        return [
            ("What should a landscaping website do first?", "It should quickly explain who the company serves, what services it wants to sell, where it works, why it can be trusted, and how to request an estimate."),
            ("Why do good-looking landscaping websites still fail?", "Many look fine but hide the next step, bury proof, ignore local intent, or use generic copy that does not qualify the buyer."),
        ]
    if category == "Client Stories":
        return [
            ("Why publish operator stories on a marketing site?", "The right story shows how real lawn and landscape companies think through positioning, proof, operations, reviews, and growth. That is more useful than generic marketing theory."),
            ("How should a landscaping company use this lesson?", "Look for the repeatable move behind the story, then apply it to the company website, local SEO, reviews, follow-up, and sales process."),
        ]
    return [
        ("What is the practical takeaway for landscaping companies?", "The advice only matters if it helps the company attract better-fit leads, convert more of them, and follow up consistently."),
        ("How should this be implemented?", "Start with the highest-value service or market, make the page and offer clearer, track the result, and improve from there."),
    ]


def read_time(words: int) -> int:
    return max(3, round(words / 190))


def date_label(iso_date: str) -> str:
    return datetime.fromisoformat(iso_date[:10]).strftime("%B %-d, %Y")


def split_template() -> tuple[str, str]:
    template_path = BLOG_DIR / "why-landscaping-seo-gets-traffic-not-qualified-leads" / "index.html"
    if template_path.exists():
        template = read(template_path)
    else:
        template = subprocess.check_output(
            [
                "git",
                "show",
                "origin/main:resources/blog/why-landscaping-seo-gets-traffic-not-qualified-leads/index.html",
            ],
            cwd=ROOT,
            text=True,
        )
    body_start = template.index("<body>")
    main_start = template.index("  <main id=\"main\">")
    footer_start = template.index("<footer class=\"footer-v2\">")
    head_shell = template[:body_start]
    shell_before_main = template[body_start:main_start]
    footer = template[footer_start:]
    return head_shell + shell_before_main, footer


def schema_scripts(post: Post, category: str, faq: list[tuple[str, str]]) -> str:
    blogposting = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BlogPosting",
                "headline": post.title,
                "description": post.excerpt,
                "datePublished": post.date[:10],
                "dateModified": post.modified[:10],
                "image": f"{SITE}{DEFAULT_IMAGE}",
                "url": post.new_url,
                "mainEntityOfPage": post.new_url,
                "articleSection": category,
                "author": {"@id": f"{SITE}/#matt-foreman"},
                "publisher": {"@id": f"{SITE}/#organization"},
            },
            {"@type": "Person", "@id": f"{SITE}/#matt-foreman", "name": "Matt Foreman", "url": f"{SITE}/author/matt-foreman/"},
            {"@type": "Organization", "@id": f"{SITE}/#organization", "name": "Lawn & Land Marketing", "url": SITE, "logo": f"{SITE}/assets/logos/logo-horizontal.svg"},
        ],
    }
    faqpage = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faq
        ],
    }
    return (
        '<script type="application/ld+json">'
        + json.dumps(blogposting, ensure_ascii=False, separators=(",", ":"))
        + "</script>\n  "
        + '<script type="application/ld+json">'
        + json.dumps(faqpage, ensure_ascii=False, separators=(",", ":"))
        + "</script>"
    )


def make_head(prefix: str, post: Post, category: str, faq: list[tuple[str, str]]) -> str:
    description = (post.excerpt or post.notes).strip()
    if len(description) > 158:
        description = description[:155].rsplit(" ", 1)[0] + "..."
    head = prefix
    head = re.sub(r"<title>.*?</title>", f"<title>{esc(post.title)} | Lawn &amp; Land Marketing</title>", head, count=1, flags=re.S)
    head = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{esc(description)}">', head, count=1, flags=re.S)
    head = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{esc(post.new_url)}">', head, count=1, flags=re.S)
    head = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{esc(post.title)} | Lawn &amp; Land Marketing">', head, count=1, flags=re.S)
    head = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{esc(description)}">', head, count=1, flags=re.S)
    head = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{esc(post.new_url)}">', head, count=1, flags=re.S)
    head = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{esc(post.title)} | Lawn &amp; Land Marketing">', head, count=1, flags=re.S)
    head = re.sub(r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{esc(description)}">', head, count=1, flags=re.S)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\s*<script type="application/ld\+json">.*?</script>', schema_scripts(post, category, faq), head, count=1, flags=re.S)
    return head


def related_posts(post: Post, posts: list[Post]) -> list[Post]:
    category = post_category(post.title, post.slug)
    same = [p for p in posts if p.slug != post.slug and post_category(p.title, p.slug) == category]
    rest = [p for p in posts if p.slug != post.slug and p not in same]
    return (same + rest)[:3]


def article_html(post: Post, all_posts: list[Post]) -> str:
    prefix, footer = split_template()
    category = post_category(post.title, post.slug)
    faq = make_faq(post, category)
    head_prefix = make_head(prefix, post, category, faq)
    body_html, headings = clean_body_html(post.content_html)
    summary, bullets = topic_summary(post, category)
    words = len(clean_text(post.content_html).split())
    related = related_posts(post, all_posts)
    title_short = post.title[:84]
    toc_items = "".join(f'<li><a href="#{hid}">{esc(text)}</a></li>' for hid, text in headings[:6])
    if not toc_items:
        toc_items = '<li><a href="#quick-answer">Quick answer</a></li>'
    bullet_html = "".join(f"<li>{esc(b)}</li>" for b in bullets)
    faq_html = "".join(f'<div class="faq-item"><h3>{esc(q)}</h3><p>{esc(a)}</p></div>' for q, a in faq)
    related_html = "".join(
        f'''<a class="related-card" href="{p.new_path}">
          <div class="related-card-img"><img src="{DEFAULT_IMAGE}" alt="{esc(p.title)}" style="width:100%;height:100%;object-fit:cover;display:block;"></div>
          <div class="related-card-body"><span class="related-card-cat">{esc(post_category(p.title, p.slug))}</span><h4>{esc(p.title)}</h4></div>
        </a>'''
        for p in related
    )
    main = f'''
  <main id="main">

  <section class="article-hero">
    <div class="container">
      <nav class="article-breadcrumb"><a href="/">Home</a><span>/</span><a href="/resources/blog/">Blog</a><span>/</span><span>{esc(title_short)}</span></nav>
      <span class="article-category-badge">{esc(category)}</span>
      <h1 class="article-headline">{esc(post.title)}</h1>
      <div class="article-meta">
        <div class="article-author">
          <div class="article-author-photo" style="background:url('/assets/images/matt-author.jpg') center/cover;"></div>
          <div><a href="/author/matt-foreman/" class="article-author-name">Matt Foreman</a><span class="article-author-title">Founder &amp; Owner, Lawn &amp; Land Marketing</span></div>
        </div>
        <div class="article-meta-right">
          <span class="article-date">{date_label(post.date)}</span>
          <span class="article-read-time">{read_time(words)} min read</span>
        </div>
      </div>
      <figure class="article-hero-img"><img src="{DEFAULT_IMAGE}" alt="{esc(post.title)}" style="width:100%;height:420px;object-fit:cover;display:block;"></figure>
    </div>
  </section>

  <section class="article-layout">
    <div class="article-container">
      <article class="article-content">
        <p class="article-lead">{esc(summary)}</p>

        <section id="quick-answer" class="article-callout article-callout--lime">
          <div class="callout-body"><strong>The short version:</strong><ul>{bullet_html}</ul></div>
        </section>

        {body_html}

        <div class="article-cta-block">
          <div class="article-cta-inner">
            <div class="article-cta-label">Get a sharper plan</div>
            <h3>Want the version built around your market?</h3>
            <p>Bring us the services you want more of, the markets you care about, and the leads you are tired of getting. We will show you where the current system is leaking.</p>
            <div class="article-cta-btns"><a href="/get-started/book-strategy-call/" class="btn btn--lime btn--lg">Book your Growth Diagnostic call</a></div>
          </div>
        </div>

        <section>
          <h2>Frequently asked questions</h2>
          <div class="article-faq">{faq_html}</div>
        </section>

        <div class="author-block">
          <div class="author-block-photo" style="background:url('/assets/images/matt-author.jpg') center/cover;"></div>
          <div>
            <div class="author-block-label">About the author</div>
            <a href="/author/matt-foreman/" class="author-block-name">Matt Foreman</a>
            <div class="author-block-role">Founder &amp; Owner, Lawn &amp; Land Marketing</div>
            <p class="author-block-bio">Matt Foreman is the founder and owner of Lawn &amp; Land Marketing, a digital marketing agency built exclusively for the green industry. He writes from the work his team does every day across websites, SEO, paid ads, reviews, automation, and the systems that turn attention into booked work.</p>
          </div>
        </div>
      </article>

      <aside class="article-aside">
        <div class="toc-inner">
          <div class="toc-label">In this article</div>
          <ol class="toc-list">{toc_items}</ol>
        </div>
        <div class="article-related" style="margin-top:28px;">
          <h3>Related articles</h3>
          <div class="article-related-grid">{related_html}</div>
        </div>
      </aside>
    </div>
  </section>

  </main>
'''
    return head_prefix + main + footer


def index_html(posts: list[Post]) -> str:
    prefix, footer = split_template()
    prefix = re.sub(r"<title>.*?</title>", "<title>Blog: Landscaping Marketing Insights | Lawn &amp; Land Marketing</title>", prefix, count=1, flags=re.S)
    prefix = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Sharp, practical marketing guidance for lawn and landscape operators: SEO, paid ads, websites, reviews, automation, and client stories.">', prefix, count=1, flags=re.S)
    prefix = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{SITE}/resources/blog/">', prefix, count=1, flags=re.S)
    blog_schema = {
        "@context": "https://schema.org",
        "@type": "Blog",
        "@id": f"{SITE}/resources/blog/#blog",
        "name": "Lawn & Land Marketing Blog",
        "description": "Practical, first-hand marketing insight for green-industry companies.",
        "url": f"{SITE}/resources/blog/",
        "publisher": {"@id": f"{SITE}/#organization"},
        "blogPost": [
            {"@type": "BlogPosting", "@id": p.new_url, "headline": p.title, "url": p.new_url, "datePublished": p.date[:10]}
            for p in posts[:20]
        ],
    }
    prefix = re.sub(r'<script type="application/ld\+json">.*?</script>\s*<script type="application/ld\+json">.*?</script>', '<script type="application/ld+json">' + json.dumps(blog_schema, ensure_ascii=False, separators=(",", ":")) + "</script>", prefix, count=1, flags=re.S)
    featured = posts[0]
    cards = "".join(
        f'''<article class="blog-card">
          <div class="blog-card-img"><img src="{DEFAULT_IMAGE}" alt="{esc(p.title)}"></div>
          <div class="blog-card-content">
            <div class="blog-meta"><span>{esc(post_category(p.title, p.slug))}</span><span>•</span><span>{date_label(p.date)}</span></div>
            <h3><a href="{p.new_path}">{esc(p.title)}</a></h3>
            <p>{esc(p.excerpt)}</p>
            <a class="blog-read-more" href="{p.new_path}">Read article →</a>
          </div>
        </article>'''
        for p in posts[1:]
    )
    main = f'''
  <main id="main">
    <section class="simple-hero" style="--hero-image: url('/assets/images/blog/qualified-landscaping-leads.jpg');">
      <div class="hero-inner">
        <div class="hero-copy" data-reveal="fade-up">
          <div class="crumbs"><a href="/">Home</a><span>/</span><a href="/resources/">Resources</a><span>/</span><span>Blog</span></div>
          <div class="hero-kicker">Green Industry Insights</div>
          <h1>Sharp takes and practical growth advice for the green industry.</h1>
          <p>No fluff, no generic agency talk. SEO, ads, websites, reviews, automation, and client stories from the team doing the work every day.</p>
        </div>
      </div>
    </section>

    <section class="blog-section">
      <div class="container">
        <article class="blog-featured">
          <div class="blog-featured-visual"><img src="{DEFAULT_IMAGE}" alt="{esc(featured.title)}" style="width:100%;height:100%;object-fit:cover;display:block;"><span class="blog-featured-tag">{esc(post_category(featured.title, featured.slug))}</span></div>
          <div class="blog-featured-content">
            <div class="blog-meta"><span>{date_label(featured.date)}</span><span>•</span><span>{read_time(int(re.sub(r'\\D', '', str(featured.imps16 or 1200)) or '1200'))} min read</span></div>
            <h2><a href="{featured.new_path}">{esc(featured.title)}</a></h2>
            <p>{esc(featured.excerpt)}</p>
            <a href="{featured.new_path}" class="btn btn--lime">Read the article</a>
          </div>
        </article>
        <div class="blog-grid">{cards}</div>
      </div>
    </section>
  </main>
'''
    return prefix + main + footer


def update_sitemap(posts: list[Post]) -> None:
    sitemap = read(ROOT / "sitemap.xml")
    extra = "\n".join(
        f'  <url><loc>{SITE}{p.new_path}</loc><changefreq>monthly</changefreq><priority>0.55</priority><lastmod>{p.modified[:10]}</lastmod></url>'
        for p in posts
    )
    if "<!-- Migrated Blog Posts -->" in sitemap:
        sitemap = re.sub(r"\n  <!-- Migrated Blog Posts -->.*?\n\n  <!-- Legal -->", f"\n  <!-- Migrated Blog Posts -->\n{extra}\n\n  <!-- Legal -->", sitemap, flags=re.S)
    else:
        sitemap = sitemap.replace("\n  <!-- Legal -->", f"\n  <!-- Migrated Blog Posts -->\n{extra}\n\n  <!-- Legal -->")
    write(ROOT / "sitemap.xml", sitemap)


def update_vercel_redirects(posts: list[Post], audit: dict[str, dict[str, str]]) -> None:
    path = ROOT / "vercel.json"
    data = json.loads(read(path))
    redirects = data.setdefault("redirects", [])
    redirects = [r for r in redirects if not r.get("source", "").startswith("/blog")]
    redirects.append({"source": "/blog", "destination": "/resources/blog/", "permanent": True})
    redirects.append({"source": "/blog/", "destination": "/resources/blog/", "permanent": True})
    for p in posts:
        redirects.append({"source": f"/blog/{p.slug}", "destination": p.new_path, "permanent": True})
        redirects.append({"source": f"/blog/{p.slug}/", "destination": p.new_path, "permanent": True})
    for slug, row in audit.items():
        if row["Migration Action"] != "Scrap":
            continue
        target = SCRAP_REDIRECT_TARGETS.get(slug, "landscaper-marketing-101-how-to-attract-more-clients-and-grow-your-business")
        redirects.append({"source": f"/blog/{slug}", "destination": f"{NEW_BLOG_BASE}{target}/", "permanent": True})
        redirects.append({"source": f"/blog/{slug}/", "destination": f"{NEW_BLOG_BASE}{target}/", "permanent": True})
    data["redirects"] = redirects
    write(path, json.dumps(data, indent=2) + "\n")


def main() -> None:
    audit = load_audit()
    raw_posts = fetch_posts()
    posts: list[Post] = []
    for raw in raw_posts:
        slug = raw["slug"]
        if slug not in audit:
            continue
        row = audit[slug]
        if row["Migration Action"] == "Scrap":
            continue
        posts.append(
            Post(
                slug=slug,
                title=clean_text(raw["title"]["rendered"]),
                excerpt=clean_text(raw.get("excerpt", {}).get("rendered", "")),
                content_html=raw["content"]["rendered"],
                date=raw["date"],
                modified=raw["modified"],
                action=row["Migration Action"],
                notes=row["Technical Optimization Notes"],
                clicks16=int(float(row["GSC Clicks 16mo"] or 0)),
                imps16=int(float(row["GSC Impressions 16mo"] or 0)),
                clicks90=int(float(row["GSC Clicks 90d"] or 0)),
                imps90=int(float(row["GSC Impressions 90d"] or 0)),
            )
        )
    posts.sort(key=lambda p: (p.imps16, p.clicks16, p.date), reverse=True)

    for child in BLOG_DIR.iterdir():
        if child.is_dir():
            shutil.rmtree(child)

    for post in posts:
        if post.action == "Preserve":
            preserved = subprocess.check_output(
                ["git", "show", f"origin/main:resources/blog/{post.slug}/index.html"],
                cwd=ROOT,
                text=True,
            )
            write(BLOG_DIR / post.slug / "index.html", preserved)
        else:
            write(BLOG_DIR / post.slug / "index.html", strip_trailing_ws(article_html(post, posts)))

    write(BLOG_DIR / "index.html", strip_trailing_ws(index_html(posts)))
    update_sitemap(posts)
    update_vercel_redirects(posts, audit)

    print(f"generated {len(posts)} migrated blog posts")
    print(f"scrap redirects: {sum(1 for row in audit.values() if row['Migration Action'] == 'Scrap')}")


if __name__ == "__main__":
    main()
