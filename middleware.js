export function middleware(request) {
  const url = new URL(request.url);

  if (url.hostname === 'lawnland-site.vercel.app') {
    url.hostname = 'lawnandlandmarketing.com';
    url.protocol = 'https:';
    return Response.redirect(url, 308);
  }
}

export const config = {
  matcher: '/:path*',
};
