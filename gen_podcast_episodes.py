#!/usr/bin/env python3
"""Keep the podcast page's latest-6 episodes (cards + schema) in sync with the channel RSS.

Rewrites two marked regions on resources/mow-money-mow-problems-podcast/index.html:
  <!-- EPISODES:START/END -->       the 6 episode cards (each links to its YouTube video, new tab)
  <!-- PODCAST_SCHEMA:START/END -->  PodcastSeries + per-episode PodcastEpisode + VideoObject JSON-LD

New episodes appear automatically and older ones drop off. Real per-episode upload dates come
from the feed (never copied across episodes). Idempotent. Run on a schedule
(.github/workflows/podcast-episodes.yml) and after any edit.
"""
import re, os, html, json, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(ROOT, 'resources', 'mow-money-mow-problems-podcast', 'index.html')
CHANNEL_ID = 'UCDquVUlNKHjfFSA8C239qIw'
FEED = f'https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}'
DOMAIN = 'https://lawnandlandmarketing.com'
BASE = DOMAIN + '/resources/mow-money-mow-problems-podcast/'
YT = 'https://www.youtube.com/@MowMoneyMowProblemsPodcast'
N = 6


def esc(t):
    return t.replace('&', '&amp;')


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; LawnLandBot/1.0)'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode('utf-8')


def latest(xml, n=N):
    out = []
    for e in re.findall(r'<entry>(.*?)</entry>', xml, re.S):
        vid = re.search(r'<yt:videoId>([^<]+)</yt:videoId>', e)
        title = re.search(r'<title>([^<]+)</title>', e)
        pub = re.search(r'<published>([^<]+)</published>', e)
        if not vid or not title:
            continue
        t = html.unescape(title.group(1)).strip()
        parts = [p.strip() for p in t.split(' - ')]
        m = re.search(r'(\d+)', parts[0]) if parts else None
        num = m.group(1) if m else ''
        guest = parts[1] if len(parts) > 1 else t
        company = parts[2] if len(parts) > 2 else ''
        date = pub.group(1).strip() if pub else ''
        out.append((vid.group(1), num, guest, company, date))
        if len(out) >= n:
            break
    return out


def card(vid, num, guest, company, date):
    g, c = esc(guest), esc(company)
    return (
        f'        <a class="pod-ep" href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener">\n'
        f'          <div class="pod-video">\n'
        f'            <img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="Episode {num}: {g}, {c}" loading="lazy">\n'
        f'            <span class="pod-play" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></span>\n'
        f'          </div>\n'
        f'          <div class="pod-ep-body">\n'
        f'            <span class="pod-ep-badge">Episode {num}</span>\n'
        f'            <h3 class="pod-ep-title">{g}</h3>\n'
        f'            <div class="pod-ep-co">{c}</div>\n'
        f'          </div>\n'
        f'        </a>'
    )


def schema(eps):
    sid = BASE + '#podcast'
    nodes = [{
        "@type": "PodcastSeries", "@id": sid, "name": "Mow Money, Mow Problems",
        "description": "A weekly podcast where host Matt Foreman talks with green-industry business owners about growing, running, and surviving the business.",
        "url": BASE, "image": DOMAIN + "/assets/images/og-share.jpg",
        "webFeed": FEED, "sameAs": [YT],
        "author": {"@id": DOMAIN + "/#matt-foreman"}, "publisher": {"@id": DOMAIN + "/#organization"},
    }]
    for vid, num, guest, company, date in eps:
        watch = f"https://www.youtube.com/watch?v={vid}"
        nm = f"Episode {num}: {guest}" + (f", {company}" if company else "")
        desc = (f"Mow Money, Mow Problems Episode {num}: Matt Foreman talks with {guest}"
                + (f" of {company}" if company else "") + " about growing a green-industry business.")
        epnum = int(num) if num.isdigit() else num
        nodes.append({"@type": "PodcastEpisode", "@id": BASE + f"#episode-{num}", "name": nm,
                      "episodeNumber": epnum, "datePublished": date, "description": desc, "url": watch,
                      "partOfSeries": {"@id": sid}, "associatedMedia": {"@id": BASE + f"#video-{num}"}})
        nodes.append({"@type": "VideoObject", "@id": BASE + f"#video-{num}", "name": nm, "description": desc,
                      "thumbnailUrl": f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg", "uploadDate": date,
                      "embedUrl": f"https://www.youtube.com/embed/{vid}", "contentUrl": watch})
    return {"@context": "https://schema.org", "@graph": nodes}


def main():
    eps = latest(fetch(FEED))
    if not eps:
        print("No episodes parsed from RSS; page unchanged.")
        return 0
    s = open(PAGE, encoding='utf-8').read()
    cards = '\n'.join(card(*e) for e in eps)
    s2 = re.sub(r'<!-- EPISODES:START -->.*?<!-- EPISODES:END -->',
                lambda m: '<!-- EPISODES:START -->\n' + cards + '\n        <!-- EPISODES:END -->',
                s, count=1, flags=re.S)
    ld = '<script type="application/ld+json">' + json.dumps(schema(eps), ensure_ascii=False, separators=(',', ':')) + '</script>'
    s2 = re.sub(r'<!-- PODCAST_SCHEMA:START -->.*?<!-- PODCAST_SCHEMA:END -->',
                lambda m: '<!-- PODCAST_SCHEMA:START -->\n  ' + ld + '\n  <!-- PODCAST_SCHEMA:END -->',
                s2, count=1, flags=re.S)
    if s2 == s:
        print("Already current:", [e[1] for e in eps])
        return 0
    open(PAGE, 'w', encoding='utf-8').write(s2)
    print("Updated episodes + schema:", [e[1] for e in eps])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
