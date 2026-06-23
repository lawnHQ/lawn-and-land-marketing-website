#!/usr/bin/env python3
"""
Universal header/footer builder for the Lawn & Land website.

SINGLE SOURCE OF TRUTH — edit ONLY these two files, never individual pages:
  - _header.html  -> announcement bar + main nav (the whole site header)
  - _footer.html  -> the site footer

This script stamps those partials into every page. Edit a partial, then run
this script (or just push — Vercel runs it on deploy via vercel.json), and
every page updates. You never edit the header or footer on a page again.

Usage:
  python3 build.py            # stamp partials into all pages
  python3 build.py --check    # verify pages are in sync (exit 1 if not)
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
SKIP_DIRS = {'.git', 'node_modules', 'docs', '.github', 'redirect-manager'}

# (partial file, regex that matches that block inside a page)
PARTIALS = [
    ('_header.html', re.compile(r'<div class="announcement-bar">.*?</nav>', re.S)),
    ('_footer.html', re.compile(r'<footer class="footer-v2">.*?</footer>', re.S)),
]


def read(path):
    with open(path, encoding='utf-8') as f:
        return f.read()


def load_partials():
    loaded = []
    for fname, regex in PARTIALS:
        path = os.path.join(ROOT, fname)
        if not os.path.exists(path):
            sys.exit(f"ERROR: missing partial {fname}")
        content = read(path).strip()
        if not regex.match(content):
            sys.exit(f"ERROR: {fname} does not look like a valid block (must match its tag)")
        loaded.append((fname, regex, content))
    return loaded


def find_pages():
    pages = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith('.html') and not fn.startswith('_') and fn != 'PAGE_TEMPLATE.html':
                pages.append(os.path.join(dirpath, fn))
    return sorted(pages)


def main():
    check_only = '--check' in sys.argv
    partials = load_partials()
    pages = find_pages()

    changed, out_of_sync = [], []
    for page in pages:
        rel = os.path.relpath(page, ROOT)
        src = read(page)
        new = src
        for fname, regex, content in partials:
            if regex.search(new):
                new = regex.sub(lambda m: content, new, count=1)
        if new != src:
            if check_only:
                out_of_sync.append(rel)
            else:
                with open(page, 'w', encoding='utf-8') as f:
                    f.write(new)
                changed.append(rel)

    if check_only:
        if out_of_sync:
            print("OUT OF SYNC (%d) — run `python3 build.py`:" % len(out_of_sync))
            for p in out_of_sync:
                print("  ", p)
            sys.exit(1)
        print("All %d pages in sync with _header.html / _footer.html ✓" % len(pages))
        return

    print("Stamped universal header + footer into %d pages." % len(pages))
    if changed:
        print("Updated %d page(s):" % len(changed))
        for p in changed:
            print("  ", p)
    else:
        print("All pages were already in sync — nothing to update.")


if __name__ == '__main__':
    main()
