/* Sidebar expand/collapse and mobile toggle */
(function () {
  'use strict';

  // ── Expand/collapse book nodes ──────────────────────────────────────────
  document.querySelectorAll('.nav-toggle').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var expanded = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!expanded));
      var children = btn.parentElement.querySelector('.nav-children');
      if (children) {
        children.classList.toggle('open', !expanded);
      }
    });
  });

  // Auto-open the path to the current page
  var current = document.querySelector('.nav-link.current');
  if (current) {
    var el = current.parentElement;
    while (el) {
      if (el.classList && el.classList.contains('nav-children')) {
        el.classList.add('open');
        var toggle = el.previousElementSibling;
        // previousElementSibling may be the toggle button or the link
        while (toggle && toggle.tagName !== 'BUTTON') {
          toggle = toggle.previousElementSibling;
        }
        if (toggle) toggle.setAttribute('aria-expanded', 'true');
      }
      el = el.parentElement;
    }
  }

  // ── Mobile sidebar toggle ───────────────────────────────────────────────
  var sidebar = document.getElementById('sidebar');
  var overlay = null;

  function openSidebar() {
    sidebar.classList.add('open');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.4);z-index:199;';
      overlay.addEventListener('click', closeSidebar);
      document.body.appendChild(overlay);
    }
  }

  function closeSidebar() {
    sidebar.classList.remove('open');
    if (overlay) { overlay.remove(); overlay = null; }
  }

  ['sidebarToggle', 'sidebarToggleMobile'].forEach(function (id) {
    var btn = document.getElementById(id);
    if (btn) {
      btn.addEventListener('click', function () {
        sidebar.classList.contains('open') ? closeSidebar() : openSidebar();
      });
    }
  });
})();
