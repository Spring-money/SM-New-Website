/* Spring Money website v1.2: header dropdowns, headline preview, demo switches, self-onboarding + CRM,
   pricing illustration and calculators. No libraries, no tracking. Extends site.js and v2.js. */
(function () {
  "use strict";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var inr = function (n) { return "₹" + Math.round(n).toLocaleString("en-IN"); };
  var words = function (n) {
    var a = Math.abs(n), s = n < 0 ? "−" : "";
    if (a >= 1e7) return s + "₹" + (a / 1e7).toLocaleString("en-IN", { maximumFractionDigits: 2 }) + " crore";
    if (a >= 1e5) return s + "₹" + (a / 1e5).toLocaleString("en-IN", { maximumFractionDigits: 2 }) + " lakh";
    return s + "₹" + Math.round(a).toLocaleString("en-IN");
  };

  /* ---------- Header dropdowns ---------- */
  var dds = $$(".dd");
  var closeAll = function (except) { dds.forEach(function (d) { if (d !== except) $(".dd-btn", d).setAttribute("aria-expanded", "false"); }); };
  dds.forEach(function (d) {
    var b = $(".dd-btn", d);
    b.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = b.getAttribute("aria-expanded") === "true";
      closeAll(d);
      b.setAttribute("aria-expanded", open ? "false" : "true");
    });
    d.addEventListener("keydown", function (e) { if (e.key === "Escape") { b.setAttribute("aria-expanded", "false"); b.focus(); } });
    var here = (location.pathname.split("/").pop() || "index.html");
    $$(".dd-menu a", d).forEach(function (a) { if (a.getAttribute("href") === here) { a.setAttribute("aria-current", "page"); d.classList.add("current"); } });
  });
  document.addEventListener("click", function (e) { if (!e.target.closest || !e.target.closest(".dd")) closeAll(); });

  /* ---------- Hero headline preview (open item 1): ?h=A ... ?h=F ---------- */
  var H = { A: "Know every client like your finest.", B: "The attention your top clients get. Now for every client.",
    C: "Wealth management, as personal as the family it serves.", D: "Every family's wealth, seen whole.",
    E: "Private-banking care, for every client you serve.", F: "Deliver hyper-personalised wealth management for every client." };
  var hl = $("[data-headline]");
  var hq = (location.search.match(/[?&]h=([A-F])/i) || [])[1];
  if (hl && hq && H[hq.toUpperCase()]) hl.textContent = H[hq.toUpperCase()];

  /* ---------- Demo feature switches ---------- */
  $$(".tg").forEach(function (t) {
    t.addEventListener("click", function () { t.setAttribute("aria-checked", t.getAttribute("aria-checked") === "true" ? "false" : "true"); });
  });

  /* ---------- Self-onboarding + CRM, one client on both sides ---------- */
  $$("[data-obcrm]").forEach(function (root) {
    var map = root.getAttribute("data-obcrm").split(";").map(function (x) { var p = x.split(","); return [+p[0], +p[1]]; });
    var steps = $$(".jstep", root), scr = $$(".jscreen", root), ds = $$(".jdesc", root);
    var fun = $$(".crm-fun span", root), tasks = $$(".crm-tasks li", root), book = $(".crm-book", root), bookTxt = $("[data-book]", root), lead = $("[data-leadst]", root);
    var i = 0, timer = null, user = false;
    var show = function (k) {
      i = k;
      steps.forEach(function (s, j) { s.setAttribute("aria-pressed", j === k ? "true" : "false"); s.classList.toggle("done", j < k); });
      scr.forEach(function (s, j) { s.classList.toggle("on", j === k); });
      ds.forEach(function (s, j) { s.classList.toggle("on", j === k); });
      var st = map[k][0], tk = map[k][1];
      fun.forEach(function (f, j) { f.classList.toggle("on", j <= st); });
      tasks.forEach(function (t, j) { t.classList.toggle("on", j <= tk); t.classList.toggle("done", j < tk); });
      var inBook = st >= fun.length - 1;
      book.classList.toggle("on", inBook);
      bookTxt.textContent = inBook ? "Added to your book" : "Not in your book yet";
      if (lead) lead.textContent = inBook ? "Client" : (st >= 1 ? "Onboarding" : "Lead");
    };
    steps.forEach(function (s, j) { s.addEventListener("click", function () { user = true; clearInterval(timer); show(j); }); });
    show(0);
    if (!reduce && "IntersectionObserver" in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          clearInterval(timer);
          if (e.isIntersecting && !user) timer = setInterval(function () { show((i + 1) % steps.length); }, 3000);
        });
      }, { threshold: 0.4 }).observe(root);
    }
  });

  /* ---------- Pricing illustration: 3 bps a year, billed monthly ---------- */
  $$("[data-pcalc]").forEach(function (root) {
    var r = $("input[type=range]", root);
    var upd = function () {
      var cr = +r.value, year = cr * 1e7 * 0.0003;
      $("[data-pc-aum]", root).textContent = "₹" + cr.toLocaleString("en-IN") + " crore";
      $("[data-pc-year]", root).textContent = inr(year);
      $("[data-pc-month]", root).textContent = inr(year / 12);
      r.style.setProperty("--p", ((cr - r.min) / (r.max - r.min) * 100) + "%");
    };
    r.addEventListener("input", upd); upd();
  });

  /* ---------- Calculators ---------- */
  var fvSip = function (p, mr, n) { return mr === 0 ? p * n : p * ((Math.pow(1 + mr, n) - 1) / mr) * (1 + mr); };
  var fvStep = function (p, step, yrs, rate) { // monthly SIP, raised once a year, returns [fv, invested]
    var mr = rate / 1200, fv = 0, inv = 0, amt = p;
    for (var y = 0; y < yrs; y++) { for (var m = 0; m < 12; m++) { fv = (fv + amt) * (1 + mr); inv += amt; } amt *= 1 + step / 100; }
    return [fv, inv];
  };
  var emiOf = function (P, rate, months) { var r = rate / 1200; return r === 0 ? P / months : P * r * Math.pow(1 + r, months) / (Math.pow(1 + r, months) - 1); };
  var balance = function (P, rate, months, paid) { var r = rate / 1200, e = emiOf(P, rate, months); return r === 0 ? P - e * paid : P * Math.pow(1 + r, paid) - e * (Math.pow(1 + r, paid) - 1) / r; };
  var G = "#149B72", B = "#2E6FD8", Y = "#7D8180";

  var CALC = {
    sip: function (v) { var n = v.yrs * 12, fv = fvSip(v.amt, v.ret / 1200, n), inv = v.amt * n;
      return { big: ["Could grow to", fv], rows: [["You invest", inr(inv)], ["Estimated gains", inr(fv - inv)]], bar: [["Invested", inv, B], ["Gains", fv - inv, G]],
        assume: "Assumes the same SIP on the same date every month and a steady " + v.ret + "% yearly return, compounded monthly. Real returns vary." }; },
    lumpsum: function (v) { var fv = v.amt * Math.pow(1 + v.ret / 100, v.yrs);
      return { big: ["Could grow to", fv], rows: [["You invest", inr(v.amt)], ["Estimated gains", inr(fv - v.amt)]], bar: [["Invested", v.amt, B], ["Gains", fv - v.amt, G]],
        assume: "Assumes a steady " + v.ret + "% yearly return, compounded yearly, and no withdrawals." }; },
    stepup: function (v) { var r = fvStep(v.amt, v.step, v.yrs, v.ret), flat = fvSip(v.amt, v.ret / 1200, v.yrs * 12);
      return { big: ["Could grow to", r[0]], rows: [["You invest", inr(r[1])], ["Estimated gains", inr(r[0] - r[1])], ["Without the step-up", inr(flat)], ["Monthly SIP in the last year", inr(v.amt * Math.pow(1 + v.step / 100, v.yrs - 1))]],
        bar: [["Invested", r[1], B], ["Gains", r[0] - r[1], G]], assume: "Assumes the SIP rises by " + v.step + "% once a year and a steady " + v.ret + "% yearly return, compounded monthly." }; },
    siptarget: function (v) { var n = v.yrs * 12, need = v.target / fvSip(1, v.ret / 1200, n);
      return { big: ["Monthly SIP needed", need], rows: [["You invest", inr(need * n)], ["Estimated gains", inr(v.target - need * n)]], bar: [["Invested", need * n, B], ["Gains", v.target - need * n, G]],
        assume: "Target of " + words(v.target) + " in " + v.yrs + " years, at a steady " + v.ret + "% yearly return. The target is in future rupees; add inflation if it is today's cost." }; },
    steptarget: function (v) { var one = fvStep(1, v.step, v.yrs, v.ret), p = v.target / one[0];
      return { big: ["Starting monthly SIP needed", p], rows: [["Monthly SIP in the last year", inr(p * Math.pow(1 + v.step / 100, v.yrs - 1))], ["You invest", inr(p * one[1])], ["Estimated gains", inr(v.target - p * one[1])]],
        bar: [["Invested", p * one[1], B], ["Gains", v.target - p * one[1], G]], assume: "The SIP rises by " + v.step + "% a year; steady " + v.ret + "% yearly return, compounded monthly." }; },
    sipswp: function (v) { var c = fvSip(v.amt, v.ret / 1200, v.yrs * 12), m = v.wyrs * 12, r = v.wret / 1200, w = r === 0 ? c / m : c * r / (1 - Math.pow(1 + r, -m));
      return { big: ["Monthly withdrawal possible", w], rows: [["Corpus when the SIP ends", inr(c)], ["You invest", inr(v.amt * v.yrs * 12)], ["Total withdrawn", inr(w * m)]],
        bar: [["Invested", v.amt * v.yrs * 12, B], ["Withdrawn", w * m, G]], assume: "SIP for " + v.yrs + " years at " + v.ret + "%, then equal monthly withdrawals for " + v.wyrs + " years at " + v.wret + "%, ending at zero. Ignores tax and exit loads." }; },
    retire: function (v) {
      var yrs = Math.max(0, v.rage - v.age), ry = Math.max(1, v.life - v.rage), e0 = v.exp * 12 * Math.pow(1 + v.inf / 100, yrs);
      var g = v.inf / 100, r = v.pret / 100, need = 0;
      for (var k = 0; k < ry; k++) need += e0 * Math.pow(1 + g, k) / Math.pow(1 + r, k);
      var have = v.have * Math.pow(1 + v.ret / 100, yrs), gap = Math.max(0, need - have), sip = yrs > 0 ? gap / fvSip(1, v.ret / 1200, yrs * 12) : 0;
      return { big: ["Corpus needed at " + v.rage, need], rows: [["Monthly expenses at retirement", inr(e0 / 12)], ["Your savings could grow to", inr(have)], ["Monthly SIP needed", inr(sip)]],
        bar: [["From savings", Math.min(have, need), B], ["Still to build", gap, Y]], assume: "Expenses grow at " + v.inf + "% a year. Returns: " + v.ret + "% before retirement, " + v.pret + "% after. The corpus lasts until age " + v.life + ". Ignores tax." }; },
    edu: function (v) { var fc = v.cost * Math.pow(1 + v.inf / 100, v.yrs), have = v.have * Math.pow(1 + v.ret / 100, v.yrs), gap = Math.max(0, fc - have), sip = gap / fvSip(1, v.ret / 1200, v.yrs * 12);
      return { big: ["Monthly SIP needed", sip], rows: [["Cost in " + v.yrs + " years", inr(fc)], ["Your savings could grow to", inr(have)], ["Still to build", inr(gap)]],
        bar: [["From savings", Math.min(have, fc), B], ["From the SIP", gap, G]], assume: "Education costs rise at " + v.inf + "% a year; investments return " + v.ret + "% a year." }; },
    fdretire: function (v) {
      var bal = v.corpus, exp = v.exp, mr = v.rate / 1200, months = 0;
      while (bal > 0 && months < 1200) { bal = bal * (1 + mr) - exp; months++; if (months % 12 === 0) exp *= 1 + v.inf / 100; }
      var yrs = months >= 1200 ? "100+ years" : (Math.floor(months / 12) + " years" + (months % 12 ? ", " + (months % 12) + " months" : ""));
      var interest = v.corpus * v.rate / 1200;
      return { bigText: ["Your corpus could last", yrs], rows: [["Interest a month today", inr(interest)], ["Expenses a month today", inr(v.exp)], ["Interest covers today's expenses", interest >= v.exp ? "Yes" : "No"]],
        assume: "Withdrawals of " + inr(v.exp) + " a month, rising " + v.inf + "% each year; FD interest of " + v.rate + "% a year, compounded monthly; ignores tax on interest and rate changes on renewal." }; },
    cgt: function (v) {
      var gain = v.sell - v.buy, tax = 0, label, note;
      if (gain <= 0) { label = "No tax on a loss"; note = "A capital loss can be set off against gains under the tax rules."; }
      else if (v.kind === "debt") { tax = gain * v.slab / 100; label = "Taxed at your slab rate"; note = "Debt funds bought from 1 April 2023 are taxed at your income-tax slab, however long you hold them."; }
      else if (v.months > 12) { var free = Math.max(0, 125000 - v.used), taxable = Math.max(0, gain - free); tax = taxable * 0.125; label = "Long-term gain"; note = "Held over 12 months: 12.5% on gains above ₹1.25 lakh in a financial year (₹" + Math.round(free).toLocaleString("en-IN") + " of the exemption left)."; }
      else { tax = gain * 0.20; label = "Short-term gain"; note = "Held 12 months or less: 20% on the gain."; }
      return { big: ["Estimated tax", tax], rows: [["Gain", inr(Math.max(gain, 0))], ["Type", label], ["After tax", inr(v.sell - tax)]], assume: note + " Before surcharge and 4% cess. Rules as of 2025-26; check current rules." }; },
    emi: function (v) { var n = v.yrs * 12, e = emiOf(v.loan, v.rate, n), tot = e * n;
      return { big: ["Monthly EMI", e], rows: [["Total interest", inr(tot - v.loan)], ["Total paid", inr(tot)]], bar: [["Principal", v.loan, B], ["Interest", tot - v.loan, Y]],
        assume: "Fixed rate of " + v.rate + "% for " + v.yrs + " years, with no prepayments." }; },
    buyrent: function (v) {
      var dp = v.price * v.down / 100, loan = v.price - dp, n = v.tenure * 12, e = loan > 0 ? emiOf(loan, v.rate, n) : 0, mr = v.ret / 1200;
      var rentInv = dp, buyInv = 0, rent = v.rent;
      for (var m = 1; m <= v.yrs * 12; m++) {
        var emi = m <= n ? e : 0, diff = emi - rent;
        rentInv = rentInv * (1 + mr) + Math.max(diff, 0); buyInv = buyInv * (1 + mr) + Math.max(-diff, 0);
        if (m % 12 === 0) rent *= 1 + v.rinc / 100;
      }
      var home = v.price * Math.pow(1 + v.app / 100, v.yrs), owed = Math.max(0, loan > 0 ? balance(loan, v.rate, n, Math.min(n, v.yrs * 12)) : 0);
      var buyNW = home - owed + buyInv, rentNW = rentInv, better = buyNW >= rentNW ? "Buying" : "Renting and investing";
      return { big: ["Ahead after " + v.yrs + " years", Math.abs(buyNW - rentNW)], verdict: better + " comes out ahead in this illustration.",
        rows: [["If you buy: home value less loan, plus savings", inr(buyNW)], ["If you rent: investments", inr(rentNW)], ["Monthly EMI", inr(e)]],
        bar: [["Buy", buyNW, G], ["Rent", rentNW, B]], assume: "Whoever pays less each month invests the difference at " + v.ret + "%. Ignores stamp duty, maintenance, tax benefits and the cost of moving." }; },
    car: function (v) {
      var dp = v.price * v.down / 100, loan = v.price - dp, n = v.tenure * 12, e = loan > 0 ? emiOf(loan, v.rate, n) : 0, keep = v.yrs * 12;
      var paid = e * Math.min(n, keep), owed = loan > 0 && keep < n ? balance(loan, v.rate, n, keep) : 0, resale = v.price * v.resale / 100;
      var carCost = dp + paid + owed + v.run * keep - resale, c = v.commute, comm = 0;
      for (var m = 1; m <= keep; m++) { comm += c; if (m % 12 === 0) c *= 1 + v.cinc / 100; }
      return { big: ["Difference over " + v.yrs + " years", Math.abs(carCost - comm)], verdict: (carCost <= comm ? "Owning the car" : "Commuting") + " costs less in this illustration.",
        rows: [["Owning the car, net of resale", inr(carCost)], ["Commuting", inr(comm)], ["Monthly car EMI", inr(e)]],
        bar: [["Car", carCost, Y], ["Commute", comm, B]], assume: "Car: down payment, EMIs, running costs and any loan left, less resale at " + v.resale + "% of the price. Commute cost rises " + v.cinc + "% a year. Ignores what the money could earn elsewhere." }; },
    fdrd: function (v) {
      var n = v.yrs * 12, q = v.rate / 400, rd = 0, total = v.amt * n;
      for (var k = 1; k <= n; k++) rd += v.amt * Math.pow(1 + q, (n - k + 1) / 3);
      var fd = total * Math.pow(1 + q, v.yrs * 4);
      return { big: ["RD maturity", rd], rows: [["You deposit in total", inr(total)], ["FD of the same total, paid upfront", inr(fd)], ["Extra from the FD", inr(fd - rd)]],
        bar: [["RD", rd, B], ["FD", fd, G]], assume: "Both at " + v.rate + "% a year, compounded quarterly. The FD needs the whole amount on day one; the RD spreads it over " + n + " months. Interest is taxable." }; },
    endow: function (v) {
      var diff = Math.max(0, v.eprem - v.tprem), r = v.ret / 100, inv = 0;
      for (var y = 0; y < v.yrs; y++) inv = (inv + diff) * (1 + r);
      var irr = (function () { var lo = -0.99, hi = 1; for (var i = 0; i < 80; i++) { var mid = (lo + hi) / 2, fv = 0; for (var y = 0; y < v.yrs; y++) fv = (fv + v.eprem) * (1 + mid); if (fv > v.mat) hi = mid; else lo = mid; } return (lo + hi) / 2; })();
      return { big: ["Term plan plus investing", inv], verdict: (inv >= v.mat ? "Term cover plus investing" : "The endowment plan") + " comes out ahead in this illustration.",
        rows: [["Endowment maturity value", inr(v.mat)], ["Yearly amount invested", inr(diff)], ["Return built into the endowment", (irr * 100).toFixed(1) + "% a year"]],
        bar: [["Term + invest", inv, G], ["Endowment", v.mat, B]], assume: "Both give the same life cover for " + v.yrs + " years. The premium difference is invested each year at " + v.ret + "%. Ignores tax and the endowment's bonuses beyond the value you entered." }; }
  };

  var render = function (out, r) {
    var html = '<span class="illus">Illustrative</span>';
    if (r.big) html += '<div class="big"><span>' + r.big[0] + '</span><b>' + inr(r.big[1]) + '</b>' + (Math.abs(r.big[1]) >= 1e5 ? '<span>' + words(r.big[1]) + '</span>' : '') + '</div>';
    if (r.bigText) html += '<div class="big"><span>' + r.bigText[0] + '</span><b>' + r.bigText[1] + '</b></div>';
    if (r.verdict) html += '<p class="cverdict">' + r.verdict + '</p>';
    if (r.bar) {
      var tot = r.bar.reduce(function (a, b) { return a + Math.max(0, b[1]); }, 0) || 1;
      html += '<div class="cbar" aria-hidden="true">' + r.bar.map(function (b) { return '<i style="width:' + (Math.max(0, b[1]) / tot * 100) + '%;background:' + b[2] + '"></i>'; }).join("") + '</div>';
      html += '<div class="ckey">' + r.bar.map(function (b) { return '<span><i style="background:' + b[2] + '"></i>' + b[0] + '</span>'; }).join("") + '</div>';
    }
    if (r.rows) html += '<dl>' + r.rows.map(function (x) { return '<dt>' + x[0] + '</dt><dd>' + x[1] + '</dd>'; }).join("") + '</dl>';
    if (r.assume) html += '<p class="cassume"><b>Assumptions.</b> ' + r.assume + '</p>';
    out.innerHTML = html;
  };

  $$("[data-calc]").forEach(function (sec) {
    var id = sec.getAttribute("data-calc"), out = $("[data-out]", sec), fn = CALC[id];
    var get = function () {
      var v = {};
      $$("input[type=number], select", sec).forEach(function (el) { v[el.getAttribute("data-k")] = el.tagName === "SELECT" ? el.value : (parseFloat(el.value) || 0); });
      return v;
    };
    var paint = function (r) { r.style.setProperty("--p", ((r.value - r.min) / (r.max - r.min) * 100) + "%"); };
    var run = function () { try { render(out, fn(get())); } catch (e) { out.textContent = "Check the numbers entered."; } };
    $$(".cfrow", sec).forEach(function (row) {
      var rg = $("input[type=range]", row), nb = $("input[type=number]", row);
      rg.addEventListener("input", function () { nb.value = rg.value; paint(rg); run(); });
      nb.addEventListener("input", function () { var x = parseFloat(nb.value); if (!isNaN(x)) { rg.value = Math.min(Math.max(x, +rg.min), +rg.max); paint(rg); } run(); });
      paint(rg);
    });
    $$("select", sec).forEach(function (s) { s.addEventListener("change", run); });
    run();
  });

  /* show one calculator at a time when scripts run (all stay visible without JS) */
  var wrap = $("[data-calcs]");
  if (wrap) {
    var panels = $$("[data-calc]", wrap), links = $$("[data-cl]", wrap);
    var pick = function (id, scroll) {
      if (!CALC[id]) id = "sip";
      panels.forEach(function (p) { p.hidden = p.getAttribute("data-calc") !== id; });
      links.forEach(function (a) { a.setAttribute("aria-current", a.getAttribute("data-cl") === id ? "true" : "false"); });
      if (scroll) { var t = $("#c-" + id); if (t) t.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" }); }
    };
    links.forEach(function (a) { a.addEventListener("click", function (e) { e.preventDefault(); var id = a.getAttribute("data-cl"); history.replaceState(null, "", "#c-" + id); pick(id, true); }); });
    pick((location.hash.match(/^#c-(\w+)/) || [])[1], !!location.hash);
  }

  /* contact form: draft site, not connected */
  var form = $("form[data-demo]");
  if (form) form.addEventListener("submit", function () {
    setTimeout(function () { var st = $(".form-status", form); if (st && st.textContent) st.textContent = "Preview site: this form is not connected yet, so nothing was sent. Use WhatsApp or email below."; }, 0);
  });
})();
