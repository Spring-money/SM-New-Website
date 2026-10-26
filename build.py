#!/usr/bin/env python3
"""Generates the static pages of the Spring Money website (v1.2, revision brief of 19 Oct 2026).
Run: python3 build.py   Output is plain HTML; no build step is needed to view the site."""
import os
from _shell import ROOT, GIT, WA, MAIL, SENSE_STATUS, page, cta, faq, soon, redirect_stub
from _depth import dashboard_mock, roles, PRESETS, FAQ_PLATFORM, FAQ_SENSE, FAQ_HOME, obcrm
from _features import directory, count, status_chip
from _orbit import orbit_section
from _assets import faq_page_body, faq_jsonld, ORG_JSONLD
from _company import about_body, principles_body, team_body
from _calc import calculators_body

APP = "yourfirm.manthan.money"
ADMIN = "yourfirm.manthan.money/admin"

# ------------------------------------------------------------------ Spring Sense scene
def sense_scene(compact=False):
    return f'''<div class="sense{' compact' if compact else ''}" data-sense data-sl="mfd">
  <div class="sense-window">
    <div class="browser-bar"><i></i><i></i><i></i><span class="url">{ADMIN}/spring-sense</span></div>
    <div class="sw-body">
      <aside class="sw-side" aria-hidden="true">
        <div class="firm"><span class="firm-mark">S</span><span class="firm-name">Sahyadri Wealth</span></div>
        <ul class="side-nav"><li>Clients</li><li>Task centre</li><li>Reconciliation</li><li class="on">Spring Sense</li><li>Reports</li><li>Chat</li></ul>
      </aside>
      <div class="sw-main">
        <div class="sw-top"><span class="sw-title" data-title>Meeting Prep &amp; Summaries</span><span class="ai-chip">AI-generated &middot; for your review</span></div>
        <div class="sw-scenes">
          <div class="scene" data-scene="1">
            <div class="s2col">
              <div class="card"><h4 class="a" style="--i:0">Before the meeting: client brief</h4>
                <div class="ln a" style="--i:1">Goals on file: child's education, retirement</div>
                <div class="ln a" style="--i:2">Since the last meeting: 2 SIPs ran, 1 nominee added</div>
                <div class="ln a" style="--i:3">Open item: KYC refresh due</div>
                <div class="ln a" style="--i:4">Talking points (draft) ready to edit</div></div>
              <div class="card"><h4 class="a" style="--i:5">After the meeting: summary and actions</h4>
                <div class="ln a" style="--i:6"><span class="tick done"></span>Send revised goal sheet</div>
                <div class="ln a" style="--i:7"><span class="tick"></span>Collect address proof</div>
                <div class="ln a" style="--i:8"><span class="tick"></span>Book next review in 3 months</div></div>
            </div>
            <p class="small muted a" style="--i:9;margin-top:10px">Drafted by Spring Sense. Edited and owned by your team.</p>
          </div>
          <div class="scene" data-scene="2">
            <div class="card draft-doc">
              <h4 class="a" style="--i:0">Review draft &middot; Rao family (demo)</h4>
              <p class="wipe" style="--i:0">Holdings across the family's accounts were brought together. Two SIPs ran on schedule.</p>
              <p class="wipe" style="--i:1">Suggestions for discussion: two items, listed below for you to edit.</p>
              <p class="wipe dim" style="--i:2">Next step: review with the client on Thursday.</p>
              <div class="actions a" style="--i:3"><span class="mini-btn">Edit</span><span class="mini-btn go press">Approve</span>
                <span class="statuses"><span class="st-wait">Awaiting approval by Priya Nair</span><span class="st-ok">Approved by Priya Nair &middot; ready to share</span></span></div>
            </div>
          </div>
          <div class="scene" data-scene="3">
            <div class="card">
              <h4 class="a" style="--i:0">Drafts waiting for your approval</h4>
              <div class="ln a" style="--i:1"><span style="flex:1"><b>SIP reminder</b><br><span class="muted">"Your SIP runs on the 5th. Nothing to do on your side."</span></span><span class="chip-swap" style="--i:0"><span class="c1 chipx chip-blue">Draft</span><span class="c2 chipx chip-green">Approved</span></span></div>
              <div class="ln a" style="--i:2"><span style="flex:1"><b>Birthday message</b><br><span class="muted">"Wishing you a happy birthday from all of us."</span></span><span class="chip-swap" style="--i:1"><span class="c1 chipx chip-blue">Draft</span><span class="c2 chipx chip-green">Approved</span></span></div>
              <div class="ln a" style="--i:3"><span style="flex:1"><b>Document request</b><br><span class="muted">"Please share a copy of your address proof."</span></span><span class="chipx chip-blue">Draft &middot; waiting for you</span></div>
            </div>
            <p class="small muted a" style="--i:5;margin-top:10px">Nothing is sent until a person on your team approves it.</p>
          </div>
          <div class="scene" data-scene="4">
            <div class="card">
              <h4 class="a" style="--i:0">3 items flagged this morning</h4>
              <div class="flag a" style="--i:1"><span class="chipx chip-amber">Reconciliation</span><span>One order does not match the registrar feed</span><span class="mini-btn">Open in task centre</span></div>
              <div class="flag a" style="--i:2"><span class="chipx chip-amber">KYC expiry</span><span>KYC expires in 12 days: Kulkarni family</span><span class="mini-btn">Assign</span></div>
              <div class="flag a" style="--i:3"><span class="chipx chip-red">Missing document</span><span>Address proof not on file: Rao family</span><span class="mini-btn">Request</span></div>
            </div>
          </div>
          <div class="scene" data-scene="5">
            <div class="ask-in a" style="--i:0"><span class="t typed">Which client families have a SIP ending this quarter?</span><span class="caret"></span></div>
            <div class="card a" style="--i:6;margin-top:10px">
              <h4>Answer drawn from your firm's client records</h4>
              <div class="ln">Three families have a SIP ending before 31 December (demo data).</div>
              <div class="ln"><span class="chipx chip-blue">Rao</span><span class="chipx chip-blue">Kulkarni</span><span class="chipx chip-blue">Deshmukh</span></div>
              <p class="small muted" style="margin-top:8px">AI-generated. Check it before you use it.</p>
            </div>
          </div>
        </div>
        <div class="sw-gate"><span class="gate-ico" aria-hidden="true"></span><span><b>Approval gate</b> Nothing leaves the platform until a person on your team approves it.</span></div>
      </div>
      <nav class="sw-rail" aria-label="Spring Sense AI capabilities">
        <p>AI Capabilities</p>
        <button class="agent-btn" aria-pressed="true"><i><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h9l4 4v14H6Z"/><path d="M14 3v5h5"/><path d="M9 12h7M9 16h5"/></svg></i>Meeting Prep &amp; Summaries</button>
        <button class="agent-btn" aria-pressed="false"><i><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 15l3-3 2 2 3-4"/><path d="M8 7h5"/></svg></i>Portfolio Review Generator</button>
        <button class="agent-btn" aria-pressed="false"><i><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v11H9l-5 4Z"/><path d="M8 10h8"/></svg></i>Automated Client Follow-ups</button>
        <button class="agent-btn" aria-pressed="false"><i><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.2 7.5 9.5 4.3-1.3 7.5-4.9 7.5-9.5V6Z"/><path d="m9 12 2 2 4-4"/></svg></i>Ops &amp; Compliance Verification</button>
        <button class="agent-btn" aria-pressed="false"><i><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v4M12 17v4M3 12h4M17 12h4"/><path d="m12 8 1.4 2.6L16 12l-2.6 1.4L12 16l-1.4-2.6L8 12l2.6-1.4Z"/></svg></i>Spring Sense Assistant</button>
      </nav>
    </div>
  </div>
</div>
<div class="sense-foot">
  <div class="grp"><button type="button" class="pp" aria-pressed="true"><span>Pause demo</span></button></div>
  <span>Illustrative visuals and data. For preview only.</span>
</div>'''

SENSE_BG = '<div class="sense-bg" aria-hidden="true"><svg viewBox="0 0 1300 1300"><circle cx="650" cy="650" r="620"/><circle cx="650" cy="650" r="470"/><circle cx="650" cy="650" r="330"/></svg></div>'
SENSE_BADGE = f'<span class="sense-badge"><img class="ss-ic" src="assets/spring-sense.svg" alt="">Spring Sense &middot; {SENSE_STATUS.lower()}</span>'

# ------------------------------------------------------------------ partners (Ready / Planned)
# name, logo file, what it does, live|plan, dark tile
PARTNERS = [
 ("BSE StAR MF", "bse-star-mf.png", "Orders", "live", False),
 ("NSE", "nse.svg", "Orders", "live", False),
 ("MF Utilities", "mfu.png", "Orders and KYC status", "live", False),
 ("CAMS", "cams.svg", "Registrar feed", "live", False),
 ("KFintech", "kfintech.svg", "Registrar feed", "live", False),
 ("CKYC", "zoop.svg", "via Zoop", "live", False),
 ("Finarkein", "finarkein.svg", "Account Aggregator: consent-based account data", "live", False),
 ("Digio", "digio.svg", "Aadhaar e-sign and e-mandates", "live", False),
 ("Signzy", "signzy.svg", "KYC", "live", False),
 ("OTPless", "otpless.svg", "Sign-in codes", "live", False),
 ("AiSensy", "aisensy.png", "WhatsApp messaging", "live", False),
 ("DigiLocker", None, "Documents with consent", "plan", False),
 ("MF Central", "mfcentral.svg", "CAS and service requests", "plan", False),
 ("smallcase Gateway", "smallcase-gateway.svg", "Model portfolios and stock baskets", "plan", False),
 ("Appreciate", "appreciate.webp", "Global investing", "plan", False),
 ("CMOTS", "cmots.png", "Market and fund data", "plan", False),
 ("CAS Parser", "cas-parser.png", "Holdings import", "plan", False),
 ("Volt Money", "volt-money.svg", "Loan against mutual funds", "plan", True),
 ("Blostem", None, "Fixed deposits", "plan", False),
 ("Nuvama", "nuvama.svg", "Wealth data and bonds", "plan", False),
 ("IndiaBonds", "indiabonds.png", "Bonds", "plan", True),
 ("The Wealth Company", None, "Fund house pilot", "plan", False),
 ("Exotel", "exotel.png", "Calling and recording", "plan", False),
]

def wall(mini=False):
    tiles = ""
    for n, f, sub, st, dark in PARTNERS:
        zc = {"cmots.png": "zoom", "mfu.png": "tall"}.get(f, "")
        attr = (' class="' + zc + '"') if zc else ""
        inner = (f'<img src="assets/partners/{f}" alt="{n}" {attr}>' if f else f'<span class="txt">{n}</span>')
        label, cls = ("Live", "state live") if st == "live" else ("Coming soon", "state plan")
        tiles += f'<li class="tile" data-state="{st}"><span class="logo{" dark" if dark else ""}">{inner}</span><span class="nm">{n}</span><span class="{cls}">{label}</span>' + ("" if mini else f'<span class="sub">{sub}</span>') + '</li>'
    tools = f'''<div class="wall-tools" role="group" aria-label="Filter partners">
  <button class="fchip" data-f="all" aria-pressed="true" type="button">All Rails</button>
  <button class="fchip" data-f="live" aria-pressed="false" type="button">Live Integrations</button>
  <button class="fchip" data-f="plan" aria-pressed="false" type="button">Pipeline</button>
  <span class="small muted" data-count role="status">{len(PARTNERS)} shown</span></div>'''
    return f'<div data-wall>{tools}<ul class="wall" style="list-style:none;margin:0;padding:0">{tiles}</ul><p class="wall-note">Logos belong to their respective owners. "Coming Soon" integrations represent active pipeline developments.</p></div>'

# ------------------------------------------------------------------ mocks
def planner_mock():
    return f'''<div class="mock" role="img" aria-label="Demo screen of the task centre, with invented data">
  <div class="browser-bar"><i></i><i></i><i></i><span class="url">{ADMIN}/tasks</span></div>
  <div class="portal">
    <div class="portal-side"><div class="firm"><span class="firm-mark">S</span><span class="firm-name">Sahyadri Wealth</span></div>
      <ul class="side-nav"><li>Clients</li><li>CRM</li><li class="on">Task centre</li><li>Reconciliation</li><li>Execution centre</li><li>Reports</li><li>Chat</li><li>Admin</li></ul></div>
    <div class="portal-main">
      <div class="pm-head"><span class="pm-title">Task centre &middot; this week</span><span class="badge">Preview</span></div>
      <div class="pm-cards"><div class="pm-card"><b>Open tasks</b><div class="bar"><span style="width:55%"></span></div></div><div class="pm-card"><b>Reviews due</b><div class="bar"><span style="width:35%"></span></div></div><div class="pm-card"><b>Breaks to clear</b><div class="bar"><span style="width:20%"></span></div></div></div>
      <div class="pm-table"><div class="pm-row"><span>Task</span><span>Client family</span><span>Status</span></div>
        <div class="pm-row"><span>Refresh KYC</span><span>Kulkarni</span><span class="chip">Due soon</span></div>
        <div class="pm-row"><span>Clear order mismatch</span><span>Deshmukh</span><span class="chip">Open</span></div>
        <div class="pm-row"><span>Prepare annual review</span><span>Rao</span><span class="chip">In progress</span></div>
        <div class="pm-row"><span>Share document</span><span>Joshi</span><span class="chip">Done</span></div></div>
    </div></div></div>
  <p class="mock-cap">Illustrative visuals and data. For preview only.</p>'''

def client_mock():
    return f'''<div class="mock" role="img" aria-label="Demo screen of the client view, with invented data">
  <div class="browser-bar"><i></i><i></i><i></i><span class="url">{APP}</span></div>
  <div class="cp-top"><span class="firm-mark">S</span><span class="nm">Sahyadri Wealth</span><span class="cp-tabs"><span class="on">Net worth</span><span>Portfolio</span><span>Goals</span><span>Documents</span></span></div>
  <div class="cp-body">
    <div><h4 style="font:600 12px/1.3 var(--body);color:var(--g500);margin-bottom:6px">Family net worth</h4>
      <svg class="ring" viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="44" fill="none" stroke="#F2F5F4" stroke-width="18"/><circle cx="60" cy="60" r="44" fill="none" stroke="#149B72" stroke-width="18" stroke-dasharray="118 276" transform="rotate(-90 60 60)"/><circle cx="60" cy="60" r="44" fill="none" stroke="#2E6FD8" stroke-width="18" stroke-dasharray="68 276" stroke-dashoffset="-120" transform="rotate(-90 60 60)"/><circle cx="60" cy="60" r="44" fill="none" stroke="#7D8180" stroke-width="18" stroke-dasharray="84 276" stroke-dashoffset="-190" transform="rotate(-90 60 60)"/></svg>
      <div class="legend"><span><i style="--c:#149B72"></i>Investments</span><span><i style="--c:#2E6FD8"></i>Property and deposits</span><span><i style="--c:#7D8180"></i>Retirement and other</span></div></div>
    <div><h4 style="font:600 12px/1.3 var(--body);color:var(--g500);margin-bottom:6px">Goals</h4>
      <div class="goal">Child's education<div class="bar"><span style="width:62%"></span></div></div>
      <div class="goal">Retirement<div class="bar"><span style="width:38%"></span></div></div>
      <div class="goal">Home down payment<div class="bar"><span style="width:50%"></span></div></div></div>
  </div></div>
  <p class="mock-cap">Illustrative visuals and data. For preview only.</p>'''

PHONE_HOME = '''<div class="ps-body rich">
  <p class="ps-hi">Hi Ananya</p>
  <div class="ps-net"><span>Family net worth</span><b>₹<em>1,42,18,600</em></b>
    <div class="mixbar"><i style="--w:46%;--c:#149B72"></i><i style="--w:24%;--c:#2E6FD8"></i><i style="--w:18%;--c:#7D8180"></i><i style="--w:12%;--c:#C4C9C8"></i></div>
    <div class="mixkey"><span><i style="--c:#149B72"></i>Funds</span><span><i style="--c:#2E6FD8"></i>Property</span><span><i style="--c:#7D8180"></i>EPF, PPF</span><span><i style="--c:#C4C9C8"></i>Other</span></div></div>
  <div class="ps-goal"><span>Child's education</span><i style="--w:62%"></i></div>
  <div class="ps-goal"><span>Retirement</span><i style="--w:38%"></i></div>
  <div class="ps-next"><span class="dot"></span><span>Next SIP on 5 Nov</span></div>
  <div class="ps-acts"><span>Actions</span><b>2</b></div>
</div>'''

def brand_phone(color="#9A3412", tint="#FDF0E8", firm="Sahyadri Wealth", mark="S"):
    return f'''<div class="phone" style="--t:{color};--t-tint:{tint};margin:0 auto" role="img" aria-label="Demo of a client app in a firm's own brand"><div class="phone-screen">
  <div class="ps-top"><span class="firm-mark">{mark}</span><p>{firm}</p><small>Home</small></div>
  {PHONE_HOME}
  <div class="ps-credit">Technology by Spring Money</div></div></div>'''

SWITCHES = [("Client self-onboarding", "Sign-up in your app, with KYC and e-sign", True), ("Advisory agreement step", "Where your registration needs it", True),
            ("Fee mandates", "UPI AutoPay or bank transfer", False), ("Orders on BSE, NSE and MFU", "For your team and, if you choose, your clients", True),
            ("Spring Sense", "Drafts for your team to approve", True), ("Client-side transactions", "Clients buy, start a SIP or redeem", False)]

def switches_mock():
    rows = "".join(f'<div class="swr"><span>{n}<small>{d}</small></span><button type="button" class="tg" role="switch" aria-checked="{"true" if on else "false"}" aria-label="{n}"></button></div>' for n, d, on in SWITCHES)
    return f'<div class="switches"><div class="sw-h"><span>Modules for Sahyadri Wealth</span><small>Firm settings</small></div>{rows}</div><p class="mock-cap">Interactive preview. Toggle modules above.</p>'

MARQ_TPL = '''
  <section class="marquee-sec" aria-label="Partners">
    <div class="wrap"><p class="marquee-label">Built on trusted rails</p></div>
    <div class="marquee"><div class="marquee-track">{MARQ}</div></div>
  </section>
'''
BOOST = ' class="boost"'

# ------------------------------------------------------------------ HOME
def home():
    stage = open(os.path.join(ROOT, "_home_hero.html")).read()
    items = "".join((f'<span class="mq{" dark" if d else ""}"><img src="assets/partners/{f}" alt="{n}" {BOOST if f in ("cmots.png","mfu.png") else ""}></span>' if f else f'<span class="mq txt">{n}</span>') for n, f, s, st, d in PARTNERS if st == "live")
    groups = [("crm","CRM &amp; Lead Management"),("onboarding","Onboarding &amp; KYC"),("planning","Data Collection &amp; Financial Planning"),("portfolio","Portfolio &amp; Performance Reporting"),
              ("transactions","Multi-Asset Execution"),("operations","Back-Office Operations"),("engagement","Client Portal &amp; Engagement"),("revenue","Revenue &amp; Billing"),
              ("compliance","Compliance &amp; Admin"),("dashboard","Practice Intelligence Dashboard"),("sense","Spring Sense AI")]
    body = stage + MARQ_TPL.replace("{MARQ}", items + items.replace('<span class="mq', '<span aria-hidden="true" class="mq').replace(' alt="', ' alt="" data-alt="')) + f'''
  <section class="section" id="value">
    <div class="wrap">
      <div class="section-head reveal"><h2>What changes when your practice runs on Manthan.</h2></div>
      <div class="p3">
        <div class="p3-row reveal">
          <div><span class="eyebrow">Practice Intelligence</span><h3>Grow your practice. Family by family.</h3>
            <p>Real-time book metrics, automated action items, and upcoming client reviews — unified in one place. Connected holdings, documents, and conversations mean your daily workflow prioritizes itself.</p>
            <a class="tlink" href="manthan.html#dashboard">Explore the practice dashboard</a></div>
          <div>{dashboard_mock()}</div>
        </div>
        <div class="p3-row flip reveal">
          <div><span class="eyebrow">Your brand</span><h3>Your brand. Front and center.</h3>
            <p>Give your clients a seamless digital portal under your own brand. From total net worth and goal tracking to upcoming SIPs, deliver complete visibility while maintaining full brand ownership.</p>
            <a class="tlink" href="#brand">Preview the client app</a></div>
          <div>{brand_phone()}<p class="mock-cap" style="text-align:center">Illustrative visuals and data. For preview only.</p></div>
        </div>
        <div class="p3-row reveal">
          <div><span class="eyebrow">Modular Architecture</span><h3>Built around the way you work.</h3>
            <p>Enable only the modules your firm needs. Seamlessly align roles, onboarding, compliance agreements, and fee mandates to match your exact regulatory setup and operational workflow.</p>
            <a class="tlink" href="features.html">Explore platform modularity</a></div>
          <div>{switches_mock()}</div>
        </div>
      </div>
    </div>
  </section>

''' + orbit_section("Beyond mutual funds. Beyond standard portfolios.") + f'''
  <section class="section tint" id="onboarding">
    <div class="wrap">
      <div class="section-head reveal"><span class="eyebrow">Self-onboarding and CRM</span><h2>Self-onboarding for them. Automated CRM for you.</h2>
        <p class="lede">Explore the interactive flow below. As a client completes onboarding on the left, Manthan automatically updates your CRM and assigns team workflows on the right.</p></div>
      {obcrm()}
    </div>
  </section>

  <section class="section" id="practice">
    <div class="wrap">
      <div class="section-head reveal"><h2>From first conversation to annual review.</h2></div>
      <div class="flow six" role="list"><span class="flow-line" aria-hidden="true"></span>
        <div class="step" role="listitem"><span class="step-num">1</span><h3>CRM</h3><p>Leads, interactions, and communication history—unified in one central pipeline.</p></div>
        <div class="step" role="listitem"><span class="step-num">2</span><h3>Onboarding</h3><p>Automated self-onboarding featuring KYC verification, Aadhaar e-sign, and eNACH mandates.</p></div>
        <div class="step" role="listitem"><span class="step-num">3</span><h3>Holistic View</h3><p>Consolidate net worth, liabilities, and insurance coverage across every data source.</p></div>
        <div class="step" role="listitem"><span class="step-num">4</span><h3>Execution</h3><p>Seamless order execution, tracking, and settlement across all supported product lines.</p></div>
        <div class="step" role="listitem"><span class="step-num">5</span><h3>Operations</h3><p>Automated reconciliation, task routing, and exception management for back-office teams.</p></div>
        <div class="step" role="listitem"><span class="step-num">6</span><h3>Client Reviews</h3><p>Bespoke performance reports and goal tracking—delivered under your firm’s brand.</p></div></div>
    </div>
  </section>

  <section class="section sense-sec on-dark" id="sense">
    {SENSE_BG}
    <div class="wrap">
      <div class="sense-head">
        {SENSE_BADGE}
        <h2>AI prepares the work. Your team stays in control.</h2>
        <p class="lede">Five specialized AI capabilities built into your daily workflow. Use them individually or whenever your team needs them.</p>
      </div>
      {sense_scene(compact=False)}
      <ul class="stat-line" style="justify-content:center;margin-top:34px"><li>Strict approval gates before client delivery</li><li>Clear labeling on all AI-generated drafts</li><li>Full advisor ownership &amp; compliance control</li></ul>
      <p style="text-align:center;margin-top:22px"><a class="tlink" href="spring-sense.html">Discover all 5 agents</a></p>
    </div>
  </section>

  <section class="section brandkit" id="brand">
    <div class="wrap bk-grid">
      <div class="reveal"><h2>Your brand. Front and center.</h2>
        <p class="lede" style="margin-top:20px">Deliver a bespoke, consumer-grade app experience under your own identity. Custom logos, primary palettes, and typography—powered seamlessly in the background.</p>
        <div class="bk-lists"><div><h3>What you customize</h3><ul><li>Firm name &amp; App Store identity</li><li>Brand colors &amp; primary accents</li><li>Custom typography &amp; fonts</li><li>Logo, icons, &amp; splash screens</li><li>Contact &amp; registration details</li></ul></div>
          <div class="fixed"><h3>What Manthan powers</h3><ul><li>UX architecture &amp; component layout</li><li>Accessible contrast &amp; WCAG standards</li><li>Regulatory disclaimers &amp; risk notices</li><li>Core infrastructure &amp; security</li><li>Minimal technology credit</li></ul></div></div></div>
      <div class="kit" data-kit>
        <div class="kit-panel"><h3>Preview your brand</h3>
          <div class="field"><label for="kit-name" class="kit-label" style="font-weight:500;margin:0">Firm name</label><input id="kit-name" type="text" placeholder="Your firm" maxlength="24" autocomplete="organization"></div>
          <div><p class="kit-label">Colour</p><div class="swatches" role="group" aria-label="Colour">
            <button aria-label="Rust" aria-pressed="true" data-c="#9A3412" data-tint="#FDF0E8" style="--sw:#9A3412"></button>
            <button aria-label="Royal blue" aria-pressed="false" data-c="#1D4ED8" data-tint="#EEF4FF" style="--sw:#1D4ED8"></button>
            <button aria-label="Violet" aria-pressed="false" data-c="#6D28D9" data-tint="#F3EEFF" style="--sw:#6D28D9"></button>
            <button aria-label="Teal" aria-pressed="false" data-c="#0F766E" data-tint="#E6F4F2" style="--sw:#0F766E"></button>
            <button aria-label="Charcoal" aria-pressed="false" data-c="#334155" data-tint="#EEF1F4" style="--sw:#334155"></button></div></div>
          <div><p class="kit-label">Font</p><div class="fonts" role="group" aria-label="Font">
            <button aria-pressed="true" data-font="Inter, sans-serif" style="font-family:Inter">Inter</button>
            <button aria-pressed="false" data-font="Poppins, sans-serif" style="font-family:Poppins">Poppins</button>
            <button aria-pressed="false" data-font="Montserrat, sans-serif" style="font-family:Montserrat">Montserrat</button></div></div>
          <p class="small muted">Live preview updates the client app interface in real time.</p></div>
        <div class="phone" style="--t:#9A3412;--t-tint:#FDF0E8" aria-label="Preview of your brand in front of your clients" role="img"><div class="phone-screen">
          <div class="ps-top"><span class="firm-mark" data-kit-mark>Y</span><p data-kit-name>Your firm</p><small>Your brand</small></div>
          {PHONE_HOME}
          <div class="ps-credit">Technology by Spring Money</div></div></div>
      </div>
    </div>
  </section>

  <section class="section" id="rules">
    <div class="wrap"><div class="section-head reveal"><h2>Built for compliance. Engineered for speed.</h2></div>
      <div class="rules-grid">
        <div class="rule"><h3>Rules built into every flow</h3><p>Onboarding, audit trails, and approval chains automatically align with Indian regulatory frameworks.</p></div>
        <div class="rule"><h3>Mandatory compliance shields</h3><p>Customize your templates freely—while mandatory risk warnings and identity blocks stay protected and intact.</p></div>
        <div class="rule"><h3>Unified client document vaults</h3><p>Agreements, statements, and signed disclosures securely vaulted under each client profile.</p></div></div></div>
  </section>

  <section class="section" style="padding-top:0" id="partners">
    <div class="wrap">
      <div class="section-head reveal"><h2>Deeply integrated. Built on trusted rails.</h2>
        <p class="lede">Direct connections across exchanges, registrars, KYC verification, e-sign platforms, and data aggregators - ready out of the box.</p></div>
      {wall()}
      <p style="margin-top:28px"><a class="tlink" href="partners.html">How partners fit in</a></p>
    </div>
  </section>

  <section class="section brandkit" id="depth"><div class="wrap split" style="align-items:center">
    <div class="reveal"><h2>Everything your practice needs. Pre-configured.</h2><p class="lede" style="margin-top:18px">From CRM and onboarding to orders, operations, billing and Spring Sense. Each feature is marked Ready or Planned.</p>
      <p style="margin-top:26px"><a class="btn btn-secondary" href="features.html">Explore all capabilities</a></p></div>
    <ul class="fteaser">''' + "".join(f'<li><a href="features.html#f-{g}"><b>{n}</b></a></li>' for g, n in groups) + '''</ul>
  </div></section>

  <section class="section" style="padding-bottom:0"><div class="wrap"><a class="yt yt-big" href="https://www.youtube.com/@springmoney" target="_blank" rel="noopener">
    <span class="yt-play" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7Z"/></svg></span>
    <span><b>Product walkthroughs &amp; deep dives</b><small>Watch detailed feature tours, platform updates, and practice management insights.</small></span><span class="yt-go">Watch on YouTube</span></a></div></section>

  <section class="section"><div class="wrap split"><div class="reveal"><h2>Frequently asked questions.</h2></div><div>''' + faq(FAQ_HOME) + '''</div></div></section>''' + faq_jsonld(FAQ_HOME) + ORG_JSONLD + f'''

  <section class="cta"><div class="wrap">
    <div class="cta-box"><h2>See Manthan in your brand.</h2><div class="hero-actions"><a class="btn btn-primary" href="{GIT}">Get in touch</a></div></div>
    <div class="doors">
      <a class="door" href="manthan.html"><h3>Explore Manthan</h3><p>The operating system powering your practice—and the white-labeled app your clients experience. Includes transparent pricing.</p><span class="go">See Manthan</span></a>
      <a class="door dark" href="spring-sense.html"><h3>Discover Spring Sense AI</h3><p>Specialized AI capabilities engineered to draft briefs, run compliance checks, and automate daily back-office preparation.</p><span class="go">See Spring Sense</span></a>
    </div></div></section>
'''
    return body

def write_home():
    page("index.html", "Spring Money: wealth management, personal to every client",
         "Manthan, from Spring Money, gives wealth advisors each family's full net worth, goals and conversations in one place, under the firm's own name.", home())

# ------------------------------------------------------------------ MANTHAN (was /platform)
PRICE_INCL = ["CRM and leads", "Self-onboarding and KYC", "Financial planning", "Net-worth tracking", "BSE, NSE and MFU execution", "Portfolio reporting",
              "Compliance and audit trail", "The client app in your brand", "Unlimited team members", "Spring Sense, as it rolls out"]

def pricing():
    incl = "".join(f"<li>{x}</li>" for x in PRICE_INCL)
    return f'''  <section class="section tint" id="pricing"><div class="wrap pricing">
    <div class="reveal"><span class="eyebrow">Pricing</span><h2>3 basis points of managed assets. Everything included.</h2>
      <p class="price-big" style="margin-top:22px">0.03% <small>of all managed assets on the platform</small></p>
      <p class="lede" style="margin-top:12px">Calculated annually and billed monthly.</p>
      <ul class="incl">{incl}</ul>
      <div class="hero-actions"><a class="btn btn-primary" href="{GIT}">Get in touch</a></div></div>
    <div class="pcalc" data-pcalc>
      <span class="illus">Illustration</span>
      <div style="margin-top:16px"><label class="lbl" for="pc-aum"><span>Managed assets</span><output for="pc-aum" data-pc-aum>₹100 crore</output></label>
        <input class="range" id="pc-aum" type="range" min="25" max="1000" step="5" value="100" aria-describedby="pc-note"></div>
      <div class="res"><div><span>Yearly fee</span><b data-pc-year>₹3,00,000</b></div><div><span>Monthly bill</span><b data-pc-month>₹25,000</b></div></div>
      <p class="fine" id="pc-note">For example, ₹100 crore of managed assets comes to ₹3,00,000 a year, billed as ₹25,000 a month. Calculated annually on managed assets and billed monthly. <span class="note-ph">GST treatment: to be confirmed</span></p>
    </div>
  </div></section>
'''

def write_manthan():
    def mod(id_, flip, tag, h, lede, bullets, mock):
        bl = "".join(f"<li><b>{x}</b> {y}</li>" for x, y in bullets)
        return f'''  <section class="module{' flip' if flip else ''}" id="{id_}"><div class="wrap module-grid">
    <div class="module-text reveal"><span class="tag">{tag}</span><h2>{h}</h2><p class="lede" style="margin-top:18px">{lede}</p><ul class="bullets">{bl}</ul></div>
    <div class="reveal">{mock}</div></div></section>
'''
    body = f'''  <section class="page-hero"><div class="hero-bg" aria-hidden="true"></div><div class="wrap load">
    <p class="who">Manthan, by Spring Money</p><h1 class="display">Manthan</h1>
    <p class="lede" style="font-size:22px;max-width:30em">The platform your practice runs on, and the app your clients know you by.</p>
    <div class="hero-actions"><a class="btn btn-primary" href="{GIT}">Get in touch</a><a class="tlink" href="#pricing">See pricing</a></div></div></section>
'''
    body += mod("workspace", False, "For your team", "Your team's workspace.", "Advisors, relationship managers and operations staff work from one list.",
        [("Clients and families.", "Each family, its members and accounts in one place."), ("CRM and task centre.", "Leads, follow-ups, reviews and to-dos on one shared list."), ("Reconciliation.", "Orders and holdings matched against your data sources."), ("Execution centre.", "Orders placed and tracked in one view."), ("Reports and insights.", "Reports your team can share with clients, in your brand."), ("Calculators, chat and admin.", "Calculator results are labelled illustrative.")], planner_mock())
    body += mod("experience", True, "For your clients", "The app your clients know you by.", "Your name, logo and colours, in front of every client.",
        [("Self-onboarding.", "Sign-up with the checks your firm needs."), ("Net worth.", "Everything the family owns, owes and is protected by."), ("Goals.", "Goals your clients can follow, projected against actual."), ("Connected accounts.", "Accounts held elsewhere, brought in with the client's consent through the account aggregator."), ("Investing and activity.", "Orders and their status in one place."), ("Document vault.", "Statements, agreements and documents, kept with the client.")], client_mock())
    body += f'''  <section class="section dash-sec" id="dashboard"><div class="wrap">
    <div class="section-head reveal"><span class="tag">Practice dashboard &middot; rolling out</span><h2>The whole book, on one screen.</h2><p class="lede">Assets, SIP book, net sales and flows at the top. Below them, what needs a person today, where new clients are stuck, and which reviews are due.</p></div>
    {dashboard_mock()}
    <div class="three" style="margin-top:40px"><div class="panel"><h3>Exceptions, not surprises</h3><p>Failed orders, reconciliation breaks, expiring mandates and KYC refreshes land in one queue for your team.</p></div><div class="panel"><h3>Where the book is moving</h3><p>Net sales, flows, concentration and drift, so reviews start with the families that need them.</p></div><div class="panel"><h3>The next step, from the dashboard</h3><p>Add a client, place an order, renew mandates or export, without leaving the screen.</p></div></div>
  </div></section>

  <section class="section tint" id="journey"><div class="wrap">
    <div class="section-head reveal"><span class="tag">Self-onboarding and CRM</span><h2>Your client signs up on their own. You watch it land in your book.</h2></div>
    {obcrm()}
  </div></section>

  <section class="section" id="roles"><div class="wrap">
    <div class="section-head reveal"><h2>Everyone in the firm works from the same records.</h2><p class="lede">Each person sees what their job needs.</p></div>
    {roles()}
  </div></section>

  <section class="section" id="setup" style="padding-top:0"><div class="wrap">
    <div class="section-head reveal"><h2>Customised to your firm.</h2><p class="lede">Switch on what your practice uses. Onboarding adapts to how your firm is registered: agreements, charters and fee mandates appear where they apply.</p></div>
    {PRESETS}
    <p style="margin-top:28px"><a class="tlink" href="features.html">Browse every feature, marked Ready or Planned</a></p>
  </div></section>
'''
    body += pricing()
    body += '''  <section class="section"><div class="wrap split"><div class="reveal"><h2>Questions firms ask.</h2></div><div>''' + faq(FAQ_PLATFORM + [("How is the price worked out?", "3 basis points (0.03%) of all the assets your firm manages on the platform, calculated annually and billed monthly. Everything on this page is included, with unlimited team members.")]) + '''</div></div></section>
''' + faq_jsonld(FAQ_PLATFORM)
    body += cta("See Manthan in your own brand.")
    page("manthan.html", "Manthan: the platform for wealth advisors | Spring Money", "Manthan is the platform a wealth advisor's practice runs on, and the app their clients know them by. 3 basis points of managed assets, everything included.", body)

# ------------------------------------------------------------------ FEATURES / FAQ
def write_features():
    body = f'''  <section class="page-hero"><div class="hero-bg" aria-hidden="true"></div><div class="wrap load"><p class="who">Features</p>
    <h1>Everything your practice runs on.</h1>
    <p class="lede">Search for what your team needs, or browse by group. Each feature is marked {status_chip("ready")} or {status_chip("planned")}.</p></div></section>
  <section class="section" style="padding-top:0"><div class="wrap">''' + directory() + '''</div></section>
  <section class="section brandkit"><div class="wrap">''' + PRESETS + '''</div></section>
'''
    body += cta("See the features your firm needs, set up for you.")
    page("features.html", "Features | Manthan by Spring Money", "Every feature in Manthan, marked Ready or Planned: CRM, onboarding and KYC, planning, portfolio, transactions, operations, billing, compliance, the practice dashboard and Spring Sense.", body)

def write_faq():
    page("faq.html", "FAQ | Spring Money", "Answers about Spring Money and Manthan: the platform for wealth advisors in India, orders on BSE StAR MF, NSE and MFU, client apps in your brand, Spring Sense and the assets covered.", faq_page_body() + cta("Still have a question? Ask us."))

# ------------------------------------------------------------------ SPRING SENSE
def write_sense():
    def ch(n, h, lede, detail, never):
        return f'''<div class="chapter"><span class="n">{n}</span><div><h3>{h}</h3><p style="margin-top:10px">{lede}</p></div><div class="w"><p><b>What it does.</b> {detail}</p><p><b>You stay in control.</b> {never}</p></div></div>'''
    body = f'''  <section class="sense-sec on-dark" style="padding:clamp(56px,8vw,104px) 0 clamp(72px,9vw,128px)">
    {SENSE_BG}
    <div class="wrap">
      <div class="sense-head load">{SENSE_BADGE}
        <h1>Agents that prepare the work. People who approve it.</h1>
        <p class="lede">Three families are due a review this week. Their briefs are ready. Spring Sense drafts, checks and flags; your team reviews, edits and approves. Nothing reaches a client until a person says so.</p>
        <div class="hero-actions" style="justify-content:center"><a class="btn btn-lime" href="{GIT}">Get in touch</a><a class="tlink" href="#agents">The five agents</a></div></div>
      {sense_scene()}
    </div></section>

  <section class="section"><div class="wrap">
    <div class="section-head reveal"><h2>Three rules that never switch off.</h2></div>
    <div class="rules-grid">
      <div class="rule"><h3>A person approves first</h3><p>Spring Sense drafts. A person on your team reads, edits and approves. Nothing reaches a client until they do.</p></div>
      <div class="rule"><h3>Labelled as AI-generated</h3><p>Every Spring Sense output carries an AI-generated label, so your team and your clients know what they are reading.</p></div>
      <div class="rule"><h3>Your named professional is responsible</h3><p>The advisor or relationship manager stays named on the work. Spring Sense is a tool in their hands.</p></div></div>
  </div></section>

  <section class="section sense-sec on-dark" id="agents"><div class="wrap">
    <div class="section-head reveal"><h2>Five agents. One approval gate.</h2><p class="lede">Each agent has a narrow job, and every one stops at the approval gate.</p></div>
    <div class="chapters">
''' + ch("01", "Meeting prep and notes", "A client brief before the meeting, and a summary with actions after it.",
        "The brief covers goals, recent activity and open items. Notes become tasks for your team.", "You edit the brief and the notes before anyone relies on them.") \
 + ch("02", "Review drafts", "Drafts the review so your professional starts from a page, not a blank screen.",
        "A review draft with suggestions for discussion, for your team to edit and approve.", "Nothing is shared with the client until your professional approves it.") \
 + ch("03", "Client follow-ups", "Drafts reminders, SIP messages and birthday messages for your team.",
        "Messages go out under your firm's name, after your approval.", "Each message waits for a person to approve it.") \
 + ch("04", "Ops and compliance checks", "Flags what your back office would otherwise find late.",
        "Reconciliation breaks, KYC expiry and missing documents, listed for your team.", "It flags. Your team decides what to do and records it.") \
 + ch("05", "Ask Spring Sense", "Answers your team's questions from your firm's own client records, past and present.",
        "Ask about families, SIPs, tasks and documents in your own records.", "Answers are labelled AI-generated. Your team checks them before using them.") \
 + '''    </div></div></section>

  <section class="section"><div class="wrap split">
    <div class="reveal"><h2>How approval works.</h2><p class="lede" style="margin-top:18px">The same four steps for every agent.</p></div>
    <div class="flow vertical" role="list" style="margin-top:0"><span class="flow-line" aria-hidden="true"></span>
      <div class="step" role="listitem"><span class="step-num">1</span><h3>An agent drafts or flags</h3><p>With an AI-generated label.</p></div>
      <div class="step" role="listitem"><span class="step-num">2</span><h3>A person reviews</h3><p>A professional on your team reads it and edits it.</p></div>
      <div class="step" role="listitem"><span class="step-num">3</span><h3>A person approves</h3><p>Only then can it reach a client.</p></div>
      <div class="step" role="listitem"><span class="step-num">4</span><h3>Your name stays on it</h3><p>The professional who approved it stays named as responsible.</p></div></div>
  </div></section>

  <section class="section brandkit"><div class="wrap two">
    <div class="panel"><h3>What Spring Sense does</h3><ul><li>Drafts briefs, reviews and messages for approval</li><li>Flags reconciliation breaks, KYC expiry and missing documents</li><li>Answers questions from your firm's own client records</li></ul></div>
    <div class="panel"><h3>What it does not do</h3><ul><li>It does not give advice, and it is not an AI advisor</li><li>It does not send anything to a client on its own</li><li>It does not replace your advisor or relationship manager</li></ul></div>
  </div></section>
'''
    body += '''  <section class="section"><div class="wrap split"><div class="reveal"><h2>Questions about Spring Sense.</h2></div><div>''' + faq(FAQ_SENSE) + '''</div></div></section>
''' + faq_jsonld(FAQ_SENSE)
    body += cta("See the agents working in your own firm.")
    page("spring-sense.html", "Spring Sense: AI agents for wealth advisors | Spring Money", f"Spring Sense ({SENSE_STATUS.lower()}) gives wealth advisors personalised AI agents for meeting prep, review drafts, follow-ups, ops checks and questions. A person approves before anything reaches a client.", body)

# ------------------------------------------------------------------ RIA / MFD (kept, rewritten in the new tone)
UPGRADE = ("Upgrading from your current system.", "We'll bring your clients, holdings and history across, and show your team what changes on day one.")

def write_mfd():
    body = f'''  <section class="page-hero"><div class="hero-bg" aria-hidden="true"></div><div class="wrap load">
    <div class="load"><p class="who">For wealth advisors &middot; MFD</p><h1>Your distribution practice, on one screen.</h1>
      <p class="lede">Self-onboarding, orders across BSE StAR MF, NSE and MFU, reconciliation and portfolio statements, under your firm's name. Your firm distributes under its own AMFI registration. Spring Money supplies the technology.</p>
      <div class="hero-actions"><a class="btn btn-primary" href="{GIT}">Get in touch</a><a class="tlink" href="#day">A day in the office</a></div></div>
  </div></section>

  <section class="section" id="day" style="padding-top:clamp(40px,6vw,80px)"><div class="wrap">
    <div class="section-head reveal"><h2>A day in your distribution office.</h2><p class="lede">The five jobs your team does every day, in one place.</p></div>
    <div class="flow" role="list"><span class="flow-line" aria-hidden="true"></span>
      <div class="step" role="listitem"><span class="step-num">1</span><h3>Onboard</h3><p>Self-onboarding with CKYC checks, and KYC status through MF Utilities.</p></div>
      <div class="step" role="listitem"><span class="step-num">2</span><h3>See the whole family</h3><p>CAMS and KFintech feeds, CAS statements and the account aggregator, so each family's holdings sit together.</p></div>
      <div class="step" role="listitem"><span class="step-num">3</span><h3>Place orders</h3><p>Purchases, SIPs and redemptions through BSE StAR MF, NSE or MFU, with eNACH and NACH mandates.</p></div>
      <div class="step" role="listitem"><span class="step-num">4</span><h3>Reconcile</h3><p>Orders and holdings matched to registrar feeds, with breaks cleared from the task centre.</p></div>
      <div class="step" role="listitem"><span class="step-num">5</span><h3>Review</h3><p>Portfolio statements and service reviews for each family, and scheme suggestions for your team to offer.</p></div></div>
  </div></section>

  <section class="module" id="work"><div class="wrap module-grid">
    <div class="module-text reveal"><span class="tag">Operations</span><h2>Orders and the back office, together.</h2><p class="lede" style="margin-top:18px">The execution centre shows every order batch and what needs attention. The task centre keeps your operations team on one list.</p>
      <ul class="bullets"><li><b>Execution centre.</b> Orders through BSE StAR MF, NSE and MFU in one view.</li><li><b>Payment links.</b> Clients pay through payment links. The platform does not hold client money.</li><li><b>Reconciliation.</b> Breaks listed, assigned and cleared.</li><li><b>Messages.</b> WhatsApp and email, and a document vault kept with each client.</li></ul></div>
    <div class="reveal"><div class="mock" role="img" aria-label="Demo execution centre screen with invented data"><div class="browser-bar"><i></i><i></i><i></i><span class="url">{ADMIN}/orders</span></div>
      <div class="portal"><div class="portal-side"><div class="firm"><span class="firm-mark">S</span><span class="firm-name">Sahyadri Wealth</span></div><ul class="side-nav"><li>Clients</li><li>Task centre</li><li>Reconciliation</li><li class="on">Execution centre</li><li>Reports</li></ul></div>
      <div class="portal-main"><div class="pm-head"><span class="pm-title">Execution centre &middot; today</span><span class="badge">Preview</span></div>
        <div class="pm-table"><div class="pm-row"><span>Order batch</span><span>Exchange</span><span>Status</span></div>
          <div class="pm-row"><span>SIP instalments</span><span>BSE StAR MF</span><span class="chip">Placed</span></div>
          <div class="pm-row"><span>New purchases</span><span>NSE</span><span class="chip">Awaiting payment</span></div>
          <div class="pm-row"><span>Redemptions</span><span>MF Utilities</span><span class="chip">Needs attention</span></div></div>
        <div class="pm-cards"><div class="pm-card"><b>Mandates</b><div class="bar"><span style="width:70%"></span></div></div><div class="pm-card"><b>Breaks</b><div class="bar"><span style="width:25%"></span></div></div><div class="pm-card"><b>Reviews</b><div class="bar"><span style="width:50%"></span></div></div></div></div></div></div>
      <p class="mock-cap">Illustrative visuals and data. For preview only.</p></div>
  </div></section>

  <section class="section sense-sec on-dark"><div class="wrap sense-split">
    <div class="reveal">{SENSE_BADGE}<h2>Drafts for your team, approved by a person.</h2>
      <p class="lede" style="margin-top:20px">Agents prepare service-meeting briefs, portfolio summaries and client follow-ups, and flag KYC expiry and reconciliation breaks. They do not give advice. A person on your team approves everything before it reaches a client.</p>
      <p style="margin-top:26px"><a class="tlink" href="spring-sense.html">Meet Spring Sense</a></p></div>
    <div class="panel dark"><h3>What your team sees</h3><ul><li>Portfolio summary draft, for your team to edit</li><li>Follow-up drafts for SIP reminders and birthdays</li><li>A flag when KYC is about to expire</li><li>An AI-generated label on every output</li></ul></div>
  </div></section>

  <section class="section brandkit"><div class="wrap split">
    <div class="reveal"><h2>{UPGRADE[0]}</h2><p class="lede" style="margin-top:18px">{UPGRADE[1]}</p>
      <div class="hero-actions"><a class="btn btn-primary" href="{GIT}">Get in touch</a></div></div>
    <div>{faq([("Does Spring Money sell or suggest funds to our clients?", "No. Spring Money is a technology provider. Your firm distributes, under your own registration, and your clients' relationship is with you."),
      ("Will our clients see Spring Money?", "Only as a small technology credit. Your name, logo, colours and font are in front."),
      ("Does the platform hold client money?", "No. Clients pay through payment links and mandates. The platform does not hold client money.")])}</div>
  </div></section>
'''
    body += cta("See your distribution practice in your own brand.")
    page("for-mfd.html", "For mutual fund distributors | Manthan by Spring Money", "Manthan for mutual fund distributors: self-onboarding, orders across BSE StAR MF, NSE and MFU, reconciliation and portfolio statements, in your own brand.", body)

def write_ria():
    body = f'''  <section class="page-hero"><div class="hero-bg" aria-hidden="true"></div><div class="wrap load">
    <div class="load"><p class="who">For wealth advisors &middot; RIA</p><h1>Your advisory practice, prepared for every client.</h1>
      <p class="lede">Self-onboarding with your agreement step, financial plans, recommendations, reviews and fees, in your own brand.</p>
      <div class="hero-actions"><a class="btn btn-primary" href="{GIT}">Get in touch</a><a class="tlink" href="#flow">Your advisory workflow</a></div></div>
  </div></section>

  <section class="section" id="flow" style="padding-top:clamp(40px,6vw,80px)"><div class="wrap">
    <div class="section-head reveal"><h2>Your advisory workflow, in order.</h2><p class="lede">From the first meeting to the yearly review.</p></div>
    <div class="flow" role="list"><span class="flow-line" aria-hidden="true"></span>
      <div class="step" role="listitem"><span class="step-num">1</span><h3>Onboard</h3><p>Self-onboarding with CKYC checks, your advisory agreement and fee mandate.</p></div>
      <div class="step" role="listitem"><span class="step-num">2</span><h3>Plan</h3><p>Financial plans and goals your clients can follow, built on their whole net worth.</p></div>
      <div class="step" role="listitem"><span class="step-num">3</span><h3>Advise and review</h3><p>Recommendations and reviews, with holdings from CAMS and KFintech feeds, CAS statements and the account aggregator.</p></div>
      <div class="step" role="listitem"><span class="step-num">4</span><h3>Charge fees</h3><p>Fees and invoices, with collection through UPI AutoPay or bank transfer.</p></div>
      <div class="step" role="listitem"><span class="step-num">5</span><h3>Keep records together</h3><p>Agreements, statements and notes are kept with each client, in one vault.</p></div></div>
  </div></section>

  <section class="module" id="work"><div class="wrap module-grid">
    <div class="module-text reveal"><span class="tag">Planning</span><h2>Plans and reviews your clients can follow.</h2><p class="lede" style="margin-top:18px">Your advisor builds the plan and the review. Your client sees goals, progress and next steps in your brand.</p>
      <ul class="bullets"><li><b>Financial plan.</b> Goals and progress your clients can follow.</li><li><b>Advisory review.</b> A structured review your team can run on a schedule.</li><li><b>Recommendations.</b> Written and owned by your advisor.</li><li><b>Fees and invoices.</b> Fee screens and mandates for your team.</li></ul></div>
    <div class="reveal"><div class="mock" role="img" aria-label="Demo advisory review screen with invented data"><div class="browser-bar"><i></i><i></i><i></i><span class="url">{ADMIN}/reviews</span></div>
      <div class="portal"><div class="portal-side" style="background:#1D4ED8"><div class="firm"><span class="firm-mark">D</span><span class="firm-name">Demo Advisory</span></div><ul class="side-nav"><li>Clients</li><li>Financial plan</li><li class="on">Advisory review</li><li>Recommendations</li><li>Fees and invoices</li><li>Task centre</li></ul></div>
      <div class="portal-main" style="--t:#1D4ED8;--t-tint:#EEF4FF"><div class="pm-head"><span class="pm-title">Advisory reviews &middot; this month</span><span class="badge">Preview</span></div>
        <div class="pm-table"><div class="pm-row"><span>Client family</span><span>Review</span><span>Status</span></div>
          <div class="pm-row"><span>Rao</span><span>Annual</span><span class="chip">Scheduled</span></div>
          <div class="pm-row"><span>Kulkarni</span><span>Half-yearly</span><span class="chip">Draft ready</span></div>
          <div class="pm-row"><span>Deshmukh</span><span>Annual</span><span class="chip">Shared</span></div></div>
        <div class="pm-cards"><div class="pm-card"><b>Plans</b><div class="bar"><span style="width:60%"></span></div></div><div class="pm-card"><b>Reviews</b><div class="bar"><span style="width:45%"></span></div></div><div class="pm-card"><b>Invoices</b><div class="bar"><span style="width:30%"></span></div></div></div></div></div></div>
      <p class="mock-cap">Illustrative visuals and data. For preview only.</p></div>
  </div></section>

  <section class="section sense-sec on-dark"><div class="wrap sense-split">
    <div class="reveal">{SENSE_BADGE}<h2>Review drafts. Recommendations stay yours.</h2>
      <p class="lede" style="margin-top:20px">Agents prepare meeting briefs and review drafts, draft client follow-ups, and flag KYC expiry and missing documents. Recommendations remain the advisor's. Your advisor approves everything before it reaches a client.</p>
      <p style="margin-top:26px"><a class="tlink" href="spring-sense.html">Meet Spring Sense</a></p></div>
    <div class="panel dark"><h3>What your team sees</h3><ul><li>Review draft, with the points to cover</li><li>Meeting brief before, summary and actions after</li><li>A flag when documents are missing</li><li>An AI-generated label on every output</li></ul></div>
  </div></section>

  <section class="section brandkit"><div class="wrap split">
    <div class="reveal"><h2>{UPGRADE[0]}</h2><p class="lede" style="margin-top:18px">{UPGRADE[1]}</p>
      <div class="hero-actions"><a class="btn btn-primary" href="{GIT}">Get in touch</a></div></div>
    <div>{faq([("Does Spring Money give advice?", "No. Advice is given by your firm. Spring Money is a technology provider. Your recommendations and plans are yours."),
      ("Will our clients see our brand?", "Yes. Your clients see your name, logo, colours and font. Spring Money is a small technology credit."),
      ("Our firm holds both registrations. Can one platform handle both?", "Yes, kept apart. Each client family sits under one registration only, and advisory and distribution records stay separate.")])}</div>
  </div></section>
'''
    body += cta("See your advisory practice in your own brand.")
    page("for-ria.html", "For investment advisers | Manthan by Spring Money", "Manthan for SEBI-registered investment advisers: self-onboarding with your agreement, financial plans, recommendations, reviews and fees, in your own brand.", body)

# ------------------------------------------------------------------ PARTNERS
def write_partners():
    body = '''  <section class="page-hero"><div class="hero-bg" aria-hidden="true"></div><div class="wrap load"><p class="who">Integrations and partners</p>
    <h1>Integrated with rails and partners built for modern wealth management.</h1>
    <p class="lede">The exchanges, registrars, KYC and signing systems your operations team works with every day, and the partners we are adding.</p></div></section>
  <section class="section" style="padding-top:0"><div class="wrap">''' + wall() + '''</div></section>
  <section class="section brandkit"><div class="wrap two">
    <div class="panel"><h3>Ready</h3><p>Connections Manthan uses today: exchanges and utilities for orders, registrar feeds and the account aggregator for holdings, and systems for KYC, e-sign, mandates, sign-in codes and WhatsApp.</p></div>
    <div class="panel"><h3>Planned</h3><p>Partners we are working towards. They are not live integrations, and nothing here is a launch date.</p></div>
  </div></section>'''
    body += cta("Tell us which connections your firm needs.")
    page("partners.html", "Integrations and partners | Spring Money", "The exchanges, registrars, KYC and signing systems Manthan works with, and the partners Spring Money is adding.", body)

# ------------------------------------------------------------------ SECURITY / ABOUT / LEGAL / CONTACT
def write_security():
    body = '''  <section class="page-hero"><div class="hero-bg" aria-hidden="true"></div><div class="wrap load"><p class="who">Security</p><h1>How we handle data.</h1>
    <p class="lede">Short and plain. We publish only what we can stand behind today.</p></div></section>
  <section class="section" style="padding-top:0"><div class="wrap three">
    <div class="panel"><h3>Sign-in</h3><p>Clients and teams sign in with one-time codes.</p></div>
    <div class="panel"><h3>Each firm on its own set-up</h3><p>Every firm has its own subdomain, configuration and branding.</p></div>
    <div class="panel"><h3>Role-based access</h3><p>Each person on your team sees what their role needs.</p></div>
    <div class="panel"><h3>Documents with the client</h3><p>Agreements, statements and documents sit with each client in a vault.</p></div>
    <div class="panel"><h3>No client money</h3><p>The platform does not hold client money. Payments go through payment links and mandates.</p></div>
    <div class="panel"><h3>People approve AI work</h3><p>Spring Sense outputs are labelled AI-generated, and a person approves before anything reaches a client.</p></div>
  </div></section>
  <section class="section brandkit"><div class="wrap"><div class="note-box">We have not published certifications, where data is processed, or retention terms on this page, because we publish only what is confirmed. If your firm needs these answers, ask us and we will reply in writing.</div></div></section>'''
    body += cta("Ask us your data questions.")
    page("security.html", "How we handle data | Spring Money", "A short, plain page on how Spring Money handles data. Only confirmed facts are published.", body)

def write_about():
    page("about.html", "About Spring Money", "Spring Money is the technology partner for India's wealth advisors. Its platform, Manthan, runs each firm's practice under its own name.", about_body() + cta("Get to know us."))
    page("principles.html", "Principles and practices | Spring Money", "The principles Spring Money builds by, and the practices that keep us to them.", principles_body() + cta("Ask us how we apply them to your firm."))
    page("team.html", "Team | Spring Money", "The people building Spring Money, in Pune.", team_body() + cta("Meet the team."))

def write_legal(name, title, headings, extra=""):
    hs = "".join(f"<h2>{h}</h2><p><span class=\"pending\" style=\"color:#7A4A00;border-color:#B45309\">Text to be written by legal</span></p>" for h in headings)
    body = f'''  <section class="page-hero"><div class="hero-bg" aria-hidden="true"></div><div class="wrap load"><p class="who">Legal</p><h1>{title}</h1></div></section>
  <section class="section" style="padding-top:0"><div class="wrap legal">
    <div class="todo">To be written by legal.<small>This page is a placeholder. It holds the headings only, and no policy text has been drafted.</small></div>{extra}{hs}</div></section>'''
    page(name, f"{title} | Spring Money", f"{title} for Spring Money. Placeholder page: to be written by legal.", body)

def write_contact():
    t = open(os.path.join(ROOT, "_demo_body.html")).read()
    page("get-in-touch.html", "Get in touch | Spring Money", "Get in touch with Spring Money to see Manthan, set up the way your firm works. Or reach us on WhatsApp or at sayhi@spring.money.", t)

def write_calculators():
    page("calculators.html", "Calculators | Spring Money", "Free, illustrative calculators for wealth advisors and their clients: SIP, step-up SIP, retirement, child education, EMI, buy vs rent, FD vs RD and more.", calculators_body() + cta("Use these calculators with your clients, in your own brand."))

# ------------------------------------------------------------------ PHASE 2 SLOTS (routes exist, hidden from search)
def write_soon(name, title, who, lede):
    body = f'''  <section class="page-hero"><div class="hero-bg" aria-hidden="true"></div><div class="wrap load"><p class="who">{who}</p><h1>{title}</h1>
    <div class="soon-box" style="margin-top:28px"><p>{soon()}</p><p class="lede" style="margin-top:14px">{lede}</p>
      <div class="hero-actions"><a class="btn btn-primary" href="{GIT}">Get in touch</a></div></div></div></section>
'''
    page(name, f"{title} | Spring Money", lede, body, robots="noindex")

def write_redirects():
    with open(os.path.join(ROOT, "_redirects"), "w") as f:
        f.write("/platform       /manthan.html        301!\n/platform.html  /manthan.html        301!\n/demo           /get-in-touch.html   301!\n/demo.html      /get-in-touch.html   301!\n")
    redirect_stub("platform.html", "manthan.html", "Manthan | Spring Money")
    redirect_stub("demo.html", "get-in-touch.html", "Get in touch | Spring Money")

if __name__ == "__main__":
    write_home(); write_manthan(); write_features(); write_faq(); write_sense(); write_mfd(); write_ria(); write_partners()
    write_security(); write_about(); write_contact(); write_calculators()
    write_legal("privacy.html", "Privacy policy", ["Who we are", "What we collect on this website", "How we use it", "Your choices", "Contact"])
    write_legal("terms.html", "Terms of use", ["Using this website", "Our services", "Intellectual property", "Limits of liability", "Contact"])
    write_legal("grievances.html", "Grievances", ["Where to write to us", "Grievance officer: name, email, phone", "How we handle a grievance"],
                '<p class="muted">Contact details for the grievance officer are pending legal review. No names or numbers are shown until they are confirmed.</p>')
    write_legal("takedown.html", "Takedown policy", ["What this policy covers", "How to ask us to remove content", "What we need from you", "How we respond", "Contact"])
    write_soon("for-pms.html", "For portfolio managers", "For wealth advisors · PMS", "Manthan for PMS firms is coming soon. Get in touch if you'd like to hear when it's ready.")
    write_soon("for-ra.html", "For research analysts", "For wealth advisors · RA", "Manthan for research analysts is coming soon. Get in touch if you'd like to hear when it's ready.")
    write_soon("for-amc.html", "For AMCs", "For AMCs", "Spring Money for asset management companies is coming soon. Get in touch to talk to us.")
    write_soon("clients.html", "Clients", "About us", "Our client stories are coming soon.")
    write_soon("find-an-advisor.html", "Find an advisor", "Resources", "A directory of SEBI-registered investment advisers is coming soon.")
    write_redirects()
    print("built")
