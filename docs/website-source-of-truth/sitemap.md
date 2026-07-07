# Approved Website Sitemap

Last updated: 2026-06-24. This is the **approved route list**. For per-page build status
(developed / shell), see `page-registry.md`. For the generated XML, see repo-root `sitemap.xml`.
The Industries section below is the **canonical 8 (locked)**. Ancillary utility pages like legal
pages can exist outside this list.

## Core
- `/` — Home
- `/about/` — About
- `/matt-foreman/` — Matt Foreman entity hub (canonical personal page; replaced `/author/matt-foreman/`, 301'd)
- `/client-results/` — Client Results (tiered roster + featured case studies; nested under About; added 2026-06-21)
- `/contact/` — Contact
- `/get-started/book-strategy-call/` — Get Started / Book Strategy Call
- `/confirmation/` — post-form thank-you page (**noindex** — intentionally omitted from `sitemap.xml`; search engines shouldn't index a thank-you page, but it's tracked here + in GitHub)
- `/strategy-booked/` — post-booking thank-you page (**noindex** — intentionally omitted from public `sitemap.xml`; included here as the internal sitemap/source-of-truth route for the GHL completed-booking redirect + GA4 `booking_confirmation_view`)

## Programs
- `/programs/` — Programs hub
- `/programs/growth/` — Growth
- `/programs/authority/` — Authority

## Marketing Services
- `/marketing-services/` — Marketing Services hub
- `/marketing-services/website-design/` — Website Design
- `/marketing-services/local-seo/` — Local SEO
- `/marketing-services/gbp-management/` — GBP Management
- `/marketing-services/google-ads/` — Google Ads
- `/marketing-services/meta-ads/` — Meta Ads
- `/marketing-services/your-ai-partner/` — Your AI Partner
- `/marketing-services/reputation-management/` — Reputation Management
- `/marketing-services/automation/` — Automation
- `/marketing-services/mow-money-mow-problems/` — Mow Money, Mow Problems System (branded system page + USPTO specimen, hand-built 2026-07-07)

## Industries
- `/industries/` — Industries hub
- `/industries/landscaping/` — Landscaping
- `/industries/outdoor-living/` — Outdoor Living
- `/industries/lawn-care/` — Lawn Care
- `/industries/lawn-maintenance/` — Lawn Maintenance
- `/industries/land-clearing/` — Land Clearing
- `/industries/excavation/` — Excavation
- `/industries/septic-installation/` — Septic Installation
- `/industries/holiday-lighting/` — Holiday Lighting

## Resources
- ~~`/resources/`~~ — **no page** (2026-06-21); silo path segment only (no index page). Nav "Resources" is a non-link trigger; not in `sitemap.xml`.
- `/resources/blog/` — Blog
- ~~`/resources/meet-the-team/`~~ — **removed 2026-06-17**; team consolidated into the About page (`/about/#team`). Launch 301 → `/about/#team`.
- `/resources/experiences-reviews/` — Experiences / Reviews
- ~~`/resources/private-facebook-group/`~~ — **removed 2026-06-21**; never a real page. Nav + footer link to the external FB group (`facebook.com/groups/serviceareaexperts`).
- `/resources/mow-money-mow-problems-podcast/` — Mow Money, Mow Problems Podcast

## Case Studies
- `/case-studies/precision/` — Precision Landscape Management (migrated 2026-06-21 from the legacy WordPress `/precision-case-study/`). Launch 301: old URL to this one. No index page at `/case-studies/` itself yet; the breadcrumb crumb is a non-link label.
- `/case-studies/rock-solid/` — Rock Solid Landscape (Wauseon, OH; built 2026-06-21 into the framework from the legacy WordPress `/rock-solid-case-study/`). Launch 301: old URL to this one.

## Legal
- `/terms/` — Terms of Use
- `/privacy-policy/` — Privacy Policy

## Explicitly Killed
These routes/sections are intentionally not part of the approved public website direction.
- `/services/`
- `/pricing/`
- `/resources/guides/`

## Legacy or Non-Canonical Routes To Remove Or Redirect
- `/resources/contact/` — non-canonical, use `/contact/`
- legacy service child routes under `/services/...`

## Notes
- Section hub pages for Programs, Marketing Services, Industries, and Resources are approved.
- `/contact/` is canonical even if older internal links still point elsewhere.
- If a new page idea comes up, add it here before treating it as part of the build.
