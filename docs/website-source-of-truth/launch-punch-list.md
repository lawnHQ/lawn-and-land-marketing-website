# Launch Punch List

Running list of everything still outstanding for the `lawnandlandmarketing.com` launch.
Add to this as items come up; check them off as they're done. Last updated: 2026-06-23.

> Note: a parallel Claude session is populating real images + pushing to this repo. Keep
> lanes clear (funnel/redirect/infra vs images), and pull/rebase before pushing.

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

## Redirects / launch cutover
- [ ] **Pretty-link redirect engine** — serve the redirect-manager's branded links
  (`/update-billing`, etc.) on the main domain via a Supabase-backed lookup. WordPress serves these
  today; they break at cutover without this. *Biggest launch blocker.*
- [ ] Flip canonicals + `og:url`: `new.lawnlab.dev` → `lawnandlandmarketing.com` (mass find/replace;
  do at cutover, after images land, to avoid colliding with the image session).
- [ ] Add `robots.txt` (allow indexing on production).
- [ ] Refresh `sitemap.xml` — add `/checklist`, keep `/grow` out (noindex), real launch routes only.
- [ ] DNS switch (owner) — point `lawnandlandmarketing.com` at the new Vercel site.
- [ ] Post-cutover pass: confirm every old URL + every branded link resolves.

## Redirect manager
- [ ] Rotate the Google client secret (shared in chat earlier; unused by the ID-token design, but rotate to be safe).

## Page-review feedback (from the Site Map review sheet)
- [ ] Podcast page CTA: "schedule strategy call" → something like "Schedule Here".
- [ ] Landscaping page FAQ: currently worded to look "optional" — reword.

## Blog (separate track — Koga)
- [ ] 81-post import / blog migration.
- [ ] Blog author / EEAT: 3 owner inputs still pending.

---
*Done recently (for context): `/grow` rebuilt (on-brand, cold-traffic-optimized, proof-accurate);
`/checklist` rebuilt; old-WordPress 301 map wired in `vercel.json`; redirect manager + audit log live;
3 lead-magnet PDFs re-hosted.*
