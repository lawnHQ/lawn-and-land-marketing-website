# Website Source of Truth

Purpose: keep the Lawn & Land public website organized, resumable, and aligned as the build evolves.

This folder is only for the external website build.
It is intentionally separate from the broader internal company source-of-truth work.

Use this folder to answer:
- What pages are approved?
- What routes are canonical?
- What is live vs scaffolded vs killed?
- What still needs to be built?
- What website decisions have already been made?
- What competitor benchmark matters most?

Core files
- `sitemap.md` — approved sitemap for the public website
- `routing-rules.md` — canonical URL and linking rules
- `page-registry.md` — page-by-page inventory with status and notes
- `build-status.md` — current progress and highest-priority next work
- `service-page-template.md` — the locked `/marketing-services/*` template + generator
- `industry-page-template.md` — the locked `/industries/*` framework + SEO/GEO/EEAT strategy
- `navigation.md` — the universal header / nav / submenus + footer (single-source via build.py)
- `decisions.md` — durable website decisions log
- `benchmark-lawnline.md` — benchmark notes on Lawnline
- `restart-guide.md` — shortest path to regain context and resume work quickly

Status definitions
- `developed` — page has meaningful body content and feels intentionally built
- `scaffolded` — page exists, but is mostly shell/placeholder-level and needs real content
- `planned` — approved but not yet live
- `killed` — intentionally not part of this website
- `legacy` — route may still exist or leak internally but is not canonical

Operating rules
1. No new public page should be treated as approved unless it appears in `sitemap.md`.
2. No route should be treated as canonical unless it follows `routing-rules.md`.
3. If a page is killed, remove it from nav, footer, CTAs, sitemap references, and internal links.
4. When a page meaningfully changes, update `page-registry.md` and `build-status.md` in the same workstream.
5. Keep this website folder focused on the public site only; do not mix in internal ops naming.

Current restart-critical convention (updated 2026-06-15)
- Developed pages: the **homepage**, all **8 `/marketing-services/*` pages + the hub**, both **program
  pages** (Growth + the flagship Authority) + the **Programs hub**, and the first **industry page**
  (`/industries/landscaping/` — the locked template). See `page-registry.md` for the full status table.
- Current build: the **other 7 `/industries/*`** pages — roll the Landscaping framework to each
  (`industry-page-template.md`), one at a time. Still shells: `/about/`, `/contact/`, `/resources/*` —
  don't deepen shells with long copy until their design is approved or they're scheduled.
- Fastest re-entry: read `restart-guide.md`. The single most useful file overall is the repo-root `CLAUDE.md`.
