# SEO Charter — who we are after and how we win

**This is the orientation document.** Matt reads it weekly. Every agent reads it first, before
STRATEGY.md, before the queue, before touching anything. It changes rarely and on purpose.
Numbers live in `snapshots/` and `reports/`, never here, so this page never goes stale.

Last reviewed: 2026-09-21.

---

## 1. Who we are

Lawn & Land Marketing. A digital marketing agency that works **only** with green-industry
companies. Founded 2022, St. Petersburg, FL. 100+ companies served, 97%+ retention, NALP member,
Google Partner. Founder Matt Foreman wrote *Mow Money, Mow Problems* and hosts the podcast.

**We sell exactly eight things.** Website Design, Local SEO, Google Ads, Meta Ads, Google Business
Profile Management, Your AI Partner, Reputation Management, CRM & Automation. Nothing on this site
may claim anything else, and we never do a client's own sales, hiring, or operations.

**We are national.** Clients are all over the United States. We are not chasing St. Petersburg.

---

## 2. Who we are trying to reach

A **business owner or general manager of a green-industry company**, typically $400K to $14M in
revenue, who is good at the work and under-marketed. Not a homeowner. Not a marketer. Someone who
would rather be in the field and knows their online presence is costing them jobs.

They arrive one of three ways: searching for an agency, searching for how to fix a specific
marketing problem, or asking an AI assistant who they should hire.

**Priority order, set by Matt 2026-09-16. This decides every tie.**

| # | Trade | Why it ranks here |
|---|---|---|
| 1 | **Landscapers** | Core buyer, highest volume, biggest addressable market |
| 2 | **Outdoor living / hardscape** | High ticket, long considered sale, best fit for the Authority program |
| 3 | **Land clearing** | Underserved online, few real competitors, we already rank |
| 4 | Excavation | Same land-side story as clearing |
| 5 | Lawn care | Recurring revenue, crowded but real |
| 6 | Lawn maintenance | Route density story |
| 7 | Septic installation | Narrow but high ticket; installers, never pumping |
| 8 | Holiday lighting | **Kept for existing clients only.** No new articles, no push. It is a winter add-on our clients like seeing that we understand. |

**Two programs, two different people. Do not blur them.**
**Growth** ($400K–$1M): grew on referrals, hit the ceiling, nearly invisible online, needs to get
found for the first time. **Authority** (7-figure+): already doing marketing, wants to own the
market; the vendor-sprawl and agency-scar-tissue pains live here, not in Growth.

---

## 3. What winning looks like

In order. Each one is a real business outcome, not a vanity metric.

1. **Booked strategy calls from organic search.** The only number that pays. Everything else is a
   leading indicator.
2. **Being the answer when a green-industry owner asks any AI assistant who to hire.** Google's AI
   Overviews, ChatGPT, Claude, Perplexity. This is where the buyer is going, and it is Matt's
   stated top priority alongside the link gap.
3. **Top three for the agency terms**, not page-one-bottom. Position 5 to 9 on our head terms
   produces almost nothing.
4. **A link profile that is not just our own clients.** See section 4.

---

## 4. The four fronts, and the honest state of each

**Front 1 — Content.** Healthy. 48 articles, real depth, schema on every one. The Competitor Radar
owns publishing (new open-lane posts, refreshes, counter-content). Content is no longer the
bottleneck, so more of it is not the answer to a ranking problem.

**Front 2 — Links. This is the real gap and it is not the one we assumed.**
We have ~70 referring domains against the category leader's 459. We audited all 57 client sites on
2026-09-21: **51 already link back**. So client footer credits are not an untapped opportunity,
they are already spent, and they are roughly three quarters of our entire link profile. The problem
is not volume, it is **monoculture**: one link type, from sites we built, with near-identical brand
anchor text, 14 of them nofollow. What we lack is editorially independent links from sites we do
not control. Cold email to magazine editors is dead (Matt, 2026-09-21: zero responses). The plan is
in STRATEGY.md; the principle is that we earn links by publishing things worth citing, not by
asking.

**Front 3 — AI answers.** Google shows an AI Overview on three of our five biggest terms and cites
us in none of them. We have proprietary data nobody else has and have published none of it. Highest
priority alongside links.

**Front 4 — Local pack.** **Deliberately deprioritized** (Matt, 2026-09-21). We work nationwide, so
the three-business map result is not where our buyers come from. Keep the Google Business Profile
accurate and healthy because it still feeds general relevance; do not build a program around it.

---

## 5. Who does what

| System | Cadence | Owns |
|---|---|---|
| **Competitor Radar** (`lawnHQ/competitor-intel`) | Daily | Rank tracking on 21 competitors, page-change watch, backlink monitoring, keyword gap mining, and **all publishing**: new posts, refreshes, defense, counter-content |
| **SEO weekly review** (`.github/workflows/seo-weekly-review.yml`) | Mondays | The numbers, week-over-week movement, mechanical fixes, merging article PRs past their veto window, the written report, **and watching the radar's failure rate** |
| **This charter + STRATEGY.md** | Reviewed weekly | Why any of it is happening |

Both publishing paths write to the same blog. The radar's `ci_operator_actions` ledger is the
single source of truth for what has been targeted, so nothing gets written twice.

---

## 6. Hard rules

- Only the eight real services. No pricing anywhere. No invented facts, ever: every number carries
  a source and the date it was read.
- No geo pages, no "near me" pages, no snow removal, no holiday-lighting articles.
- Articles inform, they do not pitch. No em dashes. Cities carry a 2-letter state.
- Client facts are locked. Never name a client's own customer.
- Anything client-visible, plus DNS, secrets, billing, and Google Business Profile, needs Matt's yes.
- A publish is a pull request with a 24-hour veto window. Closing it is the veto.

---

## 7. Orientation in five minutes

1. This file.
2. The newest file in `docs/seo/reports/` — what moved last week.
3. The newest file in `docs/seo/snapshots/` — the current numbers.
4. `docs/seo/STRATEGY.md` section 6 — the running log of everything done and why.
5. `docs/seo/CONTENT-QUEUE.md` — what is next.
