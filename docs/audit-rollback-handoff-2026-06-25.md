# Lawn & Land Website Audit Fixes and Homepage Rollback Handoff

Date: 2026-06-25 13:17 EDT
Prepared by: Mercury
Repo: `lawnHQ/lawn-and-land-marketing-website`
Production domain: `https://lawnandlandmarketing.com`

## Short version

We reconciled audit findings and shipped several valid fixes, but the homepage performance pass introduced visual and interaction regressions. Specifically, a Google Fonts loading change made the site fall back to system fonts, and inline critical CSS on the homepage broke desktop navigation dropdown hover behavior.

Because those issues affected brand presentation and core navigation, we rolled back the risky homepage performance overrides while preserving the safer audit fixes.

## What was fixed and kept

These changes were considered lower risk and remain live:

1. **Schema cleanup**
   - Standardized Organization references on:
     - `https://lawnandlandmarketing.com/#organization`
   - Removed stale/conflicting `#org` style references.
   - Verified `Service.provider` references point to the canonical Organization entity.
   - Added light JSON-LD to conversion/utility pages where appropriate.

2. **Copy consistency**
   - Standardized public strategy-call copy away from old duration variants.
   - Standardized written Rock Solid results language to avoid conflicting `$1M+` / `north of a million` references near the newer `$700K to $1.4M` positioning.

3. **Local SEO page polish**
   - Clarified the `What's included` section so the grid/cards read as intentional, not like missing content.

4. **Alt text and metadata cleanup**
   - Resolved missing/weak image alt findings found during the audit sweep.
   - Some broader blog metadata cleanup was started, but not treated as a critical live fix.

5. **CSP report collector**
   - Added `/api/csp-report`.
   - Added `report-uri /api/csp-report` to the CSP Report-Only header.
   - Verified `POST /api/csp-report` returns `204`.

6. **GHL/booking redirect verification**
   - Verified the public booking page embeds the LeadConnector calendar.
   - Verified `/strategy-booked/` is separate from `/confirmation/`, has GA4, is noindex, and does not embed the booking calendar.
   - Verified GHL calendar readback redirects completed bookings to:
     - `https://lawnandlandmarketing.com/strategy-booked/`

## What went wrong

### 1. Google Fonts behavior changed

During the homepage LCP/performance pass, the Google Fonts URL was changed from:

```html
&display=swap
```

to:

```html
&display=optional
```

That was too aggressive for this brand site. `display=optional` allows the browser, especially under slower/mobile conditions, to keep fallback/system fonts instead of swapping into the intended brand fonts.

Impact:

- Site typography appeared wrong.
- Brand presentation was degraded.
- This was visible enough that Matt caught it quickly.

Fix applied:

- Restored `display=swap` sitewide.
- Verified live production no longer contains `display=optional`.

Commit:

```text
c9be3f1 Restore Google font loading behavior
```

### 2. Homepage nav dropdowns broke

The performance pass added inline critical CSS to the homepage. One rule was:

```css
.mega-panel,.dropdown-panel{display:none}
```

The actual nav system does not use `display` toggling for desktop hover. It relies on panels existing in the layout and changing opacity/pointer behavior on hover/focus.

Impact:

- Desktop homepage nav submenu hover appeared broken.
- Hovering over menu items did not reveal the dropdowns.
- This was a core UX regression.

Immediate fix applied:

```css
.mega-panel,.dropdown-panel{opacity:0;pointer-events:none}
```

Then, after concern about other hidden regressions, the broader homepage performance layer was rolled back completely.

Commits:

```text
f0e025a Fix homepage nav dropdown hover regression
58cf113 Rollback risky homepage performance overrides
```

### 3. Homepage performance optimization touched too much above the fold

The homepage performance pass included several changes intended to reduce mobile LCP/render delay:

- Inline critical homepage hero/nav CSS.
- Async/preloaded main stylesheet.
- Removal of above-fold reveal attributes from hero media/floating card.
- Mobile-only guard around the hero cycle JS.
- Font-display change.

Some of these were valid performance ideas in isolation, but together they touched core visual/interaction behavior on the homepage without enough visual regression coverage.

This was the wrong risk profile for a live brand homepage.

## Why we rolled back

We rolled back the risky homepage performance work because:

1. It already caused two confirmed production regressions:
   - Fonts appeared wrong.
   - Desktop nav dropdowns broke.

2. The affected area was high-risk:
   - Homepage hero.
   - Main navigation.
   - Brand typography.
   - Above-the-fold user experience.

3. The performance gain was not worth the uncertainty.
   - A Lighthouse/LCP improvement does not justify destabilizing brand presentation or navigation.

4. Matt was reasonably concerned about unseen regressions.
   - Once visual and interaction regressions appear, the safest next move is rollback, then revisit through preview/testing.

## What exactly was rolled back

Commit `58cf113 Rollback risky homepage performance overrides` removed/reverted:

- The `critical-home-hero` inline CSS block from `index.html`.
- The async/preload stylesheet override on the homepage.
- The homepage-specific critical nav CSS that could interfere with menus.
- The removal of hero `data-reveal` attributes.
- The mobile-only hero-cycle JS guard.

Live verification after rollback showed:

```text
critical-home-hero absent: true
normal stylesheet loading restored: true
async style preload absent: true
fonts display=swap: true
display=optional absent: true
hero reveal attrs restored: true
bad dropdown display:none absent: true
main JS cycle restored: true
Vercel production: Ready
build.py --check: pass
check_links: pass
git diff --check: pass
```

## What remains live after rollback

The rollback did **not** remove the safer audit fixes. Live production still includes:

- Schema consolidation.
- Copy consistency fixes.
- Local SEO section clarification.
- CSP report collector.
- GHL redirect verification outcome.
- Font loading restored to `display=swap`.
- Normal homepage stylesheet loading.

## Known caveats / follow-up items

1. **GHL calendar naming/duration mismatch — resolved by Matt**
   - Public site copy is aligned around the current strategy-call positioning.
   - During Mercury's readback, GHL still showed the calendar name as `Strategy Session (15-Minute)` and `slotDuration: 30`.
   - Matt has since updated GHL directly, and Mercury verified by readback that the calendar now says and reflects 20 minutes:
     - `name`: `🌿 Strategy Session (20-Minute)`
     - `slotDuration`: `20`
     - `formSubmitRedirectUrl`: `https://lawnandlandmarketing.com/strategy-booked/`
   - No further GHL calendar action is needed unless a future readback shows drift.

2. **Homepage performance should be revisited only through preview**
   - Any future LCP work should happen in a preview branch/deployment.
   - Visual QA must include desktop nav hover, mobile menu, fonts, hero layout, CTA visibility, and above-fold screenshots.

3. **Avoid broad parser rewrites unless necessary**
   - `build.py` stamps header/footer across many pages.
   - Some audit fixes caused broad diffs because generated header/footer content was restamped.
   - Future changes should prefer narrow diffs unless a full restamp is intentional.

## Recommendation for next pass

Do not chase Lighthouse first.

Recommended order:

1. Run a production visual/functional regression pass:
   - Homepage desktop nav hover.
   - Mobile menu.
   - Fonts.
   - Header/footer CTAs.
   - Booking page.
   - Contact form page.
   - Checklist form page.
   - Service/program/industry hub rendering.

2. Keep schema/copy fixes as-is unless the auditor finds a specific issue.

3. Revisit homepage LCP only in a preview deployment with before/after screenshots and interaction checks.

4. If desired, update GHL calendar naming/duration only after explicit approval.

## Commit reference

Relevant commits:

```text
af0ab53 Fix audit findings: schema, LCP, copy consistency
6a61b2e Ignore local Vercel project state
cc33562 Stabilize homepage CLS after LCP pass
7557744 Inline critical nav CSS for stable async homepage load
b906cc0 Add CSP report collector and mobile-safe hero cycle
c9be3f1 Restore Google font loading behavior
f0e025a Fix homepage nav dropdown hover regression
58cf113 Rollback risky homepage performance overrides
```

The safest current production state is after:

```text
58cf113 Rollback risky homepage performance overrides
```
