// ROLOBAND — public JS
document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.main-nav');

  // Header scroll efekti
  const onScroll = () => {
    if (window.scrollY > 30) header?.classList.add('scrolled');
    else header?.classList.remove('scrolled');
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobil menü
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

  // Hero video — bağlantı yavaşsa poster göster
  const heroVideo = document.querySelector('.hero-media video');
  if (heroVideo) {
    heroVideo.addEventListener('error', () => {
      heroVideo.style.display = 'none';
    });
  }

  // Sayım animasyonu (hero-stat .num)
  const counters = document.querySelectorAll('[data-count]');
  if (counters.length && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
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
