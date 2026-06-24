# Lawn & Land Marketing — Website

The future public website for **Lawn & Land Marketing**, a digital-marketing agency working
**exclusively with green-industry / lawn care & landscaping companies**. Static, multi-page,
hand-built HTML/CSS/JS (no framework).

- **Live staging:** https://new.lawnlab.dev (also the Vercel project domain
  https://lawnland-site.vercel.app — same deploy). Both reflect `main`.
- **Production (not launched yet):** lawnandlandmarketing.com
- **Deploy:** push to `main` → GitHub Actions (`.github/workflows/deploy.yml`) → Vercel production
  (~1–2 min). Auth-protected Vercel previews are auto-created per branch.
- **Branches:** all progress lives on `main`; the working branch is `site-foundation`, kept in sync —
  push to **both** (`origin site-foundation` then `origin site-foundation:main`).

> **Read `CLAUDE.md` (repo root) first** — it's the full, current orientation for any session.
> The deep source-of-truth docs live in `docs/website-source-of-truth/` (start with `restart-guide.md`,
> then `page-registry.md` for the authoritative per-page status).

## Universal header & footer (single source)
The header (announcement bar + nav) and footer are defined once and stamped into every page.
Never edit them on individual pages.
- Edit the header → `_header.html` · Edit the footer → `_footer.html`
- Apply to all pages → `python3 build.py` · Verify sync → `python3 build.py --check`

`vercel.json` runs `build.py` on every deploy, so editing a partial and pushing updates every page.
One page is exempt by design: `/get-started/book-strategy-call/` runs stripped minimal chrome (it
uses non-`.announcement-bar` / non-`.footer-v2` markup, so `build.py` skips it). Full nav / submenu +
footer reference: `docs/website-source-of-truth/navigation.md`.

## Service pages are generated; everything else is hand-built
The 8 `/marketing-services/*` detail pages are **generated**, not hand-edited:
- Copy lives in **`_content.json`** (one object per service).
- `python3 gen_service.py` renders each `marketing-services/<slug>/index.html` from the
  `website-design` page as the structural template, generating all internal links by construction.
- Then `python3 build.py` stamps the header/footer. **Don't hand-edit generated service HTML.**

The homepage, the services hub, the program pages, the **industry pages**, the **case studies**, and
the **client-results roster** are **hand-built** (reusing the shared `styles.css` + `service-page.css`
classes — `svc-*`, `simple-hero`, `svc-cta` — plus `industry.css` for `/industries/*` and inline
`.cs-*` / `.cr-*` for the case studies and roster). `PAGE_TEMPLATE.html` is the blank-page scaffold.
Specs: `service-page-template.md`, `industry-page-template.md`, `case-study-template.md`.

## Current state at a glance
**The site is content-complete and in pre-launch review.** Developed:
- **Homepage** (`/`) — the benchmark page.
- **Marketing Services:** the hub + all **8 detail pages** (generated).
- **Programs:** the hub + **Growth** and the flagship **Authority**.
- **Industries:** the hub + all **canonical 8** (landscaping, lawn-care, lawn-maintenance,
  outdoor-living, land-clearing, excavation, septic-installation, holiday-lighting).
- **About** (+ `#team`), **Contact** (live GHL form), **Confirmation**, **Get Started / Book a Call**.
- **Legal:** Terms of Use, Privacy Policy.
- **Resources** (content pages under the `/resources/` SEO silo — there is no hub page):
  Blog, Experiences & Reviews, Mow Money Podcast.
- **Case Studies** (`/case-studies/`): **Precision** and **Rock Solid** (built on the locked
  `case-study-template.md`).
- **Client Results** roster (`/client-results/`) — tiered case-studies + client roster, under About.

**Landed (2026-06-21):** real FAQ answers + `FAQPage` schema on all 8 service pages, verified
conviction stats (Google Ads now L&L's own 8-12% conversion rate), the `og:image` share graphic
sitewide, About team headshots, and Precision + Rock Solid case-study sign-offs.

**Launch prep still pending (see `seo-launch-checklist.md`):** real images for the labeled
placeholders, `robots.txt`, and the staging→production canonical/`og` flip. More case studies (e.g.
From The Ground Up) slot into the framework as they're approved.

See `docs/website-source-of-truth/page-registry.md` for the full per-page status table.

## Canonical routes (truth)
`/` · `/about/` (+ `#team`) · `/client-results/` · `/contact/` · `/get-started/book-strategy-call/` ·
`/programs/...` · `/marketing-services/...` (8 + hub) · `/industries/...` (the canonical 8 + hub) ·
`/case-studies/...` (precision, rock-solid) · `/resources/...` (blog, experiences-reviews,
mow-money-mow-problems-podcast — silo only, **no `/resources/` index page**) · `/terms/` · `/privacy-policy/`.

**Retired — keep out of internal linking** (`routing-rules.md`): `/services/`, `/pricing/`,
`/resources/guides/`, `/resources/contact/`, `/resources/meet-the-team/` (→ `/about/#team`),
`/resources/private-facebook-group/` (→ the external FB group), `/results/`, `/team/`, `/good-fit/`,
`/book/`, `/podcast/`, `/tools/marketing-audit/`. (Note: `/case-studies/` was reintroduced 2026-06-21
and is **no longer retired**.)

## Non-negotiables
- **No pricing** anywhere (every CTA → the free strategy call). **No invented facts** (placeholders
  for anything unverifiable; conviction stats real + sourced; client revenue/ROI owner-confirmed).
- **Brand:** Lucide stroke icons only (no emoji); Twilight `#6837EF` never blends with green; the
  `.hl` Twilight marker is one impact phrase per surface and `font-weight: inherit` (matches the
  heading weight). **Em-dash-free** body copy. City/county names carry a 2-letter state code.

## Repo structure
```text
├── CLAUDE.md                       # Orientation — read first (auto-loaded by Claude Code)
├── README.md                       # This file
├── index.html                      # Homepage (developed benchmark)
├── _header.html  _footer.html      # Universal header/footer partials (stamped by build.py)
├── PAGE_TEMPLATE.html              # Blank-page scaffold ({{PAGE_TITLE}}/{{H1}}; build.py skips it)
├── build.py                        # Stamps header/footer into every page
├── gen_service.py  _content.json   # Generates the 8 marketing-services pages
├── sitemap.xml                     # Real route sitemap (production domain; launch artifact)
├── about/  contact/  confirmation/ strategy-booked/ programs/ # all developed
├── get-started/book-strategy-call/ # the booking CTA destination (minimal-chrome, build.py-exempt)
├── marketing-services/             # 8 detail pages (generated) + hub (hand-built)
├── industries/                     # hub + the canonical 8 (all developed)
├── case-studies/                   # precision/ + rock-solid/ (hand-built from case-study-template)
├── client-results/                 # the tiered roster (under About)
├── resources/                      # blog/ experiences-reviews/ mow-money-mow-problems-podcast/ (silo, no hub)
├── terms/  privacy-policy/         # legal
├── assets/css/{styles.css, service-page.css, industry.css}   js/main.js   images/  videos/  logos/
├── docs/website-source-of-truth/   # the durable docs
└── .github/workflows/deploy.yml    # push main → Vercel production
```

## Working rules
- This repo is the website source of truth; every change goes through git.
- Push `main` to deploy; keep `site-foundation` in sync (push both). Don't deploy via Vercel CLI as
  the normal workflow, and **don't deploy to the production domain** — not launching yet.
- Don't reintroduce retired routes. Keep `docs/website-source-of-truth/` current in the same
  workstream as any structural change.
