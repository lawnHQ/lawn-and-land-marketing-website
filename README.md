# Lawn & Land Marketing — Website

The future public website for **Lawn & Land Marketing**, a digital-marketing agency working
**exclusively with green-industry / lawn care & landscaping companies**. Static, multi-page,
hand-built HTML/CSS/JS (no framework).

- **Live staging:** https://new.lawnlab.dev (also the Vercel project domain
  https://lawnland-site.vercel.app — same deploy). Both reflect `main`.
- **Production (not launched yet):** lawnandlandmarketing.com
- **Deploy:** push to `main` → GitHub Actions (`.github/workflows/deploy.yml`) → Vercel production
  (~1–2 min). Auth-protected Vercel previews are auto-created per branch.

> **Read `CLAUDE.md` (repo root) first** — it's the full, current orientation for any session.
> The deep source-of-truth docs live in `docs/website-source-of-truth/`.

## Universal header & footer (single source)
The header (announcement bar + nav) and footer are defined once and stamped into every page.
Never edit them on individual pages.
- Edit the header → `_header.html` · Edit the footer → `_footer.html`
- Apply to all pages → `python3 build.py` · Verify sync → `python3 build.py --check`

`vercel.json` runs `build.py` on every deploy, so editing a partial and pushing updates every page.
Full nav / submenu + footer reference: `docs/website-source-of-truth/navigation.md`.

## Service pages are generated
The 8 `/marketing-services/*` detail pages are **generated**, not hand-edited:
- Copy lives in **`_content.json`** (one object per service).
- `python3 gen_service.py` renders each `marketing-services/<slug>/index.html` from the
  `website-design` page as the structural template, generating all internal links by construction.
- Then `python3 build.py` stamps the header/footer.

Don't hand-edit generated service HTML — regeneration overwrites it. The homepage, the services hub,
the program pages, and the **industry pages** are **hand-built** (reusing the same `svc-*` / `simple-hero` /
`svc-cta` classes). Specs: `docs/website-source-of-truth/service-page-template.md` (services) and
`industry-page-template.md` (industries).

## Current state at a glance
**Developed:** the homepage · all 8 `/marketing-services/*` detail pages + the `/marketing-services/`
hub · both program pages — **Growth** (`/programs/growth/`) and the flagship **Authority**
(`/programs/authority/`) — and the **Programs hub** (`/programs/`) · the first **industry page**
(`/industries/landscaping/` — the locked template; see `industry-page-template.md`).

**Current build / next up:** the **other 7 `/industries/*`** pages (canonical 8 locked) — roll the
Landscaping framework to each, one at a time · `/about/`, `/contact/`, and `/resources/*` (shells).
The 8 service pages await owner inputs (real FAQ answers → FAQ schema, verified conviction stats, real images).

See `docs/website-source-of-truth/page-registry.md` for the full per-page status table.

## Canonical routes (truth)
`/` · `/about/` · `/contact/` · `/get-started/book-strategy-call/` · `/programs/...` ·
`/marketing-services/...` · `/industries/...` (the canonical 8) · `/resources/...`

**Retired — keep out of internal linking:** `/services/`, `/pricing/`, `/resources/guides/`,
`/resources/contact/`, `/case-studies/`, `/results/`, `/team/`, `/good-fit/`, `/book/`, `/podcast/`,
`/tools/marketing-audit/`, and older orphan/article URLs.

## Non-negotiables
- **No pricing** anywhere (every CTA → the free strategy call). **No invented facts** (placeholders
  for anything unverifiable; conviction stats real + sourced).
- **Brand:** Lucide stroke icons only (no emoji); Twilight `#6837EF` never blends with green; the
  `.hl` Twilight marker is one impact phrase per surface. City/county names carry a state code.

## Repo structure
```text
├── CLAUDE.md                       # Orientation — read first (auto-loaded by Claude Code)
├── README.md                       # This file
├── index.html                      # Homepage (developed benchmark)
├── _header.html  _footer.html      # Universal header/footer partials (stamped by build.py)
├── build.py                        # Stamps header/footer into every page
├── gen_service.py  _content.json   # Generates the 8 marketing-services pages
├── sitemap.xml                     # Real route sitemap (production domain; launch artifact)
├── about/  contact/  programs/     # growth + authority + hub = developed
├── get-started/book-strategy-call/ # the booking CTA destination
├── marketing-services/             # 8 detail pages (generated) + hub (hand-built, developed)
├── industries/                     # hub + canonical 8 (landscaping developed; other 7 shells)
├── resources/                      # hub + 5 (shells)
├── assets/css/{styles.css, service-page.css}   js/main.js   images/  logos/
├── docs/website-source-of-truth/   # the durable docs
└── .github/workflows/deploy.yml    # push main → Vercel production
```

## Working rules
- This repo is the website source of truth; every change goes through git.
- Push `main` to deploy; keep `site-foundation` in sync (push both). Don't deploy via Vercel CLI as
  the normal workflow, and **don't deploy to the production domain** — not launching yet.
- Don't reintroduce retired routes or deepen shell pages with long copy until their design is approved.
- Keep `docs/website-source-of-truth/` current in the same workstream as any structural change.
