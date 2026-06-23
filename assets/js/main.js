// Lawn & Land Marketing v38 — Mega Menu + Premium Footer

// ─ REDUCED MOTION ─
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

// ─ CURSOR GLOW ─
const glow = document.getElementById('cursorGlow');
if (glow && !reduceMotion && window.matchMedia('(pointer:fine)').matches) {
  let gx = 0, gy = 0, gPending = false;
  document.addEventListener('mousemove', e => {
    gx = e.clientX; gy = e.clientY;
    if (!gPending) {
      gPending = true;
      requestAnimationFrame(() => {
        glow.style.left = gx + 'px';
        glow.style.top = gy + 'px';
        gPending = false;
      });
    }
  });
} else if (glow) { glow.style.display = 'none'; }

// ─ SCROLL REVEAL ─
const revealEls = document.querySelectorAll('[data-reveal]');
const revealObs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      const delay = e.target.dataset.delay || 0;
      setTimeout(() => e.target.classList.add('revealed'), parseInt(delay));
      revealObs.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });
revealEls.forEach(el => revealObs.observe(el));

// ─ COUNTER ANIMATION ─
function animateCount(el) {
  const decimals = parseInt(el.dataset.decimals) || 0;
  const target = parseFloat(el.dataset.count);
  const prefix = el.dataset.prefix || '';
  const suffix = el.dataset.suffix || '';
  const duration = 1800;
  const start = performance.now();
  const update = (now) => {
    const progress = Math.min((now - start) / duration, 1);
    const ease = 1 - Math.pow(1 - progress, 3);
    const raw = ease * target;
    const current = decimals ? raw.toFixed(decimals) : Math.round(raw);
    el.textContent = prefix + current + suffix;
    if (progress < 1) requestAnimationFrame(update);
  };
  requestAnimationFrame(update);
}
const counterObs = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting && e.target.dataset.count) {
      animateCount(e.target);
      counterObs.unobserve(e.target);
    }
  });
}, { threshold: 0.5 });
document.querySelectorAll('[data-count]').forEach(el => counterObs.observe(el));

// ─ WORD CYCLE (hero) — slide up/down transition ─
const cycleEl = document.getElementById('heroCycle');
if (cycleEl) {
  const words = ['Landscaping Companies.', 'Lawn Care Businesses.', 'The Green Industry.'];
  let idx = 0;

  // Set initial transition
  cycleEl.style.transition = 'opacity 0.45s ease, transform 0.45s ease';

  if (!reduceMotion) setInterval(() => {
    // Slide out current word upward
    cycleEl.style.opacity = '0';
    cycleEl.style.transform = 'translateY(-18px)';

    setTimeout(() => {
      // Swap word, reset below (no transition)
      cycleEl.style.transition = 'none';
      cycleEl.style.transform = 'translateY(18px)';
      idx = (idx + 1) % words.length;
      cycleEl.textContent = words[idx];

      // Force reflow, then slide in
      void cycleEl.offsetHeight;
      cycleEl.style.transition = 'opacity 0.45s ease, transform 0.45s ease';
      cycleEl.style.opacity = '1';
      cycleEl.style.transform = 'translateY(0)';
    }, 420);
  }, 3400);
}

// ─ VIDEO FACADE ─
const videoFacade = document.getElementById('videoFacade');
const heroIframe  = document.getElementById('heroIframe');
if (videoFacade && heroIframe) {
  videoFacade.addEventListener('click', () => {
    // Iframe ships with no src (data-src only) so the YouTube player isn't
    // downloaded on page load — set it on first click to start playback.
    if (!heroIframe.src) heroIframe.src = heroIframe.dataset.src + '&autoplay=1';
    heroIframe.closest('.hero-video-wrap').classList.add('playing');
    heroIframe.focus();
  });
}

// ─ MOBILE NAV ─
const navToggle = document.getElementById('navToggle');
const navMenu = document.getElementById('navMenu');
if (navToggle && navMenu) {
  navToggle.addEventListener('click', () => {
    const open = navMenu.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', open);
    navToggle.querySelectorAll('span')[0].style.transform = open ? 'rotate(45deg) translate(5px, 5px)' : '';
    navToggle.querySelectorAll('span')[1].style.opacity = open ? '0' : '1';
    navToggle.querySelectorAll('span')[2].style.transform = open ? 'rotate(-45deg) translate(5px,-5px)' : '';
  });
}

// ─ MEGA MENU — mobile click toggles ─
document.querySelectorAll('.nav-item.nav-mega > .nav-link').forEach(btn => {
  btn.addEventListener('click', (e) => {
    if (window.innerWidth <= 768) {
      // On mobile the parent row is an accordion toggle, not a link —
      // stop it from navigating to the hub so the submenu can expand.
      e.preventDefault();
      const item = btn.closest('.nav-item');
      // Close others
      document.querySelectorAll('.nav-item.nav-mega').forEach(i => {
        if (i !== item) i.classList.remove('open');
      });
      item.classList.toggle('open');
    }
  });
});

// Close mega panels on outside click
document.addEventListener('click', e => {
  if (!e.target.closest('.nav-mega')) {
    document.querySelectorAll('.nav-item.nav-mega').forEach(i => i.classList.remove('open'));
  }
});

// Legacy dropdown toggles (non-mega)
document.querySelectorAll('.nav-item.nav-dropdown > .nav-link').forEach(btn => {
  btn.addEventListener('click', (e) => {
    if (window.innerWidth <= 768) {
      e.preventDefault();
      btn.closest('.nav-item').classList.toggle('open');
    }
  });
});

// ─ SERVICES TABS ─
const tabs = document.querySelectorAll('.svc-tab');
const panels = document.querySelectorAll('.svc-panel');
tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    tabs.forEach(t => t.classList.remove('active'));
    panels.forEach(p => p.classList.remove('active'));
    tab.classList.add('active');
    const target = document.querySelector(`.svc-panel[data-panel="${tab.dataset.tab}"]`);
    if (target) target.classList.add('active');
  });
});

// ─ FAQ ACCORDION ─
document.querySelectorAll('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.faq-item');
    const isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(i => {
      i.classList.remove('open');
      i.querySelector('.faq-q').setAttribute('aria-expanded', 'false');
      const a = i.querySelector('.faq-a');
      if (a) a.hidden = true;
    });
    if (!isOpen) {
      item.classList.add('open');
      btn.setAttribute('aria-expanded', 'true');
      const a = item.querySelector('.faq-a');
      if (a) a.hidden = false;
    }
  });
});

// ─ INDUSTRY FAQ — exclusive <details> accordion (one open at a time) ─
document.querySelectorAll('.ind-faq').forEach(group => {
  const items = group.querySelectorAll(':scope > details');
  items.forEach(d => {
    d.addEventListener('toggle', () => {
      if (!d.open) return;
      items.forEach(other => { if (other !== d) other.open = false; });
    });
  });
});

// Testimonial video click-to-play
document.querySelectorAll('.testi-video-wrap').forEach(wrap => {
  wrap.addEventListener('click', () => {
    const videoId = wrap.dataset.videoid;
    if (!videoId || wrap.classList.contains('playing')) return;
    const iframe = document.createElement('iframe');
    iframe.src = `https://www.youtube.com/embed/${videoId}?autoplay=1&rel=0&playsinline=1`;
    iframe.allow = 'autoplay; encrypted-media';
    iframe.allowFullscreen = true;
    wrap.appendChild(iframe);
    wrap.classList.add('playing');
  });
});

// ─ WIDOW GUARD ─
// text-wrap:balance evens line WIDTHS, not word counts, so a heading can still
// strand a single word on its last line (hard <br> hooks, long compound words,
// or just certain viewport widths). This glues the final inter-word space of
// each <br>-delimited segment with a non-breaking space, so every heading's
// last line always carries 2+ words at any width. Skips nav/footer chrome, the
// animated hero H1, and any heading already hand-glued (contains a nbsp).
(function widowGuard() {
  const orig = new WeakMap();   // heading -> clean original innerHTML (pre-glue)
  const skip = new WeakSet();   // headings we never touch
  function glueSegment(nodes) {
    let full = '';
    const map = [];
    const collect = (n) => {
      if (n.nodeType === 3) {
        for (let k = 0; k < n.nodeValue.length; k++) map.push([n, k]);
        full += n.nodeValue;
      } else if (n.nodeType === 1) {
        const tw = document.createTreeWalker(n, NodeFilter.SHOW_TEXT);
        let x;
        while (x = tw.nextNode()) {
          for (let k = 0; k < x.nodeValue.length; k++) map.push([x, k]);
          full += x.nodeValue;
        }
      }
    };
    nodes.forEach(collect);
    let idx = -1;
    for (let i = 1; i < full.length - 1; i++) {
      if (full[i] === ' ' && /\S/.test(full[i - 1]) && /\S/.test(full[i + 1])) idx = i;
    }
    if (idx < 0) return;
    const [node, off] = map[idx];
    node.nodeValue = node.nodeValue.slice(0, off) + '\u00A0' + node.nodeValue.slice(off + 1);
  }
  function glue(h) {
    let seg = [];
    const segs = [seg];
    [].forEach.call(h.childNodes, (c) => {
      if (c.nodeType === 1 && c.tagName === 'BR') segs.push(seg = []);
      else seg.push(c);
    });
    segs.forEach(glueSegment);
  }
  function process(h) {
    if (skip.has(h)) return;
    if (orig.has(h)) {
      h.innerHTML = orig.get(h);                          // reset before re-gluing (resize re-runs)
    } else {
      if (h.closest('header,footer,nav') ||               // chrome
          h.querySelector('.hero-cycle') ||               // animated hero H1
          h.textContent.indexOf('\u00A0') !== -1) {       // already hand-glued
        skip.add(h); return;
      }
      orig.set(h, h.innerHTML);
    }
    glue(h);
    // SAFETY: if gluing pushed the heading's content past its box (an unbreakable
    // two-word unit wider than a narrow column), revert so it wraps naturally
    // instead of overflowing into neighbouring content.
    if (h.scrollWidth > h.clientWidth + 1) h.innerHTML = orig.get(h);
  }
  function run() { [].forEach.call(document.querySelectorAll('h1,h2,h3,h4'), process); }
  run();
  let rt;
  window.addEventListener('resize', () => { clearTimeout(rt); rt = setTimeout(run, 150); });
})();
