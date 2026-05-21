// ROLOBAND ? public JS
document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.menu-toggle');
  const nav    = document.querySelector('.main-nav');

  // Header scroll efekti
  const onScroll = () => {
    if (window.scrollY > 30) header?.classList.add('scrolled');
    else header?.classList.remove('scrolled');
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobil menu
  toggle?.addEventListener('click', () => nav?.classList.toggle('open'));

  // Aktif link
  const path = window.location.pathname;
  document.querySelectorAll('.main-nav a').forEach(a => {
    const href = a.getAttribute('href');
    if (!href) return;
    if (href === path || (href !== '/' && path.startsWith(href))) {
      a.classList.add('active');
    }
  });

  // Hero video ? hata durumunda gizle
  const heroVideo = document.querySelector('.hero-media video');
  if (heroVideo) {
    heroVideo.addEventListener('error', () => { heroVideo.style.display = 'none'; });
  }

  // bfcache: geri butonuyla donuste page-exit temizle
  window.addEventListener('pageshow', e => {
    if (e.persisted) {
      document.body.classList.remove('page-exit');
      document.body.classList.remove('intro-active');
    }
  });

  // Sayfa gecis animasyonu
  document.querySelectorAll('a[href]').forEach(link => {
    const href = link.getAttribute('href') || '';
    if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:') || link.target === '_blank') return;
    link.addEventListener('click', e => {
      const dest = link.href;
      if (!dest || !dest.startsWith(window.location.origin)) return;
      e.preventDefault();
      const destPath = new URL(dest).pathname;
      if (destPath === '/' || destPath === '') {
        sessionStorage.setItem('rb_skip_intro', '1');
      }
      document.body.classList.add('page-exit');
      setTimeout(() => { window.location.href = dest; }, 240);
    });
  });

  // Moduler Bant Grid Animasyonu
  const beltGrid = document.getElementById('beltGrid');
  if (beltGrid) {
    const section = beltGrid.closest('.belt-viz-section');
    const CELL = 30, GAP = 3, STEP = CELL + GAP;
    let cols = 0, rows = 0, cells = [], prevState = null, animFrame = null;

    function buildGrid() {
      if (animFrame) { cancelAnimationFrame(animFrame); animFrame = null; }
      beltGrid.innerHTML = '';
      cols = Math.ceil((section.offsetWidth || window.innerWidth) / STEP) + 1;
      rows = Math.ceil((section.offsetHeight || 420) / STEP) + 1;
      beltGrid.style.gridTemplateColumns = `repeat(${cols}, ${CELL}px)`;
      beltGrid.style.gridTemplateRows    = `repeat(${rows}, ${CELL}px)`;
      for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
          const el = document.createElement('div');
          el.className = 'belt-cell';
          el.dataset.col = c; el.dataset.row = r;
          beltGrid.appendChild(el);
        }
      }
      cells = Array.from(beltGrid.children);
      prevState = new Uint8Array(cells.length);
    }
    buildGrid();

    function wave() {
      const t = Date.now() / 1100;
      cells.forEach((cell, idx) => {
        const c = +cell.dataset.col, r = +cell.dataset.row;
        const h = 0.42
          + 0.32 * Math.sin(t * 1.3  + c * 0.38)
          + 0.14 * Math.sin(t * 0.75 - c * 0.52);
        const lit = (rows - 1 - r) < Math.round(h * rows) ? 1 : 0;
        if (lit !== prevState[idx]) {
          prevState[idx] = lit;
          cell.classList.toggle('lit', !!lit);
        }
        const edgeRow = rows - 1 - Math.round(h * rows);
        if (r === edgeRow && lit) {
          cell.classList.add('pulse');
          setTimeout(() => cell.classList.remove('pulse'), 280);
        }
      });
      animFrame = requestAnimationFrame(wave);
    }

    const beltIO = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting && !animFrame) {
        animFrame = requestAnimationFrame(wave);
      } else if (!entry.isIntersecting && animFrame) {
        cancelAnimationFrame(animFrame); animFrame = null;
      }
    }, { threshold: 0.1 });
    beltIO.observe(section);

    let resizeTimer = null;
    window.addEventListener('resize', () => {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(() => {
        buildGrid();
        const rect = section.getBoundingClientRect();
        if (rect.bottom > 0 && rect.top < window.innerHeight && !animFrame) {
          animFrame = requestAnimationFrame(wave);
        }
      }, 150);
    }, { passive: true });
  }

  // ?? Scroll reveal animasyonu ??
  // Icerik her zaman gorunur. Viewport'a girerken rb-animate sinifi eklenir,
  // bu sinif CSS keyframe animasyonu tetikler (opacity 0?1, translateY).
  document.querySelectorAll(
    '.section-heading, .b2b-value-inner, .cta-banner, .cert-items, .page-header .container, .kvkk-header'
  ).forEach(el => { if (!el.dataset.reveal) el.dataset.reveal = ''; });

  document.querySelectorAll(
    '.product-grid, .categories-grid, .compare-grid, .industry-grid, .footer-grid, .b2b-sectors, .cert-cards, .cert-strip .cert-items'
  ).forEach(el => { if (!el.dataset.stagger) el.dataset.stagger = ''; });

  const revealEls = Array.from(document.querySelectorAll('[data-reveal], [data-stagger]'));

  function triggerAnimate(el) {
    if (el.dataset.rbDone) return;
    el.dataset.rbDone = '1';
    el.classList.add('rb-animate');
  }

  function isInView(el) {
    const r = el.getBoundingClientRect();
    return r.top < window.innerHeight + 80 && r.bottom > 0;
  }

  // Sayfa yuklendiginde viewport icindeki elemanlari hemen animasyon olmadan goster
  // (hero bolumunun altindaki ilk bolumler dahil)
  revealEls.forEach(el => {
    if (isInView(el)) triggerAnimate(el);
  });

  // Scroll ile gelen elemanlar
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      revealEls.forEach(el => { if (isInView(el)) triggerAnimate(el); });
      ticking = false;
    });
  }, { passive: true });

  // IntersectionObserver (ek guvenlik)
  if ('IntersectionObserver' in window) {
    const revealIO = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) triggerAnimate(e.target); });
    }, { threshold: 0.05, rootMargin: '0px 0px 80px 0px' });
    revealEls.forEach(el => revealIO.observe(el));
  }

  // ?? Sayim animasyonu (hero-stat) ??
  const counters = document.querySelectorAll('[data-count]');
  if (counters.length && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        const el = e.target;
        const target = parseInt(el.dataset.count, 10) || 0;
        const suffix = el.dataset.suffix || '';
        let cur = 0;
        const step = Math.max(1, Math.ceil(target / 60));
        const tick = () => {
          cur += step;
          if (cur >= target) { el.textContent = target + suffix; return; }
          el.textContent = cur + suffix;
          requestAnimationFrame(tick);
        };
        tick();
        io.unobserve(el);
      });
    }, { threshold: 0.5 });
    counters.forEach(c => io.observe(c));
  }
});
