/* Spring Money website, revamp draft v0.1. No libraries, no tracking. */
(function () {
  "use strict";
  document.documentElement.classList.add("js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* Header border on scroll + mobile menu */
  var header = $(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("scrolled", window.scrollY > 8); };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    var menuBtn = $(".menu-btn");
    if (menuBtn) {
      menuBtn.addEventListener("click", function () {
        var open = header.classList.toggle("menu-open");
        menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
      });
      $$(".nav-links a").forEach(function (a) {
        a.addEventListener("click", function () { header.classList.remove("menu-open"); menuBtn.setAttribute("aria-expanded", "false"); });
      });
    }
  }

  /* Demo firms. All names, domains and numbers are invented. */
  var FIRMS = [
    {
      name: "Demo Wealth", mark: "D", color: "#9A3412", tint: "#FDF0E8", url: "demowealth.manthan.money",
      who: "Wealth manager", nav: ["Clients", "Reviews", "Suggestions", "Orders", "Reconciliation", "Task centre"],
      on: 1, title: "Reviews this month", chip: "Review", bars: [72, 48, 85], kind: "Wealth manager", k1: "468.4", k2: "2.1", k3: "412", r1n: "Kulkarni family", r1s: "Review draft ready", r2n: "Rao family", r2s: "SIP mandate renewal", r3n: "Deshmukh family", r3s: "KYC refresh due", cn: "Hi Meera", cv: "18,42,500", cs: "Next SIP on 5 Nov", toast: "Spring Sense: review draft ready", toastSub: "Waiting for your approval"
    },
    {
      name: "Demo Wealth", mark: "D", color: "#1D4ED8", tint: "#EEF4FF", url: "demowealth.manthan.money",
      who: "Wealth manager", nav: ["Clients", "Reviews", "Plans", "Orders", "Reconciliation", "Task centre"],
      on: 1, title: "Reviews this month", chip: "Review", bars: [58, 80, 40], kind: "Wealth manager", k1: "742.9", k2: "3.4", k3: "268", r1n: "Iyer family", r1s: "Review on Thursday", r2n: "Menon family", r2s: "Plan update due", r3n: "Shah family", r3s: "Annual review booked", cn: "Hi Arjun", cv: "62,10,300", cs: "Review on Thursday", toast: "Spring Sense: meeting brief ready", toastSub: "For Thursday, 11:00"
    },
    {
      name: "Demo Wealth", mark: "D", color: "#6D28D9", tint: "#F3EEFF", url: "demowealth.manthan.money",
      who: "Wealth manager", nav: ["Clients", "Families", "Reviews", "Orders", "Reconciliation", "Task centre"],
      on: 1, title: "Reviews this month", chip: "Review", bars: [64, 66, 70], kind: "Wealth manager", k1: "931.5", k2: "4.6", k3: "905", r1n: "Patil family", r1s: "Review draft ready", r2n: "Joshi family", r2s: "SIP mandate renewal", r3n: "Gupta family", r3s: "Documents missing", cn: "Hi Kabir", cv: "34,75,900", cs: "2 actions waiting", toast: "Spring Sense: 3 items flagged", toastSub: "KYC expiry and reconciliation"
    }
  ];

  var stage = $(".stage[data-cycle]");
  if (stage) {
    var idx = 0, timer = null, paused = false;
    var dots = $$(".dots button", stage.parentNode);
    var apply = function (i, instant) {
      var f = FIRMS[i];
      var set = function () {
        stage.style.setProperty("--t", f.color);
        stage.style.setProperty("--t-tint", f.tint);
        $$("[data-f]", stage).forEach(function (el) {
          var k = el.getAttribute("data-f");
          if (k === "nav") {
            el.innerHTML = f.nav.map(function (n, j) { return "<li" + (j === f.on ? ' class="on"' : "") + ">" + n + "</li>"; }).join("");
          } else if (f[k] !== undefined) { el.textContent = f[k]; }
        });
        $$(".bar span", stage).forEach(function (b, j) { b.style.width = f.bars[j % f.bars.length] + "%"; });
        dots.forEach(function (d, j) { d.setAttribute("aria-pressed", j === i ? "true" : "false"); });
        stage.classList.remove("swapping");
        var t = $(".toast", stage);
        if (t) { t.classList.remove("show"); setTimeout(function () { t.classList.add("show"); }, reduce ? 0 : 700); }
      };
      if (instant || reduce) { set(); return; }
      stage.classList.add("swapping");
      setTimeout(set, 330);
    };
    var next = function () { idx = (idx + 1) % FIRMS.length; apply(idx); };
    var start = function () { if (!reduce && !timer) timer = setInterval(function () { if (!paused) next(); }, 3600); };
    apply(0, true);
    start();
    stage.addEventListener("mouseenter", function () { paused = true; });
    stage.addEventListener("mouseleave", function () { paused = false; });
    dots.forEach(function (d, j) {
      d.addEventListener("click", function () { idx = j; apply(j); clearInterval(timer); timer = null; });
    });
    document.addEventListener("visibilitychange", function () { paused = document.hidden; });
  }

  /* Label switcher: the UI naming map by licence */
  var LABELS = {
    mfd: ["Distributor (ARN)", "Portfolio review", "Scheme suggestions", "Calculators (education only)", "Not shown"],
    ria: ["Investment Adviser", "Advisory review", "Recommendations", "Financial plan", "Fees and invoices"],
    both: ["Set by each family's lane", "Set by each family's lane", "Set by each family's lane", "Set by each family's lane", "Advice lane only"]
  };
  $$("[data-lanes]").forEach(function (root) {
    var buttons = $$(".toggle button", root);
    var pill = $(".toggle .pill", root);
    var cells = $$(".lb-row dd", root);
    var current = root.getAttribute("data-start") || "mfd";
    var placePill = function () {
      var b = buttons.filter(function (x) { return x.getAttribute("data-lane") === current; })[0];
      if (!b || !pill) return;
      pill.style.width = b.offsetWidth + "px";
      pill.style.transform = "translateX(" + (b.offsetLeft - 4) + "px)";
    };
    var render = function (lane, animate) {
      cells.forEach(function (dd, i) {
        var text = LABELS[lane][i];
        var old = dd.querySelector("span");
        var span = document.createElement("span");
        span.textContent = text;
        if (lane === "mfd" && i === 4 || lane === "both" && i < 4) span.className = "hidden-tag";
        if (!animate || reduce || !old) { dd.innerHTML = ""; dd.appendChild(span); return; }
        span.classList.add("in-start");
        dd.appendChild(span);
        old.classList.add("out");
        requestAnimationFrame(function () { requestAnimationFrame(function () { span.classList.remove("in-start"); }); });
        setTimeout(function () { if (old.parentNode) old.parentNode.removeChild(old); }, 520);
      });
    };
    buttons.forEach(function (b) {
      b.addEventListener("click", function () {
        current = b.getAttribute("data-lane");
        buttons.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        placePill();
        render(current, true);
      });
    });
    render(current, false);
    placePill();
    window.addEventListener("resize", placePill);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(placePill);
  });

  /* Brand kit: recolour the demo app */
  var kit = $("[data-kit]");
  if (kit) {
    var phone = $(".phone", kit);
    $$(".swatches button", kit).forEach(function (b) {
      b.addEventListener("click", function () {
        phone.style.setProperty("--t", b.getAttribute("data-c"));
        phone.style.setProperty("--t-tint", b.getAttribute("data-tint"));
        $$(".swatches button", kit).forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      });
    });
    $$(".fonts button", kit).forEach(function (b) {
      b.addEventListener("click", function () {
        $(".ps-top p", kit).style.fontFamily = b.getAttribute("data-font");
        $$(".fonts button", kit).forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      });
    });
    var nameInput = $("#kit-name", kit);
    if (nameInput) nameInput.addEventListener("input", function () {
      var v = nameInput.value.trim() || "Your firm";
      $("[data-kit-name]", kit).textContent = v;
      $("[data-kit-mark]", kit).textContent = v.charAt(0).toUpperCase();
    });
  }

  /* Scroll-linked moments */
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      var el = e.target;
      if (el.classList.contains("flow")) {
        el.classList.add("drawn");
        $$(".step-num", el).forEach(function (n, i) { n.style.setProperty("--d", (0.25 + i * 0.3) + "s"); });
      }
      if (el.classList.contains("statement")) el.classList.add("lit");
      if (el.classList.contains("reveal")) el.classList.add("in");
      io.unobserve(el);
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -8% 0px" }) : null;
  $$(".flow, .statement, .reveal").forEach(function (el) {
    if (io && !reduce) io.observe(el);
    else { el.classList.add("drawn", "lit", "in"); }
  });

  /* Demo request form: not connected to anything yet */
  var form = $("form[data-demo]");
  if (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var status = $(".form-status", form);
      if (!form.checkValidity()) { form.reportValidity(); return; }
      status.textContent = "Draft site: this form is not connected yet. Nothing was sent.";
    });
  }

  var y = $("[data-year]");
  if (y) y.textContent = new Date().getFullYear();
})();
