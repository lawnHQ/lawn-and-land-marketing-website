/* Free Google Maps heatmap: form (/tools/google-maps-heatmap/) and results
   (/tools/google-maps-heatmap/results/). The scan itself runs on the
   ll-heatmap service; this file only talks to its three endpoints. */
(function () {
  'use strict';

  var script = document.currentScript;
  var API = (script && script.getAttribute('data-api')) || 'https://ll-heatmap.vercel.app';
  // Local testing only: ?api=http://localhost:3107
  try {
    var qa = new URLSearchParams(location.search).get('api');
    if (qa && /^http:\/\/(localhost|127\.0\.0\.1):\d+$/.test(qa) && /^(localhost|127\.0\.0\.1)$/.test(location.hostname)) API = qa;
  } catch (e) {}

  var RESULTS_PATH = '/tools/google-maps-heatmap/results/';

  function $(id) { return document.getElementById(id); }
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function post(path, body) {
    return fetch(API + path, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) })
      .then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, status: r.status, body: j }; }); });
  }
  function track(name, params) {
    try { if (window.gtag) gtag('event', name, params || {}); } catch (e) {}
  }

  /* ─────────────────────────── FORM PAGE ─────────────────────────── */
  var form = $('hmForm');
  if (form) {
    var selected = null;
    var findBtn = $('hmFind'), list = $('hmListings'), findMsg = $('hmFindMsg');
    var step2 = $('hmStep2'), step3 = $('hmStep3');
    var trade = form.elements.trade, keyword = form.elements.keyword;
    var keywordTouched = false;

    function setMsg(el, text, kind) {
      if (!text) { el.hidden = true; el.textContent = ''; return; }
      el.hidden = false; el.className = 'hm-msg hm-msg--' + (kind || 'err'); el.textContent = text;
    }
    function enable(step, on) { step.setAttribute('aria-disabled', on ? 'false' : 'true'); }

    trade.addEventListener('change', function () {
      var opt = trade.options[trade.selectedIndex];
      var kw = opt && opt.getAttribute('data-keyword');
      if (kw && (!keywordTouched || !keyword.value.trim())) keyword.value = kw;
      if (!kw && !keywordTouched) keyword.value = '';
    });
    keyword.addEventListener('input', function () { keywordTouched = true; });

    function pick(listing, btn) {
      selected = listing;
      Array.prototype.forEach.call(list.querySelectorAll('.hm-listing'), function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
      enable(step2, true); enable(step3, true);
      if (!form.elements.business.value) form.elements.business.value = listing.title;
    }

    function find() {
      var name = form.elements.bizname.value.trim(), city = form.elements.city.value.trim();
      if (name.length < 3) { setMsg(findMsg, 'Enter your business name as it shows on Google.'); return; }
      setMsg(findMsg, ''); findBtn.disabled = true; findBtn.textContent = 'Searching Google Maps...';
      list.innerHTML = ''; selected = null; enable(step2, false); enable(step3, false);
      post('/api/lookup', { name: name, city: city }).then(function (r) {
        findBtn.disabled = false; findBtn.textContent = 'Find my listing';
        if (!r.ok) { setMsg(findMsg, r.body.error || 'Search is unavailable right now. Please try again.'); return; }
        var items = r.body.listings || [];
        if (!items.length) { setMsg(findMsg, 'No listings found. Try the exact name from Google Maps, and add your city and state.', 'info'); return; }
        track('heatmap_lookup', { results: items.length });
        items.forEach(function (l) {
          var b = document.createElement('button');
          b.type = 'button'; b.className = 'hm-listing'; b.setAttribute('aria-pressed', 'false');
          var where = l.address ? esc(l.address) : 'Service-area business (address hidden on Google)';
          var rating = l.rating ? ' &middot; ' + esc(l.rating) + '&#9733; (' + esc(l.reviews) + ' reviews)' : '';
          b.innerHTML = '<svg viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>' +
            '<span>' + esc(l.title) + '<small>' + where + rating + '</small></span>';
          b.addEventListener('click', function () { pick(l, b); });
          list.appendChild(b);
        });
        if (items.length === 1) pick(items[0], list.firstChild);
        else setMsg(findMsg, 'Pick your listing below.', 'info');
      }).catch(function () {
        findBtn.disabled = false; findBtn.textContent = 'Find my listing';
        setMsg(findMsg, 'Search is unavailable right now. Please try again.');
      });
    }
    findBtn.addEventListener('click', find);
    [form.elements.bizname, form.elements.city].forEach(function (el) {
      el.addEventListener('keydown', function (e) { if (e.key === 'Enter') { e.preventDefault(); find(); } });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var msg = $('hmSubmitMsg'), btn = $('hmSubmit');
      if (!selected) { setMsg(msg, 'Find and select your Google Business Profile first.'); return; }
      if (!form.elements.consent.checked) { setMsg(msg, 'Please check the box so we can send you your results.'); return; }
      var data = {
        name: form.elements.name.value, email: form.elements.email.value, phone: form.elements.phone.value,
        business: form.elements.business.value || selected.title, website: form.elements.website.value,
        revenueBand: form.elements.revenueBand.value, trade: form.elements.trade.value, keyword: form.elements.keyword.value,
        listing: selected, company_url: form.elements.company_url.value, consent: true
      };
      setMsg(msg, ''); btn.disabled = true; btn.textContent = 'Starting your scan...';
      post('/api/scan', data).then(function (r) {
        if (!r.ok || !r.body.token) {
          btn.disabled = false; btn.textContent = 'Run my free scan';
          setMsg(msg, (r.body && r.body.error) || 'We could not start your scan. Please try again.');
          if (r.body && r.body.field && form.elements[r.body.field]) form.elements[r.body.field].focus();
          return;
        }
        // Team demo scans (our own domain) never count as ad conversions.
        var internal = /@lawnandlandmarketing\.com\s*$/i.test(data.email || '');
        if (!r.body.reused && !internal) {
          track('generate_lead', { lead_source: 'google_maps_heatmap' });
          try { if (window.fbq) fbq('track', 'Lead', { content_name: 'Google Maps Heatmap' }); } catch (err) {}
        }
        location.href = RESULTS_PATH + '?t=' + encodeURIComponent(r.body.token) + (r.body.reused ? '&seen=1' : '') + (API !== 'https://ll-heatmap.vercel.app' && /localhost|127\.0\.0\.1/.test(API) ? '&api=' + encodeURIComponent(API) : '');
      }).catch(function () {
        btn.disabled = false; btn.textContent = 'Run my free scan';
        setMsg(msg, 'We could not reach the scan service. Please try again.');
      });
    });
  }

  /* ─────────────────────────── RESULTS PAGE ─────────────────────────── */
  var mapEl = $('hrMap');
  if (mapEl) {
    var token = new URLSearchParams(location.search).get('t') || '';
    var overlay = $('hrOverlay'), bar = $('hrBar');
    var COLORS = { top3: '#5DCA49', mid: '#E8C33A', low: '#F08A3C', none: '#E54834' };
    function colorFor(rank) { return rank == null ? COLORS.none : rank <= 3 ? COLORS.top3 : rank <= 10 ? COLORS.mid : COLORS.low; }

    function showOverlay(title, text, progress) {
      overlay.hidden = false;
      overlay.innerHTML = '<div><h2>' + esc(title) + '</h2><p>' + text + '</p>' +
        (progress != null ? '<div class="hr-bar"><i id="hrBar" style="width:' + progress + '%"></i></div>' : '') + '</div>';
    }

    if (!/^[a-f0-9]{36}$/.test(token)) {
      showOverlay('We could not find that scan', 'Check the link in your email, or <a href="/tools/google-maps-heatmap/" style="color:var(--lime)">run a new free scan</a>.');
      return;
    }

    var map = null, rendered = false, tries = 0;

    function milesBetween(a, b) {
      var R = 3958.8, t = Math.PI / 180;
      var dLat = (b.lat - a.lat) * t, dLng = (b.lng - a.lng) * t;
      var h = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.cos(a.lat * t) * Math.cos(b.lat * t) * Math.sin(dLng / 2) * Math.sin(dLng / 2);
      return 2 * R * Math.asin(Math.sqrt(h));
    }

    function reading(d) {
      var s = d.summary, pts = d.points || [], c = { lat: d.business.lat, lng: d.business.lng };
      var near = pts.filter(function (p) { return milesBetween(c, p) <= d.grid.radiusMi / 2; });
      var far = pts.filter(function (p) { return milesBetween(c, p) > d.grid.radiusMi * 0.75; });
      function share(arr) { return arr.length ? Math.round(arr.filter(function (p) { return p.rank != null && p.rank <= 3; }).length / arr.length * 100) : 0; }
      var nearShare = share(near), farShare = share(far);
      var html = '';
      if (s.top3Points === 0 && s.foundPoints === 0) {
        html += '<p>Your listing did not show up in the top 20 anywhere we searched for &ldquo;' + esc(d.keyword) + '.&rdquo; For this search, homeowners in this area are not seeing you on Google Maps at all.</p>' +
          '<p>That usually points to a profile problem (wrong primary category, a listing Google does not connect to this service, or a new or suspended profile) more than a distance problem. It is fixable, and worth a closer look.</p>';
      } else if (s.top3Points === 0) {
        html += '<p>You show up in ' + s.foundShare + '% of the area, but never in the top 3. Most calls from Google Maps go to the first three listings, so right now those calls are going to someone else.</p>';
      } else if (s.top3Share >= 60) {
        html += '<p>You hold the top 3 across most of this map. The job now is protecting it and pushing into the spots where you slip.</p>';
      } else if (s.top3Share < 15) {
        html += '<p>You make the top 3 in only ' + s.top3Points + ' of ' + s.points + ' spots' +
          (nearShare > farShare ? ', all close to your listing' : '') + '. Across most of this area, homeowners searching &ldquo;' + esc(d.keyword) +
          '&rdquo; see three other companies before they see you.</p>';
      } else {
        html += '<p>You are in the top 3 in ' + s.top3Share + '% of the spots we searched. ';
        html += nearShare > farShare + 15
          ? 'That share is ' + nearShare + '% within ' + Math.round(d.grid.radiusMi / 2) + ' miles of your listing and ' + farShare + '% toward the edges, the classic pattern of a profile that wins close to home and fades with distance.</p>'
          : 'The weak spots are not just the far edges, which usually means competitors have stronger signals (reviews, categories, local pages) in those parts of town.</p>';
      }
      var mid = (d.grid.size - 1) / 2;
      var here = pts.filter(function (p) { return p.row === mid && p.col === mid; })[0];
      if (!d.business.address && here && (here.rank == null || here.rank > 3)) {
        html += '<p>Your listing hides its street address. Google generally ranks a service-area business from its verified (hidden) address, not from the pin it shows on the map, so your strongest spots may sit away from the center of this grid.</p>';
      }
      var comps = d.competitors || [];
      if (comps.length && d.business.reviews != null) {
        var avg = Math.round(comps.slice(0, 3).reduce(function (a, x) { return a + (x.reviews || 0); }, 0) / Math.min(3, comps.length));
        html += '<p>The three listings that hold the top 3 most often average ' + avg + ' Google reviews. Your listing has ' + esc(d.business.reviews) + '.</p>';
      }
      return html;
    }

    function render(d) {
      rendered = true;
      overlay.hidden = true;
      var s = d.summary;
      $('hrStats').innerHTML =
        '<div class="hr-stat hr-stat--lead"><b>' + s.top3Share + '%</b><span>Top 3 share: in the top 3 at ' + s.top3Points + ' of ' + s.points + ' spots</span></div>' +
        '<div class="hr-stat"><b>' + s.foundShare + '%</b><span>Shows up at all (top 20)</span></div>' +
        '<div class="hr-stat"><b>' + (s.avgRank != null ? s.avgRank : '&ndash;') + '</b><span>Average rank where you show up</span></div>' +
        (d.previous ? (function (p) {
          var diff = Math.round((s.top3Share - p.top3Share) * 10) / 10;
          return '<div class="hr-stat hr-stat--lead"><b>' + (diff === 0 ? 'No change' : (diff > 0 ? '+' : '') + diff + ' pts') + '</b><span>Top 3 share since your last scan on ' + esc(shortDate(p.date)) +
            ' (' + p.top3Share + '%' + (p.keyword !== d.keyword ? ', for &ldquo;' + esc(p.keyword) + '&rdquo;' : '') + ')</span></div>';
        })(d.previous) : '') +
        '<div class="hr-next">Your next free scan unlocks <b>' + esc(longDate(d.nextScanAt)) + '</b>. Come back then to see what changed.</div>';
      $('hrReading').innerHTML = reading(d);
      var comps = d.competitors || [];
      $('hrComp').innerHTML = comps.length ? comps.map(function (c) {
        return '<li><span class="n">' + esc(c.title) + '</span><span class="m">' + esc(c.category || '') +
          (c.rating ? ' &middot; ' + esc(c.rating) + '&#9733; (' + esc(c.reviews) + ')' : '') + '</span><span class="s">' + c.top3Share + '%</span></li>';
      }).join('') + '<li><span class="n hr-you">' + esc(d.business.title) + ' (you)</span><span class="m">' +
        (d.business.rating ? esc(d.business.rating) + '&#9733; (' + esc(d.business.reviews) + ')' : '') + '</span><span class="s hr-you">' + s.top3Share + '%</span></li>'
        : '<li><span class="n">No clear competitor holds this map.</span></li>';
      $('hrResults').hidden = false;

      var features = (d.points || []).map(function (p) {
        return { type: 'Feature', geometry: { type: 'Point', coordinates: [p.lng, p.lat] },
          properties: { rank: p.rank, label: p.rank == null ? '20+' : String(p.rank), color: colorFor(p.rank), top3: (p.top3 || []).join('|') } };
      });
      function draw() {
        map.addSource('pts', { type: 'geojson', data: { type: 'FeatureCollection', features: features } });
        map.addLayer({ id: 'pts-c', type: 'circle', source: 'pts', paint: {
          'circle-radius': ['interpolate', ['linear'], ['zoom'], 8, 12, 10, 17, 12, 22, 14, 26],
          'circle-color': ['get', 'color'], 'circle-opacity': 0.92, 'circle-stroke-width': 2, 'circle-stroke-color': 'rgba(7,16,10,0.85)' } });
        map.addLayer({ id: 'pts-l', type: 'symbol', source: 'pts', layout: {
          'text-field': ['get', 'label'], 'text-font': ['Noto Sans Bold'], 'text-size': ['interpolate', ['linear'], ['zoom'], 8, 11, 10, 13, 12, 15, 14, 17],
          'text-allow-overlap': true }, paint: { 'text-color': '#07100a' } });
        map.on('click', 'pts-c', function (e) {
          var p = e.features[0].properties;
          var who = p.top3 ? p.top3.split('|').filter(Boolean) : [];
          new maplibregl.Popup({ offset: 12 }).setLngLat(e.lngLat).setHTML(
            (p.rank === null || p.rank === undefined || p.rank === 'null' ? '<b>Not in the top 20</b> here' : 'You rank <b>#' + esc(p.label) + '</b> here') +
            (who.length ? '<br><span style="color:rgba(255,255,255,.65)">Top 3 here:</span><br>' + who.map(function (w, i) { return (i + 1) + '. ' + esc(w); }).join('<br>') : '')
          ).addTo(map);
        });
        map.on('mouseenter', 'pts-c', function () { map.getCanvas().style.cursor = 'pointer'; });
        map.on('mouseleave', 'pts-c', function () { map.getCanvas().style.cursor = ''; });
        var el = document.createElement('div'); el.className = 'hr-pin'; el.title = d.business.title;
        new maplibregl.Marker({ element: el }).setLngLat([d.business.lng, d.business.lat]).addTo(map);
        var b = new maplibregl.LngLatBounds();
        features.forEach(function (f) { b.extend(f.geometry.coordinates); });
        map.__fit = b;
        map.resize();
        map.fitBounds(b, { padding: 28, duration: 0 });
      }
      if (map.__ready) draw(); else (map.__queue = map.__queue || []).push(draw);
    }

    function longDate(iso) { return new Date(iso).toLocaleDateString(undefined, { weekday: 'long', month: 'long', day: 'numeric' }); }
    function shortDate(iso) { return new Date(iso).toLocaleDateString(undefined, { month: 'short', day: 'numeric' }); }

    function notice(d) {
      if (new URLSearchParams(location.search).get('seen') !== '1') return;
      var el = $('hrNotice');
      el.innerHTML = '<b>This business was already scanned on ' + esc(shortDate(d.createdAt)) + '.</b> Free scans refresh once a week per business, so here is that map' +
        (d.keyword ? ' for &ldquo;' + esc(d.keyword) + '&rdquo;' : '') + '. <b>Your next fresh scan unlocks ' + esc(longDate(d.nextScanAt)) + '.</b> Want every service you sell scanned now? <a href="/get-started/book-strategy-call/">Book a free strategy call</a>.';
      el.hidden = false;
    }

    function head(d) {
      $('hrTitle').textContent = d.business.title;
      var when = new Date(d.completedAt || d.createdAt);
      $('hrMeta').innerHTML = '&ldquo;' + esc(d.keyword) + '&rdquo; &middot; ' + d.grid.points + ' spots, ' + d.grid.size + '&times;' + d.grid.size +
        ' grid, ' + d.grid.radiusMi + ' miles out, about ' + d.grid.spacingMi + ' miles apart &middot; ' + when.toLocaleDateString(undefined, { month: 'long', day: 'numeric', year: 'numeric' });
    }

    function poll() {
      fetch(API + '/api/scan/' + token).then(function (r) { return r.json().then(function (j) { return { ok: r.ok, status: r.status, body: j }; }); })
        .then(function (r) {
          if (r.status === 404) { showOverlay('We could not find that scan', 'Check the link in your email, or <a href="/tools/google-maps-heatmap/" style="color:var(--lime)">run a new free scan</a>.'); return; }
          if (!r.ok) throw new Error('bad');
          var d = r.body;
          head(d);
          notice(d);
          if (!map) {
            map = new maplibregl.Map({ container: 'hrMap', style: 'https://tiles.openfreemap.org/styles/dark', center: [d.business.lng, d.business.lat], zoom: 10, attributionControl: { compact: true }, cooperativeGestures: true });
            map.addControl(new maplibregl.NavigationControl({ showCompass: false }), 'top-right');
            // map.loaded() is false while tiles stream in, even after 'load' has fired, so
            // waiting on it can miss the event entirely. Track readiness ourselves.
            map.on('load', function () { map.__ready = true; (map.__queue || []).forEach(function (fn) { fn(); }); map.__queue = []; });
            // Keep the map fitted to the grid when the container changes size (phone rotation, layout shift).
            if (window.ResizeObserver) new ResizeObserver(function () { map.resize(); if (map.__fit) map.fitBounds(map.__fit, { padding: 28, duration: 0 }); }).observe(mapEl);
            // Start with the attribution collapsed to its (i) button so it never covers the grid.
            map.once('load', function () { var a = mapEl.querySelector('.maplibregl-ctrl-attrib'); if (a) a.classList.remove('maplibregl-compact-show'); });
          }
          if (d.status === 'completed') { render(d); return; }
          if (d.status === 'failed') {
            showOverlay('Your scan hit a snag', 'Google did not answer enough of our searches this time. Our team has been notified and will run your scan by hand and email you the map.');
            return;
          }
          var pct = Math.round((d.progress || 0) / d.grid.points * 100);
          showOverlay('Scanning Google Maps...', 'Searching &ldquo;' + esc(d.keyword) + '&rdquo; from ' + (d.progress || 0) + ' of ' + d.grid.points + ' spots. This usually takes under a minute, and we will email you the link too.', pct);
          if (++tries < 150) setTimeout(poll, 2500);
        })
        .catch(function () { if (++tries < 150) setTimeout(poll, 4000); });
    }
    showOverlay('Loading your map...', '', 0);
    poll();
  }
})();
