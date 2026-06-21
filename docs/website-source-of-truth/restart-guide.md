# Restart Guide

Use this when coming back to the Lawn & Land website after time away. Updated 2026-06-15.

## One-paragraph truth
The **homepage**, **all 8 `/marketing-services/*` detail pages + the services hub**, **both program
pages** (**Growth** + the flagship **Authority**), the **Programs hub**, and the first **industry page**
(`/industries/landscaping/` — the locked template) are built. Service pages run off a locked template +
a generator (`gen_service.py` reading `_content.json`); the homepage, hub, program pages, and industry
pages are hand-built using the same `simple-hero` / `svc-*` / `svc-cta` classes (industry pages add a
reusable `.ind-*` block — see `industry-page-template.md`). Still to build: the **other 7 industry
pages** (canonical 8 locked; currently shells), and About / Contact / Resources (shells). The 2026-06-15
nav-submenu overhaul is done (see `navigation.md`). Nothing is launched publicly — staging is
new.lawnlab.dev (also lawnland-site.vercel.app); the eventual home is lawnandlandmarketing.com.

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
  `?v=` query sitewide** so browsers fetch fresh (current: `styles.css?v=138`, `service-page.css?v=3`).
- **Deploy:** commit + push `main` (also keep `site-foundation` in sync). GitHub Actions → Vercel,
  ~1–2 min. Verify on the live URL with a hard refresh.

## Canonical routes (treat as truth)
`/` · `/about/` · `/contact/` · `/get-started/book-strategy-call/` · `/programs/...` ·
`/marketing-services/...` · `/industries/...` (the canonical 8) · `/resources/...` ·
`/case-studies/...` (page 1: `/case-studies/precision/`)

Retired / keep OUT of internal linking: `/services/`, `/pricing/`, `/resources/guides/`,
`/resources/contact/`, `/results/`, `/team/`, `/good-fit/`, `/book/`,
`/podcast/`, `/tools/marketing-audit/`, and older orphan/article URLs.

## The next best moves
1. **Roll the industry-page framework to the remaining 7** (`industry-page-template.md`; Landscaping is
   built and is the template) — one at a time, each with its own researched seasonality + FAQ.
2. Finalize the 8 service pages with owner inputs (FAQ answers → FAQ schema; verify conviction
   stats; real images).
3. Design + build About / Contact / Resources.

## Guardrails
- **No pricing** anywhere — every CTA → the free strategy call.
- **No invented facts** — placeholders for anything unverifiable; conviction stats real + sourced.
- **Brand:** Lucide icons only (no emoji); Twilight `#6837EF` never blends with green; the `.hl`
  marker is one impact phrase per surface.
- **Don't deploy to lawnandlandmarketing.com** — not launching yet.
- Keep these docs current in the same workstream as any structural change.
