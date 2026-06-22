#!/usr/bin/env python3
"""Generate FAQPage JSON-LD for blog posts from their visible FAQ block.

The blog FAQ is rendered as:
    <div class="article-faq">
      <div class="faq-item"><h3>Question?</h3><p>Answer.</p></div>
      ...
    </div>
This scans every resources/blog/<slug>/index.html, extracts those Q&A pairs, and
injects (or refreshes) a FAQPage <script type="application/ld+json"> in the <head>
so the FAQ is eligible for rich results / AI extraction.

Idempotent: re-running strips any existing FAQPage block and rebuilds it from the
current visible FAQ, so the schema text always matches what's on the page. Run this
after writing or importing posts (it is part of the blog framework, alongside the
per-post BlogPosting schema that links author -> #matt-foreman).
"""
import re, os, json, html

ROOT = os.path.dirname(os.path.abspath(__file__))
BLOG = os.path.join(ROOT, 'resources', 'blog')


def strip_tags(t):
    return html.unescape(re.sub(r'<[^>]+>', '', t)).strip()


def extract_faq(s):
    items = []
    for m in re.finditer(r'<div class="faq-item"><h3>(.*?)</h3>\s*<p>(.*?)</p>\s*</div>', s, re.S):
        q, a = strip_tags(m.group(1)), strip_tags(m.group(2))
        if q and a:
            items.append((q, a))
    return items


def faqpage_ld(items):
    obj = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ],
    }
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(',', ':')) + '</script>'


def strip_existing_faqpage(s):
    for m in re.finditer(r'\s*<script type="application/ld\+json">(.*?)</script>', s, re.S):
        if '"@type":"FAQPage"' in m.group(1) or '"@type": "FAQPage"' in m.group(1):
            s = s.replace(m.group(0), '')
    return s


def main():
    if not os.path.isdir(BLOG):
        print("no blog dir found at", BLOG)
        return
    count = 0
    for slug in sorted(os.listdir(BLOG)):
        p = os.path.join(BLOG, slug, 'index.html')
        if not os.path.isfile(p):
            continue
        s = open(p, encoding='utf-8').read()
        items = extract_faq(s)
        s = strip_existing_faqpage(s)
        if items:
            s = s.replace('</head>', '  ' + faqpage_ld(items) + '\n</head>', 1)
            print(f"  {slug}: FAQPage ({len(items)} Q&A)")
            count += 1
        else:
            print(f"  {slug}: no FAQ block, skipped")
        open(p, 'w', encoding='utf-8').write(s)
    print(f"done: FAQPage written on {count} post(s)")


if __name__ == '__main__':
    main()
