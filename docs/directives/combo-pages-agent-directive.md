# Directive: Build the Next 10 Service + Industry Combination Pages

Owner: Lawn & Land Marketing  
Repo: `LawnAndLandMarketing/lawn-and-land-marketing-website`  
Primary production domain: `https://lawnandlandmarketing.com`  
Canonical production Vercel project: `lawnland-site`  
Date: 2026-06-25

## Mission

Build the next 10 **service + industry combination pages** to the same or higher quality standard as the first live page:

`/marketing-services/lawn-care-seo/`

These pages should feel like a natural part of the website, not bolted-on SEO pages. Each page must have a clear strategic reason to exist, avoid cannibalizing the core service pages or industry pages, and be linked from the correct service cards on the relevant industry pages.

The strategy is correct: instead of adding these pages awkwardly to the main nav, replace selected industry-page service card links so the user naturally moves from an industry page into a more specific service-for-that-industry page.

Example already live:

- `/industries/lawn-care/`
- card: `Lawn Care SEO`
- links to: `/marketing-services/lawn-care-seo/`

## Do not start by cloning blindly

Before building the 10 new pages, first review and clean up the existing model page:

`marketing-services/lawn-care-seo/index.html`

Known cleanup items from audit:

- Fix punctuation artifacts such as:
  - `Lawn Care SEO, fully handled .`
  - `Lawn Care SEO, answered .`
- Preserve the canonical, meta description, robots, OG/Twitter tags, `Service` schema, and `FAQPage` schema.
- Improve mobile performance where practical. Current live check showed SEO 100 and CLS 0, but mobile performance/LCP was weak on the combo page. Do not use risky homepage-style critical-CSS hacks unless both LCP and CLS pass.
- Treat this page as the quality baseline only after the cleanup pass.

## Page architecture: avoid cannibalization

Every page must have a distinct job.

### Core service page

Example: `/marketing-services/local-seo/`

Owns the broad service concept across the green industry.

Intent:

- local SEO as a service
- how Lawn & Land handles SEO generally
- green-industry-wide positioning

Do not rewrite combo pages as generic duplicates of the core service page.

### Industry page

Example: `/industries/lawn-care/`

Owns the broad vertical.

Intent:

- marketing for that industry overall
- the full growth system for that trade
- industry-specific demand cycle, proof, service mix, and program fit

Do not rewrite combo pages as a second version of the industry page.

### Combo page

Example: `/marketing-services/lawn-care-seo/`

Owns one service applied to one industry.

Intent:

- specific searcher has both the service and industry in mind
- `SEO for lawn care companies`
- `Google Ads for landscaping companies`
- `website design for outdoor living contractors`

A combo page should answer: **what changes when this specific marketing service is done for this specific kind of contractor?**

## Locked anti-cannibalization rules

1. One primary keyword target per page.
2. One unique business spine per page.
3. Do not reuse the same intro, H2 structure, FAQ set, or examples with only the industry name swapped.
4. The H1 must be specific, but not spammy.
5. The first paragraph must answer the exact service + industry intent immediately.
6. Use internal links to clarify hierarchy:
   - combo page links back to the relevant industry page
   - combo page links back to the relevant core service page
   - relevant industry service card links to the combo page
7. Do not add all combo pages to the main nav or footer service list unless Matt explicitly approves. The point is natural contextual discovery, not nav stuffing.
8. Do not create orphan pages. Every new page needs at least one contextual internal link from the relevant industry page before it is considered complete.
9. Update `sitemap.xml` for every new indexable page.
10. No em dashes in copy.

## Critical industry spine rules

These are locked from prior site strategy decisions.

### Lawn Care vs Lawn Maintenance

Do not blur these.

- **Lawn Care** = the lawn's health. Recurring treatment programs: fertilization, weed control, aeration, overseeding, insect/disease treatment. Spine: recurring revenue, renewals, retention, LTV.
- **Lawn Maintenance** = the property's upkeep and appearance. Mowing, route density, weekly service, crew efficiency. Spine: route density and mowing operations.

Do not make both pages lead with “fill the route.” Lawn maintenance owns route density. Lawn care can mention route density only as a supporting benefit of recurring programs.

### Landscaping vs Outdoor Living

- **Landscaping** = broader landscaping services, maintenance/design/install mix, local demand, proof, trust, service-area presence.
- **Outdoor Living** = higher-ticket design-build/hardscape projects, portfolio proof, design consultation, longer sales cycle, financing/decision complexity.

Do not let outdoor living pages sound like generic landscaping pages.

### Septic Installation

The site has consciously chosen **septic installation**, not septic pumping/service.

- Target installers.
- Do not chase emergency pumping/service keywords.
- If emergency septic service is ever added, that would be a separate page with a separate spine.

### Holiday Lighting

Owns seasonal booking and rebooking.

- pre-sell
- booking window
- installation season
- takedown/rebooking

Do not write it like a normal year-round SEO/ads page.

### Land Clearing / Excavation

These are project-based, location-sensitive, and condition-sensitive.

- Land Clearing: acreage, forestry mulching, defensible space, before/after proof, mobilization radius.
- Excavation: sitework, grading, trenching, drainage, residential/commercial split, 811/conditions, trust/scope clarity.

Do not merge them into the same “heavy equipment contractor” copy.

## Target page set

Use this as the working target set unless Matt provides a different approved list.

### SEO combo pages

1. `/marketing-services/landscaping-seo/`
   - Primary intent: SEO for landscaping companies
   - Link from `/industries/landscaping/` Local SEO card
   - Core service parent: `/marketing-services/local-seo/`

2. `/marketing-services/lawn-maintenance-seo/`
   - Primary intent: SEO for lawn maintenance / mowing companies
   - Link from `/industries/lawn-maintenance/` Local SEO card
   - Must emphasize route density and mowing/upkeep, not treatment-program LTV

3. `/marketing-services/outdoor-living-seo/`
   - Primary intent: SEO for outdoor living / hardscape / design-build companies
   - Link from `/industries/outdoor-living/` Local SEO card
   - Must emphasize portfolio, design consultations, high-ticket projects, trust

4. `/marketing-services/holiday-lighting-seo/`
   - Primary intent: SEO for holiday lighting companies
   - Link from `/industries/holiday-lighting/` Local SEO card
   - Must emphasize seasonal pre-booking and rebooking

5. `/marketing-services/land-clearing-seo/`
   - Primary intent: SEO for land clearing companies
   - Link from `/industries/land-clearing/` Local SEO card
   - Must emphasize acreage owners, forestry mulching, defensible space, mobilization radius

6. `/marketing-services/excavation-seo/`
   - Primary intent: SEO for excavation companies
   - Link from `/industries/excavation/` Local SEO card
   - Must emphasize sitework/grading/trenching/drainage and serious-project trust

7. `/marketing-services/septic-installation-seo/`
   - Primary intent: SEO for septic installation companies
   - Link from `/industries/septic-installation/` Local SEO card
   - Must not target septic pumping/emergency service as the main intent

### Paid search combo pages

8. `/marketing-services/lawn-care-google-ads/`
   - Primary intent: Google Ads for lawn care companies
   - Link from `/industries/lawn-care/` Google & Local Service Ads card
   - Must emphasize recurring-program signups, treatment demand, seasonal push windows

9. `/marketing-services/landscaping-google-ads/`
   - Primary intent: Google Ads for landscaping companies
   - Link from `/industries/landscaping/` Google & Local Service Ads card
   - Must emphasize qualified job mix, service-area targeting, budget waste control

10. `/marketing-services/outdoor-living-google-ads/`
   - Primary intent: Google Ads for outdoor living / hardscape companies
   - Link from `/industries/outdoor-living/` Google & Local Service Ads card
   - Must emphasize high-ticket consults, project qualification, portfolio-led landing experience

If Matt changes the target list, preserve the same rules: one service + one industry, one unique spine, one industry-card link.

## Required page template standards

Use the existing `lawn-care-seo` page as the structural starting point, but improve it. Each new page must include:

1. Full HTML page under:
   - `marketing-services/{slug}/index.html`
2. `<title>` focused on the exact combo intent.
3. Meta description, around 145-160 characters, specific to the industry/service.
4. `<meta name="robots" content="index, follow">`
5. Canonical URL on `https://lawnandlandmarketing.com/.../`
6. OG and Twitter metadata.
7. `Service` JSON-LD with:
   - `provider` as `https://lawnandlandmarketing.com/#organization`
   - `serviceType` matching the combo page
   - description unique to the page
8. `FAQPage` JSON-LD matching visible FAQs.
9. One H1 only.
10. Clear breadcrumbs.
11. Contextual links to:
    - relevant industry page
    - core service page
    - closely related service pages where useful
    - strategy call / get started path
12. Relevant CTA language that matches the page intent.
13. No placeholder/invented case studies or fake stats.
14. No pricing unless already approved elsewhere.
15. No client claims that are not already supported by the site.

## Content quality bar

The copy should sound like Lawn & Land:

- direct
- operator-level
- specific to green-industry realities
- no agency fluff
- no generic “drive traffic and grow your business” filler
- no puns except “Let’s get growing” if already part of the CTA system
- no em dashes
- no fake guarantees
- no keyword stuffing

Every page should include concrete examples of searches, but keep them natural.

Good:

> Rank for the treatment and service-area searches that actually turn into recurring lawn care programs: fertilization, weed control, aeration, and lawn care near me.

Bad:

> Our lawn care SEO services help lawn care companies with lawn care SEO so your lawn care business ranks for lawn care SEO keywords.

## Recommended page structure

Use this structure unless there is a strong reason to deviate:

1. Hero
   - breadcrumbs
   - kicker
   - H1
   - answer-first paragraph
   - primary CTA
   - secondary CTA to the relevant industry/core service page

2. Why this combo matters
   - Explain what changes when this service is applied to this trade
   - Must include business-model reality, not just marketing tactics

3. What gets built/managed
   - Service-specific deliverables
   - Industry-specific examples

4. Search/lead intent module
   - What prospects are searching for
   - Which terms are valuable
   - Which terms are bad-fit or wasteful

5. Conversion/system module
   - Website/landing page/GBP/CRM/follow-up relationship
   - Show that the channel does not work in isolation

6. Proof / standards / measurement
   - Use real broad proof already supported by the site
   - Do not invent page-specific case studies unless sourced

7. FAQ
   - 4-6 visible FAQs
   - Answers must be direct and not repetitive

8. CTA
   - Match current Lawn & Land CTA style
   - No hard-sell hype

## Industry card linking instructions

For every new combo page, update the matching card on the relevant `/industries/{industry}/index.html` page.

Example pattern:

```html
<a class="ind-svc" href="/marketing-services/lawn-care-seo/">
  ...
  <h3>Lawn Care SEO</h3>
  ...
  <span class="is-link">Lawn Care SEO →</span>
</a>
```

Rules:

1. Update the card `href` to the combo page.
2. Update the card heading only if it improves clarity.
3. Keep the existing visual design/classes intact.
4. Do not create visual inconsistency across the industry grid.
5. Do not change unrelated cards.
6. Do not update global nav/mega menu links to combo pages unless Matt explicitly asks.
7. Preserve the core service pages in the footer/nav as the broad service destinations.

## Internal link rules on combo pages

Each combo page should link to:

- the matching industry page near the top or middle
- the matching core service page
- at least 1-2 adjacent service pages if relevant
- the get-started/strategy call path

Example for `/marketing-services/landscaping-seo/`:

- `/industries/landscaping/`
- `/marketing-services/local-seo/`
- `/marketing-services/gbp-management/`
- `/marketing-services/website-design/`
- `/get-started/book-strategy-call/`

Do not create link farms. Links should read naturally.

## Sitemap requirement

Add each new combo page to `sitemap.xml`.

Recommended values:

- `changefreq`: `monthly`
- `priority`: `0.7` for primary combo pages, unless Matt specifies otherwise
- `lastmod`: current date of build

## Performance requirements

Run Lighthouse on at least:

- existing `lawn-care-seo` page after cleanup
- 2 representative new combo pages
- any page where hero/image/CSS differs materially

Targets:

- SEO: 100
- Accessibility: 95+
- Best Practices: 95+
- CLS: 0 or near 0, never ship visible layout shift
- Mobile performance: improve where practical, but do not trade stability/brand rendering for a score

Known caution: the existing combo page had mobile performance around 67 and LCP around 6.1s in one live check. Improve this if possible, but do not repeat the homepage critical-CSS/font-display mistake. Keep brand fonts stable. Do not use `display=optional`.

## Validation commands

Run before final handoff:

```bash
python3 build.py --check
python3 scripts/check_links.py
python3 -m json.tool vercel.json >/tmp/vercel_json_ok.json
git diff --check
```

Also run live/local spot checks for:

```bash
curl -I https://lawnandlandmarketing.com/marketing-services/{slug}/
```

If deploying, verify production after deploy with cache-busting URLs.

## Final handoff format

When done, report:

1. Pages created with URLs.
2. Industry cards updated with source page + old href + new href.
3. Sitemap entries added.
4. Validation commands run and result.
5. Lighthouse results for sampled pages.
6. Any content/cannibalization concerns that remain.
7. Any pages intentionally not linked and why.

## Hard stop conditions

Stop and ask before proceeding if:

- the exact 10-page list differs from this directive and no approval exists
- a proposed page would clearly cannibalize an existing industry/core service page
- a combo page requires claims, case studies, stats, or service details not already supported by Lawn & Land source material
- the build requires global nav/footer restructuring
- the work would require domain/Vercel project changes

## Success definition

This project is successful when:

- all 10 combo pages are live-ready, indexable, and internally linked
- no page is orphaned
- industry pages feel more useful, not more cluttered
- combo pages have distinct search intent and business spines
- the site architecture is stronger for rankings without looking like SEO pages were stuffed into the site
