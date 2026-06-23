# Launch Punch List

Running list of everything still outstanding for the `lawnandlandmarketing.com` launch.
Add to this as items come up; check them off as they're done. Last updated: 2026-06-23.

> Note: a parallel Claude session is populating real images + pushing to this repo. Keep
> lanes clear (funnel/redirect/infra vs images), and pull/rebase before pushing.
> Owner also keeps a Google Sheet (owner-inputs tracker); mirror items there via paste-blocks.

## Forms / integrations
- [ ] **`/checklist` — wire the lead form to GHL.** The native form (First / Last / Email / Phone)
  captures the lead and delivers the PDF on submit, but submissions are **not saved anywhere yet**
  (localStorage stub). Connect before this gets real traffic. Options:
  - **Inbound webhook (preferred)** — create a webhook/automation in GHL, POST the form fields to it
    (keeps the on-brand native form). Need the webhook URL.
  - **GHL form embed** — drop in the GHL form iframe (`OhY6Qt2Y4QWBBQlExOxg`); fully wired but uses
    GHL's default form styling.

## Images (parallel session in progress)
- [ ] Real photos for the labeled placeholders (service, program, industry, case-study pages).
- [ ] **Precision case study image is labeled "Precision Turf Care"** (wrong company name) — fix. *(from the page-review sheet)*

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
- [ ] **Blog redirects** (coordinate with Koga's redirect map). Old posts live at `/blog/<slug>/`, new at
  `/resources/blog/<slug>/`. Need: `/blog/<slug>/` → `/resources/blog/<slug>/` for the 19 migrated; and
  `/blog/<slug>/` → nearest keeper (or `/resources/blog/`) for the 62 cuts. None are in `vercel.json` yet.
- [ ] **Real images for the 18 new articles** (image pass) — hero + card thumbnails are `.img-ph` placeholders
  for now (#17 already has its real image). Schema `image` URLs point to planned `/assets/images/blog/*` files.
- [ ] **3 broken posts still LIVE on WordPress** (not migrated): #16 leaked AI instructions, #24 + #72 copy-paste
  errors. Unpublish on the old site now (credibility).
- [ ] 3 EEAT owner inputs still pending (for the author/byline system).

## Redirects / launch cutover
- [ ] Flip canonicals + `og:url`: `new.lawnlab.dev` → `lawnandlandmarketing.com` (mass find/replace;
  do at cutover, after images land, to avoid colliding with the image session).
- [ ] Add `robots.txt` (allow indexing on production).
- [ ] Refresh `sitemap.xml` — add `/checklist`, keep `/grow` out (noindex), real launch routes only.
- [ ] DNS switch (owner) — point `lawnandlandmarketing.com` at the new Vercel site.
- [ ] Post-cutover pass: confirm every old URL + every structural redirect resolves.

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
