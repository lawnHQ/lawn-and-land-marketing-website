# Page Registry

Last updated: 2026-06-15. This table is the authoritative page-by-page inventory + status.

Status key
- **developed** — real body content and strategic substance; intentionally built
- **scaffolded** — live shell (header + hero + blank/placeholder body + CTA/footer); needs real content
- **planned** — approved but not live
- **killed** — intentionally removed from scope
- **legacy** — non-canonical route to keep out of internal linking

## Approved Canonical Pages
| Section | Page | Route | Status | Notes |
|---|---|---|---|---|
| Core | Home | `/` | **developed** | Benchmark page. Hero → stats → industries → services → proof row → programs → Why L&L → testimonials → logo marquee (Twilight band) → FAQ → CTA. Org + WebSite + FAQPage schema. |
| Core | About | `/about/` | scaffolded | Shell until design phase. |
| Core | Contact | `/contact/` | scaffolded | Shell until design phase. |
| Core | Get Started | `/get-started/book-strategy-call/` | scaffolded | The booking destination; every CTA on the site routes here. |
| Programs | Programs hub | `/programs/` | **developed** | Simple two-program window — hero + Growth (six-figure) and Authority (seven-figure) cards linking into each program, plus a "not sure?" CTA. |
| Programs | Growth | `/programs/growth/` | **developed** | Built lean from the real contract. Pain cards → four-pillar Twilight section → 2-col Why Us → CTA. Service + BreadcrumbList schema, OG/Twitter. No pricing. |
| Programs | Authority | `/programs/authority/` | **developed** | The flagship. Built from the contract + pitch deck: pain cards → Twilight "domination" pillars → everything-included grid → value play → Roadmap to Domination → partnership/credibility two-column → CTA. Service + BreadcrumbList schema, OG/Twitter. No pricing. |
| Marketing Services | Services hub | `/marketing-services/` | **developed** | Hand-built SEO silo; "one machine" framing, 4 featured + wrap-up grid, ItemList schema. |
| Marketing Services | Website Design | `/marketing-services/website-design/` | **developed** | Generated template; reference build for the generator. |
| Marketing Services | Local SEO | `/marketing-services/local-seo/` | **developed** | Generated template. |
| Marketing Services | GBP Management | `/marketing-services/gbp-management/` | **developed** | Generated template. |
| Marketing Services | Google Ads | `/marketing-services/google-ads/` | **developed** | Generated template. |
| Marketing Services | Meta Ads | `/marketing-services/meta-ads/` | **developed** | Generated template. |
| Marketing Services | Your AI Partner | `/marketing-services/your-ai-partner/` | **developed** | Generated template. |
| Marketing Services | Reputation Management | `/marketing-services/reputation-management/` | **developed** | Generated template. |
| Marketing Services | Automation | `/marketing-services/automation/` | **developed** | Generated template. |
| Industries | Industries hub | `/industries/` | scaffolded | Shell. |
| Industries | Lawn Care | `/industries/lawn-care/` | **developed** | 2nd industry page, off the locked template. The lawn's HEALTH = recurring treatment program (fert, weed, aeration, overseeding, insect & disease). Spine re-pointed 2026-06-17 to **recurring revenue** (renewals/retention/LTV); route density is support only. 4-season demand-cycle (winter prepay/renewals → spring rush → summer fulfill + book fall → fall aerate/overseed/re-sign); 8-service grid; real proof + testimonials (framed "lawn and landscape"); `@graph` schema. No pricing. |
| Industries | Lawn Maintenance | `/industries/lawn-maintenance/` | **developed** | 3rd industry page, off the locked template. The property's UPKEEP = mowing/cleanups/bed maintenance; **route density is the headline** (the spine lawn-care ceded). 4-season demand-cycle (winter lock routes/prepay → spring sign-up rush → summer tighten + pre-sell fall → fall cleanups/leaf + snow upsell + re-sign); 8-service grid; real lawn/landscape proof + testimonials; 8-Q FAQ (incl. lawn-care vs maintenance distinction, route-tightness, commercial/HOA); `@graph` schema. No pricing. |
| Industries | Landscaping | `/industries/landscaping/` | **developed** | First industry page + the **locked template** (`industry-page-template.md`). Hero+trust strip → answer-first definition (2-col) → specialist-vs-generalist table → demand-cycle module → service grid (8, incl. AI standout) → 5-step process → real proof + video testimonials → Growth/Authority fit → FAQ accordion → CTA. `@graph` schema (Org+Service+WebPage+Breadcrumb+FAQPage). No pricing. |
| Industries | Outdoor Living | `/industries/outdoor-living/` | **developed** | 4th industry page, off the locked template. High-ticket design-build/hardscape — portfolio-as-product, long visual sale, financing as a close lever. Demand-cycle inverted for design-build (winter sell/design pipeline → spring already-booked + photograph → summer build + harvest reviews → fall re-open selling + lock pipeline + financing); portfolio-first 8-service grid; real landscape/outdoor-living proof + testimonials; 8-Q FAQ (incl. spring-isn't-the-time, tire-kickers vs qualified, portfolio, financing); `@graph` schema. Keyword-differentiated from Landscaping. No pricing. |
| Industries | Land Clearing | `/industries/land-clearing/` | scaffolded | Canonical 8. Shell. |
| Industries | Excavation | `/industries/excavation/` | scaffolded | Canonical 8. Shell. |
| Industries | Septic Services | `/industries/septic-services/` | scaffolded | Canonical 8. Shell. |
| Industries | Holiday Lighting | `/industries/holiday-lighting/` | scaffolded | Canonical 8. Shell. |
| Resources | Resources hub | `/resources/` | scaffolded | Shell. |
| Resources | Blog | `/resources/blog/` | scaffolded | Exists but pulled from homepage nav/flow as unfinished; needs content strategy. |
| Resources | Meet The Team | `/resources/meet-the-team/` | scaffolded | Shell. |
| Resources | Experiences / Reviews | `/resources/experiences-reviews/` | scaffolded | Shell. |
| Resources | Private Facebook Group | `/resources/private-facebook-group/` | scaffolded | Shell. |
| Resources | Mow Money, Mow Problems Podcast | `/resources/mow-money-mow-problems-podcast/` | scaffolded | Shell. |

## Service-area note
Industry pages are exactly the **canonical 8** above — locked this build. Earlier non-canonical
industries (e.g. snow removal) were deleted, and the nav submenu, footer, and `sitemap.xml` were
reconciled to these 8.

## Killed / Non-Canonical / Legacy (keep OUT of nav, footer, CTAs, sitemap, internal links)
| Type | Route | Action |
|---|---|---|
| killed | `/services/` (+ `/services/...` child routes) | Retired; use `/marketing-services/...`. Do not reintroduce. |
| killed | `/pricing/` | Retired; **no pricing on the site**. Do not reintroduce. |
| killed | `/resources/guides/` | File deleted; keep retired. |
| killed | `/case-studies/` (+ children), `/results/`, `/tools/marketing-audit/` | Not part of the approved site. |
| legacy | `/resources/contact/` | Use `/contact/` only. |
| legacy | `/team/`, `/good-fit/`, `/book/`, `/podcast/`, old article URLs | Keep out of the internal link graph unless intentionally reintroduced via a new decision. |

## Highest-leverage work next
1. **Roll the industry-page framework to the remaining 7** (`industry-page-template.md`) — Landscaping is built and is the template.
2. Finish the 8 service pages with owner inputs (FAQ answers → FAQ schema; verify stats; real images).
3. Then About / Contact / Resources.
