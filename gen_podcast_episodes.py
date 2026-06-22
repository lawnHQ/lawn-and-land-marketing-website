#!/usr/bin/env python3
"""Keep the Mow Money, Mow Problems podcast page showing the latest 6 episodes.

Fetches the YouTube channel RSS feed, takes the 6 newest uploads, and rewrites the
episode cards between the <!-- EPISODES:START --> / <!-- EPISODES:END --> markers on
resources/mow-money-mow-problems-podcast/index.html. New episodes appear automatically
and older ones drop off. Idempotent: if the latest 6 already match, nothing changes.

Run by .github/workflows/podcast-episodes.yml on a daily schedule. Card markup mirrors
the format the page was built with, so a re-run is a no-op until a new episode publishes.
"""
import re, os, html, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGE = os.path.join(ROOT, 'resources', 'mow-money-mow-problems-podcast', 'index.html')
CHANNEL_ID = 'UCDquVUlNKHjfFSA8C239qIw'
FEED = f'https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}'
N = 6


def esc(t):
    return t.replace('&', '&amp;')


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; LawnLandBot/1.0)'})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode('utf-8')


def latest_episodes(xml, n=N):
    eps = []
    for e in re.findall(r'<entry>(.*?)</entry>', xml, re.S):
        vid = re.search(r'<yt:videoId>([^<]+)</yt:videoId>', e)
        title = re.search(r'<title>([^<]+)</title>', e)
        if not vid or not title:
            continue
        t = html.unescape(title.group(1)).strip()
        # "Ep. 18 - John and Julia Brown - Lawn and Land Services - The Mow Money, Mow Problems Podcast"
        parts = [p.strip() for p in t.split(' - ')]
        m = re.search(r'(\d+)', parts[0]) if parts else None
        num = m.group(1) if m else ''
        guest = parts[1] if len(parts) > 1 else t
        company = parts[2] if len(parts) > 2 else ''
        eps.append((vid.group(1), num, guest, company))
        if len(eps) >= n:
            break
    return eps


def card(vid, num, guest, co):
    g, c = esc(guest), esc(co)
    return (
        f'        <div class="pod-ep">\n'
        f'          <div class="pod-video" data-vid="{vid}">\n'
        f'            <img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="Episode {num}: {g}, {c}" loading="lazy">\n'
        f'            <button class="pod-play" aria-label="Play episode {num}"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg></button>\n'
        f'          </div>\n'
        f'          <div class="pod-ep-body">\n'
        f'            <span class="pod-ep-badge">Episode {num}</span>\n'
        f'            <h3 class="pod-ep-title">{g}</h3>\n'
        f'            <div class="pod-ep-co">{c}</div>\n'
        f'          </div>\n'
        f'        </div>'
    )


def main():
    eps = latest_episodes(fetch(FEED))
    if not eps:
        print("No episodes parsed from RSS; leaving the page unchanged.")
        return 0
    cards = '\n'.join(card(*e) for e in eps)
    block = '<!-- EPISODES:START -->\n' + cards + '\n        <!-- EPISODES:END -->'
    s = open(PAGE, encoding='utf-8').read()
    new = re.sub(r'<!-- EPISODES:START -->.*?<!-- EPISODES:END -->', lambda m: block, s, count=1, flags=re.S)
    if new == s:
        print("Episodes already current:", [e[1] for e in eps])
        return 0
    open(PAGE, 'w', encoding='utf-8').write(new)
    print("Updated to latest episodes:", [e[1] for e in eps])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
