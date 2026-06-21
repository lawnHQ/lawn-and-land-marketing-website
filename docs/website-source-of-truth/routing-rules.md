# Routing Rules

## Canonical Rules
- Canonical contact route is `/contact/`.
- Canonical service hub is `/marketing-services/`.
- Canonical service detail pages live under `/marketing-services/...`.
- Programs live under `/programs/...`.
- Industry pages live under `/industries/...`.
- Resource pages live under `/resources/...` except contact, which is top-level at `/contact/`.
- Case studies live under `/case-studies/...` (reintroduced 2026-06-21 per builder directive; previously killed). No index page exists at `/case-studies/` itself yet, so its breadcrumb crumb is a non-link label. First page: `/case-studies/precision/`.

## Killed Routes
These should not appear in nav, footer, CTAs, page copy, breadcrumbs, sitemap planning docs, or internal links.
- `/services/`
- `/pricing/`
- `/resources/guides/`

## Legacy Routes
These are legacy or non-canonical and should be removed from internal linking or redirected intentionally.
- `/resources/contact/` → use `/contact/`
- legacy service detail routes under `/services/...`
- any pricing references that imply `/pricing/` is a live page

## Sitewide Link Hygiene Rules
1. Main navigation must point Marketing Services to `/marketing-services/`, not `/services/`.
2. Footer service links must point to `/marketing-services/...` routes only.
3. Contact links should resolve to `/contact/` unless a specific CTA should go directly to `/get-started/book-strategy-call/`.
4. Killed pages should not remain discoverable through 404 pages, popular links, or footer lists.
5. If a route is intentionally retired, document it in `decisions.md` and remove it from `page-registry.md` as canonical.

## Cleanup Status
- Main nav now points Marketing Services to `/marketing-services/`.
- Homepage service CTAs now use `/marketing-services/...` child routes.
- Internal linking no longer exposes `/resources/contact/`.
- `/resources/guides/` has been removed from internal structure and the page file was deleted.
- 404 page has been cleaned so it no longer promotes the retired service/contact/guides routes.

## Launch redirects (301)
- **`/precision-case-study/` → `/case-studies/precision/`** — the old WordPress case study is indexed and has history; preserve it with a 301 at launch. (Set alongside the canonical flip from `new.lawnlab.dev` to `lawnandlandmarketing.com`.)
- **`/rock-solid-case-study/` → `/case-studies/rock-solid/`** — same: the old indexed WordPress case study gets a 301 to the new URL at launch.

## Remaining Link QA To Handle Later
- Decide whether any retired routes should eventually receive redirects at the hosting layer.
- If a route is intentionally reintroduced later, record that decision before adding it back into internal linking.

## Killed routes — fuller list (keep out of nav, footer, CTAs, copy, breadcrumbs, sitemap, links)
`/services/` (+ children) · `/pricing/` · `/resources/guides/` · `/resources/contact/` ·
`/results/` · `/team/` · `/good-fit/` · `/book/` · `/podcast/` ·
`/tools/marketing-audit/` · older orphan/article URLs. Use the canonical equivalents instead
(`/case-studies/` was reintroduced 2026-06-21 as an approved silo and is no longer killed)
(`/marketing-services/...`, `/contact/`, `/resources/...`, `/get-started/book-strategy-call/`).

## Current build convention (updated 2026-06-15)
- Developed: the homepage, the 8 `/marketing-services/*` pages + hub, and both program pages
  (`/programs/growth/`, `/programs/authority/`).
- Still shells (don't deepen with long copy until their design is approved or they're scheduled):
  the 8 `/industries/*` pages, `/about/`, `/contact/`, and `/resources/*`.
  (The 8 industry pages are the next scheduled build.)
- See `page-registry.md` for per-page status and `build-status.md` for priorities.
