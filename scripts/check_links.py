#!/usr/bin/env python3
"""Asset-integrity guard for the live site.

Scans every committed .html and .css file and verifies that each LOCAL asset it
references (images, css, js, fonts, pdf, etc.) actually exists on disk. Catches
the class of regression we hit during the WordPress migration: broken <img>
sources, renamed files, and stale CSS url() backgrounds reaching production.

External URLs, mailto/tel, data: URIs, and extensionless "pretty" page links
(handled by Vercel rewrites/redirects) are intentionally skipped. Exits non-zero
with a list if anything is missing, so CI fails before a bad deploy.
"""
import re, sys, os, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

ASSET_EXT = ('.webp', '.jpg', '.jpeg', '.png', '.svg', '.ico', '.gif', '.avif',
             '.css', '.js', '.mjs', '.pdf', '.woff', '.woff2', '.ttf',
             '.xml', '.txt', '.json', '.mp4', '.webm')
SKIP_PREFIX = ('http://', 'https://', '//', 'data:', 'mailto:', 'tel:', 'javascript:', '#')

ref_re = re.compile(r'(?:src|href)\s*=\s*"([^"]+)"')
url_re = re.compile(r'url\(\s*[\'"]?([^\'")]+)')


def refs(text):
    for m in ref_re.finditer(text):
        yield m.group(1)
    for m in url_re.finditer(text):
        yield m.group(1)


def main():
    files = [f for f in glob.glob('**/*.html', recursive=True) + glob.glob('**/*.css', recursive=True)
             if 'redirect-manager' not in f and 'node_modules' not in f]
    missing = []
    for f in files:
        base = os.path.dirname(f)
        text = open(f, encoding='utf-8', errors='ignore').read()
        for ref in refs(text):
            clean = ref.split('#')[0].split('?')[0].strip()
            if not clean or clean.startswith(SKIP_PREFIX):
                continue
            if os.path.splitext(clean)[1].lower() not in ASSET_EXT:
                continue
            path = clean.lstrip('/') if clean.startswith('/') else os.path.normpath(os.path.join(base, clean))
            if not os.path.exists(path):
                missing.append(f"{f}  ->  {ref}")

    if missing:
        print(f"❌ BROKEN ASSET REFERENCES ({len(set(missing))}):")
        for m in sorted(set(missing))[:150]:
            print("   " + m)
        sys.exit(1)
    print(f"✅ all asset references resolve ({len(files)} html/css files scanned)")


if __name__ == '__main__':
    main()
