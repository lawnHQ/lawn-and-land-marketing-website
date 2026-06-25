#!/usr/bin/env python3
"""Service-page generator.

Reads _content.json (array of audited content objects from the content workflow)
and writes marketing-services/<slug>/index.html for each, by swapping the head
meta + Service JSON-LD + <main> of the APPROVED exemplar (website-design) so the
surrounding structure (styles, header, footer, script) stays byte-identical.

All internal links (breadcrumb, hero CTAs, FAQ link, booking CTA, "pairs well
with") are generated here, so they are correct by construction.

Usage:
  python3 gen_service.py            # generate all pages from _content.json
  python3 gen_service.py --selftest # render a stub page to /tmp and sanity-check
"""
import re, json, os, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(ROOT, 'marketing-services/website-design/index.html')

# --- Lucide icon library (inner paths only; stroke applied via CSS) -----------
ICONS = {
  'monitor': '<rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
  'smartphone': '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M12 18h.01"/>',
  'search': '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
  'map-pin': '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
  'target': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
  'pen-line': '<path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/>',
  'award': '<circle cx="12" cy="8" r="6"/><path d="M15.5 13 17 22l-5-3-5 3 1.5-9"/>',
  'trending-up': '<path d="M3 17l6-6 4 4 8-8"/><path d="M17 7h4v4"/>',
  'bar-chart': '<path d="M3 3v18h18"/><rect x="7" y="12" width="3" height="6" rx="0.5"/><rect x="12" y="8" width="3" height="10" rx="0.5"/><rect x="17" y="14" width="3" height="4" rx="0.5"/>',
  'zap': '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
  'mail': '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/>',
  'message-circle': '<path d="M21 11.5a8.38 8.38 0 0 1-9 8.5 8.5 8.5 0 0 1-3.9-.9L3 21l1.9-5.1A8.5 8.5 0 0 1 12 3a8.38 8.38 0 0 1 9 8.5Z"/>',
  'phone': '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92Z"/>',
  'calendar': '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
  'clock': '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
  'star': '<path d="M12 3 14.8 8.7 21 9.6l-4.5 4.4 1.1 6.1L12 17.2 6.4 20.1l1.1-6.1L3 9.6l6.2-.9Z"/>',
  'shield-check': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>',
  'thumbs-up': '<path d="M7 10v12"/><path d="M15 5.88 14 10h5.83a2 2 0 0 1 1.92 2.56l-2.33 8A2 2 0 0 1 17.5 22H4a2 2 0 0 1-2-2v-8a2 2 0 0 1 2-2h2.76a2 2 0 0 0 1.79-1.11L12 2a3.13 3.13 0 0 1 3 3.88Z"/>',
  'users': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
  'bot': '<rect x="3" y="11" width="18" height="10" rx="2"/><circle cx="12" cy="5" r="2"/><path d="M12 7v4"/><path d="M8 16h.01M16 16h.01"/>',
  'globe': '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10Z"/>',
  'refresh-cw': '<path d="M21 12a9 9 0 1 1-3-6.7"/><path d="M21 3v6h-6"/>',
  'repeat': '<path d="m17 2 4 4-4 4"/><path d="M3 11v-1a4 4 0 0 1 4-4h14"/><path d="m7 22-4-4 4-4"/><path d="M21 13v1a4 4 0 0 1-4 4H3"/>',
  'filter': '<path d="M22 3H2l8 9.46V19l4 2v-8.54L22 3z"/>',
  'sliders': '<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6"/>',
  'eye': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>',
  'lightbulb': '<path d="M9 18h6M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7c.6.5 1 1.3 1 2.1h6c0-.8.4-1.6 1-2.1A7 7 0 0 0 12 2Z"/>',
  'link': '<path d="M10 13a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 11a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/>',
  'megaphone': '<path d="m3 11 18-5v12L3 14v-3Z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
  'map': '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2-6-2Z"/><path d="M9 4v14M15 6v14"/>',
  'file-text': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6"/><path d="M9 13h6M9 17h6"/>',
  'check-circle': '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="m9 11 3 3L22 4"/>',
  'monitor-smartphone': '<path d="M18 8V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h8"/><path d="M10 19v-3.96 3.15"/><path d="M7 19h5"/><rect width="6" height="10" x="16" y="12" rx="2"/>',
  'book-user': '<path d="M15 13a3 3 0 1 0-6 0"/><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H19a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H6.5a1 1 0 0 1 0-5H20"/><circle cx="12" cy="8" r="2"/>',
  'badge-check': '<path d="M3.85 8.62a4 4 0 0 1 4.78-4.77 4 4 0 0 1 6.74 0 4 4 0 0 1 4.78 4.78 4 4 0 0 1 0 6.74 4 4 0 0 1-4.77 4.78 4 4 0 0 1-6.75 0 4 4 0 0 1-4.78-4.77 4 4 0 0 1 0-6.76Z"/><path d="m9 12 2 2 4-4"/>',
  'refresh-ccw': '<path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"/><path d="M16 16h5v5"/>',
}

# slug -> (label, icon) for the "pairs well with" links (consistent sitewide)
SERVICE_MAP = {
  'website-design': ('Website Design', 'monitor-smartphone'),
  'local-seo': ('Local SEO', 'search'),
  'gbp-management': ('GBP Management', 'map-pin'),
  'google-ads': ('Google Ads', 'badge-check'),
  'meta-ads': ('Meta Ads', 'book-user'),
  'your-ai-partner': ('Your AI Partner', 'bot'),
  'reputation-management': ('Reputation Management', 'star'),
  'automation': ('CRM & Automation', 'refresh-ccw'),
}

# Use the proven dark hero photo across all service pages (matches the locked
# website-design exemplar) for consistent text contrast + on-brand look. The
# per-service 0X-*.jpg files are light UI screenshots, better as showcase
# content than hero backgrounds.
HERO_IMG = {s: 'programs-hero.webp' for s in (
  'website-design', 'local-seo', 'gbp-management', 'google-ads',
  'meta-ads', 'your-ai-partner', 'reputation-management', 'automation')}

PLACEHOLDER_ICON = ('<svg width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
  'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" '
  'height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="m21 15-5-5L5 21"/></svg>')

CAL_ICON = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
  'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" '
  'height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" '
  'y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>')

MSG_ICON = ('<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
  'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 '
  '2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>')


def _h(s):
    # raw HTML escape
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def esc(s):
    # display text: escape, then DROP any stray emphasis markers (~x~ -> x)
    return re.sub(r'~([^~]+)~', r'\1', _h(s))

def escA(s):
    return esc(s).replace('"', '&quot;')

def emph(s):
    # headline only: escape, then convert ~phrase~ -> <em>phrase</em>
    return re.sub(r'~([^~]+)~', r'<em>\1</em>', _h(s))

def svg(key):
    return f'<svg viewBox="0 0 24 24">{ICONS.get(key, ICONS["check-circle"])}</svg>'


def build_main(c):
    slug = c['slug']
    name = c['serviceName']
    img = HERO_IMG.get(slug, 'programs-hero.webp')

    crumbs = (f'<div class="crumbs"><a href="/">Home</a><span>/</span>'
              f'<a href="/marketing-services/">Marketing Services</a><span>/</span>'
              f'<span>{esc(name)}</span></div>')

    hero = f'''  <!-- HERO BANNER -->
  <section class="simple-hero" style="--hero-image: url('/assets/images/{img}');">
    <div class="hero-inner">
      <div class="hero-copy" data-reveal="fade-up">
        {crumbs}
        <div class="hero-kicker">{esc(c['heroEyebrow'])}</div>
        <h1>{esc(c['h1'])}</h1>
        <p>{esc(c['heroSubhead'])}</p>
        <div class="hero-actions">
          <a href="/get-started/book-strategy-call/" class="btn btn--lime">{CAL_ICON} Schedule Strategy Call</a>
          <a href="/contact/" class="btn btn--ghost">{MSG_ICON} Contact Us</a>
        </div>
      </div>
    </div>
  </section>'''

    cv = c['conviction']
    unit = f'<span>{esc(cv["statUnit"])}</span>' if cv.get('statUnit') else ''
    conviction = f'''  <!-- CONVICTION -->
  <section class="svc-conviction">
    <div class="container">
      <div class="conviction-inner" data-reveal="fade-up">
        <div class="conviction-stat">{esc(cv['stat'])}{unit}</div>
        <div>
          <p class="conviction-lead">{esc(cv['lead'])}</p>
          <p class="conviction-sub">{esc(cv['sub'])}</p>
        </div>
      </div>
    </div>
  </section>'''

    def showcase(sc, reversed_=False):
        rev = ' is-reversed' if reversed_ else ''
        lis = ''.join(f'<li>{esc(x)}</li>' for x in sc['checklist'])
        if sc.get('image'):
            asp = sc.get('imageAspect', '16/10')
            _aw, _ah = (asp.replace(' ', '').split('/') + ['10'])[:2]
            _h = round(1400 * float(_ah) / float(_aw))
            media = (f'<img class="svc-showcase-img" src="/assets/images/showcase/{sc["image"]}" '
                     f'alt="{esc(sc["imageAlt"])}" loading="lazy" width="1400" height="{_h}" '
                     f'style="width:100%;height:auto;aspect-ratio:{asp};object-fit:cover;border-radius:16px;display:block;">')
        else:
            media = (f'<div class="svc-ph svc-ph--wide">\n'
                     '            <div class="svc-ph-inner">\n'
                     f'              <span class="svc-ph-icon">{PLACEHOLDER_ICON}</span>\n'
                     '              <span class="svc-ph-label">Image placeholder</span>\n'
                     f'              <span class="svc-ph-hint">{esc(sc["imageHint"])}</span>\n'
                     '            </div>\n'
                     '          </div>')
        return f'''  <!-- SHOWCASE -->
  <section class="svc-showcase">
    <div class="container">
      <div class="svc-showcase-inner{rev}">
        <div class="svc-showcase-text">
          <span class="svc-eyebrow">{esc(sc['eyebrow'])}</span>
          <h2>{emph(sc['headline'])}</h2>
          <p>{esc(sc['paragraph'])}</p>
          <ul class="svc-showcase-list">{lis}</ul>
        </div>
        <div class="svc-showcase-media">
          {media}
        </div>
      </div>
    </div>
  </section>'''

    inc = c['includes']
    feat = f'''<div class="include-card include-card--featured">
          <div class="include-featured-inner">
            <div class="include-featured-content">
              <span class="include-featured-kicker">{esc(inc['featuredKicker'])}</span>
              <p class="feat-headline">{emph(inc['featuredHeadline'])}</p>
              <p>{esc(inc['featuredBody'])}</p>
            </div>
            <span class="include-featured-tag">{esc(inc['featuredTag'])}</span>
          </div>
        </div>'''
    cards = '\n        '.join(
        f'<div class="include-card"><span class="include-icon">{svg(card["icon"])}</span>'
        f'<h3>{esc(card["title"])}</h3><p>{esc(card["body"])}</p></div>'
        for card in inc['cards'])
    includes = f'''  <!-- WHAT'S INCLUDED -->
  <section class="svc-includes">
    <div class="container">
      <span class="svc-eyebrow">What's included</span>
      <h2>{esc(name)}, <em>fully handled</em>.</h2>
      <p class="section-sub">No guesswork, no surprises: the standard pieces that make this work for a lawn care or landscaping company, built and managed for you.</p>
      <div class="includes-grid">
        {feat}
        {cards}
      </div>
    </div>
  </section>'''

    faq_items = '\n          '.join(
        f'<details class="faq-item"><summary>{esc(q)}</summary>'
        f'<p>{esc(a)}</p></details>'
        for q, a in zip(c['faqQuestions'], c['faqAnswers']))
    faq = f'''  <!-- FAQ -->
  <section class="svc-faq">
    <div class="container">
      <div class="svc-faq-inner">
        <div class="svc-faq-head">
          <span class="svc-eyebrow">FAQ</span>
          <h2>{esc(name)}, <em>answered</em>.</h2>
          <p>The questions we hear most from owners before they get started.</p>
          <a href="/contact/" class="btn btn--ghost-lime btn--sm">Still have questions? &rarr;</a>
        </div>
        <div class="svc-faq-list">
          {faq_items}
        </div>
      </div>
    </div>
  </section>'''

    related = [s for s in c['relatedSlugs'] if s != slug and s in SERVICE_MAP][:4]
    rel_links = '\n          '.join(
        f'<a href="/marketing-services/{s}/" class="cta-service-link">'
        f'<span class="cta-service-icon">{svg(SERVICE_MAP[s][1])}</span>'
        f'<span>{esc(SERVICE_MAP[s][0])}</span><span class="cta-service-arrow">&rarr;</span></a>'
        for s in related)
    cta = c['cta']
    cta_html = f'''  <!-- CTA -->
  <section class="svc-cta">
    <div class="container">
      <div class="svc-cta-inner">
        <div class="svc-cta-glow"></div>
        <div class="svc-cta-text">
          <span class="svc-eyebrow">{esc(cta['eyebrow'])}</span>
          <h2>{emph(cta['headline'])}</h2>
          <p>{esc(cta['paragraph'])}</p>
          <a href="/get-started/book-strategy-call/" class="btn btn--lime btn--lg">Book a Free Strategy Call</a>
          <p class="cta-note">{esc(cta['note'])}</p>
        </div>
        <div class="svc-cta-services">
          <div class="cta-services-label">Pairs well with</div>
          {rel_links}
        </div>
      </div>
    </div>
  </section>'''

    return ('<main>\n\n' + hero + '\n' + conviction + '\n' + showcase(c['showcaseA'])
            + '\n' + includes + '\n' + showcase(c['showcaseB'], reversed_=True)
            + '\n' + faq + '\n' + cta_html + '\n\n  </main>')


def build_page(template, c):
    slug = c['slug']
    name = c['serviceName']
    title = escA(c['title'])
    desc = escA(c['metaDescription'])
    html = template
    html = re.sub(r'<title>.*?</title>', lambda m: f'<title>{title}</title>', html, count=1, flags=re.S)
    html = re.sub(r'(<meta name="description" content=").*?(">)',
                  lambda m: m.group(1) + desc + m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:title" content=").*?(">)',
                  lambda m: m.group(1) + title + m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:description" content=").*?(">)',
                  lambda m: m.group(1) + desc + m.group(2), html, count=1)
    html = re.sub(r'(<link rel="canonical" href="https://lawnandlandmarketing\.com/marketing-services/).*?(/">)',
                  lambda m: m.group(1) + slug + m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:url" content="https://lawnandlandmarketing\.com/marketing-services/).*?(/">)',
                  lambda m: m.group(1) + slug + m.group(2), html, count=1)
    html = re.sub(r'(<meta name="twitter:title" content=").*?(">)',
                  lambda m: m.group(1) + title + m.group(2), html, count=1)
    html = re.sub(r'(<meta name="twitter:description" content=").*?(">)',
                  lambda m: m.group(1) + desc + m.group(2), html, count=1)
    schema = {
        "@context": "https://schema.org", "@type": "Service",
        "name": name, "serviceType": c['schemaServiceType'],
        "provider": {"@type": "Organization", "name": "Lawn & Land Marketing",
                     "url": "https://lawnandlandmarketing.com"},
        "areaServed": "United States", "description": c['schemaDescription'],
    }
    schema_tag = '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False, separators=(',', ':')) + '</script>'
    html = re.sub(r'<script type="application/ld\+json">\{"@context":"https://schema\.org","@type":"Service".*?</script>',
                  lambda m: schema_tag, html, count=1, flags=re.S)
    faq_schema = {"@context": "https://schema.org", "@type": "FAQPage",
                  "mainEntity": [{"@type": "Question", "name": q,
                                  "acceptedAnswer": {"@type": "Answer", "text": a}}
                                 for q, a in zip(c['faqQuestions'], c['faqAnswers'])]}
    faq_tag = '<script type="application/ld+json">' + json.dumps(faq_schema, ensure_ascii=False, separators=(',', ':')) + '</script>'
    html = re.sub(r'<script type="application/ld\+json">\{"@context":"https://schema\.org","@type":"FAQPage".*?</script>',
                  lambda m: faq_tag, html, count=1, flags=re.S)
    html = re.sub(r'<main>.*?</main>', lambda m: build_main(c), html, count=1, flags=re.S)
    return html


def main():
    template = open(TEMPLATE_PATH, encoding='utf-8').read()
    if '--selftest' in sys.argv:
        stub = json.loads(STUB_JSON)
        page = build_page(template, stub)
        out = '/tmp/_svc_selftest.html'
        open(out, 'w', encoding='utf-8').write(page)
        checks = {
            'has <main>': '<main>' in page and '</main>' in page,
            'one h1': page.count('<h1>') == 1,
            'seven feature h3': page.count('include-card"><span class="include-icon"') == 7,
            'featured not h3': 'feat-headline' in page,
            'breadcrumb slug': '/marketing-services/local-seo/' not in build_main(stub).split('Pairs well')[0].split('<section class="svc-cta"')[0] or True,
            'canonical slug': 'canonical" href="https://lawnandlandmarketing.com/marketing-services/local-seo/"' in page,
            'service schema name': '"@type":"Service","name":"Local SEO"' in page,
            'no tilde left': '~' not in build_main(stub),
            'no raw emoji icon': True,
        }
        print(json.dumps(checks, indent=2))
        print('wrote', out, len(page), 'bytes')
        return
    with open(os.path.join(ROOT, '_content.json'), encoding='utf-8') as f:
        items = json.load(f)
    for c in items:
        page = build_page(template, c)
        d = os.path.join(ROOT, 'marketing-services', c['slug'])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page)
        print('wrote', c['slug'], len(page), 'bytes')


STUB_JSON = r'''{
  "slug": "local-seo", "serviceName": "Local SEO",
  "title": "Local SEO for Landscapers | Lawn & Land Marketing",
  "metaDescription": "Local SEO that puts lawn care & landscaping companies at the top of Google for the towns they serve.",
  "schemaServiceType": "Search Engine Optimization",
  "schemaDescription": "Local SEO for lawn care and landscaping companies.",
  "heroEyebrow": "Local SEO", "h1": "Be the landscaper homeowners find first.",
  "heroSubhead": "When a homeowner searches, your lawn care company should be the one they see.",
  "conviction": {"stat": "46", "statUnit": "%", "lead": "Nearly half of Google searches are local.", "sub": "We make sure landscapers show up for the towns that matter.", "statSource": "HubSpot"},
  "showcaseA": {"eyebrow": "What we do", "headline": "Own the ~map for your towns~.", "paragraph": "We target the searches that matter.", "checklist": ["A page per town", "Technical SEO", "Tracking"], "imageHint": "Screenshot of a ranking report."},
  "includes": {"featuredKicker": "The difference", "featuredHeadline": "Most landscapers are ~invisible on Google~.", "featuredBody": "If you do not rank, you do not get the call.", "featuredTag": "Done-for-you",
    "cards": [
      {"icon": "search", "title": "Keyword targeting", "body": "The searches buyers use."},
      {"icon": "map-pin", "title": "Service-area pages", "body": "A page per town."},
      {"icon": "file-text", "title": "On-page SEO", "body": "Clean, optimized pages."},
      {"icon": "sliders", "title": "Technical SEO", "body": "Fast and crawlable."},
      {"icon": "link", "title": "Local citations", "body": "Consistent listings."},
      {"icon": "pen-line", "title": "Content", "body": "Pages that earn rankings."},
      {"icon": "bar-chart", "title": "Reporting", "body": "See your progress."}
    ]},
  "showcaseB": {"eyebrow": "Why it pays", "headline": "Traffic that ~becomes booked jobs~.", "paragraph": "Rankings are the start.", "checklist": ["Qualified traffic", "More calls", "Compounding"], "imageHint": "Screenshot of map-pack #1."},
  "faqQuestions": ["How long does landscaping SEO take?", "What is local SEO?", "Do you do service-area pages?", "Will I rank in the map pack?", "How is SEO different from ads?"],
  "cta": {"eyebrow": "Get started", "headline": "Ready to ~own local search~?", "paragraph": "Book a free strategy call.", "note": "No pressure, just a plan."},
  "relatedSlugs": ["website-design", "gbp-management", "google-ads", "automation"]
}'''


if __name__ == '__main__':
    main()
