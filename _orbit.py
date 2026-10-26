"""Net-worth solar system (revision brief 6.1, 19 Oct 2026). Original illustrations; no third-party emoji.
The family sits at the centre; what it owns, owes and is protected by sits in orbit.
Sources per item follow the brief's 'likely source' column. Open item 3: AJ/product to confirm each before launch."""

I = {
 "mkt": '<path d="M3 20h18"/><path d="M5 16l4-5 3 3 6-7"/><path d="M15 7h3v3"/>',
 "dep": '<path d="M3 10 12 4l9 6"/><path d="M5 10v8M9.7 10v8M14.3 10v8M19 10v8"/><path d="M3 20h18"/>',
 "ret": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "ins": '<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.2 7.5 9.5 4.3-1.3 7.5-4.9 7.5-9.5V6Z"/><path d="m9 12 2 2 4-4"/>',
 "alt": '<rect x="3" y="13" width="7" height="7" rx="1.5"/><rect x="14" y="13" width="7" height="7" rx="1.5"/><rect x="8.5" y="4" width="7" height="7" rx="1.5"/>',
 "phy": '<path d="M4 11 12 5l8 6"/><path d="M6 10v10h12V10"/><path d="M10 20v-5h4v5"/>',
 "lia": '<rect x="2.5" y="5.5" width="19" height="13" rx="2"/><path d="M2.5 10h19M6 15h4"/>',
}
SVG = lambda k: f'<svg viewBox="0 0 24 24" aria-hidden="true">{I[k]}</svg>'

AA, FEED, CAS, MAN, EXCH, PART = "Account Aggregator", "Registrar feed", "CAS", "Manual entry", "Exchange", "Partner feed"

# key, name, status (live = transact today / track = track today / soon = coming with partners), ring, angle, status text, intro, items [(name, sources, note)]
GROUPS = [
 ("mkt", "Market-linked", "live", 1, 270, "Transact mutual funds · track the rest",
  "Equities, mutual funds, ETFs, bonds and other market securities, tracked together.",
  [("Mutual funds", [FEED, CAS, EXCH], "Transact today"), ("Equities and shares", [CAS, AA], "Track today"), ("ETFs", [CAS, AA], "Track today"),
   ("REITs and InvITs", [CAS, AA], "Track today"), ("Bonds and debentures", [CAS, MAN], "Track today · transact with partners"),
   ("Government securities", [AA, MAN], "Track today"), ("Sovereign gold bonds", [CAS, AA], "Track today")]),
 ("dep", "Deposits and cash", "track", 1, 0, "Track today",
  "Savings, current accounts and fixed deposits across banks.",
  [("Fixed deposits", [AA, MAN], "Track today · transact with partners"), ("Recurring deposits", [AA, MAN], "Track today"), ("Savings and current accounts", [AA, MAN], "Track today")]),
 ("ret", "Retirement", "track", 1, 90, "Track today",
  "Provident funds, pensions and retirement accounts, in full view.",
  [("EPF", [AA, MAN], "Track today"), ("PPF", [AA, MAN], "Track today"), ("NPS", [AA, MAN], "Track today")]),
 ("ins", "Insurance", "track", 1, 180, "Track today",
  "Life, health and general policies in one place, so gaps in cover are easy to spot.",
  [("Term life", [AA, MAN], "Track today"), ("Health", [AA, MAN], "Track today"), ("ULIPs", [AA, MAN], "Track today"),
   ("Endowment and traditional plans", [AA, MAN], "Track today"), ("General insurance", [MAN], "Track today")]),
 ("alt", "Alternatives", "track", 2, 315, "Track today",
  "PMS, AIFs, unlisted equity and private assets, included in asset allocation.",
  [("PMS", [MAN, PART], "Track today"), ("AIFs", [MAN, PART], "Track today"), ("Unlisted shares and ESOPs", [MAN], "Track today")]),
 ("phy", "Physical assets", "track", 2, 135, "Track today",
  "Real estate, precious metals and other tangible assets, alongside liquid portfolios.",
  [("Real estate", [MAN], "Track today"), ("Gold and jewellery", [MAN], "Track today"), ("Vehicles", [MAN], "Track today")]),
 ("lia", "Liabilities", "soon", 2, 225, "Track today · loans against funds coming",
  "Home loans, loans and credit lines, so net worth is accurate.",
  [("Home, car and personal loans", [AA, MAN], "Track today"), ("Loan against mutual funds", [PART], "Coming with partners"), ("Credit cards", [AA, MAN], "Track today")]),
]

ADVISER = '''<svg class="char ic" viewBox="0 0 64 64" aria-hidden="true"><rect x="12" y="22" width="40" height="34" rx="4" fill="#006E4A"/><path d="M8 24 32 8l24 16Z" fill="#0E5235"/><rect x="18" y="30" width="8" height="8" rx="1.5" fill="#B4E1D2"/><rect x="38" y="30" width="8" height="8" rx="1.5" fill="#B4E1D2"/><rect x="18" y="43" width="8" height="8" rx="1.5" fill="#F0FAF7"/><rect x="28" y="40" width="8" height="16" rx="1.5" fill="#FCFFFE"/><rect x="38" y="43" width="8" height="8" rx="1.5" fill="#F0FAF7"/></svg>'''

CLIENT = '''<svg class="char ic" viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="18" r="8" fill="#2E6FD8"/><path d="M18 52c0-9 6-15 14-15s14 6 14 15Z" fill="#2E6FD8"/><circle cx="14" cy="26" r="6" fill="#149B72"/><path d="M3 52c0-7 4-12 11-12 3 0 5 1 7 2-3 3-5 6-5 10Z" fill="#149B72"/><circle cx="50" cy="26" r="6" fill="#7D8180"/><path d="M61 52c0-7-4-12-11-12-3 0-5 1-7 2 3 3 5 6 5 10Z" fill="#7D8180"/></svg>'''

def planet(p, i):
    k, n, s, ring, ang, st = p[:6]
    return (f'<button type="button" class="pl pl-{s} r{ring}" style="--a:{ang}deg" data-pl="{i}" aria-pressed="{"true" if i == 0 else "false"}" aria-label="{n}: {st}">'
            f'<span class="pl-in"><span class="pl-dot">{SVG(k)}</span><span class="pl-nm">{n}</span></span></button>')

def detail(p, i):
    k, n, s, ring, ang, st, intro, items = p
    rows = "".join(f'<li><span>{nm}<span class="od-src">{" ".join(f"<span class=src>{x}</span>" for x in srcs)}</span></span><span class="small muted">{note}</span></li>' for nm, srcs, note in items)
    return f'<div class="od{" on" if i == 0 else ""}" data-od="{i}"><span class="od-ic od-{s}">{SVG(k)}</span><h3>{n}</h3><span class="od-st st-{s}">{st}</span><p>{intro}</p><ul class="nw-items">{rows}</ul></div>'

def orbit_section(headline):
    details = "".join(detail(p, i) for i, p in enumerate(GROUPS))
    return f'''  <section class="section assets-sec" id="assets"><div class="wrap">
    <div class="assets-head reveal"><h2 class="mfsh">{headline}</h2>
      <p class="nw-frame">Investments are only one part of the story. Manthan brings together everything a family owns, owes and protects in one view.</p></div>
    <div class="solar-wrap">
      <div class="solar" data-solar>
        <div class="orbit o1" aria-hidden="true"></div><div class="orbit o2" aria-hidden="true"></div>
        <div class="sun"><div class="sun-glow" aria-hidden="true"></div><div class="duo">{ADVISER}{CLIENT}</div><p class="sun-l">Your firm <span>&amp;</span> the family</p></div>
        <div class="orb-ring orb1">{"".join(planet(p, i) for i, p in enumerate(GROUPS) if p[3] == 1)}</div>
        <div class="orb-ring orb2">{"".join(planet(p, i) for i, p in enumerate(GROUPS) if p[3] == 2)}</div>
      </div>
      <div class="solar-side">
        <div class="od-box" aria-live="polite">{details}</div>
        <div class="key"><span><i class="k-live"></i>Transact today</span><span><i class="k-track"></i>Track today</span><span><i class="k-soon"></i>Coming with partners</span></div>
        <p class="small muted">Data sources: Account Aggregator, registrar feeds, CAS uploads or direct entry.</p>
      </div>
    </div>
  </div></section>
'''
