# Launch Punch List

Running list of everything still outstanding for the production site.
Add to this as items come up; check them off as they're done. Last updated: 2026-06-26.

> Note: a parallel Claude session is populating real images + pushing to this repo. Keep
> lanes clear (funnel/redirect/infra vs images), and pull/rebase before pushing.
> Owner also keeps a Google Sheet (owner-inputs tracker); mirror items there via paste-blocks.

## Production maintenance status (updated 2026-06-26)
- [x] Production domain live on `lawnandlandmarketing.com`.
- [x] Canonicals + `og:url` production-domain aligned.
- [x] `robots.txt` exists and points to the sitemap.
- [x] `sitemap.xml` exists on the production domain.
- [ ] Keep structural redirects and old URL coverage verified after major route changes.
- [ ] Keep form/tracking items below handled as separate operational tasks, not launch blockers.

## Forms / integrations
- [ ] **`/checklist` — wire the lead form to GHL.** The native form (First / Last / Email / Phone)
  captures the lead and delivers the PDF on submit, but submissions are **not saved anywhere yet**
  (localStorage stub). Connect before this gets real traffic. Options:
  - **Inbound webhook (preferred)** — create a webhook/automation in GHL, POST the form fields to it
    (keeps the on-brand native form). Need the webhook URL.
  - **GHL form embed** — drop in the GHL form iframe (`OhY6Qt2Y4QWBBQlExOxg`); fully wired but uses
    GHL's default form styling.

## Images (parallel session in progress)
- [x] **All `svc-ph` 'Image placeholder' boxes filled (2026-06-24):** homepage panels, the 8 service-detail first images, and the 4 marketing-services hub featured cards. Industry/program pages have empty styled image areas (`ind-ph`/`why-ph`), not labeled placeholders; optional to fill later.
- [x] **Fixed "Precision Turf Care" -> "Precision Landscape Management"** in the proof-image alt (homepage + authority page) (2026-06-24).

## `/grow` (Facebook funnel) — built + auditor-approved
- [ ] Ad → page message-match + trade-specific variants (needs the live Facebook ads to audit against).
- [ ] Decision: put the Facebook pixel **site-wide** (retargeting any visitor) or keep it only on `/grow`?

## Blog
- [x] Audit of the 81 posts → done (`blog-audit.md`): 19 keepers, 62 cuts.
- [x] **Migrate the 19 keepers to `/resources/blog/` (2026-06-23)** — original publish dates preserved, one
  canonical article template (`article.css`), BlogPosting + FAQPage schema, Matt Foreman byline. Reused +
  standardized 6 of Koga's; built 13 fresh from the legacy WordPress posts. Index rebuilt (21 cards, 5 filters).
  Process recorded in `blog-migration-spec.md`.
- [x] **Closed Koga's `koga/blog-migration-optimization` PR (#1) — superseded** (2026-06-23). It carried 12
  cut-list filler posts + only 6 keepers; closed (not merged) so the filler can't come back. Branch left intact for reference.
- [x] **Blog redirects wired in `vercel.json`** (2026-06-23): catch-all `/blog/:slug` → `/resources/blog/:slug/`
  for the 19 keepers; the 62 cut posts topic-mapped to the nearest keeper (podcast recaps → `/client-results/`).
  170 redirects total, both slash variants. They fire at launch on the production domain.
- [ ] **Real images for the 18 new articles** (image pass) — hero + card thumbnails are `.img-ph` placeholders
  for now (#17 already has its real image). Schema `image` URLs point to planned `/assets/images/blog/*` files.
- [ ] **3 broken posts still LIVE on WordPress** (not migrated): #16 leaked AI instructions, #24 + #72 copy-paste
  errors. Unpublish on the old site now (credibility).
- [ ] 3 EEAT owner inputs still pending (for the author/byline system).

## Redirects / production cutover
- [x] Canonicals + `og:url` flipped to `lawnandlandmarketing.com`.
- [x] Added `robots.txt` (2026-06-24): allow-all, disallow `/grow/` + `/confirmation/`, points to sitemap.
- [x] Refreshed `sitemap.xml` (2026-06-23) — added `/checklist` + the 19 blog posts (53 URLs; `/grow` already excluded).
- [x] Production domain live on the new Vercel site.
- [ ] Ongoing: confirm every old URL + every structural redirect resolves after future route changes.

## Redirect manager
- [ ] Rotate the Google client secret (shared in chat earlier; unused by the ID-token design, but rotate to be safe).

## Page-review feedback (from the Site Map review sheet)
- [ ] Podcast page CTA: "schedule strategy call" → something like "Schedule Here".
- [ ] Landscaping page FAQ: currently worded to look "optional" — reword.

## Post-launch (after go-live)
- [ ] **Pretty-link redirect engine** — serve the redirect-manager's branded links (`/update-billing`,
  `/schedule`, QR links, etc.) on the main domain via a real-time Supabase lookup (Vercel edge middleware)
  + click counting. **Owner decided post-launch (2026-06-23).** NOTE: until it's built, those branded
  pretty-links won't redirect on the new domain. The structural old-page 301s in `vercel.json` are
  unaffected and still fire at launch. Stopgap if needed: keep WordPress serving the branded links, or
  point the highest-traffic ones somewhere manually.

---
*Done recently (for context): `/grow` rebuilt (on-brand, cold-traffic-optimized, proof-accurate);
`/checklist` rebuilt; old-WordPress 301 map wired in `vercel.json`; redirect manager + audit log live;
3 lead-magnet PDFs re-hosted.*
