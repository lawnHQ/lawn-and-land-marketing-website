#!/usr/bin/env python3
"""One-time consent for read-only Google Search Console + GA4 access.

Run it ONCE, signed into Google as matt@lawnandlandmarketing.com (the account
that owns the GSC property and has Editor on the GA4 property):

    doppler run -p vault -c prd -- python3 scripts/seo/google_auth.py

It opens a browser consent screen, catches the redirect on localhost, and
writes the refresh token to ~/.secrets/google-seo.env (chmod 600). No secret
is printed. The snapshot script reads that file.

Scopes requested (read-only):
  - https://www.googleapis.com/auth/webmasters.readonly   (Search Console)
  - https://www.googleapis.com/auth/analytics.readonly    (GA4 Data API)

If the first API call later fails with "API has not been used in project
... before or it is disabled", click the link in the error once to enable
the Search Console API / Google Analytics Data API on the OAuth client's
Google Cloud project. That is a one-click browser step.
"""
import http.server
import json
import os
import secrets
import stat
import sys
import urllib.parse
import urllib.request
import webbrowser

SCOPES = [
    "https://www.googleapis.com/auth/webmasters.readonly",
    "https://www.googleapis.com/auth/analytics.readonly",
]
OUT = os.path.expanduser("~/.secrets/google-seo.env")


def main():
    raw = os.environ.get("GOOGLE_OAUTH_CLIENT_JSON")
    if not raw:
        sys.exit("GOOGLE_OAUTH_CLIENT_JSON missing. Run via: doppler run -p vault -c prd -- python3 scripts/seo/google_auth.py")
    c = json.loads(raw)
    c = c.get("installed") or c.get("web") or c
    client_id, client_secret = c["client_id"], c["client_secret"]

    state = secrets.token_urlsafe(16)
    code_holder = {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            if q.get("state", [""])[0] == state and "code" in q:
                code_holder["code"] = q["code"][0]
                body = b"<h2>Done. You can close this tab and return to the terminal.</h2>"
            else:
                body = b"<h2>Missing or mismatched code. Re-run the script.</h2>"
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *a):
            pass

    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    redirect = f"http://localhost:{srv.server_port}/"
    url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode({
        "client_id": client_id,
        "redirect_uri": redirect,
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "access_type": "offline",
        "prompt": "consent",
        "state": state,
        "login_hint": "matt@lawnandlandmarketing.com",
    })
    print("Opening the Google consent screen. If it does not open, paste this URL into a browser signed in as matt@:\n\n" + url + "\n")
    webbrowser.open(url)
    while "code" not in code_holder:
        srv.handle_request()

    data = urllib.parse.urlencode({
        "code": code_holder["code"],
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect,
        "grant_type": "authorization_code",
    }).encode()
    tok = json.loads(urllib.request.urlopen("https://oauth2.googleapis.com/token", data=data).read())
    if "refresh_token" not in tok:
        sys.exit("No refresh_token returned. Re-run; if it keeps happening, revoke the app at myaccount.google.com/permissions and try again.")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    os.chmod(os.path.dirname(OUT), stat.S_IRWXU)
    with open(OUT, "w") as f:
        f.write(f"GOOGLE_SEO_REFRESH_TOKEN={tok['refresh_token']}\n")
    os.chmod(OUT, stat.S_IRUSR | stat.S_IWUSR)
    print(f"Saved refresh token to {OUT} (scopes: {tok.get('scope')}).")
    print("Next: doppler run -p mac-claude -c prd -- python3 scripts/seo/snapshot.py")


if __name__ == "__main__":
    main()
