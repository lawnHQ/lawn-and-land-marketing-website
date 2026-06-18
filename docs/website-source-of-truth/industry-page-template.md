# Industry Page — Universal Template & Strategy

The eight `/industries/*` pages are our **heavy keyword + GEO play**: the page a business owner lands
on when they search "[their trade] marketing" or "marketing for [their trade] companies." Each one
must prove we deeply understand *their* business — services, customers, and especially their **seasonal or
demand rhythm** — and convert that trust into a booked strategy call.

- **Reference build:** `/industries/landscaping/` — the first page and the **locked template**. Match its
  *current* structure exactly when cloning (it has evolved since first build).
- **Built 2026-06-15; refined through 2026-06-16** per owner feedback + a third-party SEO audit: two-column
  intro, real testimonials, the standalone "Why Lawn & Land" section removed, canonical service icons,
  "ahead of the seasons" framing, honest schema date (no visible chip), and answer-first openers. The
  `decisions.md` log has the full trail.
- **HAND-BUILT** (not generated like service pages). Each reuses `simple-hero`, `.svc-cta`, and the
  homepage `.proof-cases` row, plus the reusable `.ind-*` framework now in a **shared `industry.css`**.
- **Stylesheets:** link `styles.css`, `service-page.css`, **and `/assets/css/industry.css`** (the `.ind-*`
  framework — shared across all `/industries/*` pages, so one edit propagates everywhere; bump its `?v=`
  when you touch it). Wrap content in `<main id="main">`.

## The thesis (why this structure wins)
Generic "home-services marketing" pages lose to specialists. We win by **demonstrating first-hand
expertise** (EEAT "Experience") and structuring every section so both Google and AI answer engines
(GEO) can lift it cleanly. The single sharpest weapon is the **demand-cycle module** — proof we know the
owner's calendar (or demand pattern) better than they expect. Our #1 benchmark, Lawnline, has **no FAQ on any industry page
and real seasonality on only one** — those two are our biggest openings, so we lean into both hard.
*(Competitor sites change — **re-verify the Lawnline teardown when you build each new page** rather than
trusting this snapshot; the FAQ + demand-cycle edge only holds while the gap is real.)*

## Sections, in order
Each section lists its job and why it's there for SEO / GEO / EEAT.

1. **Hero** (`.simple-hero`) — breadcrumb · `[Industry] Marketing` eyebrow (the keyword) · ONE
   keyword-bearing `<h1>` · full-white subhead with native vocabulary · two CTAs · an **above-fold
   trust strip** (`.hero-trust`: NALP · Google Partner · green-industry focused — keep it to ~3 badges).
   *SEO: H1 keyword. EEAT: badges up top. GEO: a crisp definition follows immediately.*
2. **Answer-first definition + owner's reality** — a **two-column block** (`.ind-split`): an image
   placeholder on the **left** (`.ind-ph`), and on the **right** (right-aligned, `.ind-split-text`) an
   eyebrow + a punchy H2 + a **bolded one-sentence definition** of "[industry] marketing" followed by
   3–4 sentences naming the owner's real pain. *GEO: the bolded sentence is the quotable definition.
   EEAT: empathy = Experience.* (No visible "updated" date — see **Freshness** under Non-negotiables.)
3. **Why generic marketing fails + comparison table** (`.ind-compare`) — answer-first paragraph, then a
   **specialist-vs-generalist table** (rows tuned to the trade: knows your season / speaks your language /
   builds the right site / filters your leads / proof that closes). *GEO: tables cite well. EEAT: expertise.
   This table **is the "why us"** — there is no separate credentials/why-us section (removed as redundant).*
4. **The demand-cycle module — THE centerpiece** (`.ind-band` + `.ind-seasons`/`.ind-season` cards) — H2
   with a `.hl` highlight, cards split **"On the ground"** vs **"What we market,"** closed with a regional
   note. **Pick the layout that fits the trade — do NOT blindly clone four seasons:**
   - **(A) 4-season calendar** for the *seasonal* trades — landscaping, lawn-care, lawn-maintenance,
     outdoor-living, holiday-lighting: Winter / Spring / Summer / Fall, headline "…**ahead of the seasons**."
   - **(B) demand-mode cards** for the *less-seasonal* trades, where a 4-season frame is forced filler and
     *undercuts* the "we know your business" promise. Use 3–4 cards keyed to how demand actually shows up:
     - **Septic installation** (repositioned to installers, NOT pump-service): Replacement (failed systems,
       high-intent homeowner search) · New construction (builder/GC, permit pipeline) · Real-estate (point-of-sale
       upgrade) · Compliance (county mandates, advanced systems). Headline "We market for **how install work actually comes in**."
     - **Excavation / land-clearing:** project pipeline + **frost/dig-season + permit/ground-condition
       windows**, not a consumer-season rush.
   - Same CSS (`.ind-seasons` grid handles any card count) — a **copy + card-count decision, not a rebuild.**
   *The information-gain play competitors can't write — but only if it's the RIGHT cycle for the trade.*
5. **What we build** (`.ind-services`) — answer-first intro + a grid of service cards, **each linking to
   its `/marketing-services/*` page**, using the **canonical service icons** (see `navigation.md`), with
   industry-specific copy. Include all 8 services; make the **Your AI Partner** card the Twilight-textured
   standout (`.ind-svc--ai`). *SEO: hub-and-spoke internal links. GEO: extractable list.*
6. **How we work** (`.ind-steps`) — a numbered 1→5 process. *GEO: numbered steps cite well. EEAT:
   transparency stands in for the price transparency we deliberately omit.*
7. **Proof + testimonials** — **Proof, Not Promises** (`.proof-cases`) with the three real client cases
   (numbers), then a **testimonials section** (`.testi-section`, the homepage's real video testimonials).
   Numbers *and* voices. *EEAT Experience + Trust. Real, attributed only — never invented.*
   **Reuse rule (important):** every real testimonial/case number is a **lawn/landscape client.** Keep the
   real content on every page, but change the **framing copy** (proof eyebrow + lede, testimonial header +
   subhead) per trade: use the industry name where the clients match the page (lawn-care, lawn-maintenance,
   outdoor-living); on **septic, land-clearing, excavation, holiday-lighting** genericize to **"green
   industry"** and add a **bridge line** — "the same system and team we'd put behind your [trade] business."
   Honest (no fake same-trade testimonials), and it tells a different-trade owner why to care. Don't hard-code
   the page's own trade into these framing lines when cloning (the landscaping page carries an HTML comment to this effect).
   **Septic is the hardest bridge** — it's the furthest trade from lawn/landscape, so "the same system and team"
   reads thin on its own. There, bridge on the **transferable mechanism**, not similarity: the engine being sold
   is getting found first for high-ticket local work, the proof and reviews that win a permit-gated job, and
   follow-up across a long sale — *exactly* what wins a septic installer regardless of the client's trade. Make
   the bridge line say that, e.g. "the same engine — found-first, proof that wins trust, follow-up that closes
   the job — behind your install business." (The live septic-installation page uses this mechanism-bridge.)
8. **Program fit** (`.ind-fit`) — two cards linking **Growth** (6-figure, lime) and **Authority**
   (7-figure, Twilight). *SEO: internal links to programs; qualifies the visitor.* (There is **no
   standalone "Why Lawn & Land" section** — removed 2026-06-16 as redundant with the hero badge, the
   comparison table, and the FAQ. Credentials live in the hero trust strip + footer.)
9. **FAQ** (`.ind-faq`, visible `<details>` accordion, 6–8 Q&As, **answer-first 40–60 words**) +
    **`FAQPage` schema**. Cover the objection + **"cost" intent** (answer the intent, **never a price**) +
    the seasonality question. *GEO: top AI-extraction zone — the gap Lawnline leaves wide open.*
10. **Final CTA** (`.svc-cta` Twilight band) — book the free call + "Explore" links (a sibling industry + Programs).

**Head schema:** one `<script type="application/ld+json">` with an `@graph`:
**Organization + Service + WebPage (`dateModified`) + BreadcrumbList + FAQPage.** Schema text must match
the visible text. Keep `dateModified` accurate — bump it on a real content edit (see Freshness). **Don't add
`Review`/`AggregateRating` for first-party testimonials** — Google doesn't surface self-serving review rich
results and it risks a self-serving flag; the visible testimonials already carry the EEAT for humans and AI.
(Only consider review schema for genuine aggregated third-party reviews, e.g. a real Google rating.)

## SEO / GEO / EEAT principles baked in
1. **One keyword H1** containing the literal "[industry] marketing" phrase (not just the two words split
   across a sentence); H2s are real questions or specific claims with keyword *variants*. Keep clever hook
   lines (e.g. "You're not hard to hire, you're hard to find") as **kickers/eyebrows**, not as the H1 or a
   money-section H2 — let the heading carry the term. Avoid pure clichés as money-section H2s ("Don't take
   our word for it").
2. **Answer-first**: the first ~40–75 words under every H2 stand alone and answer the heading — that's what AI lifts.
3. **High-citation formats**: at least one comparison **table** + one **numbered** process + bulleted lists.
4. **Information gain**: 2–3 things only a true specialist could write (the seasonality math, the trade's economics). The moat.
5. **Real signals only** (EEAT): real proof cases, real credentials, native vocabulary. **Never fabricate** — including dates (see Freshness).
6. **Internal links**: every service mentioned links out; link both programs and ≥1 sibling industry; breadcrumb up.

## Per-industry "what to swap" (the structure stays identical)
- Hero eyebrow / H1 / subhead + `<title>` / meta / OG / Twitter (keyword = "[industry] marketing")
- The answer-first **definition** sentence
- The 5 **comparison-table** rows (tuned to the trade's economics)
- The **demand-cycle module** — *research this per industry; it's the centerpiece (4-season vs demand-mode — see §4)*
- The **service-grid** emphasis + copy (all 8 services, trade-specific framing)
- **Proof-row** intro line (the three cases stay the real ones)
- The **FAQ** (trade-specific questions; keep the cost + seasonality ones)
- Schema `serviceType`, `name`, `breadcrumb`, FAQ entities

## Research method (do this per page BEFORE building)
Brief up, per industry: (1) the **business model / service mix** and where the money is; (2) **customer
segments** and how they buy; (3) the **demand cycle** — quarter-by-quarter for seasonal trades, or by
demand-mode for the rest — framed as marketing *ahead of demand*, not in sync with it; (4) the biggest
**business + marketing pains**; (5) **native vocabulary**. Landscaping's
brief is the depth bar to hit — its core insight: a landscaper is *three businesses* (**design** qualifies →
**installs** earn the money → **maintenance** sustains and feeds the next install), the cardinal sin is
marketing *in sync* with demand instead of *ahead* of it, the portfolio is the product, and reviews are the
gatekeeper. Use parallel research agents (Lawnline teardown + domain brief + current SEO/GEO/EEAT playbook)
the way the landscaping build did.

## Per-industry seed angles (starting points — research + sharpen per page; NOT yet facts)
> These are **hunches to test, not copy to ship.** Two hard rules learned from the first two builds:
> - **Demand-mode (non-seasonal) trades — septic, land-clearing, excavation — CANNOT be written from the seed.**
>   The seed only tells you *that* it's demand-mode, not the actual demand triggers, permit/season windows, or
>   buyer segments. The demand-cycle module is the page's centerpiece; an un-researched one *undercuts* the
>   "we know your business" promise. Run the real research pass (see Research method) before writing §4 for these.
> - **Lawn-care vs. lawn-maintenance axis — DECIDED 2026-06-17 (owner).** They overlap hard and would
>   **cannibalize** each other if both led on "the route." The locked split, in the owner's own terms:
>   **Lawn Care = the lawn's HEALTH** — a recurring treatment program (fertilization, weed control, aeration,
>   overseeding, **insect & disease treatment**). Its spine is **recurring revenue — renewals, retention, LTV**;
>   route density is a *supporting* point only. **Lawn Maintenance = the property's UPKEEP & appearance** —
>   mowing, landscape-bed maintenance, spring & fall cleanups, keeping it tidy, nice, and tight (broader than
>   mow/blow/edge). Its angle is **reliable recurring upkeep + route density** (where the mowing margins live),
>   distinct from lawn-care's treatment program. The Lawn Care page was **re-pointed to recurring-revenue on
>   2026-06-17** (its H1 had been "…fill the route," which belonged to maintenance). When you build
>   lawn-maintenance, the route/density + reliability story is **ITS** territory — different H1 keyword,
>   comparison rows, and FAQ — so the two never compete for the same query.
- **Lawn Care** *(= lawn HEALTH)* — recurring treatment program: fertilization, weed control, aeration, overseeding, insect & disease treatment. Spine = recurring revenue (renewals / retention / LTV); winter = pre-sell annual programs. Route density is support, not the headline.
- **Lawn Maintenance** *(= property UPKEEP & appearance)* — mowing, landscape-bed maintenance, spring & fall cleanups; keeping the property tidy, nice, and tight. Reliability + tight routes + thin margins; retention + filling open capacity; route/density is the margin game here (the angle lawn-care gives up).
- **Outdoor Living** — highest-ticket; long research cycle; portfolio + financing; sell in fall/winter, build next season.
- **Land Clearing** — project-based; acreage + equipment; permits; weather / ground-condition windows.
- **Excavation** — project-based, residential + commercial/bid; insurance + trust; dig-season + frost windows.
- **Septic Installation** — the owner's real prospect is **installers, not pumpers**: high-ticket, permit-gated install business. Failed-system replacement (homeowner search) + new construction (builder/GC) + real-estate upgrades + county-mandate compliance. Two-buyer split; closer to Excavation than to a pumping company.
- **Holiday Lighting** — hyper-seasonal: the year is won by booking Sept–Nov, installing Oct–Dec; pre-sell last year's list in late summer.

**Build order — ALL 8 DONE (2026-06-17).** Built in this order: **landscaping** (template) → **lawn-care** →
**lawn-maintenance** → **outdoor-living** (the recurring/seasonal four, layout-A 4-season) → **holiday-lighting**
(phase-based) → **land-clearing** → **excavation** → **septic-installation** (the demand-mode four, layout-B).
Proven across the set: the `.ind-seasons` grid takes any 4 cards, so the demand-cycle module flexes between a
4-season calendar (layout-A), a phase cycle (holiday lighting), and demand-mode cards (clearing/excavation/septic)
with no CSS change — it's a copy + card-label decision. The `.hl` headline must name the REAL cycle, not
"ahead of the seasons", except where that genuinely fits (holiday lighting; partially the dig/clear windows).

## Non-negotiables
- **No pricing.** The "cost" FAQ answers intent and routes to the free call.
- **No invented facts.** Real proof + real credentials only; anything unverifiable is a clearly-marked placeholder.
- **Lucide icons only** (stroke, 1.75, round, `currentColor`) — never emoji / unicode glyphs.
- **Google Partner badge = the real multicolor Google "G" logo** (the homepage one), wherever it appears
  (currently the hero trust strip — the on-page credential strip was removed). Never a generic check/circle
  icon. The hero strip needs `.ht-logo` on that `<svg>` so the lime-stroke rule doesn't recolor it.
- **`.hl` Twilight highlight**: one impact phrase per surface (use it on the demand-cycle H2).
- **Twilight `#6837EF` never blends with green.**
- **No em dashes in customer-facing copy** (brand rule, adopted 2026-06-17). Use commas, periods, or restructure;
  en dashes in ranges (Sept–Nov, 3–5 years) are fine. Applies to visible copy, meta, and the `@graph` text.
  The four demand-mode pages (holiday-lighting, land-clearing, excavation, septic) were built clean; the first
  four pages and the shared nav/footer were brought em-dash-free too (a sitewide pass completed 2026-06-17; the whole site and the build sources are clean).
- **Freshness — honest only.** Keep `dateModified` in the page's `@graph` schema, bumped **only on real
  updates**. **No visible "updated" chip, and never auto-stamp the current month** — that's "fake
  freshness" Google distrusts (it cross-checks the date against real content change) and it violates
  "no invented facts." Earn freshness by genuinely refreshing the page — the natural hook is a seasonal
  content refresh — and bump the schema date then. (Decided 2026-06-16; the visible `.ind-updated` chip
  was removed.)

## CSS / build notes
- The `.ind-*` framework now lives in **`/assets/css/industry.css`** (shared; `industry.css?v=1`),
  extracted from the page `<style>` after page 2 (lawn-care). New industry pages just **link it** — do
  **not** re-inline the block. Edit the framework in one place and bump `industry.css?v=` sitewide on the
  `/industries/*` pages. Page-specific one-offs can still go in that page's small `<style>`.
- Industry pages are **not generated** — hand-edit the page `index.html`. Reuse `simple-hero`,
  `.container`, `.svc-cta`, `.proof-cases`.
- After any header/footer edit, run `python3 build.py`. Schema uses the production domain; the page
  canonical stays staging (`new.lawnlab.dev`) until launch.

## Build checklist (per industry page)
- [ ] Hero: keyword eyebrow + ONE keyword H1 + full-white subhead + dual CTA + trust strip
- [ ] Answer-first definition (quotable bolded first sentence; no visible "updated" date)
- [ ] Comparison table (5 trade-tuned rows)
- [ ] Demand-cycle module (researched; **4-season cards OR demand-mode cards** per the trade; `.hl` headline; regional note)
- [ ] Service grid (8 cards incl. the Twilight AI standout, each links its service page, trade-specific copy)
- [ ] 5-step process
- [ ] Proof row (real cases) + testimonials section (real video testimonials, attributed)
- [ ] Program-fit cards (Growth + Authority)
- [ ] FAQ (6–8, answer-first; cost + seasonality + objection; no price) + `FAQPage` schema
- [ ] Twilight CTA + sibling-industry / programs links
- [ ] `@graph` schema (Org + Service + WebPage + Breadcrumb + FAQPage), matching the visible text
- [ ] **Answer-first pass:** read ONLY the first sentence under each H2, top to bottom — each must stand
      alone and answer its own heading (no "It depends…" / "There are a few…" openers). That string of
      first sentences is what an AI answer engine lifts; if it reads as a coherent summary, the page is GEO-ready.
- [ ] One H1; verify on preview (desktop + mobile); commit + push both branches; update
      `page-registry.md` + `build-status.md`
