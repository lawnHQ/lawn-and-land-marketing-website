# Service Page — Universal Template

Every `/marketing-services/*` detail page uses this exact section order. Only the
**content** changes per service; the **structure stays identical** for consistency
and SEO. Reference build: `/marketing-services/website-design/`.
Styles: `assets/css/service-page.css` (`svc-*` classes). Approved by Matt 2026-06-13.

## Sections, in order

1. **Hero** (`.simple-hero`)
   Breadcrumb · service eyebrow · keyword-led H1 (benefit + service) · one-line
   subhead · two CTAs (Schedule Strategy Call / Contact) · background image.

2. **Conviction strip** (`.svc-conviction`)
   One bold stat + a single punchy sentence + one supporting line. One memorable
   proof point per service. Not a wall of text.

3. **Showcase A — text + image** (`.svc-showcase`)
   Left: short paragraph + 3-item checklist ("what we build/do"). Right: a
   **labeled image placeholder** (`.svc-ph`) describing the screenshot to add.

4. **What's Included** (`.svc-includes`)
   One featured card + a grid of 7 deliverable cards. Each card = brand **Lucide
   icon** (stroke only) + short title + one line. Scannable, low text.

5. **Showcase B — text + image, reversed** (`.svc-showcase` + `.is-reversed`)
   Second angle (e.g. "built to rank/convert"). Same pattern as Showcase A,
   image on the opposite side, with its own labeled placeholder.

6. **FAQ** (`.svc-faq`)
   5 collapsible Q&As (`<details>`), targeting long-tail searches. Always pair
   with `FAQPage` JSON-LD in the head.

7. **CTA** (`.svc-cta`)
   Booking CTA + "Pairs well with" list linking 3–4 related services.

## Head requirements (per page)
- Unique `<title>`, meta description, canonical.
- `link` to `styles.css` **and** `service-page.css`.
- JSON-LD: `Service` schema + `FAQPage` schema (matching the on-page FAQ).

## Non-negotiables
- **Icons:** Lucide SVG, **stroke only**, 1.75 weight, round caps, `currentColor`
  (Limeade for emphasis). **No emoji or unicode glyphs as icons.** Ever.
- **Removed by decision:** a "How It Works" / process section (page-specific and
  low-value — people care that it works, not how).
- Keep copy tight and scannable — alternate text and visuals, never a wall of text.
- Buttons never wrap to two lines.

## SEO rules
- **Keyword variants:** lead with the primary term (e.g. "landscaping website design") but naturally work in 2–3 variants — "lawn care," "landscaper," "lawn care company website" — across subheads/body. No stuffing.
- **Heading hierarchy:** one H1; section titles are H2; the 7 "What's Included" cards are parallel H3s. The featured card's line is a styled paragraph (`.feat-headline`), NOT an H3, so the feature H3s stay clean siblings.
- **Schema:** `Service` JSON-LD always; `FAQPage` JSON-LD only once the FAQ answers are real (never fabricated Q&A).
- **No invented facts:** any unverifiable claim (timelines, specific deliverables, numbers) is a `[NEEDS YOUR INPUT — …]` placeholder, not a stated fact.
- **Planned (not built yet):** a tightly-scoped "Related articles" feed (max 3, below the FAQ near the final CTA) for internal-link/silo value — add ONLY once that service has matching blog articles; an empty module is bloat.

## Image placeholders
Each showcase ships a labeled `.svc-ph` placeholder telling the team exactly what
image to drop in (e.g. "Screenshot of a Google map-pack result ranking #1").
Swap the hint text to fit each service.

## How these pages are built (tooling)
- `_content.json` is the **editable source of all service-page copy** — one object
  per service (h1, conviction, showcases, 7 deliverable cards, FAQ questions, CTA,
  related services). Edit copy here, then regenerate.
- `python3 gen_service.py` renders each `/marketing-services/<slug>/index.html` from
  `_content.json`, using the `website-design` page as the structural template. It
  generates every internal link (breadcrumb, hero CTAs, "Pairs well with", hero
  image) **by construction**, so links can't drift.
- `python3 build.py` then stamps the universal header/footer.
- All 8 service heroes use `programs-hero.jpg` (dark photo) for text contrast.
- Conviction stats are **real, sourced** industry figures (`statSource` in
  `_content.json`) — verify before launch. FAQ answers are `[NEEDS YOUR INPUT]`
  placeholders until finalized; `FAQPage` schema is added per page only then.
