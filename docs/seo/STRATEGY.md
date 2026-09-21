# lawnandlandmarketing.com — SEO strategy and operating file

Owner of this file: the SEO strategist session (Claude). Matt reviews outcomes.
Baseline date: **2026-09-10** (site relaunched 2026-06-26, so this is the 75-day mark).
Snapshots live in `docs/seo/snapshots/` (run `scripts/seo/snapshot.py`). Read the newest
snapshot before trusting any number in this file.

## 1. Where we are (baseline, all live-verified 2026-09-10)

| Source | Window | Number |
|---|---|---|
| Google Search Console | Jun 9 – Sep 8 (3 mo) | **302 clicks, 113K impressions, 0.3% CTR, avg position 23.9** |
| GSC (pre-relaunch reference) | May 28 – Jun 24 (28 d) | 93 clicks, 40.1K impressions, 0.23% CTR, pos 24.7 |
| GA4 (property 332001543) | last 30 d | 1.2K active users; sessions: Paid Search 779, Direct 368, **Organic Search 175**, Paid Social 116, Organic Social 61, Referral 47, AI Assistant 6; 133 key events (definition unverified) |
| DataForSEO Labs (US) | live | 57 ranked keywords, 2 in top 3, 9 in top 10, est. traffic value 64/mo |
| DataForSEO Backlinks | live | 845 backlinks from **68 referring domains**, domain rank 264, spam score 5 |
| Landscape Leadership (the leader) | live | 820 keywords, 325 in top 10, est. value 3,518/mo, **459 referring domains**, rank 200 |
| PageSpeed mobile | live | Home 93–96 · Service page 56–71 (LCP 5–8 s) · Industry page 43 (LCP 8.4 s) · Blog post 52 (LCP 8.7–9.0 s). Lab numbers swing ±15 between runs; no CrUX field data yet |
| Crawl of all 101 sitemap URLs | live | All 200, canonicals self-referencing, one H1 each, GA4 on every page, no noindex, OG images present, 237 legacy redirects working |
| Google Business Profile (L&L) | live | Category "Marketing agency", St. Petersburg FL, steady 5-star reviews through Jul 2026 |

**Branded vs non-branded.** ~130 of the 302 clicks are the brand ("lawn and land marketing",
"lawn & land marketing", "lawn and land", "mow money mow problems"). Non-brand organic is
roughly 55 clicks/month.

**The single biggest fact:** the head terms are already on page 1 and produce nothing.

| Query (GSC, 3 mo) | Impressions | Clicks | Radar position today |
|---|---:|---:|---:|
| lawn care marketing | 9,075 | 1 | 8–9 |
| landscaping marketing agency | 3,342 | 1 | 5 |
| lawn care marketing agency | 2,071 | 1 | 5 |
| marketing agency for landscapers | 385 | 1 | – |

14,800 impressions → 4 clicks. Position 5–9 on these SERPs sits under a **local 3-pack**
(Landscape Leadership, Lawnline, landscapemarketer.com / lawncaremarketer.com), an **AI
Overview** (on "lawn care marketing" and "lawn care marketing agency"), Reddit, and YouTube.
Page-1-bottom is invisible here. The work is to get into the pack, into the AI answer, and
into the top 3, and to make the snippet worth clicking.

## 2. What is working (keep doing)

Competitor Radar daily positions (Supabase `ci_rankings`, US desktop), first check → 2026-09-10:

- landscaping marketing agency **17 → 5** (home) · lawn care marketing agency **12 → 5** (home)
- landscaping marketing company 14 → 11 · landscaper marketing 23 → 13 · marketing for landscapers 23 → 13
- green industry marketing agency 61 → **5** and best green industry marketing agencies → **2** (the comparison post)
- fall lawn care marketing 52 → **1** · SEO for holiday lighting companies → **1** · landscaping reputation management **1** · SEO for outdoor living companies **2** · SEO for excavation companies 13 → 4 · forestry mulching marketing 13 → 5

The open-lane strategy (vertical + seasonal posts) is landing. The blog engine (47 posts,
median 2,100 words, BlogPosting + FAQPage schema on every post) is the asset.

## 3. What is broken (diagnosis)

1. **Cannibalization on the money terms.** "landscaping SEO" (480/mo) and "SEO for landscaping
   companies" (170) rank via the blog *category page* `/resources/blog/category/seo/` (titled
   "Landscaping SEO & Local Search") at 12–15, not via `/marketing-services/landscaping-seo/`.
   "landscape marketing" (390) and "marketing for landscapers" (390) rank via the **blog index**
   at 13–21, not via a money page. "lawn care SEO" slid 16 → 34 on the service page.
2. **The 11 vertical service pages are near-orphans.** `landscaping-seo`, `lawn-care-seo`,
   `lawn-maintenance-seo`, `outdoor-living-seo`, `holiday-lighting-seo`, `land-clearing-seo`,
   `excavation-seo`, `septic-installation-seo`, `lawn-care-google-ads`, `landscaping-google-ads`,
   `outdoor-living-google-ads` get 1–8 internal links each and are absent from the nav and the
   `/marketing-services/` hub. Google is ranking the pages we link 111 times and ignoring the
   ones we link once.
3. **Not in the local pack.** The 3-pack on agency queries is built from keyword-named GBPs.
   L&L's GBP is correct but generic (one category, no services/description tuned to
   "landscaping marketing agency").
4. **Not cited in AI Overviews.** AI Overviews appear on 3 of the 5 head SERPs; L&L is not a
   reference. `llms.txt` exists; there is no citation-bait (original data, benchmarks) yet.
5. **Link deficit.** 68 referring domains vs 459 for the leader. The real links are client-site
   footer credits (independentlawnservice, allaroundtampa, lc-lm, bollinger, junknation…); the
   rest is directory noise. No industry-press, podcast, or list-page links.
6. **SERP snippet hygiene.** 48 of 47 blog posts + 1 page have titles over 65 characters (most
   80–106, truncated); 15 pages have meta descriptions over 160.
7. **Mobile performance on the two templates that carry 90 pages.** Service and blog templates
   load at LCP 8–9 s on mobile (home is 2.9 s). Causes: hero images not prioritized on those
   templates, and 207 KB of third-party JS (two gtag loaders + Meta pixel) parsed before paint.
   Not a ranking factor at this traffic level (no CrUX data) but it is a conversion factor.
8. **Measurement gaps.** The GBP Performance API is not enabled on GCP project 489025929507 (so
   L&L's own GBP calls/clicks can't be pulled yet; one-click enable). No API access to GSC/GA4 (fixed by `scripts/seo/google_auth.py`, needs
   Matt's one-time consent); GSC is not linked to GA4 (GA4 is prompting for it); the GA4 key
   events definition has not been verified (133 in 30 days looks broad).

## 4. The plan (next 90 days, in priority order)

### P1 — Own the agency SERPs (weeks 1–4)
- **GBP:** add secondary categories (Internet marketing service, Advertising agency), a
  description that says "landscaping and lawn care marketing agency", the 8 services as GBP
  services, weekly posts, and keep the review stream going. Goal: enter the 3-pack on
  "landscaping marketing agency" / "lawn care marketing agency". (GBP edits are client-visible
  brand changes → Matt's yes first.)
- **Homepage title + meta rewrite** for the head terms with a proof hook (100+ companies, 97%
  retention, NALP). Currently "Lawn Care & Landscaping Marketing Agency | Lawn & Land".
- **Sitelinks + rich results:** already FAQPage; add `AggregateRating`-free proof (Google won't
  show self-serving stars) and make sure the About/Client Results/Programs pages have crisp
  titles so sitelinks read well.
- **Comparison post → asset:** "best green industry marketing agencies" is at #2; build the
  same play for "best landscaping marketing agencies" and "best lawn care marketing agencies"
  (Radar has them at 11 and 8 via the same post — split into dedicated posts).

### P2 — Fix cannibalization and internal linking (weeks 1–3)
- Retitle `/resources/blog/category/seo/` to a library title ("SEO articles for landscapers and
  lawn care companies") and put a prominent "Want it done for you? → Landscaping SEO service"
  block on the category page and every SEO post.
- Add the 11 vertical pages to the `/marketing-services/` hub (a "By trade" grid) and to the
  Services mega-menu; link each vertical page from its industry page with the exact-match
  anchor and from 3–5 related posts. Target: every vertical page ≥ 15 internal links.
- Make `/industries/landscaping/` the target for "landscaping marketing" / "marketing for
  landscapers": retitle to lead with "Landscaping Marketing", link from the blog index and the
  strategy category with those anchors.
- Re-check Radar 14 days after each change; success = the service page replaces the category
  page as the ranking URL.

### P3 — Snippet hygiene (week 2, one pass)
- Shorten the 48 long titles to ≤ 60 chars (keyword first, brand dropped where needed).
- Trim the 15 long meta descriptions to ≤ 155.
- Both are `_blog.json` / `_content.json` edits + regenerate; no design change.

### P4 — Template performance (weeks 3–5)
- Service + blog templates: `fetchpriority="high"` + explicit dimensions + preload on the hero
  image, lazy-load everything below the fold, compress `programs-hero.webp` and the blog
  featured images to ≤ 150 KB.
- Load gtag/Meta pixel after first interaction or after `load` (keeps GA4 counts intact for
  humans; bots never trigger it anyway). Target: mobile LCP < 3 s on all three templates.

### P5 — Links (ongoing, target 68 → 150 referring domains by March 2027)
- Audit the ~50 client sites for the footer credit link (many are missing it; every Growth/
  Authority site should carry "Website by Lawn & Land Marketing" → home).
- Get listed on the pages that rank for "best landscaping marketing agencies"
  (builtrightdigital.com, outsourceaccelerator.com, skillmammoth.com, third-angle.com) and on
  Clutch / UpCity / DesignRush / Google Partner directory / NALP member directory.
- Podcast: every Mow Money, Mow Problems guest gets an episode page here and a request for a
  link back; pitch Matt as a guest on green-industry podcasts.
- One guest article per month in Lawn & Landscape, Total Landscape Care, Turf Magazine, or
  LawnSite (all already rank on our SERPs).
- Book: Amazon author page and "Mow Money, Mow Problems" mentions should link to the site.

### P6 — AI search / GEO (weeks 4–8)
- Publish original data pages worth citing: "what a landscaping marketing agency costs" (no L&L
  pricing; industry ranges), "lawn care marketing benchmarks" (CPL, conversion rates from our
  Meta offer-vs-no-offer data), "search seasonality for lawn care" (we already have the data).
- Keep `llms.txt` current; add `dateModified` on posts; tighten Organization/Person entity
  schema (already good).

### P7 — New content lanes with measurable volume (weeks 4–12, one post/week)
Terms with volume we do not own yet: landscaping advertising (480), lawn care advertising
(320), Google Business Profile management service (390), landscaping website design (170) +
lawn care website design (260), landscaping leads (260) / lawn care leads (110), how to get
lawn care customers (170), landscaping facebook ads (320, Meta Ads page is at 23 and rising).
Skip tree service marketing (210): not a served vertical.

### P8 — Measurement (week 1)
- Matt runs `doppler run -p vault -c prd -- python3 scripts/seo/google_auth.py` once (2 min).
- Link GSC ↔ GA4 (GA4 home is prompting for it; 1 min, Matt).
- Verify which GA4 key events exist; make "book a strategy call" the primary.
- Weekly: `scripts/seo/snapshot.py` → snapshot + deltas. Monthly: this file's baseline table.

## 5. Guardrails (do not violate)
- Only L&L's 8 real services; no pricing; no invented stats; Lucide icons; em-dash-free copy;
  city + 2-letter state. See repo `CLAUDE.md`.
- No geo / city / "near me" pages (Radar scope rule). Snow removal is out.
- Never delete or hide a review; never touch DNS; GBP edits and anything client-visible need
  Matt's yes.
- Blog changes go through `_blog.json` → `gen_blog.py` → `gen_blog_schema.py` → `build.py`;
  service pages through `_content.json` → `gen_service.py` → `build.py`. Sitemap is hand-kept.
- Push to `main` = production. Verify on the live domain after every deploy.

## 6. Log
- 2026-09-10 — Baseline established (this file, snapshot `2026-09-10.json`), tooling added
  (`scripts/seo/google_auth.py`, `scripts/seo/snapshot.py`).
- 2026-09-10 — Found `docs/`, `scripts/`, `CLAUDE.md`, `README.md`, `_content.json`, `_blog.json`
  and the generator scripts publicly served on the production domain (HTTP 200). Added
  `.vercelignore` so they are no longer uploaded; `build.py` + `_header.html` / `_footer.html`
  stay in because the Vercel build needs them. Live-verified after deploy.
  **Open:** the GitHub repo `lawnHQ/lawn-and-land-marketing-website` is PUBLIC, so everything in
  it (including this file) is still readable on GitHub. Flipping it private is a one-click
  GitHub setting for Matt; the Vercel GitHub App and the Actions deploy keep working.
- 2026-09-16 — **Client priority set by Matt:** 1 Landscapers, 2 Outdoor Living, 3 Land Clearing;
  then Excavation, Lawn Care, Lawn Maintenance, Septic; Holiday Lighting stays as a page for
  existing clients but gets no dedicated push. Matt gave a standing go for on-site changes with a
  high-confidence positive impact.
- 2026-09-16 — Shipped (commit `4343a6c`): hub "Built for your trade" grid + sitewide footer links
  to the vertical SEO/Ads pages (priority order); 41 blog posts got a contextual service link in
  the CTA block; SEO category page retitled as a library and its intro links the four priority
  vertical SEO pages; blog index title de-optimized; `seoTitle` (≤60) on all 47 posts stamped by
  `gen_blog.py` (H1s untouched); 18 long meta descriptions trimmed; homepage title leads with
  Landscaping and the description names the three priority trades; `_content.json` synced to the
  live service titles/descriptions (six had drifted); hero preload on 48 pages + hero recompressed
  289→223 KB + 17 blog photos ≤150 KB; blog hero `fetchpriority=high`.
  **Measure on 2026-09-30:** Radar positions for landscaping SEO / seo for landscaping companies
  (should move from the category page to `/marketing-services/landscaping-seo/`), landscape
  marketing / marketing for landscapers (should move from `/resources/blog/` to
  `/industries/landscaping/`), and GSC CTR on the head terms.
- 2026-09-16 — **GBP applied with Matt's yes** via the new gated `gbp` write commands, each read back and verified: description replaced (742 chars, leads with "landscaping marketing agency", names the priority trades and the 8 services), secondary categories added (Internet marketing service, Marketing consultant; "Advertising agency" does not exist in the taxonomy), 8 services added with descriptions. Still open for Matt: repo → private, GSC↔GA4 link, cloud environment variables (§8).

- 2026-09-16 (later) — Matt approved deferring the marketing tags and a weekly snapshot, and asked for
  a standing automation that checks in and publishes. Shipped: deferred GA4/Google Ads/Meta Pixel
  loader on 112 pages + template (commit `0cc0b3d`, live-verified: no tag scripts at 1 s, both
  loaded by 5 s, events queued through the stubs; the two conversion thank-you pages stay eager).
  Added `docs/seo/ARTICLE-PLAYBOOK.md` (the publishing standard) and `docs/seo/CONTENT-QUEUE.md`
  (20 priority-ordered topics, radar terms excluded), `--prompt/--variant` on `gen_photos.py`,
  and two cloud routines: **Monday 7am ET weekly review** (snapshot + safe fixes + report in
  `docs/seo/reports/`) and **Tuesday/Thursday 6am ET article** (one article per run, PR with a
  24-hour veto window, merged by the next run). The routines read their credentials from the
  cloud environment variables Matt sets (see §8). `gbp` CLI gained gated write commands
  (`set-description`, `set-categories`, `set-services`, `create-post`); drafts for the L&L
  listing are in `docs/seo/gbp/` awaiting Matt's yes.

## 8. Automation — GitHub Actions (moved here 2026-09-21, Matt approved)
Both routines now live in this repo, the same pattern the Competitor Radar already runs
successfully against it. The claude.ai cloud routines were abandoned because their sandbox
blocks outbound HTTPS to lawnandlandmarketing.com and api.dataforseo.com, so the snapshot
could not run there at all.

| Workflow | Schedule | What it does |
|---|---|---|
| `.github/workflows/seo-weekly-review.yml` | Mon 11:00 UTC (7am ET) | Snapshot, week-over-week diff, mechanical fixes, merge any `seo/` PR older than 24 h, write `docs/seo/reports/<date>.md`, push to main |
| `.github/workflows/seo-article.yml` | Tue + Thu 10:00 UTC (6am ET) | One article from the top open queue row, gpt-image-2 hero, opens a PR. The PR is the veto |

**Kill switch:** repository variable `SEO_AGENTS_ENABLED`. Anything other than `true` and every
scheduled run exits at the first step. Manual `workflow_dispatch` runs ignore it.

**Guards:** `--max-turns` (60 review / 90 article), job `timeout-minutes` (45 / 60), and a
`concurrency` group per workflow so runs cannot overlap.

**Secrets** (Settings > Secrets and variables > Actions). Install with
`doppler run -p vault -c prd -- python3 scripts/seo/install_actions_secrets.py`
(`--dry-run` first; it encrypts locally and never prints a value; it needs a classic PAT with
`repo` scope, the fine-grained lawnHQ token lacks the Secrets permission):

- Installed 2026-09-21: `CLAUDE_CODE_OAUTH_TOKEN`, `DATAFORSEO_LOGIN`, `DATAFORSEO_PASSWORD`,
  `PAGESPEED_API_KEY`, `GBP_CLIENT_ID`, `GBP_CLIENT_SECRET`, `OPENAI_API_KEY`.
- **Model auth runs on Matt's Claude subscription, not pay-per-token.** `claude_code_oauth_token`
  is a first-class input on `claude-code-action` ("alternative to anthropic_api_key"); the vault's
  `CLAUDE_CODE_OAUTH_TOKEN` was verified live 2026-09-21 (Bearer + `anthropic-beta:
  oauth-2025-04-20` returned 200). So the model cost of both workflows is **$0 of new API spend**;
  the runs draw on the subscription's usage allowance instead, which is shared with Matt's own
  Claude Code sessions. Mint a fresh token any time with `claude setup-token`. `ANTHROPIC_API_KEY`
  remains wired as a pay-per-token fallback and is only consulted if the OAuth secret is absent.
- **Still needed:** `GOOGLE_SEO_REFRESH_TOKEN` (re-run
  `doppler run -p mac-claude -c prd -- google-consent seo` first; the installer refuses a revoked
  token). Without it the review runs but reports no Search Console or GA4 numbers.
- **Why not local cron on the Mac?** [[feedback_ops_reliability_and_alerts]] is explicit that
  nothing operational may depend on a Mac. It sleeps, it travels, and a missed Monday is silent.
  Actions runs on GitHub's schedule whether the Mac is on or not.

**Note:** these keys now exist in a second system besides Doppler. lawnHQ has one member, so
exposure is low, but prefer scoped keys here over shared ones.

## 7. GBP edits for Matt (brand-visible, needs his hand)
Listing: "Lawn & Land Marketing", St. Petersburg FL, primary category "Marketing agency".
1. Add secondary categories: **Internet marketing service** (`categories/gcid:internet_marketing_service`) and **Marketing consultant** (`categories/gcid:marketing_consultant`). ("Advertising agency" does not exist in the GBP taxonomy; only "Direct mail advertising" does. Checked 2026-09-16.)
2. Business description: applied 2026-09-16 from `docs/seo/gbp/description.txt` (742 chars).
3. Services: draft ready at `docs/seo/gbp/services.json` (8 services, each under 300 chars).
   Apply with (after Matt's yes): `doppler run -p mac-claude -c prd -- gbp set-description accounts/101131441201055923730/locations/17130850836280261172 --file docs/seo/gbp/description.txt --confirm`, then `gbp set-categories ... --additional categories/gcid:internet_marketing_service categories/gcid:marketing_consultant --confirm`, then `gbp set-services ... --file docs/seo/gbp/services.json --confirm`. Each prints the payload and verifies by reading the listing back.
4. Weekly GBP post: reuse the newest blog post each week.
5. Keep the review stream going (the July batch is doing work). Ask happy clients for reviews
   that mention "landscaping" and the trade in the text.
- 2026-09-20 — **Article #1 published by hand after the routine was blocked.** The Thursday
  routine wrote a good draft but could not ship: the Claude GitHub App has no write access to the
  lawnHQ org (403 on push and PR), no `OPENAI_API_KEY` in the cloud environment, and the container
  is ephemeral so the draft was lost. Rewrote it locally with fresh research and shipped
  `/resources/blog/hardscape-design-software/` (target "hardscape design software", 6,600/mo,
  outdoor living). **Fact correction the draft had wrong:** Unilock Uvision is NOT free, it is
  $579.95 ($279.95 upgrade). Every price in the article was read off the vendor's own page on
  2026-09-20. Claims about Belgard and Techo-Bloc design programs and about SketchUp's free-tier
  commercial terms were DROPPED because the pages could not be reached to verify. Gotcha for the
  template: the read-time span is `article-read-time`, not `article-read`.
  **Blocked until Matt acts (all three):** (1) install the Claude GitHub App on the lawnHQ org so
  routines can open PRs, (2) add the §8 environment variables to the claude.ai Default environment,
  (3) re-run `google-consent seo` because the token is revoked again (see the revoke gotcha below).
  **Revoke gotcha:** revoking one refresh token revokes the whole grant for that user and client, so
  the freshly minted token died with the leaked one on 2026-09-16.
- 2026-09-20 (later) — **Sitewide table styling fixed.** Matt flagged the price table on the new
  article as unreadable. Root cause: no `table`/`th`/`td` rule existed in any stylesheet, so the
  bare `<table>` markup in **21 of 48 posts** had been rendering unstyled since launch. Added
  article-table styles to `article.css` (v7 → v8 sitewide), and `gen_blog.py` now wraps every
  article table in `.article-table-wrap` so it scrolls inside its own frame on mobile instead of
  breaking the page. Verified desktop and at 375px: table scrolls, body does not.
- 2026-09-21 — **Runtime finding: the cloud routines cannot do this job as built.** A live test run
  printed all seven environment variables as MISSING, and the sandbox's egress proxy blocks
  outbound HTTPS to `lawnandlandmarketing.com`, `api.dataforseo.com`, and third-party vendor sites,
  so `snapshot.py` cannot even crawl our own sitemap there and the article routine could not read
  its research sources. Setting the environment variables alone will NOT fix that.
  **Recommendation: port both routines to GitHub Actions in this repo.** That is the pattern the
  Competitor Radar already runs against this same repo (cron → python → PR with a veto window):
  no egress restrictions, repo-level secrets (this repo already uses `secrets.VERCEL_TOKEN`), and
  push rights that do not depend on a GitHub App installation.
- 2026-09-21 (later) — **Monday weekly review confirms the same block, shipped local fixes anyway.**
  Independently hit the same wall: all six snapshot env vars missing, egress denied to
  lawnandlandmarketing.com and api.dataforseo.com (403), PageSpeed on its shared daily quota (429).
  No snapshot, no comparison, no open `seo/` PRs to merge. Fixed what needed no network instead:
  added the missing `article-cta-link` line to 5 posts, trimmed 4 meta descriptions over 158 chars
  (meta/OG/Twitter/JSON-LD), verified all 48 seoTitles, the `_blog.json`↔sitemap sync, and every FAQ
  block parses clean. Flagged 2 older posts (`best-green-industry-marketing-agencies`,
  `land-clearing-marketing`) with no in-article CTA block at all, needs new copy not a mechanical
  fix. Seconds the GitHub Actions recommendation above. Report: `docs/seo/reports/2026-09-21.md`.
- 2026-09-21 (later) — **Matt's direction, and three findings that changed the plan.**
  Direction: (a) cold email to magazine editors is dead, find another way to earn links;
  (b) **deprioritize the local pack** (we sell nationwide); (c) **AI answers are a top priority**
  (Google AI Overviews, ChatGPT, Claude); (d) clean up the Competitor Radar and run it properly;
  (e) he wants a **weekly reminder of the strategy and the target buyer**, for himself and for any
  agent picking this up.
  **Finding 1 — the radar had been deadlocked for six weeks.** Its footprint guard did not
  allowlist the two files `gen_blog.py` regenerates on every run (`index.html`,
  `matt-foreman/index.html`), so 18 of its last 25 actions died on its own guard. Ledger over the
  window: 70 failed vs 48 merged; last successful open-lane publish 2026-08-07. Fixed in
  `competitor-intel` commit `2546729`, verified both directions. **Still broken:** every P1/P5
  defense play dies on "slug already exists; refusing to overwrite" because the defense path only
  knows how to create a new post, not improve an existing one. Rank defense has never really run.
  **Finding 2 — the client-footer link opportunity does not exist; it is already spent.** Audited
  all 57 client sites: **51 already link back**, 14 of them nofollow. With ~70 referring domains
  total, client sites are roughly three quarters of the entire link profile. The problem is not
  volume, it is **monoculture**: one link type, from sites we built, with near-identical brand
  anchors. Only 2 active clients lack a link (Land Care Garden Center, Premier Lawn Care) and 4
  were unreachable at audit time (Complete Lawn Service 308, Greenz Outdoor, Land Care Landscape
  Management, Outdoor FX 503). Fixing those 6 is worth doing and changes nothing structural.
  **Finding 3 — AI Overview baseline, now tracked.** `snapshot.py` gained `ai_visibility_block()`:
  for every watch term it records whether an AI Overview appears and whether we are among its
  cited domains (~$0.0035/term). First read: AI Overview on 3 of 4 sampled terms, **we are cited
  on zero**, and Landscape Leadership IS cited on "seo for landscaping companies". The weekly
  report now carries this line and the week-over-week gained/lost citations.
  Also shipped: `docs/seo/CHARTER.md` (the orientation doc, read first by Matt and every agent),
  both workflows now read it first, the weekly report opens with a "Who we are targeting" recap,
  and the review runs a credential-free **radar health check** (zero radar merges in 7 days is
  reported as a possible outage).
- 2026-09-20/21 — **Full instrumentation live.** Matt re-ran `google-consent seo`; the token
  verified against Search Console and GA4, and all 8 repo secrets are installed, so both workflows
  are now at full strength with nothing outstanding. First complete snapshot (`2026-09-20`):
  GSC 28d **116 clicks / 34,878 impressions / 0.33% CTR / pos 21.4** (prior 28d: 103 / 33,024), so
  clicks +13% and average position improved about one place since the 2026-09-16 pass. DataForSEO
  ranked keywords 60 → 69, referring domains 70 → 77. **Mobile performance is fixed**: the service,
  industry, and blog templates went from LCP 8-9 s to 3.6, 4.4 and 3.9 s and all now score 75+,
  with the homepage at 99. Crawl is clean, zero issues.
  **AI Overview baseline across all 22 watch terms: an AI Overview appears on 20 of them and we are
  cited on ZERO.** Who Google's AI does cite: Reddit 6x, YouTube 4x, then a spread of SEO-tool blogs
  and two tracked competitors (Landscape Leadership 3x, Evergrow 1x). Six of our biggest terms,
  including "lawn care marketing" and "landscape marketing agency", show an AI Overview with **no
  named sources at all**, which is an open door rather than a closed one.
  Watch-term CTR remains the standing problem: every single watch term shows 0 clicks, including
  "lawn care marketing" at 6,417 impressions and position 10.9.
