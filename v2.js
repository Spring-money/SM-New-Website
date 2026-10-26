/* Spring Money website v2. No libraries, no tracking. Extends site.js. */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* Mark current page in the nav */
  var here = (location.pathname.split("/").pop() || "index.html");
  $$(".nav-links a:not(.btn)").forEach(function (a) {
    var h = a.getAttribute("href").split("#")[0];
    if (h === here && h !== "") a.setAttribute("aria-current", "page");
  });

  /* Spring Sense: agents at work */
  $$("[data-sense]").forEach(function (root) {
    var DUR = 8500;
    var btns = $$(".agent-btn", root);
    var scenes = $$(".scene", root);
    var title = $("[data-title]", root);
    var TITLES = [
      "Meeting Prep & Summaries · Thursday 11:00",
      "Portfolio Review Generator · Rao family",
      "Automated Client Follow-ups · for approval",
      "Ops & Compliance Verification · this morning",
      "Spring Sense Assistant"
    ];
    var idx = 0, timer = null, playing = !reduce, visible = false, userStopped = false;
    var pp = $("button.pp", root.parentNode) || $("button.pp", root);
    var setPlayLabel = function () { if (pp) { pp.setAttribute("aria-pressed", playing ? "true" : "false"); pp.querySelector("span").textContent = playing ? "Pause demo" : "Play demo"; } };

    var show = function (i, fromUser) {
      idx = (i + scenes.length) % scenes.length;
      scenes.forEach(function (s, j) { s.classList.toggle("is-active", j === idx); });
      btns.forEach(function (b, j) {
        b.setAttribute("aria-pressed", j === idx ? "true" : "false");
        b.classList.remove("playing");
      });
      if (title) title.textContent = TITLES[idx];
      void root.offsetWidth;
      if (playing && !fromUser) btns[idx].classList.add("playing");
      schedule();
    };
    var schedule = function () {
      clearTimeout(timer);
      if (!playing || !visible || reduce) return;
      btns[idx].style.setProperty("--dur", DUR + "ms");
      btns[idx].classList.add("playing");
      timer = setTimeout(function () { show(idx + 1); }, DUR);
    };
    btns.forEach(function (b, j) {
      b.addEventListener("click", function () { playing = false; userStopped = true; setPlayLabel(); clearTimeout(timer); show(j, true); });
    });
    if (pp) pp.addEventListener("click", function () {
      playing = !playing; userStopped = !playing; root.classList.toggle("paused", !playing); setPlayLabel();
      if (playing) show(idx); else { clearTimeout(timer); btns.forEach(function (b) { b.classList.remove("playing"); }); }
    });
    var segBtns = $$("[data-sense-lane]", root.parentNode);
    segBtns.forEach(function (b) {
      b.addEventListener("click", function () {
        var lane = b.getAttribute("data-sense-lane");
        root.setAttribute("data-sl", lane);
        segBtns.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        show(idx, true);
      });
    });
    setPlayLabel();
    show(0, true);
    if ("IntersectionObserver" in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          visible = e.isIntersecting;
          if (visible && playing && !userStopped) show(idx);
          else if (!visible) clearTimeout(timer);
        });
      }, { threshold: 0.35 }).observe(root);
    } else { visible = true; schedule(); }
  });

  /* Partner wall filter */
  $$("[data-wall]").forEach(function (root) {
    var chips = $$(".fchip", root);
    var tiles = $$(".tile", root);
    var count = $("[data-count]", root);
    chips.forEach(function (c) {
      c.addEventListener("click", function () {
        var f = c.getAttribute("data-f");
        chips.forEach(function (x) { x.setAttribute("aria-pressed", x === c ? "true" : "false"); });
        var n = 0;
        tiles.forEach(function (t) {
          var ok = f === "all" || t.getAttribute("data-state") === f;
          t.classList.toggle("hide", !ok);
          if (ok) n++;
        });
        if (count) count.textContent = n + " shown";
      });
    });
  });
})();

/* Depth pass (Claude, 6 Oct 2026): feature directory, dashboard, client journey */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  $$("[data-fdir]").forEach(function (root) {
    var q = $("[data-fq]", root), st = "all";
    var feats = $$(".feat", root), groups = $$("[data-group]", root);
    var shown = $("[data-fshown]", root), empty = $("[data-fempty]", root);
    var esc = function (s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); };
    feats.forEach(function (f) { var h = $("h4", f), p = $("p", f); f._h = h.textContent; f._p = p.textContent; });
    var apply = function () {
      var term = (q.value || "").trim().toLowerCase(), n = 0;
      var re = term ? new RegExp("(" + esc(term) + ")", "ig") : null;
      feats.forEach(function (f) {
        var okS = st === "all" || f.dataset.st === st;
        var okQ = !term || f.dataset.text.indexOf(term) > -1;
        var ok = okS && okQ;
        f.classList.toggle("hide", !ok);
        var h = $("h4", f), p = $("p", f);
        if (re && ok) { h.innerHTML = f._h.replace(re, '<mark class="hl">$1</mark>'); p.innerHTML = f._p.replace(re, '<mark class="hl">$1</mark>'); }
        else { h.textContent = f._h; p.textContent = f._p; }
        if (ok) n++;
      });
      groups.forEach(function (g) {
        var c = $$(".feat:not(.hide)", g).length;
        g.classList.toggle("hide", c === 0);
        var gc = $("[data-gcount]", g); if (gc) gc.textContent = c + (c === 1 ? " feature" : " features");
      });
      shown.textContent = n + (n === 1 ? " feature" : " features");
      empty.hidden = n !== 0;
    };
    q.addEventListener("input", apply);
    $$("[data-fst]", root).forEach(function (b) { b.addEventListener("click", function () { st = b.dataset.fst; $$("[data-fst]", root).forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); }); apply(); }); });
    apply();
    var links = $$(".fdir-nav a", root);
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) links.forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === "#" + e.target.id); }); });
      }, { rootMargin: "-30% 0px -60% 0px" });
      groups.forEach(function (g) { io.observe(g); });
    }
  });

  $$(".dash").forEach(function (d) {
    var go = function () {
      d.classList.add("live");
      if (reduce) return;
      $$("[data-count]", d).forEach(function (b) {
        var raw = b.dataset.count, dec = (raw.split(".")[1] || "").length, target = parseFloat(raw.replace(/,/g, "")), t0 = null;
        var fmt = function (v) { var s = v.toFixed(dec); return raw.indexOf(",") > -1 ? Number(s).toLocaleString("en-IN") : s; };
        var step = function (ts) { if (!t0) t0 = ts; var k = Math.min(1, (ts - t0) / 1400); k = 1 - Math.pow(1 - k, 3); b.textContent = fmt(target * k); if (k < 1) requestAnimationFrame(step); };
        requestAnimationFrame(step);
      });
    };
    if ("IntersectionObserver" in window && !reduce) {
      var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { go(); io.disconnect(); } }); }, { threshold: 0.3 });
      io.observe(d);
    } else go();
  });

  $$("[data-journey]").forEach(function (root) {
    var steps = $$(".jstep", root), scr = $$(".jscreen", root), ds = $$(".jdesc", root), i = 0, timer = null, user = false;
    var show = function (k) {
      i = k;
      steps.forEach(function (s, j) { s.setAttribute("aria-pressed", j === k ? "true" : "false"); s.classList.toggle("done", j < k); });
      scr.forEach(function (s, j) { s.classList.toggle("on", j === k); });
      ds.forEach(function (s, j) { s.classList.toggle("on", j === k); });
    };
    steps.forEach(function (s, j) { s.addEventListener("click", function () { user = true; clearInterval(timer); show(j); }); });
    if (!reduce && "IntersectionObserver" in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          clearInterval(timer);
          if (e.isIntersecting && !user) timer = setInterval(function () { show((i + 1) % steps.length); }, 3200);
        });
      }, { threshold: 0.4 }).observe(root);
    }
  });
})();

/* Asset solar system */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  Array.prototype.forEach.call(document.querySelectorAll("[data-solar]"), function (solar) {
    var sec = solar.closest(".solar-wrap");
    var pls = Array.prototype.slice.call(solar.querySelectorAll(".pl"));
    var ods = Array.prototype.slice.call(sec.querySelectorAll(".od"));
    var cur = 0, timer = null, user = false;
    var pick = function (i) {
      cur = i;
      pls.forEach(function (p) { p.setAttribute("aria-pressed", +p.dataset.pl === i ? "true" : "false"); });
      ods.forEach(function (d) { d.classList.toggle("on", +d.dataset.od === i); });
    };
    pls.forEach(function (p) {
      p.addEventListener("click", function () { user = true; clearInterval(timer); solar.classList.add("held"); pick(+p.dataset.pl); });
    });
    if (!reduce && "IntersectionObserver" in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          clearInterval(timer);
          if (e.isIntersecting && !user) timer = setInterval(function () { pick((cur + 1) % ods.length); }, 3400);
        });
      }, { threshold: 0.35 }).observe(solar);
    }
  });
})();
