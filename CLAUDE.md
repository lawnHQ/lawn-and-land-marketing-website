# Lawn & Land Marketing — Website

Orientation for a fresh session. Read this first, then `docs/website-source-of-truth/`.
Last updated: 2026-06-21. The site is content-complete and in pre-launch review.

## What this is
The future public website for **Lawn & Land Marketing** — a digital-marketing agency working
**exclusively with green-industry / lawn care & landscaping companies**. Static, multi-page,
hand-built HTML/CSS/JS (no framework). Final home: **lawnandlandmarketing.com** —
**NOT launched yet**; we build and review on staging.

- **Live staging:** https://new.lawnlab.dev — and the Vercel project domain
  https://lawnland-site.vercel.app (same deploy). Both always reflect `main`.
- **Deploy:** push to `main` → GitHub Actions (`.github/workflows/deploy.yml`) → Vercel
  production. Takes ~1–2 min. (Vercel also auto-creates auth-protected previews per branch.)
- **Branches:** all progress lives on `main`; the working branch `site-foundation` is kept
  in sync with it — push to **both** (`origin site-foundation` then `origin site-foundation:main`).
- **Cache-bust versions in use:** `styles.css?v=141`, `main.js?v=54`, `service-page.css?v=3`,
  `industry.css?v=2` (shared `.ind-*` framework on `/industries/*`). `styles.css` carries the global
  `text-wrap: balance` (headings) / `text-wrap: pretty` (body) line-break hints; the **actual
  no-lone-word guarantee** is a widow-guard in `main.js` that glues the last two words of every
  heading (each `<br>` segment) with a non-breaking space, at any viewport width. `balance` only
  evens line *widths*, not word counts, so it can't promise this on its own. The 8 industry
  intro-hook H2s are *also* hard-glued in the HTML (JS-off safety on the most visible headings).

## Status — what's DONE (developed)
- **Homepage** (`/`) — the benchmark page. Flow (reordered for conversion): hero (YouTube
  click-to-play facade) → stats → "Industries We Serve" grid → services → **mini case-study
  proof row** (3 real clients with photos + before→after numbers) → programs → "Why L&L" →
  testimonials (gold-glow 5-star) → **"Trusted By" logo marquee on the Twilight dot-grid band**
  → FAQ (+ `FAQPage` schema) → Twilight CTA. The unfinished Blog was pulled from nav + flow.
- **All 8 `/marketing-services/*` detail pages** — built on a locked, **generated** template:
  `website-design`, `local-seo`, `google-ads`, `meta-ads`, `gbp-management`, `your-ai-partner`,
  `reputation-management`, `automation`. Per page: hero → conviction stat → showcase + labeled
  image placeholder → "What's included" (purple featured card + 7 Lucide cards) → reversed
  showcase → FAQ → Twilight CTA. `Service` JSON-LD each.
- **Marketing-services HUB** (`/marketing-services/`) — built, hand-built SEO silo ("one machine"
  framing, 4 featured services + a wrap-up grid linking all 8, `ItemList` schema).
- **Growth Program page** (`/programs/growth/`) — **built**; the first finished program page.
  Lean, Hormozi-style, built entirely from the real contract (no pricing, no invented facts):
  `simple-hero` + breadcrumb → "Sound familiar?" 3 red pain cards → **"What you get" four-pillar
  section on the Twilight textured band** (World-Class Website / Local SEO / Google-LSA / CRM &
  Lead Mgmt) → "Why us" two-column (image placeholder left, copy right) → Twilight CTA.
  `Service` + `BreadcrumbList` JSON-LD, OG + Twitter card.
- **Authority Program page** (`/programs/authority/`) — **built**; the flagship. Same lean DNA as
  Growth, elevated for established **7-figure+** companies ("own your market"): hero → 3 pain cards →
  Twilight four-pillar "domination" band → full "everything included" deliverables grid → value play
  ("a whole team for less than one hire") → **Roadmap to Domination** timeline → partnership +
  credibility two-column (50+ clients, $300K–$14M+, 97% retention, NALP) → Twilight CTA. Built from
  the contract + pitch deck. `Service` + `BreadcrumbList` JSON-LD, OG + Twitter. No pricing.
- **Programs hub** (`/programs/`) — a simple two-program window: hero + Growth (six-figure) and
  Authority (seven-figure) cards that link into each program, plus a "not sure which?" CTA.
- **About page** (`/about/`) — **built** 2026-06-17 from the owner's REAL legacy content (no invented
  facts): mission ("your personal team", preserved) → **Meet the Owner** (Matt Foreman, real family
  photo, emoji-free) → why-specialization (Twilight band) → values/transparency (incl. the "we publish
  our worst review" ethos) → condensed **good-fit / not-a-fit** framework (from the old "Is Marketing
  Right For Us" page) → stat band → CTA. `@graph` schema (Organization + Person founder + AboutPage +
  BreadcrumbList). Includes a **Meet the Team** grid (`#team`) with 10 real members (names/roles/photos
  extracted from the legacy `/our-team/`). The standalone `/resources/meet-the-team/` was **retired**
  and nav + footer **repointed to `/about/#team`** (consolidated 2026-06-17). Retention stat reads
  **97%+** (owner: actually upper-97 to low-98).
- **Landscaping industry page** (`/industries/landscaping/`) — **built**; the first of 8 and the
  **reusable industry-page template**. Hero + trust strip → answer-first definition (two-column) →
  specialist-vs-generalist comparison table → **demand-cycle module** ("ahead of the seasons", four
  season cards on the Twilight band — the signature insight; non-seasonal trades use a demand-mode layout) →
  service grid (8, incl. the Twilight AI standout) → 5-step process → real proof cases + **video
  testimonials** → Growth/Authority program-fit → **visible FAQ accordion + FAQPage schema** → Twilight
  CTA. Engineered for SEO + GEO + EEAT (one keyword H1, question H2s, answer-first openers, `@graph`
  JSON-LD, real proof only). The reusable `.ind-*` framework now lives in a **shared `/assets/css/industry.css`**
  (extracted after page 2); new industry pages link it rather than re-inlining. Full spec:
  `docs/website-source-of-truth/industry-page-template.md`.
- **All 8 industry pages built off that template** (one keyword each, distinct spine — no cannibalization).
  The recurring/seasonal four: **Lawn Care** = the lawn's HEALTH / treatment program (spine: recurring
  revenue); **Lawn Maintenance** = the property's UPKEEP / mowing (spine: route density — the angle lawn-care
  cedes); **Outdoor Living** = high-ticket design-build/hardscape (spine: portfolio + the long, financed sale).
  The **demand-mode / phase-based** four (built 2026-06-17, NO four-season calendar): **Holiday Lighting**
  (phase cycle: pre-sell → booking → install → re-book); **Land Clearing** (pipeline / ground-access / burn /
  fire-mitigation); **Excavation** (pipeline / residential-vs-commercial split / dig conditions / 811);
  **Septic Installation** (failed-system replacement / new construction / real-estate upgrade / compliance — repositioned 2026-06-17 from septic *services* to *installers*, the owner's real prospect). The last four were authored
  **em-dash-free** (new brand rule); the earlier four + the shared nav/footer were brought em-dash-free too (sitewide
  pass completed 2026-06-17). Each page: full `@graph` schema, no pricing, real proof. See `build-status.md` /
  `decisions.md` / `industry-page-template.md` for the per-trade splits.
- **Universal header + footer** via `build.py` (edit `_header.html` / `_footer.html`; stamps everywhere).
  Nav Programs submenu icons: sprout (Growth), trophy (Authority).
- **The `.hl` Twilight highlight** — the signature one-impact-phrase marker (skewed −11° `#6837EF`
  swipe behind the lower portion of a phrase, white text, sharp edges). Defined in `styles.css`;
  also locked into the brand kit (see Related assets). Use sparingly — one phrase per surface.
  **Weight rule (owner, 2026-06-21):** `.hl` uses `font-weight: inherit` so the highlighted phrase
  ALWAYS matches the surrounding heading weight (e.g. 800) — never a fixed or lighter weight. Applies
  to every `.hl` instance, here and on any other L&L surface (incl. the brand kit).
- **Precision case study** (`/case-studies/precision/`) — **built** 2026-06-21; the first page of a new
  **`/case-studies/` silo** (reintroduced from the killed list per a builder directive) and the **reusable
  case-study template** (`case-study-template.md`). Migrated + modernized from the legacy WordPress
  `/precision-case-study/`. **Hybrid structure:** answer-first hero (calls 135→536 / +297%, one `.hl`) →
  **"At a Glance" conversion unit** (`.cs-tldr`: situation→outcome narrative + the single stat band +
  spend-anchored ROI line + CTA + "full breakdown ↓" hand-off — serves the skimmer) → **sticky ToC +
  scrollspy deep dive** (serves the deep reader): **native before/after data viz** (no chart screenshots),
  full-length **click-to-play** Nate Moses video (16:9 `ajusL5iAs0Q`, "Hear from the owner"), real proof
  **screenshots** re-hosted under `assets/images/precision/` (website, LSA, GBP, Featured Snippet, CRM,
  missed-call, reviews), copyedited **em-dash-free** story, Twilight CTA. `@graph` = Organization + Article
  + VideoObject + BreadcrumbList. **Math fix** (impressions +377%, not the old "475%"); AdWords→Google Ads.
  Cross-linked from the experiences hub + 4 industry proof cards. **Launch 301** from the old URL. Inline
  CSS (`.cs-*`); no `industry.css`. Owner actions before indexing: Nate's sign-off (ROI is owner-set at 23x; revenue $4.4M to $11.2M owner-provided).
- **Rock Solid Landscape case study** (`/case-studies/rock-solid/`) — **built** 2026-06-21 into the
  framework (cloned from Precision). Wauseon, OH; owner Zach Franz; an **organic/SEO-led** story (no
  paid ads). Crossed seven figures ($700K→$1M+) in a year; 4x calls, +378% impressions, +466% clicks.
  New reusable **month-by-month table** (`.cs-table`); real #1-ranking / ChatGPT / GBP screenshots under
  `assets/images/rock-solid/`. **AI-search claim reframed** (kept the real ChatGPT-top-pick screenshot,
  dropped "we dominate AI search" + the causation overclaim, added a point-in-time caveat). Fixed the
  generic title + Precision meta. Revenue **$700K → $1.4M** (owner-confirmed 2026-06-21, their first full year, a clean 2x), standardized everywhere (case study, roster, proof cards, FAQs); the video keeps its real "Over $1M" title.
- **Client Results roster** (`/client-results/`) — **built** 2026-06-21. The tiered ROSTER (Lawnline-style),
  nested under About (breadcrumb Home / About / Client Results; an About-dropdown nav item; no top-level nav).
  **Tier 1** = featured case-study cards (Precision + Rock Solid, exact stats + "Read the full case study →");
  **Tier 2** = lighter roster cards for the other testimonial owners (qualitative, no fabricated numbers, link
  to the experiences hub). DISTINCT from the experiences video wall. Hub-and-spoke interlinking: it links into
  the case studies; the experiences hub + each case study's Explore link to it. `CollectionPage` + `ItemList`
  + `BreadcrumbList`. Inline `.cr-*` CSS.

## Status — what's NOT done (launch prep, not new builds)
Every planned page is built (homepage, 8 services + hub, 2 programs + hub, 8 industries + hub, about,
contact, confirmation, booking, legal, the 3 resources content pages, 2 case studies, client-results).
What remains is launch prep + owner inputs:
- **Service-page owner inputs** (the 8 `/marketing-services/*`): real FAQ answers + `FAQPage`
  schema are DONE (2026-06-21: all 40 owner answers wired in, schema live on all 8 pages).
  Remaining: real images for the labeled placeholders. (Conviction stats verified 2026-06-21:
  6 confirmed accurate; Google Ads swapped to L&L's own 8-12% conversion rate vs ~3-6% industry.)
- **Real images** for the remaining labeled placeholders on program / industry / case-study pages.
- **Launch cutover** (`seo-launch-checklist.md`): flip canonicals + `og:url` staging→production,
  add `og:image` share graphics + `robots.txt`, keep `sitemap.xml` current.
- **Owner sign-offs (RECEIVED 2026-06-21):** Precision + Rock Solid both approved their names,
  numbers, video, and screenshots (cleared for launch indexing). GHL calendar confirmed at 20 minutes;
  Precision LSA figures ($250/wk, 9 leads) confirmed correct.
- **More case studies**: From The Ground Up numbers ($1.8M to $3.2M) confirmed by owner 2026-06-21,
  but the owner is HOLDING the case study for now (not enough full context yet). Do NOT build it
  until the owner explicitly asks; the `case-study-template.md` framework is ready when they do.

## How the site is built (tooling)
- **Header/footer:** edit `_header.html` / `_footer.html`, then `python3 build.py` (verify with
  `python3 build.py --check`). Vercel runs `build.py` on every deploy (see `vercel.json`).
- **Service pages are GENERATED:** edit copy in **`_content.json`** (one object per service) →
  `python3 gen_service.py` (renders each `/marketing-services/<slug>/index.html` from the
  `website-design` page as the structural template; all internal links generated by construction
  so they can't drift) → `python3 build.py`. **Don't hand-edit generated service HTML.** Full
  spec: `docs/website-source-of-truth/service-page-template.md`.
- **Program / industry / other pages are HAND-BUILT** (not generated). They reuse the same
  `styles.css` + `service-page.css` (`svc-*`, `simple-hero`, `svc-cta`) classes for consistency.
- **Styles:** `assets/css/styles.css` (global, nav, `.hl`) + `assets/css/service-page.css` (`svc-*`).
  Bump the `?v=` query **sitewide** when a CSS file changes. One-liner:
  `find . -name "*.html" -not -path "./.git/*" -print0 | xargs -0 sed -i '' -E 's/styles\.css\?v=[0-9]+/styles.css?v=NN/g'`

## Brand & content rules (non-negotiable — owner reviews for these)
- **Icons:** Lucide stroke SVGs only (1.75 weight, round caps, `currentColor`). NEVER emoji or
  unicode glyphs as icons.
- **Twilight `#6837EF` (purple) NEVER blends with green.** Premium standalone accent only: the
  purple featured card, the CTA spotlight + dot-grid band, the `.hl` highlight. Greens: Limeade
  `#ACE71D`, Gator `#5DCA49`. Dark base `#07100A`.
- **No pricing anywhere** on the site — every CTA routes to the free strategy call
  (`/get-started/book-strategy-call/`).
- **No invented facts.** Anything unverifiable is a clearly-marked placeholder. Conviction stats
  must be REAL + sourced (`statSource` in `_content.json`). FAQ answers stay `[NEEDS YOUR INPUT]`
  until the owner supplies them; `FAQPage` schema is added only once answers are real.
- **Keyword variants:** lead with the page's primary term, weave 2–3 natural variants. No stuffing.
- **City/county names** always carry a 2-letter state code ("Tampa, FL"), Title Case.
- **The two program avatars are DIFFERENT — don't conflate them:**
  - **Growth** ($400K–$1M, "six-figure"): grew offline on referrals/repeat work, hit the ceiling,
    nearly invisible online, trying to get FOUND for the first time → foundation / get-found story.
  - **Authority** (7-figure+): already doing some online marketing → omnipresent / dominate-the-market
    story. The vendor-sprawl + agency-scar-tissue + "optimize what exists" pains belong HERE, not Growth.

## SEO conventions
- Per page: unique `<title>`, meta description (~155 chars), `canonical`, Open Graph + Twitter card.
  (`og:image` / share graphics are a launch task — not added yet.)
- Schema: `Service` on service pages + Growth; `BreadcrumbList` where there's a visible breadcrumb;
  `FAQPage` only when the answers are real. Homepage carries `MarketingAgency`/Organization +
  `WebSite` + `FAQPage`.
- **Schema uses the production domain** (`lawnandlandmarketing.com`) even though page **canonicals
  still point to staging** (`new.lawnlab.dev`). The canonical flip is a single launch-time find/replace.

## Launch checklist (later — `docs/website-source-of-truth/seo-launch-checklist.md`)
Flip all `new.lawnlab.dev` → `lawnandlandmarketing.com` (canonicals + `og:url`); add `og:image`
share graphics; keep the real **`sitemap.xml`** current (rebuilt 2026-06-15 to the real routes —
no killed routes); add `robots.txt`; verify the service-page conviction stats; land real FAQ
answers + `FAQPage` schema; drop real images into placeholders. **Don't deploy to the production
domain until launch.**

## Working with the owner (Matt)
Product-minded, not a deep engineer — explain **outcomes**, not git/Vercel/CLI/deploy mechanics
(handle those quietly). He reviews visible changes on the **live URL** (hard-refresh after a push;
deploys take ~1–2 min). In-tool screenshots don't render well for him.

## Related assets
- **Brand kit** — separate repo `LawnAndLandMarketing/brandkit` → https://brandkit.lawnlab.dev
  (Next.js; guide content in `public/brandkit-*.html|css`; AI-readable brief at `/brand`). The
  `.hl` Twilight emphasis marker is documented there in §09 Typography.

## Docs (`docs/website-source-of-truth/`)
`restart-guide.md` (fastest re-entry) · `build-status.md` (done / not-done) · `page-registry.md`
(page-by-page status table) · `sitemap.md` (approved routes) · `routing-rules.md` (canonical /
killed routes) · `service-page-template.md` (the locked service-page template + generator) ·
`industry-page-template.md` (the locked industry-page framework + SEO/GEO/EEAT strategy) ·
`case-study-template.md` (the `/case-studies/*` hybrid template: hero → "At a Glance" → deep dive) ·
`navigation.md` (universal header / nav / submenus + footer) · `decisions.md` (durable decisions log) ·
`seo-launch-checklist.md` · `benchmark-lawnline.md`.
**Keep these current in the same workstream as any structural change.**
