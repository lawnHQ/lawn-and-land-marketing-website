# SEO & Launch Checklist

> Status update 2026-06-26: production cutover is complete. This file is now a historical launch/audit checklist plus maintenance reference. Canonicals, Open Graph URLs, `robots.txt`, and `sitemap.xml` are production-domain aligned. New production-operating baseline lives in `current-state-2026-06-26.md`.

## Homepage launch audit (2026-06-14) — verified findings + status
Five-lens audit (CRO, technical SEO, on-page, performance, a11y), each finding adversarially
re-checked. Verified scores: CRO 7, Tech SEO 7, On-page 7, Performance 5, Accessibility 4.

**FIXED this pass (index.html / styles.css?v=122 / main.js?v=52 / _header.html):**
- Credibility: "50+" → "100+" companies (matched the approved stat).
- FAQ schema parity: rebuilt FAQPage JSON-LD to all 6 visible Q&A w/ full answers (rich-result eligible).
- Perf: hero YouTube iframe no longer ships a live `src` (data-src, set on click) — removes ~1MB+/​~dozen
  third-party requests from every load. Poster got `fetchpriority="high"` + width/height + a
  `lawnandlandmarketing.com` preconnect. Marquee logos lazy-loaded.
- Meta description trimmed to ~153 chars (CTA no longer truncated). Added og:url + twitter:card.
- Schema: enriched MarketingAgency (logo, sameAs, address, areaServed, @id, trailing-slash url) + WebSite node.
- A11y: added `<main id="main">` + skip link; global `:focus-visible`; mega-menu now keyboard-openable
  (`:focus-within`); fixed 3 sub-AA contrast labels (hero proof bar, separators, marquee label);
  `prefers-reduced-motion` block + JS gating (word-cycle, cursor-glow rAF-throttled); hero H1 has a
  stable accessible name (cycling span aria-hidden + sr-only phrase); aria-haspopup on nav triggers;
  announcement-bar 🎉 → Lucide megaphone. Normalized 3 relative links to root-absolute.

**RESOLVED with owner (2026-06-14):**
- **ROI stat** — reframed from "10.83x Avg. Annual ROI After 2 Years" to **"12–16x · Revenue Returned
  Per $1 Invested"** (fees-only basis: avg ~$48K in fees → $600K–$800K added revenue over 2 yrs).
  Deliberately framed as *revenue* (not "ROI", which implies profit) and the $48K is NOT printed —
  it would expose pricing, which the site keeps off by design.
- **12-month contract objection** — FAQ answer now pairs the honest disclosure with risk-reversal
  (97% retention + "zero risk to just have the conversation"); schema kept in parity.
- **Mini case-study proof row** ("Proof, Not Promises") — name-led cards w/ real client before→after
  numbers (owner-supplied): Rock Solid $700K→$1.3M, Precision Landscape Mgmt 200→600 calls/mo, From The
  Ground Up $1.8M→$3.2M. Subline attributes the jump to working with L&L ("same crews, same services…").
- **Section order reworked** (4-lens analysis, owner-approved): Hero → Stats → Industries → Services →
  Proof → Programs → Why Us → Testimonials → Logo marquee → FAQ → CTA. Promotes "is this for my trade?"
  (Industries) early, moves the video Testimonials to the conviction peak before the CTA, demotes the
  logo marquee, and **removed the unfinished Blog feed from the homepage** (was a dead placeholder right
  before the CTA; markup preserved in git history — rebuild as its own page when wired).

**STILL NEEDS OWNER INPUT:**
- **Analytics/conversion tracking** — none installed (no GA4/GTM/pixel). DECISION: install at full-site
  launch (GTM + GA4), not now. When ready: GTM container in <head> + fire book_call_click on every CTA.

**DEFERRED POLISH (optional, low impact — do anytime):**
- "How It Works / Roadmap to Results" section (the FAQ name-drops it; page never shows it).
- Work "marketing agency" into the H1 + a keyword into the lead "What We Do" H2 (owner copy call).
- Demote the 4 pre-H1 mega-menu `<h4>`s to non-headings (outline hygiene).
- Review schema for the 6 testimonials (entity/E-E-A-T only; Google won't show self-serving stars).
- Add `<main>`/skip-link to the OTHER pages too (this pass was homepage-only).
- Industries on-page cards: add the mega-menu microcopy blurbs. Font-weight preload. Tabs ARIA completion.


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
  retention", "since 2022").

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
- **`sitemap.xml`** — ✅ rebuilt 2026-06-15 to the real canonical routes (production domain; the
  old file listed killed paths like `/services/*`, `/pricing/`, `/book/`, `/team/` and had a
  malformed multi-`<loc>` record). Remaining at launch: confirm shell pages are content-complete
  (or prune them) before submitting to Search Console, and keep it in sync with `sitemap.md`.
- **robots.txt** — none exists. Production: allow crawl + point to the sitemap. Staging
  (`new.lawnlab.dev`): block indexing (disallow / `X-Robots-Tag: noindex` / HTTP auth) so the
  staging site isn't indexed as a duplicate. Note: pages currently ship `robots: index,follow`.
- **Social/share tags** — add `og:image` + Twitter Card (`summary_large_image`) sitewide once
  a brand share image exists.
- **Localize external legacy assets** — the hero **NALP badge** currently loads from the old WordPress
  domain (`lawnandlandmarketing.com/wp-content/uploads/.../white-nalp-logo.png`). It works on staging, but
  it's an external hard-dependency on the legacy site — if that WP install goes away at launch the badge
  404s. Move it (and any other `wp-content` assets) into `/assets/` before launch. It replicates across
  every cloned industry-page hero, so fix the source once.
- **301 redirect `/resources/meet-the-team/` → `/about/#team`** — the standalone team page was retired
  2026-06-17 and consolidated into the About page (`#team` section). Shell deleted + removed from sitemap;
  nav/footer already repoint to `/about/#team`. Add the redirect at cutover in case the old URL was ever
  shared or indexed.
- **301 redirect `/industries/septic-services/` → `/industries/septic-installation/`** — the septic page
  was renamed 2026-06-17 (services → installers). The old slug never went live/indexed (pre-launch), so this
  is low-stakes insurance, but add the redirect at cutover in case anything ever referenced the old URL.
  Decision recorded: we have **consciously vacated the "septic pumping / emergency septic service" keyword
  space** — the owner's prospect is installers, not pump-service companies. (If that ever changes, a separate
  service page is the move; it would NOT cannibalize the installer page, since its spine differs.)
- **Verify septic-install LSA eligibility** — the septic-installation page's Google Ads card references a
  "verified, insured badge" (Google Local Service Ads / Google Guaranteed). LSA leans service/repair, and a
  high-ticket *install* job may or may not fit an LSA category in a given metro (Google's septic category is
  "Sewage system"). Confirm LSA eligibility for the client's install services before relying on it; the page
  already works without an explicit LSA-category claim (we softened that wording when repositioning to
  installers on 2026-06-17).
- **Image alt text (when real photos land)** — describe what's in the image; don't keyword-stuff.
  Proof/case-study photos name the company + context ("Rock Solid Landscape crew and equipment, Ohio");
  hero reinforces the topic naturally ("landscaping design-build project"); service images name the
  service; decorative images get `alt=""`. Applies to all 8 industry pages.

## Industry pages + taxonomy
- **DONE (2026-06-14) — taxonomy reconciled to the canonical 8.** The site now has exactly
  8 industry pages, in the homepage "Industries We Serve" order: Landscaping, Outdoor Living,
  Lawn Care, Lawn Maintenance, Land Clearing, Excavation, Septic Installation, Holiday Lighting.
  - Retired pages **deleted**: `/industries/irrigation/`, `/industries/landscape-design-build/`,
    `/industries/landscape-maintenance/` (the earlier `outdoor-lighting` shell was already gone).
  - Nav mega-menu + footer rebuilt to the 8 (now in homepage order, with the matching Lucide
    icons instead of the old generic checkmark), `/industries/` hub copy updated, `sitemap.xml`
    given an Industries section, and the page-registry / sitemap.md docs aligned.
    No reference to the 3 retired slugs remains anywhere in the project.
- **Still TODO — build out the 8 shells.** All 8 are live shells (header + hero + placeholder
  body + CTA/footer) with correct self-canonical/title/meta. Build real content on the service-
  page template approach. The `/industries/` hub body is also still a placeholder.
- Optional: add `301` redirects from the 3 retired slugs at launch (harmless now — they 404 on
  staging and were never indexed).

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
