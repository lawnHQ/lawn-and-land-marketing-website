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
| Industries | Lawn Care | `/industries/lawn-care/` | scaffolded | Canonical 8 (locked). Shell — content outlined, not written. |
| Industries | Lawn Maintenance | `/industries/lawn-maintenance/` | scaffolded | Canonical 8. Shell. |
| Industries | Landscaping | `/industries/landscaping/` | scaffolded | Canonical 8. Shell. |
| Industries | Outdoor Living | `/industries/outdoor-living/` | scaffolded | Canonical 8. Shell. |
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
1. Build the **Authority Program page** (Growth structure, 7-figure+ avatar).
2. Write the **8 industry pages** (canonical 8 locked).
3. Finish the 8 service pages with owner inputs (FAQ answers → FAQ schema; verify stats; real images).
4. Then About / Contact / Resources.
