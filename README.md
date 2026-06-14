# Lawn & Land Marketing Website

Live site: https://new.lawnlab.dev
Vercel project: new-lawnlab-deploy
Auto-deploy: push to `main` -> GitHub Actions -> Vercel production

## What this repo is

This repo is the source of truth for the public Lawn & Land website.

Important: this website project is separate from any internal Ground Control concept or naming.

## Universal header & footer (single source of truth)

The site **header** (announcement bar + nav) and **footer** are defined once and
stamped into every page automatically. You never edit them on individual pages.

- Edit the header → `_header.html`  (announcement bar + main nav)
- Edit the footer → `_footer.html`
- Apply to all pages → `python3 build.py`
- Verify everything is in sync → `python3 build.py --check`

`vercel.json` runs `build.py` on every deploy, so editing a partial and pushing
is enough — every page updates. Change one file, the whole site updates.

## Service pages are generated

The 8 `/marketing-services/*` detail pages are **generated**, not hand-edited:

- Copy lives in **`_content.json`** (one object per service).
- **`python3 gen_service.py`** renders each `marketing-services/<slug>/index.html` from the
  `website-design` page as the structural template, generating all internal links
  (breadcrumb, CTAs, "pairs well with", hero image) by construction.
- Then run `python3 build.py` to stamp the universal header/footer.

Edit copy in `_content.json` and regenerate — don't hand-edit the generated HTML.
Full spec: `docs/website-source-of-truth/service-page-template.md`.

## Current state at a glance

> Full orientation for any session lives in **`CLAUDE.md`** (repo root). Quick version:

**Developed:** the homepage **and all 8 `/marketing-services/*` detail pages**, built on a
locked, generated template (see `docs/website-source-of-truth/service-page-template.md`):
website-design, local-seo, google-ads, meta-ads, gbp-management, your-ai-partner,
reputation-management, automation.

The **marketing-services hub** (`/marketing-services/`) is also built — the SEO silo page
(4 featured services + a wrap-up grid linking all 8) with the "one machine" framing.

**Still shells** (header + hero + blank body + CTA/footer): `/about/`, `/contact/`,
`/industries/*`, `/resources/*`. `/programs/*` holds an older lorem prototype, not yet
migrated to the template.

The 8 service pages await three owner inputs to be final: real FAQ answers, verified
conviction stats, and real images for the labeled placeholders.

Don't deepen the remaining shell pages with long copy until their design is approved, and
don't reintroduce retired routes.

## Canonical route rules

Use these routes as truth:
- `/marketing-services/` = canonical services hub
- `/contact/` = canonical contact route
- `/programs/...` = canonical program routes
- `/industries/...` = canonical industry routes
- `/resources/...` = canonical resource routes
- `/get-started/book-strategy-call/` = canonical primary CTA destination

Retired / non-canonical routes:
- `/services/`
- `/pricing/`
- `/resources/guides/`
- `/resources/contact/`
- older orphan routes like `/team/`, `/results/`, `/good-fit/`, `/book/`, and older article URLs should stay out of internal linking unless intentionally brought back

## What was already cleaned up

Structural cleanup already completed in this repo:
- `/services/` internal references replaced with `/marketing-services/`
- `/resources/contact/` internal references replaced with `/contact/`
- `/resources/guides/` removed from internal structure
- stale internal orphan links cleaned out of the internal link graph
- `resources/contact/index.html` deleted
- `resources/guides/index.html` deleted
- nav / footer / 404 / duplicated HTML were cleaned for route hygiene

## Where to restart quickly

Start here, in order:
1. `CLAUDE.md` (repo root) — the orientation file (auto-loaded by Claude Code)
2. `docs/website-source-of-truth/build-status.md` — what's done / not done
3. `docs/website-source-of-truth/service-page-template.md` — the locked service-page template + generator
4. `docs/website-source-of-truth/decisions.md` and `routing-rules.md`
5. `docs/website-source-of-truth/restart-guide.md`

Those docs are the fastest way to recover context.

## Repo structure

```text
├── CLAUDE.md                           # Orientation file — read this first
├── index.html                          # Homepage (developed benchmark page)
├── _header.html  _footer.html          # Universal header/footer partials (stamped by build.py)
├── build.py                            # Stamps header/footer into every page
├── gen_service.py  _content.json       # Generates the 8 marketing-services pages
├── about/  contact/  programs/
├── get-started/book-strategy-call/
├── marketing-services/                 # 8 detail pages (generated) + hub (shell)
├── industries/  resources/
├── assets/
│   ├── css/styles.css                  # global (incl. nav)
│   ├── css/service-page.css            # service-page template (svc-*)
│   ├── js/main.js   images/   logos/
├── docs/website-source-of-truth/
└── .github/workflows/deploy.yml
```

## Working rules

- This repo is the website source of truth.
- Every change should go through git.
- Push to `main` deploys production.
- Do not deploy directly with Vercel CLI as the normal workflow.
- Do not reintroduce retired routes unless there is an explicit new decision.
- Do not deepen non-home page bodies until design direction is approved.
- If restarting later, update the docs in `docs/website-source-of-truth/` in the same workstream as any structural decision.

## Recommended next phase

1. Finalize the 8 service pages with owner inputs: real FAQ answers (then add FAQ schema),
   verified conviction stats, real images for the placeholders.
2. Build the **Program pages** (`/programs/*`) on the same template approach (no pricing).
3. Design + build the remaining non-home pages (About, Contact, services hub, Industries,
   Resources).
4. Eventually: launch cutover to lawnandlandmarketing.com (not yet).

## Deployment

GitHub Actions workflow:
- `.github/workflows/deploy.yml`
- pushes to `main` trigger Vercel production deploy

## Maintainer note for future restart

If you come back cold later, assume this:
- homepage = developed benchmark page
- all 8 `/marketing-services/*` detail pages = built on the locked, generated template
  (edit `_content.json` + run `gen_service.py`), pending owner inputs (FAQ answers, stat
  verification, images)
- everything else (About, Contact, services hub, Industries, Resources) = intentionally
  held shell; `/programs/*` = older lorem prototype not yet on the template
- route hygiene + universal header/footer + service-page tooling are all in place
- read `CLAUDE.md` first
