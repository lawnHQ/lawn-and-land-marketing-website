# Website Decisions Log

## 2026-04-14
- This public website build should stay separate from the internal Ground Control concept and naming.
- The repo should maintain a dedicated website-specific source-of-truth folder for architecture and progress tracking.
- `/marketing-services/` is the canonical service section.
- `/services/` is intentionally not part of the approved website and should be retired from all internal linking.
- `/pricing/` is intentionally not part of the approved website and should not be reintroduced as a canonical page.
- `/contact/` is the canonical contact route.
- `/resources/contact/` is non-canonical and should be removed from internal linking.
- `/resources/guides/` is out of scope and should be retired.
- Approved sitemap includes Home, About, Programs, Marketing Services, Industries, Resources, and Get Started / Book Strategy Call.
- Lawnline (`https://lawnline.marketing/`) is the primary public benchmark to beat on structure, SEO strength, and overall execution quality.

## 2026-04-15
- Approved structural cleanup pass has been applied in the repo.
- `_nav.html`, `_footer.html`, homepage/service CTAs, duplicated page HTML, and `404.html` were updated to remove the retired route drift.
- `resources/contact/index.html` and `resources/guides/index.html` were deleted from the repo.
- Next work should shift from route hygiene to finishing the highest-leverage thin pages.

## 2026-04-15 (continued)
- A second route-hygiene pass removed the remaining broken internal links to orphan routes like `/team/`, `/results/`, `/good-fit/`, `/book/`, and old article URLs.
- Top-priority thin pages were deepened in this workstream: `/programs/`, `/marketing-services/`, `/about/`, and `/contact/`.
- The next highest-leverage page work should move deeper into service detail pages rather than reopening top-level architecture decisions.

## 2026-04-15 (latest)
- Homepage remains the only intentionally developed public page for now.
- All non-home public pages should currently stay header + hero + blank-body placeholder + CTA/footer until the design direction is approved.
- Written body expansion on non-home pages should pause until that design phase begins.

## 2026-04-16
- `/programs/` has been reopened as the current design exploration page.
- A simple body-layout prototype was added to `/programs/` with placeholder/lorem blocks for philosophy, quick breakdown, Growth, Authority, and right-stage guidance.
- A more aggressive visual redesign pass for `/programs/` was attempted and then rejected.
- The simpler pre-v2 Programs version was restored and is the current live state to review from.
- For now, keep the simpler `/programs/` prototype live while Matt reviews and prepares detailed feedback.
- Do not assume the rejected v2 direction should be revived without explicit approval.

## 2026-06-13
- Header and footer are now truly single-source. `_header.html` (announcement bar + nav) and `_footer.html` are the only files to edit; `build.py` stamps them into every page and runs automatically on Vercel deploy via `vercel.json` buildCommand.
- The announcement bar was folded into the universal header and unified across all 31 pages (text + `/contact/` link). Previously the homepage used a relative link and `/404.html` had a stray promo.
- Replaced the old fragile `build-pages.py` (hardcoded `/tmp` path) with `build.py`. Refreshed `_footer.html` to match the current live footer (the partial had gone stale). Brought `/404.html` into the universal header/footer.
- Decision pending from Matt: begin building out the non-home page bodies ("build it out to the best solution") — establish a reusable page design system from the homepage, then roll out across the sitemap.

## 2026-06-14 — Industries locked · homepage deepened · Growth built · `.hl` marker
- **Industries — canonical 8 LOCKED:** lawn-care, lawn-maintenance, landscaping, outdoor-living,
  land-clearing, excavation, septic-services, holiday-lighting. Non-canonical industries (e.g. snow
  removal) were deleted; nav submenu, footer, and `sitemap.xml` reconciled. Icons: Landscaping =
  tree-palm, Lawn Care = sprout (Lucide). Mobile "Industries We Serve" is a compact 2-up grid.
- **Homepage conversion pass:** reordered to hero → stats → industries → services → proof → programs
  → Why L&L → testimonials → logo marquee → FAQ → CTA. Removed the unfinished Blog from nav/flow.
  Added a mini case-study proof row (3 real clients with photos + before→after numbers; no % badges).
  Moved the "Trusted By" logo marquee above testimonials onto the Twilight dot-grid band. Testimonial
  stars → gold-glow. "Why L&L" tightened ("5+ Years" badge → "100% Green Industry Focused"). Applied a
  verified pre-launch audit; softened the ROI claim to a defensible range (kept the dollar figure off
  the page so it never implies pricing). Unified section backgrounds to kill reorder seams. Fixed the
  mobile mega-menu (caret submenus expand instead of navigating).
- **`.hl` Twilight highlight — new reusable brand element:** skewed (−11°) `#6837EF` swipe behind the
  lower portion of one impact phrase, white text, sharp edges. Defined in `styles.css`; **locked into
  the brand kit** (brandkit.lawnlab.dev, §09 Typography). One phrase per surface; never on body or greens.
- **Growth Program page built:** scrapped the old lorem `/programs/` body; built `/programs/growth/`
  lean (Hormozi-style), hand-built (not the generated service template) reusing the same classes.
  Pain cards → four-pillar "What you get" on the Twilight textured band → 2-col Why Us → Twilight CTA.
  **Avatar correction (important):** Growth = $400K–$1M "six-figure" companies that grew OFFLINE and are
  trying to get FOUND for the first time — NOT vendor-sprawl/agency-scar pains (those are Authority).
  A lime-inverted "what you get" was tried and rejected ("too bright") → Twilight purple textured band.
- **Mobile marquee fix:** homepage logo marquee didn't start on iOS until tapped. Cause: 36 lazy, unsized
  logos collapsed the `max-content` track to ~0 width + no GPU layer promotion. Fix: reserve each logo's
  intrinsic size (`width=99 height=38`) + eager-load + promote the track (translateZ / will-change /
  translate3d keyframes). Desktop unchanged.

## 2026-06-15 — Growth SEO pass · footer · docs refresh
- **Growth SEO (from an external audit):** added `Service` + `BreadcrumbList` JSON-LD, `og:url`, Twitter
  card. Aligned the meta description to "six-figure lawn care and landscaping companies" (~155 chars) to
  match the body. Promoted the hero "Growth Program" kicker to the page `<h1>` (keyword in H1), demoting
  the emotional headline to `<h2>` — pixel-identical on screen. Reworked "Why Us" into two columns (image
  placeholder left, copy right, left-aligned). `og:image` deferred to launch.
- **Footer:** "Green industry specialists since **2022**" (corrected from 2020).
- **Schema/canonical convention:** schema uses the production domain (`lawnandlandmarketing.com`); page
  canonicals still point to staging (`new.lawnlab.dev`) and flip at launch.
- **Docs refresh:** brought `CLAUDE.md`, `README.md`, `PAGES_MANIFEST.md`, and the whole
  `docs/website-source-of-truth/` set current; rebuilt `sitemap.xml` to the real routes (the old one
  listed killed routes — `/services/...`, `/pricing/`, `/case-studies/`, fake blog posts).

## 2026-06-15 — Authority Program (flagship) built
- Built `/programs/authority/` as the flagship, cloned from the Growth structure and elevated for the
  **7-figure+** avatar (established, doing real revenue, wants to *dominate* — NOT Growth's get-found
  pains). Sections: hero ("be the most known") → 3 red pain cards (outranked by inferior competitors /
  patchwork vendors / plateaued) → Twilight four-pillar "domination" band (Total Search Domination /
  Everywhere They Look / A Reputation That Closes / Your Whole Marketing Team) → full "everything
  included" deliverables grid (~18 items) → **value play** ("a whole team for less than one hire" — uses
  the ~$60–80K employee-cost anchor, never our fee) → **Roadmap to Domination** timeline (Foundation →
  Climb → Market Dominance → Total Control) → partnership + credibility two-column (50+ clients,
  $300K–$14M+, 97% retention, NALP, Google Partner) → Twilight CTA. Built from the real contract + the
  New Horizon pitch deck. `Service` + `BreadcrumbList` schema, OG/Twitter. **No pricing.** Deliberately
  excluded the deck's "Seven Figure Agency" mention (third-party brand) and specific client P&L numbers;
  used L&L's own agency credentials as proof instead. Both program pages now cross-link.
- **Refined same-day per owner feedback:** dropped "Flagship" from the hero pill; `.hl` Twilight
  highlight applied to "THE company" (problem) and "For less than one hire." (value headline);
  removed the "$60–80K math" reframe line under the value cards and tightened the value→roadmap
  spacing; re-weighted the value cards to **40/60** with the Authority-team box emphasized (bigger
  header, brighter copy, stronger border + purple glow) as the obvious choice; **replaced the
  credibility stat row with the homepage "Proof, Not Promises" section** (real client results —
  Rock Solid, Precision, From The Ground Up). The agency credentials (50+ / $300K–$14M+ / 97% /
  NALP) still live in the Why-L&L partnership paragraph.
- **Universal (same session):** every hero/banner subhead is now **full white `#fff`** (was
  `rgba(255,255,255,0.78)` / `var(--body)` grey) — `.hero-copy p` on all `.simple-hero` pages +
  `.hero-sub` on the homepage. `styles.css?v=135 → 136`.

## 2026-06-15 — Programs hub + submenu icons
- Built the **`/programs/` hub** as a simple two-program window (owner: "a quick window into both
  programs"): hero → "Two Programs / Find the one built for your stage" → two cards (Growth = six-figure,
  Authority = seven-figure; reuses the homepage `.program-card` pattern, Authority featured) each linking
  into its program page → a "not sure which?" book-a-call line. Inspiration: lawnline.marketing/programs/.
- Nav Programs submenu icons: **sprout** for Growth, **trophy** for Authority (Lucide; stamped sitewide).
- Programs submenu refined (desktop + mobile): dropped the "Recommended Path" featured card; the two
  programs now show as side-by-side themed cards — **Growth in lime, Authority in the Twilight textured
  purple** (`.mega-grid--programs` + `.mega-item--growth/--authority` in styles.css; the Authority target
  pill changed green → twilight). About/Marketing-Services dropdowns untouched.

## 2026-06-15 — Programs section LOCKED (sans images)
- Both program pages (**Growth**, **Authority**), the **`/programs/` hub**, and the **nav submenu**
  are locked pending real images — treat the build/wireframe/content as final unless the owner reopens it.
- Ran a sitewide consistency pass on every program mention (homepage "Two Paths" section, hub cards,
  nav mega, footer, homepage FAQ + schema, service-page footer link lists). All consistent: naming
  ("Growth Program" / "Authority Program"), order (Growth → Authority), tier framing (Growth =
  6-figure / under $1M / foundation-and-get-found; Authority = 7-figure / over $1M / dominate), and
  no-pricing.
- **Label convention (locked):** compact pill/badge labels use the **digit** form ("For 6-Figure
  Companies"); running prose uses the **spelled** form ("six-figure"). Standardized the hub badge (the
  lone "Six-Figure" outlier) to digit so it matches the homepage badges + nav pills — also avoids the
  spelled form wrapping in the narrow nav pills.
- **Only remaining program to-do:** drop real images into the hero/Why-Us placeholders on the program pages.

## 2026-06-15 — Nav submenu overhaul (tightened all four dropdowns)
- **About:** removed the founder/right-rail card; the dropdown is now a compact single-column
  `.mega-panel--narrow` (380px) — About / Meet The Team / **Experiences & Testimonials**. The
  Experiences item is themed in the Twilight textured purple (`.mega-item--twilight`) with a
  glowing gold star icon, and links to `/resources/experiences-reviews/`.
- **Marketing Services & Industries:** the styled promo headline ("Most Companies Don't Need
  Another Vendor." / "We Only Work In The Green Industry.") is no longer an `<h4>` — moved to a
  `<div class="mega-fc-title">` that inherits the exact former `h4` look (Rethink Sans italic 800).
  This was an **SEO fix** — nav promo copy was polluting the page heading hierarchy. The Marketing
  Services body copy was rewritten to the "one connected system… run by a single team that owns the
  result" framing.
- **Resources — full rebuild:** the featured card is now a Twilight-textured, clickable testimonials
  card (glowing gold 5-star row, "Client Experiences" label, links to `/resources/experiences-reviews/`
  — same target as the About item, anticipating a page full of testimonial videos/screenshots). The
  six items are reorganized into two columns: **Mow Money, Mow Problems** (the Podcast → on-site page
  that will show off the show + let people apply as a guest · YouTube channel ↗ · the Book → Amazon ↗)
  and **Learn & Connect** (Green Industry Insights/Blog · Private Facebook Group ↗ "Service Area
  Experts" · Contact Us). External links open in a new tab (`target="_blank" rel="noopener"`).
- **Decision (flag for Matt):** the "Mow Money, Mow Problems" **Book** links straight to the **Amazon**
  product page (new tab) rather than a dedicated on-site page — simplest path, and Amazon already
  converts. Trivial to swap to a dedicated page later if we want on-site reviews/long-form.
- New nav CSS added to `styles.css`: `.mega-panel--narrow`, `.mega-grid--single`, `.mega-item--twilight`,
  `.mega-featured-card--twilight`, `.mega-fc-stars`, and `.mega-fc-title` (extends the former
  `.mega-featured-card h4` rule so the de-headinged titles keep the identical look). `styles.css?v=137 → 138`.
  Header re-stamped sitewide via `build.py`. Programs / hub / program pages untouched.

## Open Decisions To Track Later
- **Industry-page content + template** — how deep the 8 (locked) industry pages go, and whether they
  share a reusable structure.
- **About / Contact / Resources** design direction.
- **Service-page finishing inputs** — real FAQ answers (→ add `FAQPage` schema), verified conviction
  stats, real images.
- Whether retired routes get hosting-layer redirects at launch vs. simply staying out of internal linking.
