# Build Status

Last updated: 2026-06-15.

## Overall read
The **homepage**, the **full set of 8 `/marketing-services/*` detail pages + the services hub**, **both
program pages** (Growth + the flagship Authority), the **Programs hub**, and **all 8 industry pages**
(`landscaping` — the locked template — plus `lawn-care`, `lawn-maintenance`, `outdoor-living`,
`holiday-lighting`, `land-clearing`, `excavation`, and `septic-installation`) are developed. About / Contact /
Resources remain intentional shells. Build tooling (universal
header/footer + service-page generator), the **2026-06-15 nav-submenu overhaul** (see `navigation.md`),
route hygiene, and the brand system are all in place. Nothing is launched publicly — staging is
new.lawnlab.dev (also lawnland-site.vercel.app); the eventual home is lawnandlandmarketing.com.

## What is DONE (developed)
- **Homepage** (`/`) — strongest page. Reordered for conversion: hero → stats → Industries grid →
  services → mini case-study proof row (3 real clients + photos + before→after numbers) → programs
  → Why L&L → testimonials (gold-glow stars) → "Trusted By" logo marquee on the Twilight band →
  FAQ (`FAQPage` schema) → CTA. Blog removed from nav/flow. Organization + WebSite + FAQPage schema.
- **All 8 `/marketing-services/*` detail pages** — built on the locked, **generated** template
  (`service-page-template.md`). Each: hero, conviction stat (real + sourced), showcase + labeled
  image placeholder, "What's included" (purple featured card + 7 Lucide cards), reversed showcase,
  FAQ (placeholder answers for now), Twilight CTA. `Service` JSON-LD; all internal links resolve.
- **Marketing-services HUB** (`/marketing-services/`) — hand-built SEO silo: "one machine" framing,
  4 featured services (image+text) + wrap-up grid linking the other 4, Twilight CTA, `ItemList` schema.
- **Growth Program page** (`/programs/growth/`) — built lean (Hormozi-style) from the real contract.
  `simple-hero` + breadcrumb → "Sound familiar?" 3 red pain cards → four-pillar "What you get" on
  the Twilight textured band → "Why us" two-column (image placeholder left, copy right) → Twilight
  CTA. `Service` + `BreadcrumbList` JSON-LD, OG + Twitter card. No pricing.
- **Authority Program page** (`/programs/authority/`) — the flagship, built. Elevated from Growth:
  hero → 3 pain cards → Twilight four-pillar "domination" band → full "everything included"
  deliverables grid → value play (a whole team for less than one hire) → "Roadmap to Domination"
  timeline → partnership + credibility (50+ clients, $300K–$14M+, 97% retention, NALP) two-column →
  Twilight CTA. Built from the contract + pitch deck. `Service` + `BreadcrumbList` schema, OG/Twitter. No pricing.
- **Programs hub** (`/programs/`) — simple two-program window (hero + Growth/Authority cards linking into each).
- **Landscaping industry page** (`/industries/landscaping/`) — built; the first of 8 and the **locked
  reusable template** (`industry-page-template.md`). Hero + trust strip → answer-first definition
  (two-column) → specialist-vs-generalist comparison table → demand-cycle module ("ahead of the seasons",
  Twilight band) → service grid (8, incl. the Twilight AI standout) → 5-step process → real proof cases +
  video testimonials → Growth/Authority program-fit → FAQ accordion → Twilight CTA. Built for SEO + GEO +
  EEAT; `@graph` schema (Org + Service + WebPage + Breadcrumb + FAQPage). No pricing, no invented facts.
- **Lawn Care industry page** (`/industries/lawn-care/`) — built; the 2nd off the template. Same structure,
  reframed for the **recurring treatment-program** business. Spine re-pointed 2026-06-17 to **recurring
  revenue** (renewals, retention, LTV) — route density is a *supporting* beat only, so it won't cannibalize
  the upcoming lawn-maintenance page (which gets the route/mowing spine; see `industry-page-template.md`).
  4-season demand cycle (winter prepay/renewals → spring rush → summer fulfill + book fall → fall
  aerate/overseed/re-sign), lawn-care comparison rows + FAQ (incl. retention + route-density Qs), real
  proof + testimonials framed "lawn and landscape." `@graph` schema. No pricing.
- **Lawn Maintenance industry page** (`/industries/lawn-maintenance/`) — built 2026-06-17; the 3rd off the
  template. The property's **upkeep/appearance** business (mowing, cleanups, bed maintenance); **route
  density is the headline** — the margin/"windshield time" spine lawn-care deliberately ceded. 4-season
  demand cycle (winter lock routes/prepay → spring sign-up rush → summer tighten + pre-sell fall → fall
  cleanups/leaf + snow upsell + re-sign), route-targeting comparison rows + 8-Q FAQ (lawn-care vs
  maintenance distinction, route-tightness, commercial/HOA), real lawn/landscape proof + testimonials.
  `@graph` schema. No pricing. Researched + Lawnline re-verified (their maintenance page has no FAQ/seasonality).
- **Outdoor Living industry page** (`/industries/outdoor-living/`) — built 2026-06-17; the 4th off the
  template. High-ticket **design-build/hardscape** — the portfolio is the product, a long visual sale,
  **financing** as a close lever. Demand cycle **inverted** for design-build (winter sell/design the
  pipeline → spring already-booked + photograph → summer build + harvest reviews → fall re-open selling +
  lock pipeline + financing), high-ticket/portfolio/financing comparison rows + 8-Q FAQ, portfolio-first
  service grid, real landscape/outdoor-living proof + testimonials. `@graph` schema. Keyword-differentiated
  from Landscaping (hardscape/structures/financing vs softscape). No pricing.
- **Holiday Lighting, Land Clearing, Excavation, Septic Installation** (`/industries/*`) — built 2026-06-17;
  industry pages 5–8, completing all 8. These are the **demand-mode / phase-based** trades (no four-season
  calendar): **holiday-lighting** uses a phase cycle (pre-sell → booking → install → takedown/re-book, the
  one page where "ahead of the season" still fits); **land-clearing** (pipeline / ground-access / burn /
  fire-mitigation), **excavation** (pipeline / residential-vs-commercial split / dig conditions / 811 +
  permits), and **septic-installation** (failed-system replacement / new construction / real-estate upgrade / compliance) each use demand-mode
  cards with a trade-true `.hl` headline ("how install work actually comes in", "how clearing work comes in", etc.). Clearing↔excavation
  carry mirrored disambiguation FAQs; excavation↔septic cross-link on installs. All four are **off-trade**
  for proof (real lawn/landscape clients), so framing is genericized to "green industry" + a per-trade bridge
  line (septic bridges on the transferable local-demand mechanism, the hardest case). **All four authored
  em-dash-free** per the new brand rule (the earlier four pages + the shared nav/footer still contain em
  dashes — a sitewide consistency pass is pending an owner decision). Full `@graph` schema each, honest
  `dateModified`. No pricing, no invented facts. Researched per page + Lawnline re-verified (no competitor
  page for clearing/excavation/septic; holiday maps to their thin "outdoor lighting" page). **Septic repositioned 2026-06-17** from septic *services* to septic *installers* (owner's real prospect): the page now leads on the high-ticket, permit-gated install business (failed-system + new-construction two-buyer split), slug `/industries/septic-installation/`, much closer to Excavation than to a pumping company.
- **Universal header + footer** — single source via `build.py` (`_header.html` / `_footer.html`). The
  nav submenus were overhauled 2026-06-15 (About trimmed, promo titles de-headinged for SEO, Resources
  rebuilt, Twilight/gold-star theming). Full reference: `navigation.md`.
- **Brand system** — Twilight spotlight + dot-grid CTA pattern; the `.hl` Twilight emphasis marker;
  Lucide-only icons. The `.hl` marker is also documented in the brand kit (brandkit.lawnlab.dev).

## What is NOT done
- **Industry pages — ALL 8 DONE** (`/industries/*`): landscaping, lawn-care, lawn-maintenance, outdoor-living,
  holiday-lighting, land-clearing, excavation, septic-installation. The canonical 8 are complete (see DONE above).
  Remaining polish, not blockers: real images for the placeholders, and (optional) a sitewide em-dash pass so
  the earlier four pages + nav/footer match the new no-em-dash rule.
- **About, Contact, Resources/\*** — shells.
- The 8 service pages need three **owner inputs** to be truly finished (below).

## Owner inputs needed to finalize the 8 service pages
1. **FAQ answers** — 5 per page, currently `[NEEDS YOUR INPUT]`. Once real, add `FAQPage` JSON-LD.
2. **Conviction stats** — verify the 7 industry stats (each has a `statSource` in `_content.json`).
3. **Images** — replace the labeled placeholders (each says exactly what to drop in).

## Highest-priority work next
1. **Industry pages: all 8 built.** Remaining is polish, not new builds: drop real images into the
   placeholders, and decide on the optional sitewide em-dash pass (earlier four pages + nav/footer).
2. Design + build the remaining non-home pages (About, Contact, Resources).
3. Land the service-page owner inputs (FAQ answers, conviction stats, images) → add `FAQPage` schema there.
4. **Launch cutover** to lawnandlandmarketing.com (later) — work `seo-launch-checklist.md`.

## Success criteria for a "finished" page
Live ≠ finished. A finished page has: a clear strategic purpose, a strong H1/promise, enough body
to persuade and rank, proof/trust where appropriate, clear CTA paths to the strategy call, correct
canonical internal links, the right schema — and **no invented facts** (placeholders for anything
unverified). **No pricing**, ever.
