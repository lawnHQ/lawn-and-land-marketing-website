# Build Status

Last updated: 2026-06-15.

## Overall read
The **homepage**, the **full set of 8 `/marketing-services/*` detail pages + the services hub**,
and the **Growth Program page** are developed. The Authority Program page and the 8 industry
pages are the next builds; About / Contact / Resources remain intentional shells. Build tooling
(universal header/footer + service-page generator), route hygiene, and the brand system are all
in place. Nothing is launched publicly — staging is new.lawnlab.dev (also lawnland-site.vercel.app);
the eventual home is lawnandlandmarketing.com.

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
- **Universal header + footer** — single source via `build.py` (`_header.html` / `_footer.html`).
- **Brand system** — Twilight spotlight + dot-grid CTA pattern; the `.hl` Twilight emphasis marker;
  Lucide-only icons. The `.hl` marker is also documented in the brand kit (brandkit.lawnlab.dev).

## What is NOT done
- **8 industry pages** (`/industries/*`) — **the next big build.** The canonical 8 are locked (lawn-care, lawn-maintenance,
  landscaping, outdoor-living, land-clearing, excavation, septic-services, holiday-lighting) but are
  **shells**. Content outlined, not written.
- **About, Contact, Resources/\*** — shells.
- The 8 service pages need three **owner inputs** to be truly finished (below).

## Owner inputs needed to finalize the 8 service pages
1. **FAQ answers** — 5 per page, currently `[NEEDS YOUR INPUT]`. Once real, add `FAQPage` JSON-LD.
2. **Conviction stats** — verify the 7 industry stats (each has a `statSource` in `_content.json`).
3. **Images** — replace the labeled placeholders (each says exactly what to drop in).

## Highest-priority work next
1. **Write the 8 industry pages** (canonical 8 locked) — give the shells real, persuasive content.
2. Land the service-page owner inputs above → mark those pages "finished" + add `FAQPage` schema.
3. Design + build the remaining non-home pages (About, Contact, Resources).
4. **Launch cutover** to lawnandlandmarketing.com (later) — work `seo-launch-checklist.md`.

## Success criteria for a "finished" page
Live ≠ finished. A finished page has: a clear strategic purpose, a strong H1/promise, enough body
to persuade and rank, proof/trust where appropriate, clear CTA paths to the strategy call, correct
canonical internal links, the right schema — and **no invented facts** (placeholders for anything
unverified). **No pricing**, ever.
