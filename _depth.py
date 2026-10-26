"""Depth sections for website v2 (Claude pass, 6 Oct 2026). Imported by build.py."""
from _features import directory, count

def dashboard_mock():
    tiles = [("Assets", "412.6", "Cr", "₹"), ("SIP book", "1.84", "Cr a month", "₹"), ("Client families", "1,286", "", ""), ("Net sales", "9.3", "Cr this month", "₹")]
    t = "".join(f'<div class="kpi"><span class="kpi-l">{l}</span><span class="kpi-v"><span class="cur">{w}</span><b data-count="{v}">{v}</b> <small>{u}</small></span><span class="spark"><svg viewBox="0 0 120 32" preserveAspectRatio="none"><path d="M0 26 L15 22 L30 24 L45 17 L60 19 L75 12 L90 14 L105 8 L120 9" pathLength="1"/></svg></span></div>' for l, v, u, w in tiles)
    return f'''<div class="dash mock" role="img" aria-label="Demo practice dashboard with invented figures">
  <div class="browser-bar"><i></i><i></i><i></i><span class="url">yourfirm.manthan.money/admin</span></div>
  <div class="dash-body">
    <div class="dash-head"><div><span class="dash-t">Good morning, Priya</span><span class="dash-s">Sahyadri Wealth &middot; Practice dashboard</span></div>
      <div class="dash-cta"><span class="mini-btn">Add client</span><span class="mini-btn">Place order</span><span class="mini-btn go">Renew mandates</span></div></div>
    <div class="kpis">{t}</div>
    <div class="dash-grid">
      <div class="dcard"><h5>Needs a person today</h5>
        <div class="q"><span class="chipx chip-red">Failed order</span><span>Redemption rejected by the exchange</span><span class="mini-btn">Open</span></div>
        <div class="q"><span class="chipx chip-amber">Reconciliation</span><span>2 folios do not match the registrar feed</span><span class="mini-btn">Assign</span></div>
        <div class="q"><span class="chipx chip-amber">Mandate</span><span>3 mandates expire this month</span><span class="mini-btn">Renew</span></div>
        <div class="q"><span class="chipx chip-blue">KYC</span><span>KYC refresh due for 4 families</span><span class="mini-btn">Request</span></div></div>
      <div class="dcard"><h5>Onboarding funnel</h5>
        <div class="fun"><span>Started</span><i style="--w:100%"></i><b>24</b></div>
        <div class="fun"><span>Profile done</span><i style="--w:79%"></i><b>19</b></div>
        <div class="fun"><span>KYC done</span><i style="--w:58%"></i><b>14</b></div>
        <div class="fun"><span>Account open</span><i style="--w:42%"></i><b>10</b></div>
        <h5 style="margin-top:16px">Reviews due this week</h5>
        <div class="revs"><span>Rao</span><span>Kulkarni</span><span>Deshmukh</span><span>+5</span></div></div>
    </div>
  </div></div>
  <p class="mock-cap">Illustrative visuals and data. For preview only.</p>'''

JOURNEY = [
  ("Sign in", "One-time code", "Your client signs in with a one-time code. No password to forget.",
   '<div class="jx-otp"><span>4</span><span>7</span><span>1</span><span>9</span><span>0</span><span class="on">_</span></div><p class="jx-cap">Code sent to your phone</p>'),
  ("Profile", "Who they are", "Personal details, family, accounts, address and contact, in one guided form.",
   '<div class="jx-f"><i>Full name</i><b>Ananya Rao</b></div><div class="jx-f"><i>Family members</i><b>3</b></div><div class="jx-f"><i>Bank account</i><b>Added</b></div>'),
  ("Risk profile", "A short questionnaire", "The risk questionnaire your firm uses. Your firm can make it mandatory.",
   '<p class="jx-q">If your investments fell for a few months, what would you do?</p><div class="jx-o">Wait it out</div><div class="jx-o on">Review with my adviser</div><div class="jx-o">Sell</div>'),
  ("Charter", "Your firm's rules", "Your investor charter, shown during onboarding where your firm turns it on.",
   '<div class="jx-doc"><b>Investor charter</b><i></i><i></i><i class="s"></i><i></i></div><div class="jx-o on">I have read this</div>'),
  ("Agreement", "Where it applies", "Where your firm's service needs an agreement, your template is part of onboarding.",
   '<div class="jx-doc"><b>Advisory agreement</b><i></i><i class="s"></i><i></i><i class="s"></i></div><p class="jx-cap">From your firm\'s template</p>'),
  ("Connect", "With consent", "With the client's consent, accounts held elsewhere come in through the account aggregator.",
   '<div class="jx-bank"><span>Bank A</span><b>Consent given</b></div><div class="jx-bank"><span>Bank B</span><b class="p">Fetching</b></div><p class="jx-cap">The client can see and withdraw consent</p>'),
  ("Home", "In your brand", "Goals, portfolio, plan and next actions, in your firm's own brand.",
   '<div class="jx-goal">Child\'s education<i style="--w:62%"></i></div><div class="jx-goal">Retirement<i style="--w:38%"></i></div><div class="jx-goal">Home<i style="--w:50%"></i></div>'),
]

def journey():
    steps = "".join(f'<button type="button" class="jstep" aria-pressed="{"true" if i == 0 else "false"}" data-j="{i}"><span class="jn">{i+1}</span><span><b>{t}</b><small>{s}</small></span></button>' for i, (t, s, d, x) in enumerate(JOURNEY))
    screens = "".join(f'<div class="jscreen{" on" if i == 0 else ""}" data-js="{i}"><p class="jx-h">{t}</p>{x}</div>' for i, (t, s, d, x) in enumerate(JOURNEY))
    descs = "".join(f'<p class="jdesc{" on" if i == 0 else ""}" data-jd="{i}">{d}</p>' for i, (t, s, d, x) in enumerate(JOURNEY))
    return f'''<div class="journey" data-journey>
  <div class="jsteps" role="group" aria-label="Client onboarding steps">{steps}</div>
  <div class="jstage">
    <div class="phone jphone" role="img" aria-label="Demo screens of the client experience during onboarding"><div class="phone-screen">
      <div class="ps-top"><span class="firm-mark">S</span><p>Sahyadri Wealth</p><small>Client view</small></div>
      <div class="jscreens">{screens}</div>
      <div class="ps-credit">Technology by Spring Money</div></div></div>
    <div class="jdescs" aria-live="polite">{descs}<p class="small muted" style="margin-top:14px">Illustrative visuals and data. For preview only. Steps your firm has not switched on are skipped.</p></div>
  </div>
</div>'''

ROLES = [
  ("Firm owner", ["The whole book on the practice dashboard", "Revenue, fee collection and flows", "Which features your firm switches on", "Your brand on every screen"]),
  ("Adviser or relationship manager", ["Meeting briefs and review drafts from Spring Sense", "Each family's goals, plan and holdings", "Reviews due and families at risk", "Approval on anything that reaches a client"]),
  ("Operations team", ["Execution centre for every order batch", "Reconciliation against registrar feeds", "One task list for the whole team", "Exceptions queued, not discovered late"]),
  ("Your client", ["Your firm's brand, in your client's hands", "Goals, portfolio and next actions", "Documents in one vault", "A direct line to your team"]),
]

def roles():
    return '<div class="roles">' + "".join(f'<div class="role"><h3>{r}</h3><ul>' + "".join(f"<li>{x}</li>" for x in xs) + '</ul></div>' for r, xs in ROLES) + '</div>'

PRESETS = '''<div class="presets">
  <div class="preset"><span class="pt">Start</span><h3>With what you use</h3><p>Switch on what your practice uses. Leave out what it doesn't.</p></div>
  <div class="preset"><span class="pt">Grow</span><h3>Add as you grow</h3><p>Turn more on when your team is ready. Nothing has to be replaced.</p></div>
  <div class="preset"><span class="pt">Connect</span><h3>Bring your own accounts</h3><p>Features that rely on your own vendor accounts, such as CKYC, fee payments or chat, switch on once those accounts are connected.</p></div>
</div>'''

FAQ_PLATFORM = [
 ("Is Manthan one platform?", "Yes. Your team and your clients work from the same records, so everyone sees the same picture."),
 ("Can we switch features on and off?", "Yes. Manthan is customised per firm. You start with what your practice uses and add more as you grow."),
 ("Which exchanges and registrars does it work with?", "BSE StAR MF, NSE and MF Utilities for mutual fund orders, and CAMS and KFintech feeds and CAS statements for holdings. More sources and products are planned with partners."),
 ("Will our clients see our brand?", "Yes. Your clients see your name, logo, colours and font. Spring Money is a small technology credit."),
 ("Can clients transact themselves?", "Where your firm switches it on, clients can buy, start a SIP or redeem. Payments go through payment links and mandates. The platform does not hold client money."),
 ("How do we bring existing clients across?", "We bring your clients, holdings and history across from your current system, and show your team what changes on day one."),
]
FAQ_SENSE = [
 ("When is Spring Sense available?", "Spring Sense is rolling out to firms now. Get in touch and we'll show you what it does today and when your firm can start."),
 ("Does Spring Sense give advice to our clients?", "No. Spring Sense drafts and flags for your team. A person on your team decides what reaches a client, and approves it first."),
 ("Can it send messages on its own?", "No. Every message it drafts waits for a person on your team to approve it."),
 ("How do our clients know something was AI-assisted?", "Every Spring Sense output carries an AI-generated label, and the professional who approved it stays named as responsible."),
 ("What can we ask it?", "Questions about your own firm's records: families, SIPs, tasks, documents, plans and fees. Answers are labelled AI-generated, and your team checks them before using them."),
 ("Where is our data processed, and is it used to train models?", "Ask us and we will answer in writing. We publish only what is confirmed."),
]
FAQ_HOME = [
 ("Who is Manthan built for?", "SEBI-registered investment advisors (RIAs), mutual fund distributors (MFDs), and wealth practices—whether you advise, distribute, or both."),
 ("Will our clients see the Spring Money brand?", "No. Your firm’s name, logo, brand colors, and typography lead every screen. Spring Money appears only as a subtle technology credit at the bottom."),
 ("Does Spring Money sell investments or offer financial advice?", "Never. Spring Money is strictly a technology infrastructure partner. Your firm retains complete ownership of client advice and product distribution under your own regulatory registrations."),
 ("What is Spring Sense AI?", "An integrated suite of AI capabilities designed to draft meeting briefs, prepare portfolio reviews, and check compliance rules. Nothing ever reaches a client without explicit advisor approval."),
 ("How is Manthan priced?", "3 basis points (0.03%) of assets managed on the platform per year, billed monthly. Simple, transparent pricing with all capabilities and updates included."),
 ("How do we experience a live demo?", "Reach out to schedule a private walk-through. We will configure an interactive demo environment tailored specifically to your firm’s brand and setup."),
]


# ------------------------------------------------------------------ self-onboarding + CRM (brief 6.1)
OB_STEPS = [
  ("Sign in", "<b>Instant, passwordless access.</b> Clients sign in to your branded app with a secure one-time passcode.",
   '<div class="jx-otp"><span>4</span><span>7</span><span>1</span><span>9</span><span>0</span><span class="on">_</span></div><p class="jx-cap">Code sent to the phone</p>', 0, 0),
  ("Profile", "<b>Guided profile collection.</b> Personal details, family structures, and contact data gathered in a single, intuitive form.",
   '<div class="jx-f"><i>Full name</i><b>Ananya Rao</b></div><div class="jx-f"><i>Family members</i><b>3</b></div><div class="jx-f"><i>City</i><b>Pune</b></div>', 1, 1),
  ("Risk profile", "<b>Tailored risk profiling.</b> Embedded questionnaires customized to your firm’s exact advisory framework.",
   '<p class="jx-q">If your investments fell for a few months, what would you do?</p><div class="jx-o">Wait it out</div><div class="jx-o on">Talk to my advisor</div><div class="jx-o">Sell</div>', 1, 1),
  ("KYC", "<b>Instant CKYC verification.</b> Automated PAN and CKYC record checks validate eligibility in seconds.",
   '<div class="jx-bank"><span>PAN</span><b>Verified</b></div><div class="jx-bank"><span>CKYC record</span><b>Found</b></div><div class="jx-bank"><span>KYC status</span><b>Validated</b></div>', 2, 2),
  ("Documents and e-sign", "<b>Paperless Aadhaar e-sign.</b> Agreements, charters, and client documents generated and e-signed without leaving the app.",
   '<div class="jx-doc"><b>Account opening form</b><i></i><i></i><i class="s"></i><i></i></div><div class="jx-o on">Signed with Aadhaar e-sign</div>', 2, 3),
  ("Bank and mandate", "<b>Seamless bank &amp; mandate setup.</b> Bank account verification and automated eNACH registration for effortless recurring investments.",
   '<div class="jx-bank"><span>Bank account</span><b>Verified</b></div><div class="jx-bank"><span>eNACH mandate</span><b class="p">Registering</b></div>', 3, 4),
  ("Exchange account", "<b>Automated exchange UCC creation.</b> Instant UCC creation across BSE Star MF and NSE so execution can begin immediately.",
   '<div class="jx-bank"><span>BSE StAR MF</span><b>UCC created</b></div><div class="jx-bank"><span>NSE</span><b>UCC created</b></div>', 3, 5),
  ("Welcome", "<b>Immediate client activation.</b> The client enters their personalized portal while your team receives a fully onboarded relationship.",
   '<div class="jx-goal">Child\'s education<i style="--w:12%"></i></div><div class="jx-goal">Retirement<i style="--w:6%"></i></div><p class="jx-cap">Welcome to Sahyadri Wealth</p>', 4, 6),
]
CRM_STAGES = ["Started", "Profile", "KYC", "Account open", "In your book"]
CRM_TASKS = ["Call to say hello", "Review the risk profile", "Check KYC documents", "Confirm the mandate", "Place the first SIP", "Book the first review"]

def obcrm():
    steps = "".join(f'<button type="button" class="jstep" aria-pressed="{"true" if i == 0 else "false"}" data-j="{i}"><span class="jn">{i+1}</span><span><b>{t}</b></span></button>' for i, (t, d, x, fs, tk) in enumerate(OB_STEPS))
    screens = "".join(f'<div class="jscreen{" on" if i == 0 else ""}" data-js="{i}"><p class="jx-h">{t}</p>{x}</div>' for i, (t, d, x, fs, tk) in enumerate(OB_STEPS))
    descs = "".join(f'<p class="jdesc{" on" if i == 0 else ""}" data-jd="{i}">{d}</p>' for i, (t, d, x, fs, tk) in enumerate(OB_STEPS))
    stages = "".join(f'<span{" class=on" if i == 0 else ""}>{s}</span>' for i, s in enumerate(CRM_STAGES))
    tasks = "".join(f'<li><i aria-hidden="true"></i>{t}</li>' for t in CRM_TASKS)
    data = ";".join(f"{fs},{tk}" for (t, d, x, fs, tk) in OB_STEPS)
    return (f'<div class="obcrm" data-obcrm="{data}">'
      '<div class="journey">'
      f'<div class="jsteps" role="group" aria-label="Client self-onboarding steps">{steps}</div>'
      '<div class="jstage">'
      '<div class="phone jphone" role="img" aria-label="Demo screens of a client onboarding in the firm\'s own app"><div class="phone-screen">'
      '<div class="ps-top"><span class="firm-mark">S</span><p>Sahyadri Wealth</p><small>Your client\'s app</small></div>'
      f'<div class="jscreens">{screens}</div>'
      '<div class="ps-credit">Technology by Spring Money</div></div></div>'
      f'<div class="jdescs" aria-live="polite">{descs}<p class="small muted" style="margin-top:14px">Where your firm\'s registration requires them, the agreement, investor charter and fee mandate steps appear too.</p></div>'
      '</div></div>'
      '<div class="crm" role="img" aria-label="Demo of the advisor\'s CRM, following the same client through onboarding">'
      '<div class="browser-bar"><i></i><i></i><i></i><span class="url">yourfirm.manthan.money/admin/leads</span></div>'
      '<div class="crm-body">'
      '<div class="crm-lead"><span class="ava2">AR</span><span><b>Ananya Rao</b><small>New lead · from your website</small></span><span class="chipx chip-blue" data-leadst>Lead</span></div>'
      f'<div><h5>Onboarding</h5><div class="crm-fun" style="margin-top:8px">{stages}</div></div>'
      f'<div><h5>Tasks created for your team</h5><ul class="crm-tasks" style="margin-top:8px">{tasks}</ul></div>'
      '<div class="crm-book"><span>Rao family</span><span data-book>Not in your book yet</span></div>'
      '</div></div></div>'
      '<p class="mock-cap">Illustrative visuals and data. For preview only.</p>')
