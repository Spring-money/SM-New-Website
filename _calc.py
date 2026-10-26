"""Calculators page (revision brief 6.6). Markup only; the maths lives in brand.js (CALC).
Every result is illustrative, shows its assumptions and carries the calculator disclaimer from BRAND.md."""

# id, group, title, one-line purpose, fields
# field: (key, label, unit, min, max, step, default)  or ("sel", key, label, [(value, text)], default)
CALCS = [
 ("sip", "Investing", "SIP", "What a monthly SIP could grow to.",
  [("amt", "Monthly SIP", "₹", 500, 500000, 500, 10000), ("yrs", "Years", "years", 1, 40, 1, 15), ("ret", "Expected return", "% a year", 1, 20, 0.5, 12)]),
 ("lumpsum", "Investing", "Lumpsum", "What a one-time investment could grow to.",
  [("amt", "Amount invested", "₹", 5000, 50000000, 5000, 500000), ("yrs", "Years", "years", 1, 40, 1, 10), ("ret", "Expected return", "% a year", 1, 20, 0.5, 12)]),
 ("stepup", "Investing", "Step-up SIP", "A SIP that rises every year.",
  [("amt", "Starting monthly SIP", "₹", 500, 500000, 500, 10000), ("step", "Yearly step-up", "%", 0, 30, 1, 10), ("yrs", "Years", "years", 1, 40, 1, 15), ("ret", "Expected return", "% a year", 1, 20, 0.5, 12)]),
 ("siptarget", "Investing", "SIP target", "The monthly SIP needed for a target amount.",
  [("target", "Target amount", "₹", 100000, 100000000, 50000, 5000000), ("yrs", "Years", "years", 1, 40, 1, 10), ("ret", "Expected return", "% a year", 1, 20, 0.5, 12)]),
 ("steptarget", "Investing", "Step-up SIP target", "The starting SIP needed for a target, with a yearly step-up.",
  [("target", "Target amount", "₹", 100000, 100000000, 50000, 5000000), ("step", "Yearly step-up", "%", 0, 30, 1, 10), ("yrs", "Years", "years", 1, 40, 1, 10), ("ret", "Expected return", "% a year", 1, 20, 0.5, 12)]),
 ("sipswp", "Investing", "SIP to SWP", "Build a corpus with a SIP, then draw a monthly income from it.",
  [("amt", "Monthly SIP", "₹", 500, 500000, 500, 15000), ("yrs", "SIP years", "years", 1, 40, 1, 20), ("ret", "Return while investing", "% a year", 1, 20, 0.5, 12),
   ("wyrs", "Withdrawal years", "years", 1, 40, 1, 20), ("wret", "Return while withdrawing", "% a year", 1, 15, 0.5, 8)]),
 ("retire", "Goals", "Retirement", "The corpus a retirement needs, and the SIP to get there.",
  [("age", "Current age", "years", 18, 70, 1, 35), ("rage", "Retirement age", "years", 40, 80, 1, 60), ("life", "Plan until age", "years", 60, 100, 1, 85),
   ("exp", "Monthly expenses today", "₹", 5000, 1000000, 1000, 60000), ("inf", "Inflation", "% a year", 1, 12, 0.5, 6),
   ("ret", "Return before retirement", "% a year", 1, 18, 0.5, 11), ("pret", "Return after retirement", "% a year", 1, 12, 0.5, 7), ("have", "Savings already set aside", "₹", 0, 100000000, 50000, 1000000)]),
 ("edu", "Goals", "Child education", "What education will cost, and the SIP to fund it.",
  [("cost", "Cost today", "₹", 100000, 50000000, 50000, 2000000), ("yrs", "Years until needed", "years", 1, 25, 1, 12), ("inf", "Education inflation", "% a year", 1, 15, 0.5, 9),
   ("ret", "Expected return", "% a year", 1, 18, 0.5, 11), ("have", "Savings already set aside", "₹", 0, 20000000, 25000, 200000)]),
 ("fdretire", "Goals", "FD-based retirement", "How long a fixed-deposit corpus lasts against rising expenses.",
  [("corpus", "Corpus in fixed deposits", "₹", 500000, 200000000, 100000, 15000000), ("rate", "FD interest rate", "% a year", 1, 10, 0.25, 7),
   ("exp", "Monthly expenses", "₹", 5000, 1000000, 1000, 60000), ("inf", "Inflation", "% a year", 1, 12, 0.5, 6)]),
 ("cgt", "Tax", "Capital gains tax", "Tax on gains from selling equity or debt mutual fund units.",
  [("sel", "kind", "Asset", [("eq", "Equity funds and listed shares"), ("debt", "Debt funds bought from 1 April 2023")], "eq"),
   ("buy", "Purchase value", "₹", 10000, 100000000, 10000, 500000), ("sell", "Sale value", "₹", 10000, 200000000, 10000, 800000),
   ("months", "Held for", "months", 1, 240, 1, 18), ("slab", "Your income tax slab (debt funds only)", "%", 0, 30, 5, 30), ("used", "Equity long-term gains already this year", "₹", 0, 1000000, 5000, 0)]),
 ("emi", "Everyday decisions", "EMI", "The monthly instalment on a loan, and the interest paid.",
  [("loan", "Loan amount", "₹", 50000, 100000000, 50000, 5000000), ("rate", "Interest rate", "% a year", 1, 24, 0.1, 8.5), ("yrs", "Tenure", "years", 1, 30, 1, 20)]),
 ("buyrent", "Everyday decisions", "Buy vs rent", "Owning a home against renting and investing the difference.",
  [("price", "Home price", "₹", 1000000, 200000000, 100000, 10000000), ("down", "Down payment", "%", 10, 100, 5, 20), ("rate", "Home loan rate", "% a year", 5, 15, 0.1, 8.5),
   ("tenure", "Loan tenure", "years", 5, 30, 1, 20), ("rent", "Monthly rent today", "₹", 5000, 500000, 1000, 30000), ("rinc", "Rent increase", "% a year", 0, 15, 0.5, 5),
   ("app", "Home price growth", "% a year", 0, 15, 0.5, 5), ("ret", "Return on investments", "% a year", 1, 18, 0.5, 11), ("yrs", "Compare over", "years", 3, 30, 1, 15)]),
 ("car", "Everyday decisions", "Car vs commute", "Owning a car against paying for daily travel.",
  [("price", "Car price (on road)", "₹", 300000, 10000000, 50000, 1200000), ("down", "Down payment", "%", 0, 100, 5, 20), ("rate", "Car loan rate", "% a year", 5, 18, 0.1, 9.5),
   ("tenure", "Loan tenure", "years", 1, 7, 1, 5), ("run", "Running cost a month", "₹", 1000, 100000, 500, 9000), ("yrs", "Years you keep the car", "years", 1, 15, 1, 7),
   ("resale", "Resale value at the end", "% of price", 0, 80, 5, 35), ("commute", "Commute cost a month instead", "₹", 1000, 100000, 500, 12000), ("cinc", "Commute cost increase", "% a year", 0, 15, 0.5, 6)]),
 ("fdrd", "Everyday decisions", "FD vs RD", "A lumpsum fixed deposit against a monthly recurring deposit.",
  [("amt", "Monthly RD amount", "₹", 500, 500000, 500, 10000), ("yrs", "Tenure", "years", 1, 10, 1, 5), ("rate", "Interest rate", "% a year", 1, 10, 0.25, 7)]),
 ("endow", "Everyday decisions", "Endowment vs term", "An endowment plan against term cover plus investing the difference.",
  [("eprem", "Endowment premium a year", "₹", 5000, 2000000, 5000, 100000), ("yrs", "Policy term", "years", 5, 40, 1, 20), ("mat", "Expected maturity value", "₹", 50000, 100000000, 50000, 3000000),
   ("tprem", "Term plan premium a year, same cover", "₹", 1000, 500000, 500, 12000), ("ret", "Return on investing the difference", "% a year", 1, 18, 0.5, 10)]),
]

GROUP_ORDER = ["Investing", "Goals", "Tax", "Everyday decisions"]

def field(f, cid):
    if f[0] == "sel":
        _, key, label, opts, default = f
        o = "".join(f'<option value="{v}"{" selected" if v == default else ""}>{t}</option>' for v, t in opts)
        return f'<div class="cf"><label for="{cid}-{key}">{label}</label><select id="{cid}-{key}" data-k="{key}">{o}</select></div>'
    key, label, unit, mn, mx, st, dv = f
    u = f'<span class="unit">{unit}</span>'
    return (f'<div class="cf"><label for="{cid}-{key}"><span>{label}</span>{u}</label><div class="cfrow">'
            f'<input class="range" type="range" min="{mn}" max="{mx}" step="{st}" value="{dv}" data-k="{key}" aria-label="{label}" tabindex="-1">'
            f'<input type="number" id="{cid}-{key}" min="{mn}" max="{mx}" step="{st}" value="{dv}" data-k="{key}" inputmode="decimal"></div></div>')

def calculators_body():
    index = ""
    for g in GROUP_ORDER:
        cards = "".join(f'<a href="#c-{c[0]}" data-cl="{c[0]}"><b>{c[2]}</b><span>{c[3]}</span></a>' for c in CALCS if c[1] == g)
        index += f'<div class="calc-group"><h2>{g}</h2><div class="calc-index">{cards}</div></div>'
    panels = ""
    for cid, g, title, sub, fields in CALCS:
        fs = "".join(field(f, cid) for f in fields)
        panels += (f'<section class="calc" id="c-{cid}" data-calc="{cid}" aria-labelledby="h-{cid}"><h2 id="h-{cid}">{title}</h2><p class="calc-sub">{sub}</p>'
                   f'<div class="cin">{fs}</div><div class="cout" aria-live="polite" data-out><span class="illus">Illustrative</span></div></section>')
    return f'''  <section class="page-hero"><div class="hero-bg" aria-hidden="true"></div><div class="wrap load"><p class="who">Resources</p>
    <h1>Calculators</h1>
    <p class="lede">Quick, illustrative answers for a client meeting: what a SIP could grow to, what a goal needs, what a loan costs. Every result shows its assumptions.</p></div></section>
  <section class="section" style="padding-top:0"><div class="wrap">
    <div data-calcs>{index}<div data-panels>{panels}</div></div>
    <p class="disc">Results are illustrative, based on the assumptions shown. They are not a guarantee of future returns or investment advice. Mutual fund investments are subject to market risks. Read all scheme-related documents carefully. Tax figures use the rules for listed equity and debt mutual funds as of 2025-26, before surcharge and cess; check the current rules or ask a tax professional before acting.</p>
  </div></section>
'''
