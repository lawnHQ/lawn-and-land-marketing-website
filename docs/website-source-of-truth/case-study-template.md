# Case Study Template (`/case-studies/*`)

The reusable structure for every case study in the `/case-studies/` library. Established
2026-06-21 with case study #1, **Precision Landscape Management** (`/case-studies/precision/`).
Hand-built (not generated); page-specific CSS is inline (`.cs-*`); it does NOT load
`industry.css`. Clone Precision and swap the content to build the next one.

## The hybrid principle (why it's built this way)
A case study has to serve **two readers at once**:
1. The **skimmer** who thinks in outcomes and wants proof in ~60 seconds, then a CTA.
2. The **deep, skeptical owner** who wants the methodology, the mechanism, and the receipts.

A short competitor-style page serves only #1 (and its deep reader gets nothing more). Our
hybrid serves both on one page: a tight **"At a Glance"** conversion unit up top for the
skimmer, with the **full long-form breakdown** preserved below for the deep reader.

## Page order (top to bottom)
1. **Hero** (`.simple-hero`): breadcrumb (`Home / Case Studies / <Client>` — "Case Studies" is a
   non-link crumb, no hub page exists) + kicker (`Case Study · <City, ST>`) + H1 with ONE `.hl`
   highlight on the headline number + **answer-first opener** (one quotable sentence: who, where,
   the headline outcome, the timeframe) + primary CTA + a "See the results" jump.
2. **"At a Glance" / "The short version"** (`.cs-tldr`) — the self-contained conversion unit, set on
   the **Twilight textured + dot-grid band** (the brand "spotlight" treatment: `#0d0b14` + a purple
   radial glow + the 22px white dot-grid + purple hairline borders; same recipe as the homepage stats
   bar and `.ind-band`). Lime stat numbers on the twilight band is the established pattern, not a clash.
   - eyebrow "The short version"
   - 2–3 sentence **situation → outcome** narrative (distill it LAST; do not copy the intro)
   - the **single** stat band (`.cs-tldr-stats` of `.cs-ss`) — 4 headline metrics. This is the
     ONLY stat band on the page; do not duplicate it.
   - **spend-anchored ROI line** (`.cs-tldr-roi`): "invested approximately $X and generated more
     than Nx that." If the spend isn't owner-approved for disclosure, drop the dollar figure and
     keep "more than Nx return" — never guess a number.
   - **CTA + hand-off**: `Book a Free Strategy Call` AND "Want the full breakdown? See exactly how
     we did it ↓" (anchors to `#results`). Keep the whole block ~120–150 words max.
3. **Sticky Table of Contents + body** (`.cs-layout` → `.cs-toc` + `.cs-body`), scrollspy-highlighted.
4. **Results** (`#results`): native before/after data viz (`.cs-ba` cards) + secondary stats
   (`.cs-stat`). Render numbers as designed elements, NOT screenshots.
5. **"Hear from the owner"** (`#testimonial`): full-length 16:9 testimonial via the click-to-play
   pattern (`.testi-video-wrap[data-videoid]`, no `short-vid`); caption carries the client's real
   approved quote + the page's precise numbers. ToC label + heading say "the owner" (template-
   generic), the caption names the person. Prefer the full-length video over a short clip.
6. **The deep dive**: one `.cs-section` per service area, each opening with an extractable sentence,
   real proof screenshots (`.cs-shot`, `.cs-shot--narrow` for portrait/square shots), pull-quotes
   (`.cs-callout`), and check-list mechanics (`.cs-list`). For a metric that grew over time (reviews,
   rating, revenue), use a native **then → now** comparison (`.cs-gbp`-style cards: a neutral "when we
   started" card + an arrow + a lime-accented "today" card) rather than two mismatched screenshots —
   it sidesteps screenshot-dimension problems and reads cleaner. Keep one real screenshot as the anchor.
7. **Conclusion** + **Twilight CTA** (`.svc-cta`) with 3–4 "Explore" links to the trades the study
   demonstrates + Client Experiences.

## Rules (carry forward every time)
- **No contradictions:** every NUMBER on the page uses the same precise figure set (the rounded way
  an owner speaks on video is fine inside the video; the on-page copy must match the data).
- **Real proof only:** real screenshots (hosted locally under `assets/images/<client>/`, descriptive
  alt text naming the client + the result), real video, real numbers. If a screenshot isn't
  available, leave the slot out rather than faking it. No invented spend/ROI.
- **Em-dash-free**, no pricing, all CTAs → `/get-started/book-strategy-call/`, `.hl` used once.
- **Schema** (`@graph`): Organization + Article + VideoObject (real per-video `uploadDate`) +
  BreadcrumbList ("Case Studies" crumb is name-only). Schema text matches visible text.
- **Distribution:** cross-link the case study from the experiences hub and the relevant industry
  proof cards ("Read the full case study →"). Plan a launch 301 from any old URL.
- **Owner sign-off before indexing:** named results, ROI multiple + spend, client approval to publish.

## Credibility rules (non-negotiable — what keeps the library trustworthy)
- **ROI is a standalone, defensible claim.** Calculate it on MARKETING-ATTRIBUTED revenue (spend vs. the revenue the marketing can be traced to), NOT company-wide revenue. Frame it explicitly as a marketing return ("for every $1 in marketing, more than $Nx came back"), distinct from any company-wide revenue figure shown nearby. No defensible multiple for a client? Do not invent one — omit it (the revenue trajectory can be the "return").
- **Attribution-honesty statement is MANDATORY when company-wide revenue is shown.** Pattern: "These are company-wide results, and [Client] is a strong operator in its own right. Their growth reflects their own team and execution as much as the marketing. Our role was to be one of its core drivers, and the right marketing partner to grow alongside."
- **Defensibility-check every claim.** Keep a claim only if there is real, client-specific proof. An "AI search" claim ships only with a real screenshot of THAT client surfacing in the AI answer, framed point-in-time (AI answers change) — never a generic "we dominate AI search" with no proof, and never an unprovable causation claim.
- **Verify every percentage and multiplier against the raw numbers** before publishing (the old "475%" was 377%). Reconcile conflicting source figures to ONE consistent story; when the conflict is an owner-revenue figure, prefer the owner's on-record words and flag for confirmation.
- **Real proof only:** no stock, no mockups, no invented data, and **no generated/Gemini placeholder images** in production. Strip WordPress cruft (generic or borrowed titles + meta, promo bars, lead-magnets, duplicate heading dumps, tracking pixels).

## Reusable elements (mix and match per client)
`.cs-tldr` At-a-Glance on the Twilight dot-grid band · `.cs-ba` before→after cards · `.cs-stat` secondary stats · `.cs-rev` ascending revenue bar chart (2+ bars, peak in lime) · `.cs-table` **month-by-month results table** (highlight the final row with `.is-peak`) · `.cs-gbp` then→now comparison · `.cs-shot` framed screenshots · `.cs-callout` pull-quote · `.cs-list` checklist.

## Library status
- **Precision** (`/case-studies/precision/`) — reference build, paid-led (PPC + LSA). 23x ROI (~$150K/yr spend, marketing-attributed); $4.4M→$11.2M revenue trajectory.
- **Rock Solid** (`/case-studies/rock-solid/`) — built 2026-06-21, organic/SEO-led (no ads). $700K→$1.4M revenue (owner-confirmed final figure). Introduced the `.cs-table` element + the point-in-time AI-search treatment. No ROI multiple (none available).
- **From The Ground Up** ($1.8M→$3.2M, referenced sitewide) — build into the framework once the figure + approval are confirmed.
