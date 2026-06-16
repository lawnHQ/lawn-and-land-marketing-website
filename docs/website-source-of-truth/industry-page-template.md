# Industry Page — Universal Template & Strategy

The eight `/industries/*` pages are our **heavy keyword + GEO play**: the page a business owner lands
on when they search "[their trade] marketing" or "marketing for [their trade] companies." Each one
must prove we deeply understand *their* business — services, customers, and especially **seasonality** —
and convert that trust into a booked strategy call.

- **Reference build:** `/industries/landscaping/` — the first page and the **locked template**.
- **Built / approved:** 2026-06-15 (Matt: "nailed the design, keywords, strategy, differentiator, pain points").
- **HAND-BUILT** (not generated like service pages). Each reuses `simple-hero`, `.svc-cta`, and the
  homepage `.proof-cases` row, plus a reusable `.ind-*` framework scoped in the page's own `<style>`.
- **Stylesheets:** link `styles.css` **and** `service-page.css`; the `.ind-*` classes live in the page
  `<style>` block (copy per page — see CSS notes below). Wrap content in `<main id="main">`.

## The thesis (why this structure wins)
Generic "home-services marketing" pages lose to specialists. We win by **demonstrating first-hand
expertise** (EEAT "Experience") and structuring every section so both Google and AI answer engines
(GEO) can lift it cleanly. The single sharpest weapon is the **seasonality module** — proof we know the
owner's calendar better than they expect. Our #1 benchmark, Lawnline, has **no FAQ on any industry page
and real seasonality on only one** — those two are our biggest openings, so we lean into both hard.

## Sections, in order
Each section lists its job and why it's there for SEO / GEO / EEAT.

1. **Hero** (`.simple-hero`) — breadcrumb · `[Industry] Marketing` eyebrow (the keyword) · ONE
   keyword-bearing `<h1>` · full-white subhead with native vocabulary · two CTAs · an **above-fold
   trust strip** (`.hero-trust`: NALP · Google Partner · green-industry focused · 97%+ retention).
   *SEO: H1 keyword. EEAT: badges up top. GEO: a crisp definition follows immediately.*
2. **Answer-first definition + owner's reality** (`.ind-sec` / `.ind-lede`) — a **bolded one-sentence
   definition** of "[industry] marketing" + 3–4 sentences naming the owner's real pain. Carries a visible
   **"Updated {Month YYYY}"** (`.ind-updated`). *GEO: the bolded sentence is the quotable definition.
   SEO: freshness. EEAT: empathy = Experience.*
3. **Why generic marketing fails + comparison table** (`.ind-compare`) — answer-first paragraph, then a
   **specialist-vs-generalist table** (rows tuned to the trade: knows your season / speaks your language /
   builds the right site / filters your leads / proof that closes). *GEO: tables cite well. EEAT: expertise.*
4. **Seasonality module — THE centerpiece** (`.ind-band` Twilight band + `.ind-seasons`) — H2 with a
   `.hl` highlight (e.g. "we market your company **one season ahead**"), then **four season cards**
   (Winter / Spring / Summer / Fall), each split **"On the ground"** vs **"What we market."** Close with a
   warm-climate note. *The information-gain play competitors can't write. GEO + EEAT gold.*
5. **What we build** (`.ind-services`) — answer-first intro + a grid of service cards, **each linking to
   its `/marketing-services/*` page**, with industry-specific copy. *SEO: hub-and-spoke internal links.
   GEO: extractable list.*
6. **How we work** (`.ind-steps`) — a numbered 1→5 process. *GEO: numbered steps cite well. EEAT:
   transparency stands in for the price transparency we deliberately omit.*
7. **Proof, Not Promises** (`.proof-cases`, reused from the homepage) — the **three real client cases**
   (Rock Solid Landscape, Precision Landscape Management, From The Ground Up Landscaping). *EEAT
   Experience + Trust. Real numbers only.*
8. **Why Lawn & Land + credential strip** (`.ind-cred`) — niche-only positioning + the real credential
   row (NALP · Google Partner · 100+ companies served · 97%+ retention · since 2022). *EEAT Authoritativeness.*
9. **Program fit** (`.ind-fit`) — two cards linking **Growth** (6-figure, lime) and **Authority**
   (7-figure, Twilight). *SEO: internal links to programs; qualifies the visitor.*
10. **FAQ** (`.ind-faq`, visible `<details>` accordion, 6–8 Q&As, **answer-first 40–60 words**) +
    **`FAQPage` schema**. Cover the objection + **"cost" intent** (answer the intent, **never a price**) +
    the seasonality question. *GEO: top AI-extraction zone — the gap Lawnline leaves wide open.*
11. **Final CTA** (`.svc-cta` Twilight band) — book the free call + "Explore" links (a sibling industry + Programs).

**Head schema:** one `<script type="application/ld+json">` with an `@graph`:
**Organization + Service + WebPage (`dateModified`) + BreadcrumbList + FAQPage.** Schema text must match
the visible text.

## SEO / GEO / EEAT principles baked in
1. **One keyword H1**; H2s are real questions or specific claims with keyword *variants* (never repeat the exact phrase).
2. **Answer-first**: the first ~40–75 words under every H2 stand alone and answer the heading — that's what AI lifts.
3. **High-citation formats**: at least one comparison **table** + one **numbered** process + bulleted lists.
4. **Information gain**: 2–3 things only a true specialist could write (the seasonality math, the trade's economics). The moat.
5. **Real signals only** (EEAT): real proof cases, real credentials, native vocabulary, a freshness date. **Never fabricate.**
6. **Internal links**: every service mentioned links out; link both programs and ≥1 sibling industry; breadcrumb up.

## Per-industry "what to swap" (the structure stays identical)
- Hero eyebrow / H1 / subhead + `<title>` / meta / OG / Twitter (keyword = "[industry] marketing")
- The answer-first **definition** sentence
- The 5 **comparison-table** rows (tuned to the trade's economics)
- The **seasonality module** — *research this per industry; it's the centerpiece*
- The **service-grid** emphasis + copy (same 7 services, trade-specific framing)
- **Proof-row** intro line (the three cases stay the real ones)
- The **FAQ** (trade-specific questions; keep the cost + seasonality ones)
- Schema `serviceType`, `name`, `breadcrumb`, FAQ entities

## Research method (do this per page BEFORE building)
Brief up, per industry: (1) the **business model / service mix** and where the money is; (2) **customer
segments** and how they buy; (3) the **seasonality / demand cycle** quarter-by-quarter, framed as *market
one season ahead*; (4) the biggest **business + marketing pains**; (5) **native vocabulary**. Landscaping's
brief is the depth bar to hit — its core insight: a landscaper is *three businesses* (**design** qualifies →
**installs** earn the money → **maintenance** sustains and feeds the next install), the cardinal sin is
marketing *in sync* with demand instead of *ahead* of it, the portfolio is the product, and reviews are the
gatekeeper. Use parallel research agents (Lawnline teardown + domain brief + current SEO/GEO/EEAT playbook)
the way the landscaping build did.

## Per-industry seed angles (starting points — research + sharpen per page; NOT yet facts)
- **Lawn Care** — recurring / route density; seasonal treatment programs (fert / weed / aeration); LTV > one-offs; winter = pre-sell annual programs.
- **Lawn Maintenance** — volume + tight routes + thin margins; retention + filling open capacity fast; lock contracts late winter / early spring.
- **Outdoor Living** — highest-ticket; long research cycle; portfolio + financing; sell in fall/winter, build next season.
- **Land Clearing** — project-based; acreage + equipment; permits; weather / ground-condition windows.
- **Excavation** — project-based, residential + commercial/bid; insurance + trust; dig-season + frost windows.
- **Septic Services** — split urgent/emergency intent (speed, reviews, GBP) vs. routine pumping/inspection reminders; recession-resistant.
- **Holiday Lighting** — hyper-seasonal: the year is won by booking Sept–Nov, installing Oct–Dec; pre-sell last year's list in late summer.

## Non-negotiables
- **No pricing.** The "cost" FAQ answers intent and routes to the free call.
- **No invented facts.** Real proof + real credentials only; anything unverifiable is a clearly-marked placeholder.
- **Lucide icons only** (stroke, 1.75, round, `currentColor`) — never emoji / unicode glyphs.
- **`.hl` Twilight highlight**: one impact phrase per surface (use it on the seasonality H2).
- **Twilight `#6837EF` never blends with green.**

## CSS / build notes
- The `.ind-*` framework is **scoped in the page `<style>`** (copy the block per page). Once 2–3 pages
  exist, consider extracting it to a shared `industry.css` (then bump its `?v=`). Landscaping changed **no
  global CSS** → no cache-bump (`styles.css?v=138`, `service-page.css?v=3`).
- Industry pages are **not generated** — hand-edit the page `index.html`. Reuse `simple-hero`,
  `.container`, `.svc-cta`, `.proof-cases`.
- After any header/footer edit, run `python3 build.py`. Schema uses the production domain; the page
  canonical stays staging (`new.lawnlab.dev`) until launch.

## Build checklist (per industry page)
- [ ] Hero: keyword eyebrow + ONE keyword H1 + full-white subhead + dual CTA + trust strip
- [ ] Answer-first definition + "Updated {Month YYYY}"
- [ ] Comparison table (5 trade-tuned rows)
- [ ] Seasonality module (researched; 4 cards; `.hl` headline; warm-climate note)
- [ ] Service grid (7 cards, each links its service page, trade-specific copy)
- [ ] 5-step process
- [ ] Proof row (the real three cases)
- [ ] Credential strip (real signals only)
- [ ] Program-fit cards (Growth + Authority)
- [ ] FAQ (6–8, answer-first; cost + seasonality + objection; no price) + `FAQPage` schema
- [ ] Twilight CTA + sibling-industry / programs links
- [ ] `@graph` schema (Org + Service + WebPage + Breadcrumb + FAQPage), matching the visible text
- [ ] One H1; verify on preview (desktop + mobile); commit + push both branches; update
      `page-registry.md` + `build-status.md`
