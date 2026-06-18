/**
 * Excalibur Blog UI — AI Dev Editorial Interface
 * DOM enhancements for single post pages.
 */
(function () {
  'use strict';

  var body = document.body;
  if (!body.classList.contains('excalibur-blog-single')) {
    return;
  }

  var CARD_META = {
    info: { icon: 'i', label: 'Overview' },
    workflow: { icon: '→', label: 'Workflow' },
    expert: { icon: '◆', label: 'Expert note' },
    warn: { icon: '!', label: 'Важно' },
  };

  /* ── Article meta from PHP ─────────────────────────────────── */
  function initArticleMeta() {
    var data = window.ebuArticle;
    if (!data || !data.readingTime) return;

    var meta = document.querySelector('.entry-meta');
    if (meta && !meta.querySelector('.ebu-reading-time')) {
      var span = document.createElement('span');
      span.className = 'ebu-reading-time';
      span.textContent = ' · ' + data.readingTime + ' чтения';
      meta.appendChild(span);
    }
  }

  /* ── Structure: title → TOC → cover → content ─────────────── */
  function reorderArticleStructure() {
    var content = document.querySelector('.entry-content');
    if (!content) return;

    var toc = null;
    content.querySelectorAll(':scope > ol').forEach(function (ol) {
      if (!toc && ol.querySelector('a[href^="#"]')) {
        toc = ol;
      }
    });

    if (toc) {
      toc.classList.add('ebu-article-toc');
      if (!toc.id) {
        toc.id = 'article-toc';
      }
      if (content.firstElementChild !== toc) {
        content.insertBefore(toc, content.firstElementChild);
      }
    }

    var thumb =
      document.querySelector('.entry-hero .post-thumbnail') ||
      document.querySelector('.post-thumbnail.article-post-thumbnail') ||
      document.querySelector('.post-thumbnail');

    if (!thumb || thumb.closest('.ebu-featured-media')) {
      return;
    }

    var slot = document.createElement('div');
    slot.className = 'ebu-featured-media';
    thumb.parentNode.removeChild(thumb);
    slot.appendChild(thumb);

    if (toc) {
      toc.parentNode.insertBefore(slot, toc.nextSibling);
    } else {
      content.insertBefore(slot, content.firstElementChild);
    }

    var hero = document.querySelector('.entry-hero.post-hero-section');
    if (hero && !hero.querySelector('img, .post-thumbnail')) {
      hero.style.display = 'none';
    }
  }

  /* ── Reading progress ─────────────────────────────────────── */
  function initReadingProgress() {
    var bar = document.querySelector('.reading-progress [data-reading-progress-fill]');
    if (!bar) return;

    function update() {
      var scrollTop = window.scrollY || document.documentElement.scrollTop;
      var docHeight = document.documentElement.scrollHeight - window.innerHeight;
      var pct = docHeight > 0 ? Math.min(100, (scrollTop / docHeight) * 100) : 0;
      bar.style.width = pct + '%';
    }

    window.addEventListener('scroll', update, { passive: true });
    update();
  }

  /* ── Inline TOC active state ──────────────────────────────── */
  function initInlineToc() {
    var content = document.querySelector('.entry-content');
    if (!content) return;

    var toc = content.querySelector(':scope > ol.ebu-article-toc, :scope > ol:first-of-type');
    if (!toc) return;

    var links = toc.querySelectorAll('a[href^="#"]');
    var sections = [];

    links.forEach(function (a) {
      var id = a.getAttribute('href').slice(1);
      var el = document.getElementById(id);
      if (el) sections.push({ link: a, el: el });
    });

    if (!sections.length || !window.IntersectionObserver) return;

    var activeId = '';
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            activeId = entry.target.id;
          }
        });
        if (!activeId) return;
        sections.forEach(function (s) {
          s.link.classList.toggle('is-active', s.el.id === activeId);
        });
      },
      { rootMargin: '-20% 0px -65% 0px', threshold: 0 }
    );

    sections.forEach(function (s) {
      observer.observe(s.el);
    });
  }

  /* ── Section markers on H2 ──────────────────────────────── */
  function initSectionMarkers() {
    var content = document.querySelector('.entry-content');
    if (!content) return;

    var h2s = content.querySelectorAll(':scope > h2[id]');
    var index = 0;

    h2s.forEach(function (h2) {
      if (h2.id === 'faq') return;
      index += 1;
      var marker = document.createElement('span');
      marker.className = 'ebu-section-marker';
      marker.setAttribute('aria-hidden', 'true');
      marker.textContent = String(index).padStart(2, '0');
      h2.insertBefore(marker, h2.firstChild);
    });
  }

  /* ── Blockquote → cards ───────────────────────────────────── */
  function classifyBlockquote(bq) {
    var text = (bq.textContent || '').toLowerCase();
    var html = bq.innerHTML;

    if (html.indexOf('<pre') !== -1 || html.indexOf('<code') !== -1) {
      return 'code';
    }
    if (text.indexOf('tldr') !== -1 || text.indexOf('tl;dr') !== -1) {
      return 'info';
    }
    if (text.indexOf('workflow') !== -1 || text.indexOf('→') !== -1 || text.indexOf('схема') !== -1) {
      return 'workflow';
    }
    if (text.indexOf('ошибк') !== -1 || text.indexOf('не работает') !== -1 || text.indexOf('проверьте') !== -1) {
      return 'warn';
    }
    if (text.indexOf('эксперт') !== -1 || text.indexOf('совет') !== -1 || text.indexOf('важно') !== -1) {
      return 'expert';
    }
    return 'info';
  }

  function enhanceCard(card, kind) {
    var bq = card.querySelector('blockquote');
    if (!bq) return;

    var meta = CARD_META[kind] || CARD_META.info;
    var head = document.createElement('div');
    head.className = 'ebu-card__head';
    head.innerHTML =
      '<span class="ebu-card__icon" aria-hidden="true">' + meta.icon + '</span>' +
      '<span>' + meta.label + '</span>';

    var bodyEl = document.createElement('div');
    bodyEl.className = 'ebu-card__body';
    bodyEl.appendChild(bq);

    card.appendChild(head);
    card.appendChild(bodyEl);
  }

  function wrapBlockquotes() {
    var content = document.querySelector('.entry-content');
    if (!content) return;

    content.querySelectorAll(':scope > blockquote').forEach(function (bq) {
      var kind = classifyBlockquote(bq);
      if (kind === 'code') {
        convertCodeBlockquote(bq);
        return;
      }

      var card = document.createElement('div');
      card.className = 'ebu-card ebu-card--' + kind;
      bq.parentNode.insertBefore(card, bq);
      card.appendChild(bq);
      enhanceCard(card, kind);
    });
  }

  function convertCodeBlockquote(bq) {
    var pre = bq.querySelector('pre');
    if (!pre) return;

    var code = pre.querySelector('code') || pre;
    var label = 'terminal';
    var text = code.textContent || '';

    if (text.indexOf('{') !== -1 && text.indexOf('}') !== -1) {
      label = 'config.json';
    } else if (text.indexOf('curl') !== -1 || text.indexOf('npm') !== -1) {
      label = 'terminal';
    }

    var win = document.createElement('div');
    win.className = 'ebu-code-window';
    win.innerHTML =
      '<div class="ebu-code-window__bar">' +
      '<span class="ebu-code-window__label">' + label + '</span>' +
      '<button type="button" class="ebu-code-copy" data-ebu-copy>Copy</button>' +
      '</div>';

    var bodyEl = document.createElement('div');
    bodyEl.className = 'ebu-code-window__body';
    var newPre = document.createElement('pre');
    var newCode = document.createElement('code');
    newCode.textContent = code.textContent;
    newPre.appendChild(newCode);
    bodyEl.appendChild(newPre);
    win.appendChild(bodyEl);

    bq.parentNode.insertBefore(win, bq);
    bq.remove();
  }

  function wrapPreBlocks() {
    var content = document.querySelector('.entry-content');
    if (!content) return;

    content.querySelectorAll(':scope > pre').forEach(function (pre) {
      if (pre.closest('.ebu-code-window')) return;

      var win = document.createElement('div');
      win.className = 'ebu-code-window';
      win.innerHTML =
        '<div class="ebu-code-window__bar">' +
        '<span class="ebu-code-window__label">code</span>' +
        '<button type="button" class="ebu-code-copy" data-ebu-copy>Copy</button>' +
        '</div>';

      var bodyEl = document.createElement('div');
      bodyEl.className = 'ebu-code-window__body';
      bodyEl.appendChild(pre.cloneNode(true));
      win.appendChild(bodyEl);

      pre.parentNode.insertBefore(win, pre);
      pre.remove();
    });
  }

  function initCopyButtons() {
    document.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-ebu-copy]');
      if (!btn) return;

      var win = btn.closest('.ebu-code-window');
      if (!win) return;

      var code = win.querySelector('code') || win.querySelector('pre');
      if (!code) return;

      var text = code.textContent || '';

      function done() {
        var orig = btn.textContent;
        btn.textContent = 'Copied';
        btn.classList.add('is-copied');
        setTimeout(function () {
          btn.textContent = orig;
          btn.classList.remove('is-copied');
        }, 1800);
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done).catch(function () {
          fallbackCopy(text);
          done();
        });
      } else {
        fallbackCopy(text);
        done();
      }
    });
  }

  function fallbackCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.left = '-9999px';
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand('copy');
    } catch (err) { /* noop */ }
    document.body.removeChild(ta);
  }

  function initStepLists() {
    var content = document.querySelector('.entry-content');
    if (!content) return;

    content.querySelectorAll(':scope > ol').forEach(function (ol, olIndex) {
      if (olIndex === 0 || ol.classList.contains('ebu-article-toc')) return;

      var items = ol.querySelectorAll(':scope > li');
      var hasSteps = false;
      items.forEach(function (li) {
        if (/шаг\s*\d/i.test(li.textContent)) hasSteps = true;
      });
      if (!hasSteps || items.length < 2) return;

      ol.classList.add('ebu-steps');
    });
  }

  function initChecklist() {
    var section = document.getElementById('checklist');
    if (!section) return;

    var ul = section.nextElementSibling;
    while (ul && ul.tagName !== 'UL') {
      ul = ul.nextElementSibling;
    }
    if (!ul || ul.tagName !== 'UL') return;

    ul.classList.add('ebu-checklist');
  }

  function initFaqHash() {
    if (window.location.hash !== '#faq') return;
    var faq = document.getElementById('faq');
    if (!faq) return;
    requestAnimationFrame(function () {
      var top = faq.getBoundingClientRect().top + window.scrollY - 100;
      window.scrollTo({ top: top, behavior: 'smooth' });
    });
  }

  function boot() {
    reorderArticleStructure();
    initArticleMeta();
    initReadingProgress();
    initInlineToc();
    initSectionMarkers();
    wrapBlockquotes();
    wrapPreBlocks();
    initCopyButtons();
    initStepLists();
    initChecklist();
    initFaqHash();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
