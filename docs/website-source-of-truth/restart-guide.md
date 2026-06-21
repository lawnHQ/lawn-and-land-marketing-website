# Restart Guide

Use this when coming back to the Lawn & Land website after time away. Updated 2026-06-21.

## One-paragraph truth
**The site is content-complete and in pre-launch review.** Built: the **homepage**; all **8
`/marketing-services/*`** detail pages + the services hub; **both programs** (Growth + the flagship
Authority) + the Programs hub; all **8 industry pages** + the Industries hub; **About** (+ `#team`),
**Contact** (live GHL form), **Confirmation**, **Get Started / booking**; **Terms + Privacy**; the **3
Resources content pages** (blog, experiences-reviews, podcast — under the `/resources/` SEO silo, no hub
page); **2 case studies** (`/case-studies/` — Precision + Rock Solid, on the locked `case-study-template.md`);
and the **Client Results** roster (`/client-results/`). Service pages run off a locked template + a
generator (`gen_service.py` reading `_content.json`); everything else is hand-built (reusing
`simple-hero` / `svc-*` / `svc-cta`, plus `.ind-*` for industries and `.cs-*` / `.cr-*` for the case
studies + roster). What's left is **launch prep + owner inputs** (see `build-status.md`), not new pages.
Nothing is launched publicly — staging is new.lawnlab.dev (also lawnland-site.vercel.app); the eventual
home is lawnandlandmarketing.com.

## Fastest restart path — read in order
1. `CLAUDE.md` (repo root) — the master orientation file
2. `docs/website-source-of-truth/build-status.md` — what's done / not done + next priorities
3. `docs/website-source-of-truth/page-registry.md` — page-by-page status
4. `docs/website-source-of-truth/service-page-template.md` — the locked service-page template + generator
5. `docs/website-source-of-truth/industry-page-template.md` — the locked industry-page framework + SEO/GEO/EEAT strategy
6. `docs/website-source-of-truth/navigation.md` — the universal header / nav / submenus + footer
7. `docs/website-source-of-truth/decisions.md` and `routing-rules.md`

## How to make changes
- **Header/footer (all pages):** edit `_header.html` / `_footer.html` → `python3 build.py`
  (verify sync with `python3 build.py --check`).
- **A service page's copy:** edit its object in `_content.json` → `python3 gen_service.py` →
  `python3 build.py`. **Don't hand-edit** `marketing-services/<slug>/index.html` — regeneration overwrites it.
- **A program / industry / other page:** hand-edit its `index.html` (these are not generated).
  Reuse the existing `svc-*` / `simple-hero` / `svc-cta` classes for consistency.
- **CSS / template changes:** edit `assets/css/styles.css` or `service-page.css`, then **bump the
  `?v=` query sitewide** so browsers fetch fresh (current: `styles.css?v=141`, `main.js?v=54`, `service-page.css?v=3`, `industry.css?v=2`).
- **Deploy:** commit + push `main` (also keep `site-foundation` in sync). GitHub Actions → Vercel,
  ~1–2 min. Verify on the live URL with a hard refresh.

## Canonical routes (treat as truth)
`/` · `/about/` (+ `#team`) · `/client-results/` · `/contact/` · `/get-started/book-strategy-call/` ·
`/programs/...` · `/marketing-services/...` (8 + hub) · `/industries/...` (the canonical 8 + hub) ·
`/case-studies/...` (precision, rock-solid) · `/resources/...` (blog, experiences-reviews, podcast — silo,
no hub page) · `/terms/` · `/privacy-policy/`

Retired / keep OUT of internal linking: `/services/`, `/pricing/`, `/resources/guides/`,
`/resources/contact/`, `/results/`, `/team/`, `/good-fit/`, `/book/`,
`/podcast/`, `/tools/marketing-audit/`, and older orphan/article URLs.

## The next best moves (launch prep, not new pages)
1. Land the **service-page owner inputs** (FAQ answers → `FAQPage` schema; verify conviction stats; real images).
2. Drop **real images** into the labeled placeholders sitewide.
3. Get **client sign-offs** on the case studies; add **more case studies** to the framework as approved.
4. **Launch cutover** to lawnandlandmarketing.com (later) — `seo-launch-checklist.md`.

## Guardrails
- **No pricing** anywhere — every CTA → the free strategy call.
- **No invented facts** — placeholders for anything unverifiable; conviction stats real + sourced.
- **Brand:** Lucide icons only (no emoji); Twilight `#6837EF` never blends with green; the `.hl`
  marker is one impact phrase per surface.
- **Don't deploy to lawnandlandmarketing.com** — not launching yet.
- Keep these docs current in the same workstream as any structural change.
