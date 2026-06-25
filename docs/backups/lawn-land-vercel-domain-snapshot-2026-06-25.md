# Lawn & Land main site Vercel domain snapshot

Date: 2026-06-25 15:02:17 EDT
Repo: LawnAndLandMarketing/lawn-and-land-marketing-website
Local path: /Users/kingkai/Projects/LawnAndLandMarketing/lawn-and-land-marketing-website
Commit: 58cf1138d88db7dc6a8bd3a78f0912a8a21b6fa1
Working tree status at snapshot:
```
?? docs/audit-rollback-handoff-2026-06-25.md
```

## Production mapping

- Custom domain: https://lawnandlandmarketing.com
- WWW redirect: https://www.lawnandlandmarketing.com -> https://lawnandlandmarketing.com
- Vercel project serving custom domain: lawnland-site
- Old/staging Vercel URL still public: https://lawnland-site.vercel.app

## Artifact equivalence check

- lawnandlandmarketing.com homepage sha256: 5f9ac42c0d80c3551c4f2e2b54e42ebf19bc5021cb00cecdcd605f60f6f67989 len=89950
- lawnland-site.vercel.app homepage sha256: 5f9ac42c0d80c3551c4f2e2b54e42ebf19bc5021cb00cecdcd605f60f6f67989 len=89950
- Match: True

## Recommended cleanup

Add a host-based redirect for `lawnland-site.vercel.app` to `https://lawnandlandmarketing.com` while leaving custom domains on `lawnland-site` untouched. Do not delete the `lawnland-site` Vercel project unless custom domains are first moved safely.
