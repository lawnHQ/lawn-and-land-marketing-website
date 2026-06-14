# Restart Guide

Use this when coming back to the Lawn & Land website after time away.

## One-paragraph truth
The **homepage** and **all 8 `/marketing-services/*` detail pages** are built. The service
pages run off a locked template + a generator (`gen_service.py` reading `_content.json`).
The remaining non-home pages (About, Contact, the services hub, Industries, Resources) are
still intentional shells, and `/programs/*` holds an older lorem prototype not yet migrated
to the template. Nothing is launched publicly yet — staging is new.lawnlab.dev; the eventual
home is lawnandlandmarketing.com.

## Fastest restart path
Read in order:
1. `CLAUDE.md` (repo root) — the orientation file
2. `docs/website-source-of-truth/build-status.md` — what's done / not done
3. `docs/website-source-of-truth/service-page-template.md` — the locked service-page template + how pages are generated
4. `docs/website-source-of-truth/decisions.md` and `routing-rules.md`

## How to make changes
- **Header/footer** (all pages): edit `_header.html` / `_footer.html` → `python3 build.py`.
- **A service page's copy**: edit its object in `_content.json` → `python3 gen_service.py`
  → `python3 build.py`. (Don't hand-edit the generated `marketing-services/<slug>/index.html`
  — regeneration overwrites it.)
- **A new service-template section / styling**: edit `assets/css/service-page.css` and the
  generator `gen_service.py`, then regenerate. Bump the CSS `?v=` query to cache-bust.
- Verify links + header/footer sync before pushing (`python3 build.py --check`).

## Canonical routes (treat as truth)
`/marketing-services/` · `/contact/` · `/programs/...` · `/industries/...` · `/resources/...`
· `/get-started/book-strategy-call/`

Retired / keep out of internal linking: `/services/`, `/pricing/`, `/resources/guides/`,
`/resources/contact/`, and older orphans (`/team/`, `/results/`, `/good-fit/`, `/book/`).

## The next best moves
1. Finalize the 8 service pages with the owner's inputs (FAQ answers → FAQ schema; verify
   conviction stats; real images).
2. Build the Program pages on the same template approach.
3. Design + build the remaining non-home pages.

## Guardrails
- **No invented facts** — placeholders for anything unverifiable; conviction stats must be
  real + sourced.
- **Brand**: Lucide icons only (no emoji); Twilight purple never blends with green.
- Don't deploy to lawnandlandmarketing.com — not launching yet.
