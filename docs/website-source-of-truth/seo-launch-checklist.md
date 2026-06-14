# SEO & Launch Checklist

From the 2026-06-14 multi-dimension SEO audit of the marketing-services hub (and the
broader silo). Scores at audit time: silo/internal-linking 8/10, on-page 6, technical 5,
schema 5, content-depth 4. The architecture is strong; the gaps below are optimization +
launch hygiene.

## Done (hub SEO quick pass, 2026-06-14)
- Keyword-loaded the hub H1 ("Every marketing service… landscaping & lawn care companies")
  and the featured H2s (each now names the service: "A landscaping website…", "Local SEO
  that…", "Google Ads that…").
- Added a conviction stat band (97% — homeowners research online before calling).
- Added `BreadcrumbList` + `MarketingAgency`/Organization JSON-LD (real footer data: socials,
  St. Petersburg FL) to the hub.
- Tightened the hub `<title>` + meta description (head term + "lawn care" + CTA).
- Fixed a real bug: homepage "Explore Reputation" button pointed at `/gbp-management/`.

## Pending — needs owner input (no invented facts)
- **Hub proof section** — surface existing homepage proof (real testimonials w/ revenue
  numbers, client-logo marquee, rating) on the hub. Biggest rank+convert lever. Reuse, don't
  invent; confirm the testimonials/logos are still approved/current.
- **Hub FAQ** — add 5-6 category questions ("How much does marketing for a landscaping
  company cost?", "Do you only work with landscapers?", "How is one-partner different from
  separate vendors?") + `FAQPage` schema — only once answers are real.
- **Verify stats before launch**: the hub's 97% conviction figure (source: BrightLocal-style
  local-search stat — confirm exact figure/wording), the 7 detail-page conviction stats
  (`statSource` in `_content.json`), and the footer trust bar ("50+ companies", "97%+
  retention", "since 2020").

## Pending — build work (can do anytime, no owner input)
- **BreadcrumbList on all 8 detail pages** (Home → Marketing Services → <Service>) — add to
  `gen_service.py` + regenerate so it can't drift.
- **One canonical Organization node** (`@id`, logo, address, sameAs) referenced by every
  Service `provider {@id}` — put in `_header.html` or the generator so it stamps sitewide
  (currently each detail page has an anonymous provider Org).
- **Move Service schema into `gen_service.py` + `_content.json`** so provider/host/logo/@id
  live in one place (currently copy-pasted 8×).
- Optional: enrich the hub `ItemList` items to reference each child's `Service` `@id`.

## MUST do at launch cutover (before going live on lawnandlandmarketing.com)
- **Flip all URLs from `new.lawnlab.dev` → `lawnandlandmarketing.com`**: every page's
  `<link rel="canonical">`, the hub's `ItemList` + `BreadcrumbList` URLs, `og:` URLs, and the
  detail pages' Service `provider.url` (currently the production domain — there's a host
  mismatch with the staging canonicals). Make the domain a single build variable so it can't
  drift again.
- **Fix `sitemap.xml`** — it currently lists non-existent paths (`/services/*`, `/pricing/`,
  `/book/`, `/team/`…), is missing `/marketing-services/` and the 8 real detail URLs, and has
  a malformed multi-`<loc>` record. Regenerate from the real page registry.
- **robots.txt** — none exists. Production: allow crawl + point to the sitemap. Staging
  (`new.lawnlab.dev`): block indexing (disallow / `X-Robots-Tag: noindex` / HTTP auth) so the
  staging site isn't indexed as a duplicate. Note: pages currently ship `robots: index,follow`.
- **Social/share tags** — add `og:image` + Twitter Card (`summary_large_image`) sitewide once
  a brand share image exists.

## Industry pages + taxonomy (follow-up)
- The homepage "Industries We Serve" section links 8 industries in this order:
  Landscaping, Outdoor Living, Lawn Care, Lawn Maintenance, Land Clearing, Excavation, Septic
  Services, Holiday Lighting. **4 are brand-new shell pages** (landscaping, lawn-maintenance,
  land-clearing, holiday-lighting) — build them out (like the service pages). Excavation,
  Septic Services, Outdoor Living, and Lawn Care already had pages. (Irrigation + Outdoor
  Lighting were dropped from the homepage grid; the orphaned outdoor-lighting shell was deleted,
  the pre-existing irrigation page remains.)
- **Reconcile the Industries taxonomy**: the nav/footer Industries menu still lists the OLD set
  (landscape-design-build, landscape-maintenance, excavation, septic-services) which doesn't
  match the homepage's 8. Decide the canonical list, align nav + footer + `/industries/` hub,
  and retire/redirect the dropped slugs.

## Post-launch content
- **"Mow Money, Mow Problems" dedicated page** — the free-resource (book) section was removed
  from the homepage 2026-06-14. Build it its own page under the Resources menu and link it
  there. The `book-section` markup/CSS is preserved (CSS in `styles.css`; the old homepage
  block is in git history) for reuse.

## Nice-to-have (later)
- Demote the nav mega-panel card titles from `<h4>` to non-heading elements so the document
  outline starts cleanly at the page H1 (currently 4 `<h4>`s render before the H1 — a
  `build.py` header artifact).
- `<noscript>`/`.js`-class guard for `[data-reveal]` so the H1/intro are never invisible if JS
  fails (they start at `opacity:0` until `main.js` reveals them).
- Replace the announcement-bar 🎉 emoji with a Lucide icon (brand rule) in `_header.html`.
- "Related articles / case studies" module on the hub once supporting blog content exists.
