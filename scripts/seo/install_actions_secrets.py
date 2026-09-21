#!/usr/bin/env python3
"""Install the GitHub Actions secrets the two SEO workflows need.

Run it once, from the repo root:

    doppler run -p vault -c prd -- python3 scripts/seo/install_actions_secrets.py --dry-run
    doppler run -p vault -c prd -- python3 scripts/seo/install_actions_secrets.py

It reads each value from the Doppler environment Doppler injects, encrypts it with the
repository's own public key (libsodium sealed box, the same thing the GitHub UI does in
your browser), and writes it to
Settings > Secrets and variables > Actions on lawnHQ/lawn-and-land-marketing-website.

No secret value is ever printed, logged, or written to disk. The script prints names only.

Two values are deliberately NOT sourced from Doppler:

  ANTHROPIC_API_KEY         Pass it with --anthropic-key sk-ant-...  This workflow should
                            get its OWN key, not a shared one. A shared vault key ran up
                            $1,449 in three days once; a dedicated key makes this
                            workflow's spend visible and separately revocable.
  GOOGLE_SEO_REFRESH_TOKEN  Read from ~/.secrets/google-seo.env, which is written by
                            `doppler run -p mac-claude -c prd -- google-consent seo`.
                            The script refuses to install a token that no longer works.

Needs: GITHUB_LAWNHQ_TOKEN (in vault/prd) with admin rights on the repo, and pynacl.
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request

REPO = "lawnHQ/lawn-and-land-marketing-website"
API = "https://api.github.com"

# secret name -> environment variable Doppler injects
FROM_DOPPLER = {
    "DATAFORSEO_LOGIN": "DATAFORSEO_LOGIN",
    "DATAFORSEO_PASSWORD": "DATAFORSEO_PASSWORD",
    "PAGESPEED_API_KEY": "PAGESPEED_API_KEY",
    "GBP_CLIENT_ID": "GBP_CLIENT_ID",
    "GBP_CLIENT_SECRET": "GBP_CLIENT_SECRET",
    "OPENAI_API_KEY": "OPENAI_API_KEY",
}
GOOGLE_ENV_FILE = os.path.expanduser("~/.secrets/google-seo.env")


def gh(path, token, data=None, method=None):
    req = urllib.request.Request(
        API + path,
        data=json.dumps(data).encode() if data is not None else None,
        method=method,
        headers={"Authorization": "Bearer " + token,
                 "Accept": "application/vnd.github+json",
                 "X-GitHub-Api-Version": "2022-11-28",
                 "Content-Type": "application/json",
                 "User-Agent": "ll-seo-installer"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read()
            return r.status, (json.loads(body) if body else {})
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "ignore")[:300]


def seal(public_key_b64, value):
    from nacl import encoding, public
    box = public.SealedBox(public.PublicKey(public_key_b64.encode(), encoding.Base64Encoder()))
    return base64.b64encode(box.encrypt(value.encode())).decode()


def google_token_is_live(token):
    """A dead refresh token is worse than a missing one: the workflow would look configured."""
    cid, csec = os.environ.get("GBP_CLIENT_ID"), os.environ.get("GBP_CLIENT_SECRET")
    if not (cid and csec):
        return None
    import urllib.parse
    data = urllib.parse.urlencode({"client_id": cid, "client_secret": csec,
                                   "refresh_token": token, "grant_type": "refresh_token"}).encode()
    try:
        urllib.request.urlopen(urllib.request.Request(
            "https://oauth2.googleapis.com/token", data=data), timeout=25)
        return True
    except urllib.error.HTTPError:
        return False
    except Exception:  # noqa: BLE001
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="check everything, write nothing")
    ap.add_argument("--anthropic-key", help="sk-ant-... pay-per-token fallback")
    ap.add_argument("--oauth-token", help="sk-ant-oat01-... from `claude setup-token` (preferred: uses the subscription)")
    args = ap.parse_args()

    # Fine-grained tokens usually lack the "Secrets" permission even when they are admin,
    # so try each stored token and keep the first that can actually read the repo key.
    token, key = None, None
    tried = []
    for name in ("GITHUB_TOKEN", "GITHUB_PAT", "GITHUB_LAWNHQ_TOKEN"):
        t = os.environ.get(name)
        if not t:
            continue
        status, body = gh(f"/repos/{REPO}/actions/secrets/public-key", t)
        tried.append(f"{name}={status}")
        if status == 200:
            token, key = t, body
            print(f"Using {name} (can write Actions secrets).")
            break
    if not token:
        sys.exit("No stored token can write Actions secrets on this repo (" + ", ".join(tried) + ").\n"
                 "Run under: doppler run -p vault -c prd -- ...  A classic PAT with `repo` scope works;\n"
                 "fine-grained tokens additionally need the repository \"Secrets\" write permission.")

    planned, missing = {}, []
    for name, env in FROM_DOPPLER.items():
        v = os.environ.get(env)
        planned[name] = v if v else None
        if not v:
            missing.append(f"{name} (not in the Doppler environment)")

    # Preferred: the Claude subscription token (no per-token billing). Mint a fresh one with
    # `claude setup-token` and pass --oauth-token, or let it come from Doppler if stored there.
    oauth = args.oauth_token or os.environ.get("CLAUDE_CODE_OAUTH_TOKEN")
    if oauth:
        planned["CLAUDE_CODE_OAUTH_TOKEN"] = oauth
    else:
        missing.append("CLAUDE_CODE_OAUTH_TOKEN (run `claude setup-token`, then pass --oauth-token)")

    if args.anthropic_key:
        planned["ANTHROPIC_API_KEY"] = args.anthropic_key
    elif not oauth:
        missing.append("ANTHROPIC_API_KEY (pay-per-token fallback; only needed if there is no subscription token)")

    if os.path.exists(GOOGLE_ENV_FILE):
        gt = None
        for line in open(GOOGLE_ENV_FILE):
            if line.startswith("GOOGLE_SEO_REFRESH_TOKEN="):
                gt = line.strip().split("=", 1)[1]
        if gt:
            live = google_token_is_live(gt)
            if live is True:
                planned["GOOGLE_SEO_REFRESH_TOKEN"] = gt
            elif live is False:
                missing.append("GOOGLE_SEO_REFRESH_TOKEN (the token in ~/.secrets/google-seo.env is "
                               "revoked; re-run: doppler run -p mac-claude -c prd -- google-consent seo)")
            else:
                planned["GOOGLE_SEO_REFRESH_TOKEN"] = gt
                print("NOTE: could not verify the Google token; installing it anyway.")
        else:
            missing.append(f"GOOGLE_SEO_REFRESH_TOKEN (not found in {GOOGLE_ENV_FILE})")
    else:
        missing.append(f"GOOGLE_SEO_REFRESH_TOKEN ({GOOGLE_ENV_FILE} does not exist)")

    to_write = {k: v for k, v in planned.items() if v}
    print(f"\nRepository: {REPO}")
    print(f"Will install {len(to_write)} secret(s): " + ", ".join(sorted(to_write)) or "none")
    if missing:
        print("\nNOT installing, and why:")
        for m in missing:
            print("  - " + m)

    if args.dry_run:
        print("\nDry run, nothing written.")
        return 0
    if not to_write:
        print("\nNothing to write.")
        return 1

    print()
    for name, value in sorted(to_write.items()):
        status, body = gh(f"/repos/{REPO}/actions/secrets/{name}", token,
                          {"encrypted_value": seal(key["key"], value), "key_id": key["key_id"]},
                          method="PUT")
        print(f"  {name}: {'OK' if status in (201, 204) else f'FAILED HTTP {status} {body}'}")

    # kill switch, as a repository variable so it can be flipped without a code change
    status, _ = gh(f"/repos/{REPO}/actions/variables/SEO_AGENTS_ENABLED", token,
                   {"name": "SEO_AGENTS_ENABLED", "value": "true"}, method="PATCH")
    if status not in (204, 201):
        status, _ = gh(f"/repos/{REPO}/actions/variables", token,
                       {"name": "SEO_AGENTS_ENABLED", "value": "true"}, method="POST")
    print(f"  SEO_AGENTS_ENABLED (variable): {'OK' if status in (201, 204) else f'FAILED HTTP {status}'}")

    status, listing = gh(f"/repos/{REPO}/actions/secrets", token)
    if status == 200:
        print("\nSecrets now on the repo: " +
              ", ".join(sorted(s["name"] for s in listing.get("secrets", []))))
    print("\nStill needed before the workflows can run at full strength:")
    for m in missing:
        print("  - " + m)
    return 0


if __name__ == "__main__":
    sys.exit(main())
