# Restart Guide

Use this when coming back to the Lawn & Land website after time away. Updated 2026-06-26.

## One-paragraph truth
**The site is live in production and actively maintained.** Built: the **homepage**; all **8
`/marketing-services/*`** detail pages + the services hub; the service × industry combo-page layer;
**both programs** (Growth + the flagship Authority) + the Programs hub; all **8 industry pages** + the Industries hub; **About** (+ `#team`),
**Contact** (live GHL form), **Confirmation**, **Get Started / booking**, **Strategy Booked**, **Thanks for Preparing**; **Terms + Privacy**; the **3
Resources content pages** (blog, experiences-reviews, podcast — under the `/resources/` SEO silo, no hub
page); **2 case studies** (`/case-studies/` — Precision + Rock Solid, on the locked `case-study-template.md`);
and the **Client Results** roster (`/client-results/`). Service pages run off a locked template + a
generator (`gen_service.py` reading `_content.json`); everything else is hand-built (reusing
`simple-hero` / `svc-*` / `svc-cta`, plus `.ind-*` for industries and `.cs-*` / `.cr-*` for the case
studies + roster). Production is `https://lawnandlandmarketing.com` on the `lawnland-site` Vercel project.

**Latest pass (2026-06-26):** audit reconciliation was logged, risky homepage LCP overrides were rolled back and documented, the service × industry combo-page program is live, `/thanks-for-preparing/` is live, and the universal footer now carries the centered `Grown In St. Petersburg, FL` palm badge on desktop and mobile. Start with `current-state-2026-06-26.md` for the newest operating baseline.

## Fastest restart path — read in order
1. `docs/website-source-of-truth/current-state-2026-06-26.md` — newest operating baseline and recent commits
2. `CLAUDE.md` (repo root) — the master orientation file
3. `docs/website-source-of-truth/build-status.md` — what's done / not done + next priorities
4. `docs/website-source-of-truth/page-registry.md` — page-by-page status
5. `docs/website-source-of-truth/service-page-template.md` — the locked service-page template + generator
6. `docs/website-source-of-truth/industry-page-template.md` — the locked industry-page framework + SEO/GEO/EEAT strategy
7. `docs/website-source-of-truth/navigation.md` — the universal header / nav / submenus + footer
8. `docs/website-source-of-truth/decisions.md` and `routing-rules.md`

## How to make changes
- **Header/footer (all pages):** edit `_header.html` / `_footer.html` → `python3 build.py`
  (verify sync with `python3 build.py --check`).
- **A service page's copy:** edit its object in `_content.json` → `python3 gen_service.py` →
  `python3 build.py`. **Don't hand-edit** `marketing-services/<slug>/index.html` — regeneration overwrites it.
- **A program / industry / other page:** hand-edit its `index.html` (these are not generated).
  Reuse the existing `svc-*` / `simple-hero` / `svc-cta` classes for consistency.
- **CSS / template changes:** edit `assets/css/styles.css` or `service-page.css`, then **bump the
  `?v=` query sitewide** so browsers fetch fresh (current: `styles.css?v=156`, `main.js?v=59` on the primary pages, `service-page.css?v=5`, `industry.css?v=3`). The industry-page FAQ accordion (exclusive open/close) lives in `main.js`, scoped to `.ind-faq > details`.
- **Deploy:** commit + push `main`. GitHub Actions / Vercel deploys production in ~1–2 min. Verify on `https://lawnandlandmarketing.com` with a cache-busted URL or hard refresh.

## Canonical routes (treat as truth)
`/` · `/about/` (+ `#team`) · `/client-results/` · `/contact/` · `/get-started/book-strategy-call/` ·
`/programs/...` · `/marketing-services/...` (8 + hub) · `/industries/...` (the canonical 8 + hub) ·
`/case-studies/...` (precision, rock-solid) · `/resources/...` (blog, experiences-reviews, podcast — silo,
no hub page) · `/terms/` · `/privacy-policy/`

Retired / keep OUT of internal linking: `/services/`, `/pricing/`, `/resources/guides/`,
`/resources/contact/`, `/results/`, `/team/`, `/good-fit/`, `/book/`,
`/podcast/`, `/tools/marketing-audit/`, and older orphan/article URLs.

## The next best moves
1. Keep production docs current with every structural/sitewide change.
2. Use preview-only workflows for homepage LCP, nav, font, or above-fold performance experiments.
3. Continue adding approved case studies and proof assets as owner/client sign-offs arrive.
4. Keep combo pages contextual: parent links, sitemap entries, and no main-nav stuffing unless Matt approves.

## Guardrails
- **No pricing** anywhere — every CTA → the free strategy call.
- **No invented facts** — placeholders for anything unverifiable; conviction stats real + sourced.
- **Service scope (owner's #1 accuracy rule):** copy claims ONLY L&L's 8 real services (Website, Local SEO,
  Google Ads, Meta Ads, GBP, Your AI Partner, Reputation, CRM & Automation). NEVER imply L&L does the
  client's sales, renewals, rebooking, deposits, waitlists, social-media management, or email list. Frame
  relationships/renewals as the client's; L&L's role is the marketing around them. Audit the WHOLE page
  (meta, schema, service cards, modules), not just the FAQ. See `decisions.md` (2026-06-23).
- **Brand:** Lucide icons only (no emoji); Twilight `#6837EF` never blends with green; the `.hl`
  marker is one impact phrase per surface.
- Production is live. Use preview branches/deployments for risky homepage, nav, font, tracking, or performance work.
- Keep these docs current in the same workstream as any structural change.
