# Current State Log — 2026-06-26

Owner: Lawn & Land Marketing  
Repo: `lawnHQ/lawn-and-land-marketing-website`  
Canonical production domain: `https://lawnandlandmarketing.com`  
Canonical Vercel project: `lawnland-site`

## Short version

The static Lawn & Land website is live on production and is now being operated as the production website source of truth. Recent work focused on audit reconciliation, production hardening, performance-safe page optimization, the post-booking video page, and universal footer refinements.

## Recent production work logged

### Audit reconciliation and rollback guardrails

- Reconciled public-site audit findings against live production instead of stale aliases.
- Kept safe fixes: schema cleanup, copy consistency, local SEO polish, alt/metadata cleanup, CSP report collector, and GHL booking redirect verification.
- Rolled back risky homepage performance overrides after they caused brand-font and nav-hover regressions.
- Preserved the lesson: homepage/LCP work must run in preview with font, nav, hero, CTA, console, and mobile checks before production.

Reference: `docs/audit-rollback-handoff-2026-06-25.md`

### Service + industry combo-page program

- Added and optimized service × industry combo pages without nav stuffing.
- Combo pages are linked contextually from the matching industry service cards.
- Sitemap and parent-child hierarchy were updated so the pages are discoverable and not orphaned.
- Performance pass kept brand font behavior intact and avoided homepage-style critical-CSS hacks.

Reference: `docs/directives/combo-pages-agent-directive.md`

### Post-booking video page

- Built `/thanks-for-preparing/` as the post-booking prep page.
- Recovered/restored the correct pre-meeting video path and verified live playback behavior.
- Kept the page focused on call preparation, not a general content landing page.

### Universal footer refinements

- Refined the footer trust/legal presentation across the static site.
- Added the centered palm badge: `Grown In St. Petersburg, FL`.
- On desktop, the legal row is balanced: copyright left, badge centered, legal links right.
- On mobile, the palm badge now appears at the very bottom of the legal footer, center-aligned, with mobile bottom padding.
- Current stylesheet cache-bust: `styles.css?v=156`.

Reference: `docs/website-source-of-truth/navigation.md`

## Current guardrails

1. Production domain checks must target `https://lawnandlandmarketing.com` directly.
2. The real Vercel production project for the custom domain is `lawnland-site`.
3. Universal header/footer changes start in `_header.html` or `_footer.html`, then run `python3 build.py`.
4. CSS changes require a sitewide cache-bust bump.
5. Homepage performance work is preview-only unless Matt explicitly approves production and the full visual/interaction QA passes.
6. Do not sacrifice Rethink Sans, dropdown behavior, mobile menu behavior, or homepage visual fidelity for Lighthouse scores.
7. Ground Control remains client source of truth only, not the website ops log.

## Standard verification before reporting done

Run at minimum:

```bash
python3 build.py --check
python3 scripts/check_links.py
git diff --check
```

For footer/header/sitewide CSS work, also verify:

- live source on `https://lawnandlandmarketing.com`
- desktop visual footer/header state
- mobile viewport behavior for the affected layout
- no horizontal overflow on mobile

## Recent useful commit anchors

```text
01fe063 Add mobile footer badge padding
1ba7f00 Show footer St Petersburg badge on mobile
1cfc8ff Update footer St Petersburg badge
e3a55c2 Update footer St Pete badge
96985aa Restore thanks for preparing video
30d7a80 Add thanks for preparing video page
f0ec6d7 Refine universal footer layout
035cd21 Add mobile hero asset for combo pages
fbea665 Optimize combo service page font path
21dfd81 Restore hash-verified local Rethink preload
```
