# Website Decisions Log

## 2026-04-14
- This public website build should stay separate from the internal Ground Control concept and naming.
- The repo should maintain a dedicated website-specific source-of-truth folder for architecture and progress tracking.
- `/marketing-services/` is the canonical service section.
- `/services/` is intentionally not part of the approved website and should be retired from all internal linking.
- `/pricing/` is intentionally not part of the approved website and should not be reintroduced as a canonical page.
- `/contact/` is the canonical contact route.
- `/resources/contact/` is non-canonical and should be removed from internal linking.
- `/resources/guides/` is out of scope and should be retired.
- Approved sitemap includes Home, About, Programs, Marketing Services, Industries, Resources, and Get Started / Book Strategy Call.
- Lawnline (`https://lawnline.marketing/`) is the primary public benchmark to beat on structure, SEO strength, and overall execution quality.

## 2026-04-15
- Approved structural cleanup pass has been applied in the repo.
- `_nav.html`, `_footer.html`, homepage/service CTAs, duplicated page HTML, and `404.html` were updated to remove the retired route drift.
- `resources/contact/index.html` and `resources/guides/index.html` were deleted from the repo.
- Next work should shift from route hygiene to finishing the highest-leverage thin pages.

## 2026-04-15 (continued)
- A second route-hygiene pass removed the remaining broken internal links to orphan routes like `/team/`, `/results/`, `/good-fit/`, `/book/`, and old article URLs.
- Top-priority thin pages were deepened in this workstream: `/programs/`, `/marketing-services/`, `/about/`, and `/contact/`.
- The next highest-leverage page work should move deeper into service detail pages rather than reopening top-level architecture decisions.

## 2026-04-15 (latest)
- Homepage remains the only intentionally developed public page for now.
- All non-home public pages should currently stay header + hero + blank-body placeholder + CTA/footer until the design direction is approved.
- Written body expansion on non-home pages should pause until that design phase begins.

## 2026-04-16
- `/programs/` has been reopened as the current design exploration page.
- A simple body-layout prototype was added to `/programs/` with placeholder/lorem blocks for philosophy, quick breakdown, Growth, Authority, and right-stage guidance.
- A more aggressive visual redesign pass for `/programs/` was attempted and then rejected.
- The simpler pre-v2 Programs version was restored and is the current live state to review from.
- For now, keep the simpler `/programs/` prototype live while Matt reviews and prepares detailed feedback.
- Do not assume the rejected v2 direction should be revived without explicit approval.

## 2026-06-13
- Header and footer are now truly single-source. `_header.html` (announcement bar + nav) and `_footer.html` are the only files to edit; `build.py` stamps them into every page and runs automatically on Vercel deploy via `vercel.json` buildCommand.
- The announcement bar was folded into the universal header and unified across all 31 pages (text + `/contact/` link). Previously the homepage used a relative link and `/404.html` had a stray promo.
- Replaced the old fragile `build-pages.py` (hardcoded `/tmp` path) with `build.py`. Refreshed `_footer.html` to match the current live footer (the partial had gone stale). Brought `/404.html` into the universal header/footer.
- Decision pending from Matt: begin building out the non-home page bodies ("build it out to the best solution") — establish a reusable page design system from the homepage, then roll out across the sitemap.

## Open Decisions To Track Later
- What exact visual direction from the current `/programs/` prototype should become the reusable non-home page system.
- Whether any retired routes should be redirected intentionally versus simply removed from internal linking.
- Exact completion order of service pages after top-level architecture cleanup is done.
- Whether additional proof-heavy pages like results or case studies should return later in a different form.
