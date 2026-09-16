#!/usr/bin/env python3
"""SEO snapshot for lawnandlandmarketing.com.

Pulls, in one run, everything the strategist needs to compare against the
last snapshot, and writes it to docs/seo/snapshots/<YYYY-MM-DD>.json plus a
human summary docs/seo/snapshots/<YYYY-MM-DD>.md.

Sources (all read-only):
  - DataForSEO Labs: ranked keywords, domain overview          (~$0.05/run)
  - DataForSEO Backlinks: summary + new referring domains       (~$0.05/run)
  - PageSpeed Insights: mobile scores for the 3 template types  (free)
  - Live crawl of sitemap.xml: status/title/canonical/robots    (free)
  - Google Search Console + GA4 (only once ~/.secrets/google-seo.env exists,
    created by `google-consent seo`)

Run:
    doppler run -p mac-claude -c prd -- python3 scripts/seo/snapshot.py
mac-claude/prd holds DATAFORSEO_LOGIN/PASSWORD. PAGESPEED_API_KEY is optional
(vault/prd has it; without it PSI still works at a lower quota).
"""
import base64
import concurrent.futures
import datetime as dt
import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT_DIR = os.path.join(ROOT, "docs", "seo", "snapshots")
SITE = "https://lawnandlandmarketing.com"
GSC_PROPERTY = "https://lawnandlandmarketing.com/"
GA4_PROPERTY = "properties/332001543"
TODAY = dt.date.today().isoformat()

# The 21 terms the Competitor Radar tracks daily live in Supabase (ci_keywords).
# This list is the strategist's watch set: head terms + money-page terms.
WATCH_TERMS = [
    "lawn care marketing", "lawn care marketing agency", "lawn care marketing company",
    "landscaping marketing", "landscaping marketing agency", "landscape marketing agency",
    "landscape marketing", "marketing for landscapers", "landscaper marketing",
    "landscaping seo", "seo for landscapers", "seo for landscaping companies", "lawn care seo",
    "google ads for landscapers", "landscaping facebook ads", "landscaping website design",
    "green industry marketing agency", "land clearing marketing", "excavation marketing",
    "septic company marketing", "holiday lighting marketing", "ai search optimization for landscapers",
]


def http(url, data=None, headers=None, method=None, timeout=120):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        return json.loads(urllib.request.urlopen(req, timeout=timeout).read())
    except urllib.error.HTTPError as e:
        return {"_error": e.code, "_body": e.read()[:400].decode("utf-8", "ignore")}
    except Exception as e:  # noqa: BLE001
        return {"_error": repr(e)}


# ---------------------------------------------------------------- DataForSEO
def dfs(path, body):
    login, pw = os.environ.get("DATAFORSEO_LOGIN"), os.environ.get("DATAFORSEO_PASSWORD")
    if not (login and pw):
        return {"_error": "DATAFORSEO_LOGIN/PASSWORD missing (run via doppler -p mac-claude)"}
    auth = base64.b64encode(f"{login}:{pw}".encode()).decode()
    return http("https://api.dataforseo.com" + path, json.dumps(body).encode(),
                {"Authorization": "Basic " + auth, "Content-Type": "application/json"})


def dataforseo_block():
    out = {}
    r = dfs("/v3/dataforseo_labs/google/domain_rank_overview/live",
            [{"target": "lawnandlandmarketing.com", "location_code": 2840, "language_code": "en"}])
    try:
        out["overview"] = r["tasks"][0]["result"][0]["items"][0]["metrics"]["organic"]
    except Exception:  # noqa: BLE001
        out["overview"] = r
    r = dfs("/v3/dataforseo_labs/google/ranked_keywords/live",
            [{"target": "lawnandlandmarketing.com", "location_code": 2840, "language_code": "en",
              "limit": 1000, "order_by": ["keyword_data.keyword_info.search_volume,desc"]}])
    rows = []
    try:
        for it in r["tasks"][0]["result"][0]["items"] or []:
            kd, se = it["keyword_data"], it["ranked_serp_element"]["serp_item"]
            rows.append({"keyword": kd["keyword"], "volume": kd["keyword_info"]["search_volume"],
                         "position": se.get("rank_group"), "url": se.get("relative_url"),
                         "intent": (kd.get("search_intent_info") or {}).get("main_intent")})
    except Exception:  # noqa: BLE001
        out["ranked_error"] = r
    out["ranked"] = sorted(rows, key=lambda x: (x["position"] or 999))
    r = dfs("/v3/backlinks/summary/live",
            [{"target": "lawnandlandmarketing.com", "include_subdomains": True, "backlinks_status_type": "live"}])
    try:
        s = r["tasks"][0]["result"][0]
        out["backlinks"] = {k: s.get(k) for k in ["rank", "backlinks", "referring_domains",
                                                    "referring_main_domains", "referring_domains_nofollow",
                                                    "backlinks_spam_score"]}
    except Exception:  # noqa: BLE001
        out["backlinks"] = r
    r = dfs("/v3/backlinks/referring_domains/live",
            [{"target": "lawnandlandmarketing.com", "include_subdomains": True, "backlinks_status_type": "live",
              "limit": 200, "order_by": ["first_seen,desc"]}])
    try:
        out["referring_domains"] = [{"domain": i["domain"], "rank": i["rank"], "backlinks": i["backlinks"],
                                     "first_seen": (i.get("first_seen") or "")[:10]}
                                    for i in r["tasks"][0]["result"][0]["items"] or []]
    except Exception:  # noqa: BLE001
        out["referring_domains"] = r
    return out


# ------------------------------------------------------------------ PageSpeed
def psi_block():
    key = os.environ.get("PAGESPEED_API_KEY")
    pages = [SITE + "/", SITE + "/marketing-services/local-seo/", SITE + "/industries/landscaping/",
             SITE + "/resources/blog/seo-for-landscaping-companies/"]
    out = {}
    for u in pages:
        q = {"url": u, "strategy": "mobile", "category": ["performance", "seo", "accessibility"]}
        if key:
            q["key"] = key
        r = http("https://www.googleapis.com/pagespeedonline/v5/runPagespeed?" + urllib.parse.urlencode(q, doseq=True), timeout=180)
        try:
            lr = r["lighthouseResult"]; c = lr["categories"]; a = lr["audits"]
            out[u] = {"perf": round(c["performance"]["score"] * 100), "seo": round(c["seo"]["score"] * 100),
                      "a11y": round(c["accessibility"]["score"] * 100),
                      "lcp": a["largest-contentful-paint"]["displayValue"], "cls": a["cumulative-layout-shift"]["displayValue"],
                      "tbt": a["total-blocking-time"]["displayValue"],
                      "crux": {k: v.get("category") for k, v in (r.get("loadingExperience", {}).get("metrics") or {}).items()} or None}
        except Exception:  # noqa: BLE001
            out[u] = r
    return out


# ---------------------------------------------------------------------- Crawl
def crawl_block():
    xml = urllib.request.urlopen(urllib.request.Request(SITE + "/sitemap.xml", headers={"User-Agent": "Mozilla/5.0"})).read().decode()
    urls = re.findall(r"<loc>(.*?)</loc>", xml)

    def attr(tag, b, key, val, want):
        for m in re.finditer(r"<%s\b[^>]*>" % tag, b, re.I):
            t = m.group(0)
            if re.search(r'%s\s*=\s*["\']%s["\']' % (key, re.escape(val)), t, re.I):
                w = re.search(r'\b%s\s*=\s*["\']([^"\']*)["\']' % want, t, re.I)
                if w:
                    return html.unescape(w.group(1))
        return None

    def fetch(u):
        d = {"url": u}
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (LL-SEO-snapshot)"}), timeout=30)
            d["status"] = r.status; b = r.read().decode("utf-8", "ignore")
        except Exception as e:  # noqa: BLE001
            d["status"] = repr(e); return d
        d["title"] = html.unescape((re.search(r"<title>(.*?)</title>", b, re.S | re.I) or [None, ""])[1]).strip()
        d["desc_len"] = len(attr("meta", b, "name", "description", "content") or "")
        d["canonical_ok"] = attr("link", b, "rel", "canonical", "href") == u
        d["noindex"] = "noindex" in (attr("meta", b, "name", "robots", "content") or "")
        d["h1_count"] = len(re.findall(r"<h1\b", b, re.I))
        d["ga4"] = "G-HFEP2769DS" in b
        return d

    with concurrent.futures.ThreadPoolExecutor(8) as ex:
        rows = list(ex.map(fetch, urls))
    issues = {
        "non_200": [(r["url"], r["status"]) for r in rows if r.get("status") != 200],
        "canonical_mismatch": [r["url"] for r in rows if r.get("status") == 200 and not r["canonical_ok"]],
        "noindex_in_sitemap": [r["url"] for r in rows if r.get("status") == 200 and r["noindex"]],
        "h1_not_one": [r["url"] for r in rows if r.get("status") == 200 and r["h1_count"] != 1],
        "missing_ga4": [r["url"] for r in rows if r.get("status") == 200 and not r["ga4"]],
        "desc_over_160": [r["url"] for r in rows if r.get("status") == 200 and r["desc_len"] > 160],
        "title_over_65": [r["url"] for r in rows if r.get("status") == 200 and len(r["title"]) > 65],
    }
    return {"sitemap_urls": len(urls), "issues": issues}


# ------------------------------------------------------------- Google (GSC/GA4)
def google_token():
    # Token source: env var (cloud routines / CI) or ~/.secrets/google-seo.env (Matt's Mac).
    rt = os.environ.get("GOOGLE_SEO_REFRESH_TOKEN")
    envf = os.path.expanduser("~/.secrets/google-seo.env")
    if not rt and os.path.exists(envf):
        for line in open(envf):
            if line.startswith("GOOGLE_SEO_REFRESH_TOKEN="):
                rt = line.strip().split("=", 1)[1]
    if not rt:
        return None
    # Fleet client (project 489025929507, INTERNAL consent screen, non-expiring tokens):
    # GBP_CLIENT_ID / GBP_CLIENT_SECRET are in mac-claude/prd. The old vesta-hermes client
    # (GOOGLE_OAUTH_CLIENT_JSON) is External+Testing and its tokens die after 7 days.
    cid, csec = os.environ.get("GBP_CLIENT_ID"), os.environ.get("GBP_CLIENT_SECRET")
    if not (cid and csec):
        raw = os.environ.get("GOOGLE_OAUTH_CLIENT_JSON")
        if not raw:
            return None
        c = json.loads(raw); c = c.get("installed") or c.get("web") or c
        cid, csec = c["client_id"], c["client_secret"]
    tok = http("https://oauth2.googleapis.com/token", urllib.parse.urlencode({
        "client_id": cid, "client_secret": csec,
        "refresh_token": rt, "grant_type": "refresh_token"}).encode())
    return tok.get("access_token")


def google_block(days=28):
    at = google_token()
    if not at:
        return {"_skipped": "no token: set GOOGLE_SEO_REFRESH_TOKEN or run `google-consent seo` on Matt's Mac"}
    h = {"Authorization": "Bearer " + at, "Content-Type": "application/json"}
    end = dt.date.today() - dt.timedelta(days=2)
    start = end - dt.timedelta(days=days - 1)
    prev_end = start - dt.timedelta(days=1)
    prev_start = prev_end - dt.timedelta(days=days - 1)
    out = {"window": [start.isoformat(), end.isoformat()], "prev_window": [prev_start.isoformat(), prev_end.isoformat()]}
    gsc = "https://www.googleapis.com/webmasters/v3/sites/%s/searchAnalytics/query" % urllib.parse.quote(GSC_PROPERTY, safe="")

    def q(body):
        return http(gsc, json.dumps(body).encode(), h)

    for label, s, e in [("totals", start, end), ("prev_totals", prev_start, prev_end)]:
        r = q({"startDate": s.isoformat(), "endDate": e.isoformat(), "dimensions": []})
        out[label] = (r.get("rows") or [{}])[0] if "_error" not in r else r
    for dim in ["query", "page"]:
        r = q({"startDate": start.isoformat(), "endDate": end.isoformat(), "dimensions": [dim], "rowLimit": 250})
        out["top_" + dim] = [{dim: x["keys"][0], "clicks": x["clicks"], "impressions": x["impressions"],
                              "ctr": round(x["ctr"] * 100, 2), "position": round(x["position"], 1)}
                             for x in (r.get("rows") or [])] if "_error" not in r else r
    r = q({"startDate": start.isoformat(), "endDate": end.isoformat(), "dimensions": ["query"], "rowLimit": 1000})
    watch = {}
    for x in (r.get("rows") or []):
        k = x["keys"][0]
        if k in WATCH_TERMS:
            watch[k] = {"clicks": x["clicks"], "impressions": x["impressions"], "position": round(x["position"], 1)}
    out["watch_terms"] = watch
    # GA4: sessions + key events by channel, organic landing pages
    ga = "https://analyticsdata.googleapis.com/v1beta/%s:runReport" % GA4_PROPERTY
    r = http(ga, json.dumps({"dateRanges": [{"startDate": start.isoformat(), "endDate": end.isoformat()},
                                             {"startDate": prev_start.isoformat(), "endDate": prev_end.isoformat()}],
                             "dimensions": [{"name": "sessionDefaultChannelGroup"}],
                             "metrics": [{"name": "sessions"}, {"name": "keyEvents"}, {"name": "engagedSessions"}]}).encode(), h)
    out["ga4_channels"] = r if "_error" in r else [{"channel": x["dimensionValues"][0]["value"],
                                                    "range": x["dimensionValues"][1]["value"] if len(x["dimensionValues"]) > 1 else "current",
                                                    "sessions": x["metricValues"][0]["value"], "key_events": x["metricValues"][1]["value"],
                                                    "engaged": x["metricValues"][2]["value"]} for x in r.get("rows", [])]
    r = http(ga, json.dumps({"dateRanges": [{"startDate": start.isoformat(), "endDate": end.isoformat()}],
                             "dimensions": [{"name": "landingPagePlusQueryString"}],
                             "metrics": [{"name": "sessions"}, {"name": "keyEvents"}],
                             "dimensionFilter": {"filter": {"fieldName": "sessionDefaultChannelGroup",
                                                            "stringFilter": {"value": "Organic Search"}}},
                             "limit": 50, "orderBys": [{"metric": {"metricName": "sessions"}, "desc": True}]}).encode(), h)
    out["ga4_organic_landing"] = r if "_error" in r else [{"page": x["dimensionValues"][0]["value"],
                                                           "sessions": x["metricValues"][0]["value"],
                                                           "key_events": x["metricValues"][1]["value"]} for x in r.get("rows", [])]
    return out


# ---------------------------------------------------------------------- main
def main():
    snap = {"date": TODAY, "site": SITE}
    print("DataForSEO..."); snap["dataforseo"] = dataforseo_block()
    print("Crawl..."); snap["crawl"] = crawl_block()
    print("PageSpeed..."); snap["pagespeed"] = psi_block()
    print("Google..."); snap["google"] = google_block()
    os.makedirs(OUT_DIR, exist_ok=True)
    jf = os.path.join(OUT_DIR, TODAY + ".json")
    json.dump(snap, open(jf, "w"), indent=1)

    # previous snapshot for deltas
    prev = None
    for f in sorted(os.listdir(OUT_DIR)):
        if f.endswith(".json") and f < TODAY + ".json":
            prev = json.load(open(os.path.join(OUT_DIR, f)))
    d = snap["dataforseo"]; ov = d.get("overview", {}); bl = d.get("backlinks", {})
    lines = [f"# SEO snapshot {TODAY}", ""]
    lines.append(f"- DataForSEO ranked keywords: **{ov.get('count')}** (top 3: {ov.get('pos_1', 0) + ov.get('pos_2_3', 0)}, top 10: {ov.get('pos_1', 0) + ov.get('pos_2_3', 0) + ov.get('pos_4_10', 0)}), est. traffic value {round(ov.get('etv', 0) or 0)}")
    lines.append(f"- Backlinks: {bl.get('backlinks')} from **{bl.get('referring_domains')}** referring domains (rank {bl.get('rank')})")
    if prev:
        pov = prev["dataforseo"].get("overview", {}); pbl = prev["dataforseo"].get("backlinks", {})
        lines.append(f"- vs {prev['date']}: keywords {pov.get('count')} → {ov.get('count')}, referring domains {pbl.get('referring_domains')} → {bl.get('referring_domains')}")
        pr = {r['keyword']: r['position'] for r in prev["dataforseo"].get("ranked", [])}
        moves = [(r["keyword"], pr.get(r["keyword"]), r["position"]) for r in d.get("ranked", []) if pr.get(r["keyword"]) and abs(pr[r["keyword"]] - (r["position"] or 100)) >= 5]
        if moves:
            lines.append("- Moves ≥5 positions: " + "; ".join(f"{k} {a}→{b}" for k, a, b in moves[:25]))
    g = snap["google"]
    if "_skipped" in g:
        lines.append(f"- GSC/GA4: skipped ({g['_skipped']})")
    else:
        t, p = g.get("totals", {}), g.get("prev_totals", {})
        lines.append(f"- GSC {g['window'][0]}→{g['window'][1]}: **{t.get('clicks')} clicks**, {t.get('impressions')} impressions, CTR {round((t.get('ctr') or 0) * 100, 2)}%, pos {round(t.get('position') or 0, 1)} (prev {p.get('clicks')} clicks / {p.get('impressions')} impr)")
        if g.get("watch_terms"):
            lines.append("- Watch terms: " + "; ".join(f"{k} pos {v['position']} ({v['impressions']} impr, {v['clicks']} clicks)" for k, v in sorted(g['watch_terms'].items(), key=lambda kv: kv[1]['position'])))
        ch = g.get("ga4_channels")
        if isinstance(ch, list):
            lines.append("- GA4 channels: " + "; ".join(f"{c['channel']}[{c['range']}] {c['sessions']} sess / {c['key_events']} key events" for c in ch))
    lines.append("- PageSpeed mobile: " + "; ".join(f"{u.replace(SITE, '') or '/'} perf {v.get('perf')} LCP {v.get('lcp')}" for u, v in snap["pagespeed"].items() if isinstance(v, dict) and "perf" in v))
    iss = snap["crawl"]["issues"]
    lines.append(f"- Crawl: {snap['crawl']['sitemap_urls']} sitemap URLs; issues: " + ", ".join(f"{k}={len(v)}" for k, v in iss.items() if v) or "none")
    md = os.path.join(OUT_DIR, TODAY + ".md")
    open(md, "w").write("\n".join(lines) + "\n")
    print("\n".join(lines)); print("\nWrote", jf, "and", md)


if __name__ == "__main__":
    sys.exit(main())
