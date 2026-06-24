# Lawn & Land — Link Manager (`menu.lawnandlandmarketing.com`)

Self-serve dashboard for the team to create and manage branded short links / pretty links (replaces
WordPress Pretty Links). This is the tool the team uses to manage every `lawnandlandmarketing.com/<slug>`
redirect.

**Where this lives:** this folder is version-controlled inside the website repo
(`lawn-and-land-marketing-website/redirect-manager/`) so it sits alongside the site build — but it is a
**separate app with its own deploy**, NOT part of the website. The website build ignores it: `build.py`
skips this folder, and the site redirects `/redirect-manager` → the live tool (see the site `vercel.json`)
rather than serving a copy. Editing files here does not change the website, and vice versa.

## Architecture
- **Dashboard** — `index.html` (static, no framework). Google sign-in via Google Identity Services
  (GIS, ID-token flow → no client secret). Deployed on Vercel (team `lawn-and-land-marketing`,
  project `menu-redirect-manager`, ID `prj_2wqkq3Vu7mnSh0OF0hmifIAj6xye`). **Live at
  https://menu.lawnandlandmarketing.com** (Namecheap A record → 76.76.21.21, auto-SSL).
- **Backend** — Supabase Edge Function `redirects` on project **Project Operations**
  (`ztzqnpajurlxuorrfiwd`). Endpoint: `https://ztzqnpajurlxuorrfiwd.supabase.co/functions/v1/redirects`.
  `verify_jwt=false`; the function does **custom auth**: verifies the Google ID token on every request
  (jose + Google JWKS), requires `aud = <client id>`, `email_verified`, and `hd`/email domain =
  `lawnandlandmarketing.com`. Only then does it CRUD the `redirects` table (service role).
  Source: `supabase/functions/redirects/index.ts` (deployed via the Supabase MCP).
- **Data** — `redirects` table (Project Operations): id, slug (unique), destination, active, category,
  clicks, notes, created_at, updated_at. 46 links seeded from the Rank Math export.

## Auth
- Google OAuth client (Web, **Internal** consent → Workspace-only) created by owner.
  Client ID: `719731442715-5f1tdlaqgnfmpc1o72l2endva1iia4s2.apps.googleusercontent.com` (public).
  The client SECRET is not used by this design (ID-token flow) — owner advised to rotate it.
- Restricted to `@lawnandlandmarketing.com`. To limit to specific people, add an email allowlist in the
  Edge Function's `getUser()`.

## Deploy
This folder is the source of truth. To deploy the **dashboard**, from inside `redirect-manager/`:
run `vercel link` once (select the **menu-redirect-manager** project), then
`vercel deploy --prod --yes --scope lawn-and-land-marketing`. (The `.vercel` linkage is gitignored.)
- **Edge Function:** Supabase MCP `deploy_edge_function` (project `ztzqnpajurlxuorrfiwd`, name `redirects`,
  `verify_jwt:false`), or the Supabase CLI from `supabase/functions/redirects/`.
- **OAuth Authorized JavaScript origins** (Google Cloud Console) must include every origin the dashboard
  runs on — currently `https://menu.lawnandlandmarketing.com`.

## Audit log
Every create/update/delete is recorded in an **append-only** `audit_log` table: who (verified Google
email), what (per-field from→to diff), when. The table is immutable — UPDATE/DELETE/TRUNCATE are revoked
from every role (including the service role the app uses) and blocked by triggers; only INSERT/SELECT are
allowed. The dashboard's **Activity log** tab reads it via `GET ?view=log`. No one using the tool can edit
or delete an entry (only a direct DB superuser could, which is inherent to owning the data).

## Status / open items
1. **DNS — DONE.** `menu.lawnandlandmarketing.com` is live on Vercel (Namecheap A record → 76.76.21.21,
   auto-SSL); Google sign-in verified end-to-end (Workspace-only; personal Gmail rejected).
2. **Redirect serving on the MAIN domain — DONE (2026-06-24).** `lawnandlandmarketing.com/<slug>` 302s to
   the destination via a Vercel **edge function** (`api/redirect.js` in the website repo) that looks up the
   slug in this `redirects` table in real time (anon key + an RLS policy: anon may SELECT only `active=true`
   rows). A **catch-all rewrite** in the site `vercel.json` (`/:slug` and `/:slug/`) routes only unmatched
   single-segment paths to it — rewrites are filesystem-first, so real pages and the existing redirects always
   win; unknown slugs fall through to the site 404. Self-serve preserved: dashboard edits take effect within
   ~30s (CDN `s-maxage=30`). Inactive links (`active=false`) and missing slugs return the custom 404. The
   function source `/api/redirect.js` is blocked from direct access. (WordPress no longer serves these.)
3. **Content gaps — DONE.** The 3 PDFs are re-hosted in the site repo at `/downloads/` (on `main`) and the
   redirect destinations point to `lawnandlandmarketing.com/downloads/*.pdf`. `schedule-session` +
   `schedule-strategy` → `/get-started/book-strategy-call/`. `qr-mailer` deleted.
