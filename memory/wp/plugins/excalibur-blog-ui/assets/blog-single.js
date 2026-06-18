(function () {
  'use strict';

  if (!document.body.classList.contains('excalibur-blog-single')) {
    return;
  }

  var progressRoot = document.querySelector('[data-reading-progress]');
  var progressFill = document.querySelector('[data-reading-progress-fill]');
  var floatingActions = document.querySelector('[data-floating-actions]');
  var entryContent = document.querySelector('.entry-content');
  var firstToc = entryContent ? entryContent.querySelector('ol:first-of-type') : null;

  if (firstToc && !firstToc.id) {
    firstToc.id = 'article-toc';
  }

  function updateReadingProgress() {
    if (!progressFill) {
      return;
    }
    var doc = document.documentElement;
    var scrollTop = doc.scrollTop || document.body.scrollTop;
    var height = (doc.scrollHeight || document.body.scrollHeight) - doc.clientHeight;
    var pct = height > 0 ? Math.min(100, (scrollTop / height) * 100) : 0;
    progressFill.style.width = pct + '%';
  }

  function toggleFloatingActions() {
    if (!floatingActions) {
      return;
    }
    var show = (window.scrollY || 0) > 480;
    floatingActions.hidden = !show;
    floatingActions.classList.toggle('is-visible', show);
  }

  function initReveal() {
    var items = document.querySelectorAll('.ebu-reveal-item');
    if (!items.length) {
      return;
    }

    if (!('IntersectionObserver' in window)) {
      items.forEach(function (el) {
        el.classList.add('ebu-active');
      });
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) {
            return;
          }
          entry.target.classList.add('ebu-active');
          observer.unobserve(entry.target);
        });
      },
      { threshold: 0.14, rootMargin: '0px 0px -8% 0px' }
    );

    items.forEach(function (el, index) {
      el.style.transitionDelay = Math.min(index * 70, 280) + 'ms';
      observer.observe(el);
    });
  }

  function initTocActive() {
    if (!firstToc) {
      return;
    }

    var links = firstToc.querySelectorAll('a[href^="#"]');
    if (!links.length) {
      return;
    }

    var sections = [];
    links.forEach(function (link) {
      var id = link.getAttribute('href').slice(1);
      var target = document.getElementById(id);
      if (target) {
        sections.push({ link: link, target: target });
      }
    });

    if (!sections.length) {
      return;
    }

    function setActive() {
      var scrollY = (window.scrollY || 0) + 140;
      var current = sections[0];
      sections.forEach(function (item) {
        if (item.target.offsetTop <= scrollY) {
          current = item;
        }
      });
      links.forEach(function (link) {
        link.classList.remove('is-active');
      });
      if (current && current.link) {
        current.link.classList.add('is-active');
      }
    }

    window.addEventListener('scroll', setActive, { passive: true });
    setActive();
  }

  function markFaqAnchor() {
    var headings = document.querySelectorAll('.entry-content h2');
    headings.forEach(function (heading) {
      var text = (heading.textContent || '').toLowerCase();
      if (text.indexOf('частые вопросы') !== -1 || text.indexOf('faq') !== -1) {
        if (!heading.id) {
          heading.id = 'faq';
        }
      }
    });
  }

  window.addEventListener('scroll', function () {
    updateReadingProgress();
    toggleFloatingActions();
  }, { passive: true });

  updateReadingProgress();
  toggleFloatingActions();
  initReveal();
  initTocActive();
  markFaqAnchor();
})();
