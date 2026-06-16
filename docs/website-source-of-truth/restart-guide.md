# Restart Guide

Use this when coming back to the Lawn & Land website after time away. Updated 2026-06-15.

## One-paragraph truth
The **homepage**, **all 8 `/marketing-services/*` detail pages + the services hub**, and **both
program pages** — **Growth** and the flagship **Authority** (`/programs/growth/`, `/programs/authority/`)
— are built. Service pages run off a locked template + a generator (`gen_service.py` reading
`_content.json`); the homepage, hub, and program pages are hand-built using the same `svc-*` /
`simple-hero` / `svc-cta` classes. Still to build: the **8 industry pages** (canonical 8 locked,
currently shells), and About / Contact / Resources (shells). The Programs hub is built — a simple two-program window. Nothing is launched
publicly — staging is new.lawnlab.dev (also lawnland-site.vercel.app); the eventual home is
lawnandlandmarketing.com.

## Fastest restart path — read in order
1. `CLAUDE.md` (repo root) — the master orientation file
2. `docs/website-source-of-truth/build-status.md` — what's done / not done + next priorities
3. `docs/website-source-of-truth/page-registry.md` — page-by-page status
4. `docs/website-source-of-truth/service-page-template.md` — the locked service-page template + generator
5. `docs/website-source-of-truth/decisions.md` and `routing-rules.md`

## How to make changes
- **Header/footer (all pages):** edit `_header.html` / `_footer.html` → `python3 build.py`
  (verify sync with `python3 build.py --check`).
- **A service page's copy:** edit its object in `_content.json` → `python3 gen_service.py` →
  `python3 build.py`. **Don't hand-edit** `marketing-services/<slug>/index.html` — regeneration overwrites it.
- **A program / industry / other page:** hand-edit its `index.html` (these are not generated).
  Reuse the existing `svc-*` / `simple-hero` / `svc-cta` classes for consistency.
- **CSS / template changes:** edit `assets/css/styles.css` or `service-page.css`, then **bump the
  `?v=` query sitewide** so browsers fetch fresh (current: `styles.css?v=135`, `service-page.css?v=3`).
- **Deploy:** commit + push `main` (also keep `site-foundation` in sync). GitHub Actions → Vercel,
  ~1–2 min. Verify on the live URL with a hard refresh.

## Canonical routes (treat as truth)
`/` · `/about/` · `/contact/` · `/get-started/book-strategy-call/` · `/programs/...` ·
`/marketing-services/...` · `/industries/...` (the canonical 8) · `/resources/...`

Retired / keep OUT of internal linking: `/services/`, `/pricing/`, `/resources/guides/`,
`/resources/contact/`, `/case-studies/`, `/results/`, `/team/`, `/good-fit/`, `/book/`,
`/podcast/`, `/tools/marketing-audit/`, and older orphan/article URLs.

## The next best moves
1. **Write the 8 industry pages** (`/industries/*`, canonical 8 locked; currently shells) — the next big build.
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
