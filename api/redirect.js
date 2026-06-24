// Branded short-link serving layer for lawnandlandmarketing.com/<slug>.
//
// Looks up <slug> in the redirect-manager's Supabase `redirects` table in real time
// and 302-redirects to its destination. Self-serve: the team edits links in the
// dashboard (menu.lawnandlandmarketing.com) and changes take effect within ~30s.
//
// Reached via the catch-all rewrite in vercel.json, which is filesystem-first — so
// real site pages and the existing WordPress redirects always win, and only unmatched
// single-segment paths reach this function. No active match -> the site's custom 404.

export const config = { runtime: 'edge' };

const SUPABASE_URL = 'https://ztzqnpajurlxuorrfiwd.supabase.co';
// Public anon key. RLS restricts the anon role to SELECT on active redirects only,
// so this is safe to ship (it can read nothing but the public branded-link list).
const SUPABASE_ANON =
  'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp0enFucGFqdXJseHVvcnJmaXdkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzQ1NTE5MTQsImV4cCI6MjA5MDEyNzkxNH0.V8QBgUmZ22WGUCRktQ2UVkgZWWSFPOGIDAW0oLHFc9w';

export default async function handler(request) {
  const url = new URL(request.url);
  const slug = (url.searchParams.get('slug') || '')
    .trim()
    .toLowerCase()
    .replace(/^\/+|\/+$/g, '');

  if (slug && !slug.includes('/')) {
    try {
      const lookup =
        `${SUPABASE_URL}/rest/v1/redirects` +
        `?slug=eq.${encodeURIComponent(slug)}&active=eq.true&select=destination&limit=1`;
      const res = await fetch(lookup, {
        headers: { apikey: SUPABASE_ANON, authorization: `Bearer ${SUPABASE_ANON}` },
      });
      if (res.ok) {
        const rows = await res.json();
        const dest = rows && rows[0] && rows[0].destination;
        if (dest) {
          return new Response(null, {
            status: 302,
            headers: {
              location: dest,
              // browser never caches; CDN refreshes within 30s so dashboard edits go live fast
              'cache-control': 'public, max-age=0, s-maxage=30',
            },
          });
        }
      }
    } catch (_) {
      // fall through to the 404 page
    }
  }

  // No active branded link for this slug -> serve the site's custom 404 page.
  try {
    const notFound = await fetch(new URL('/404.html', url.origin));
    if (notFound.ok) {
      return new Response(await notFound.text(), {
        status: 404,
        headers: { 'content-type': 'text/html; charset=utf-8' },
      });
    }
  } catch (_) {
    // fall through to the minimal 404
  }
  return new Response('Not Found', {
    status: 404,
    headers: { 'content-type': 'text/plain; charset=utf-8' },
  });
}
