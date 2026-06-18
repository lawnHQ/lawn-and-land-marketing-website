# Universal Header, Navigation & Footer

The header (announcement bar + nav) and the footer are **single-source**. Edit only `_header.html` and
`_footer.html`; `python3 build.py` stamps them into every page (verify with `python3 build.py --check`).
**Never hand-edit the nav or footer inside a page** — `build.py` overwrites those regions. Vercel runs
`build.py` on deploy. Last overhaul: 2026-06-15.

## Top-level nav (in order)
`Home` · **About** ▾ · **Programs** ▾ · **Marketing Services** ▾ · **Industries** ▾ · **Resources** ▾ ·
`Get Started` (lime CTA, `.nav-cta--primary`, animated shimmer).
Each ▾ is a `.nav-item.nav-mega` containing a `.mega-panel`. On mobile the hamburger (`#navToggle`)
opens an accordion; caret items expand instead of navigating.

## Submenus (current state)

**About** — narrow single column (`.mega-panel--narrow` + `.mega-grid--single`):
- About → `/about/`
- **Experiences & Testimonials** → `/resources/experiences-reviews/` — Twilight-textured
  (`.mega-item--twilight`) with a **gold star** icon.
- *(The former founder/right-rail card was removed in the overhaul.)*
- *("Meet The Team" was sunset 2026-06-17 — the team now lives as a section on the About page
  (`/about/#team`); the standalone nav item, footer link, and page were all removed per the owner.)*

**Programs** — two themed cards (`.mega-grid--programs`):
- **Growth** → `/programs/growth/` — lime theme (`.mega-item--growth`), **sprout** icon, pill "For 6-Figure Companies".
- **Authority** → `/programs/authority/` — Twilight-textured (`.mega-item--authority`), **trophy** icon, pill "For 7-Figure Companies".

**Marketing Services** — wide two columns + featured card (`.mega-grid--wide`):
- *Acquire Demand*: Website Design · Local SEO · GBP Management · Google Ads
- *Convert & Retain*: Meta Ads · Your AI Partner · Reputation Management · CRM & Automation
- Featured: **"Most Companies Don't Need Another Vendor."** (`.mega-fc-title`, **not** an `<h4>`) →
  `/get-started/book-strategy-call/`.

**Industries** — wide two columns + featured card:
- *Lawn & Landscape*: Landscaping · Outdoor Living · Lawn Care · Lawn Maintenance
- *Land & Specialty*: Land Clearing · Excavation · Septic Installation · Holiday Lighting
- Featured: **"We Only Work In The Green Industry."** (`.mega-fc-title`) → `/about/`.

**Resources** — wide two columns + **Twilight testimonials** featured card:
- *Mow Money, Mow Problems*: The Podcast → `/resources/mow-money-mow-problems-podcast/` · YouTube Channel ↗ (external) · The Book ↗ (Amazon)
- *Learn & Connect*: Green Industry Insights / Blog → `/resources/blog/` · Private Facebook Group ↗ (Service Area Experts) · Contact Us → `/contact/`
- Featured: **Client Experiences** — a clickable `<a class="mega-featured-card mega-featured-card--twilight">`
  with a **gold 5-star row** (`.mega-fc-stars`) → `/resources/experiences-reviews/`.
- External links open in a new tab (`target="_blank" rel="noopener"`).

## Canonical service icons (consistent sitewide — Lucide)
Every place a marketing service is shown with an icon uses the **same** icon. The machine source of
truth is **`SERVICE_MAP` in `gen_service.py`** (it drives the service-page "pairs well with" CTAs); the
submenu, homepage, hub, and industry-page service grids must match it.

| Service | Lucide icon |
|---|---|
| Website Design | `monitor-smartphone` |
| Local SEO | `search` |
| GBP Management | `map-pin` |
| Google Ads | `badge-check` |
| Meta Ads | `book-user` |
| Your AI Partner | `bot` |
| Reputation Management | `star` |
| CRM & Automation | `refresh-ccw` |

The service formerly called **"Automation"** is now **"CRM & Automation"** everywhere (display name only;
the URL slug stays `/marketing-services/automation/`). When adding the new Lucide icons, pull the path
data verbatim from the Lucide source so it renders correctly.

## Mega-menu CSS system (in `assets/css/styles.css`)
- `.mega-panel` (+ `.mega-panel--narrow`, 380px) — the dropdown shell; hover or `.show` reveals it.
- `.mega-grid` (default 2-col) + `--single` (1fr) + `--wide` (2 item cols + a featured col; exact tracks
  set by a per-page inline override) + `--programs` (two themed cards).
- `.mega-item` (link row) + `--twilight` (purple texture + gold icon) / `--growth` (lime) / `--authority` (purple texture).
- `.mega-icon` / `.mega-icon svg` — sized + lime-stroked by a **per-page inline `<style>`** block (the
  global rule is intentionally dim; the inline block sets `opacity:1` + lime stroke).
- `.mega-col-label` — the uppercase column label.
- `.mega-featured-card` (+ `--twilight`, a clickable variant) — the right-rail promo. Parts:
  `.mega-featured-label`, **`.mega-fc-title`** (the de-headinged promo title — keeps the old `<h4>` look),
  `.mega-featured-btn`, `.mega-fc-stars` (gold star row), plus a `::before` accent line.
- `.mega-target-pill` (+ `--growth` lime / `--authority` twilight-soft) — the audience pills on Programs.
- **Twilight texture recipe** (reused on twilight items/cards and the seasonality/CTA bands):
  `background-color:#0d0b14` + a purple radial glow + a white dot-grid radial (`background-repeat:
  no-repeat,repeat`), with purple borders `rgba(104,55,239,…)`.

## Conventions / decisions locked (2026-06-15 overhaul)
- **Promo headlines are NOT headings.** The featured-card titles use `.mega-fc-title` (a `<div>` styled
  exactly like the old `<h4>`) so nav promo copy never pollutes the page heading hierarchy — an **SEO fix**.
- **Twilight = the premium / testimonial signal**: the About "Experiences" item, the Authority program,
  and the Resources testimonials card. **Gold stars** (`#FFC83D`, with glow) mark testimonials.
- **Lucide icons only** (no emoji). Programs pills use the **digit** form ("6-Figure"); running prose uses
  the **spelled** form ("six-figure").
- **Get Started** CTA lives in the nav (`.nav-cta--primary`) and routes to the free strategy call.

## Footer (`_footer.html`, `.footer-v2`)
Single-source, stamped by `build.py`. Rows: (1) brand + social + a "Ready to grow?" CTA card;
(2) four link columns — **Marketing Services** (8), **Industries** (the canonical 8), **Company**,
**Resources**; (3) a trust bar (100+ companies · 97%+ retention · since 2022); (4) a legal bar
(© Lawn & Land Marketing · St. Petersburg, FL · hello@lawnandlandmarketing.com). Tagline: "Green
industry specialists since 2022."

## How to change the nav or footer
1. Edit `_header.html` (announcement + nav) or `_footer.html`.
2. If you touched the mega CSS, edit `styles.css` and **bump `styles.css?v=` sitewide**
   (`find . -name "*.html" -not -path "./.git/*" -print0 | xargs -0 sed -i '' -E 's/styles\.css\?v=NN/styles.css?v=NN+1/g'`).
3. `python3 build.py` to re-stamp; `python3 build.py --check` to confirm all pages are in sync.
4. Commit + push both branches; verify on the live URL with a hard refresh.
