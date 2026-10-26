"""Feature directory for the website (revision brief, 19 Oct 2026).
Source: the product inventory (manthan-inventory.md, 5 Oct 2026) plus the springmoney.ai items the brief asks to bring back.
Every feature carries a status:
  ready   = live today, or close enough that we are comfortable announcing it as available
  planned = on the roadmap, not ready to announce; always shown with a "Planned" label
Anything not on the roadmap is left out. Labels are AJ's call (open item 4); the planned ones are listed in CHANGELOG-v1.2.md.
Notes: vendor = switches on once the firm's own vendor account is connected; new = rolling out to firms now; ai = AI, approved by a person."""

R, P = "ready", "planned"

GROUPS = [
 ("crm", "CRM and lead management", "Every prospect and conversation, from the first call.", [
  ("Lead capture", "Leads from your website, campaigns and referrals land in one list, with sync logs so none are lost.", R, ""),
  ("Pipeline", "Leads and opportunities move through stages your team can see at a glance.", R, ""),
  ("Calls, notes and meetings", "Call logs, notes and meetings kept with the lead or client they belong to.", R, ""),
  ("360° client profile", "Each family in one profile: members, accounts, holdings, goals and conversations.", R, ""),
  ("Lead scoring", "Leads ranked by how likely they are to become clients, so your team calls the right ones first.", P, ""),
 ]),
 ("onboarding", "Onboarding and KYC", "Bring a client in properly, once, with the checks your firm needs.", [
  ("Self-onboarding in your app", "Clients sign up on their own in your firm's app, with a one-time code. No password to forget.", R, ""),
  ("CKYC lookup", "Pull a client's KYC record during sign-up. Switches on once your KYC vendor account is connected.", R, "vendor"),
  ("KYC status", "See where each client's KYC stands, inside the onboarding flow.", R, ""),
  ("Risk profile", "A risk questionnaire your firm can make mandatory.", R, ""),
  ("Investor charter", "Your investor charter, shown during onboarding where your firm turns it on.", R, ""),
  ("Customer information form", "The details your onboarding needs, in one structured form.", R, ""),
  ("Regulatory details", "A dedicated onboarding step for regulatory details, for every client.", R, ""),
  ("Advisory agreement", "Your firm's agreement template, signed during onboarding where it applies.", R, ""),
  ("Aadhaar e-sign", "Agreements and forms signed digitally with Aadhaar-based e-sign.", R, "vendor"),
  ("Fee mandate", "Set how an advisory client pays your fee, through UPI AutoPay or bank transfer. Switches on once your payment vendor is connected.", R, "vendor"),
  ("Exchange accounts (UCC and CAN)", "Open the client's BSE StAR MF or NSE account (UCC) and MF Utilities account (CAN) from the platform.", R, ""),
  ("NACH and UPI AutoPay mandates", "Register eNACH, NACH or UPI AutoPay mandates for SIPs and fees.", R, ""),
  ("Welcome email", "Each new client gets a welcome email when onboarding starts.", R, ""),
  ("Video KYC", "Complete in-person verification over a recorded video call.", P, ""),
 ]),
 ("planning", "Data collection and financial planning", "Know the whole family before you plan or suggest anything.", [
  ("Family and personal details", "Personal details, family, bank accounts, address and contact.", R, ""),
  ("Goals", "Record goals, plan for them and track progress, projected against actual.", R, ""),
  ("Net worth", "Assets, liabilities and insurance, from feeds, statements, the account aggregator or manual entry.", R, ""),
  ("Cash flow", "Income and expenses, so plans start from real numbers.", R, ""),
  ("Financial plan", "A financial plan your clients can follow.", R, ""),
  ("Asset allocation", "Set and review the family's allocation.", R, ""),
  ("Suitability check", "Record the suitability check behind each recommendation.", R, ""),
  ("Calculators", "Capital gains tax, child education, lumpsum and SIP, retirement, SIP target, SIP to SWP, step-up SIP and step-up SIP target. Results are illustrative.", R, ""),
  ("Expense trackers", "Everyday and retirement expense trackers for the client.", R, ""),
 ]),
 ("portfolio", "Portfolio and performance reporting", "One picture of what each family holds, for your team and for the client.", [
  ("Multi-asset portfolio", "Mutual funds, equities, PMS, AIFs and other assets, grouped for the family.", R, ""),
  ("Holdings and performance", "Folio-level holdings, allocation and performance, with XIRR.", R, ""),
  ("Plan-wise allocation", "See how a portfolio splits across plan types.", R, ""),
  ("Transaction history", "Every transaction with its details, for you and your client.", R, ""),
  ("Daily valuation", "Values updated daily from NAVs, with an on-demand refresh.", R, ""),
  ("Assets under advice", "A view of the assets your firm advises on.", R, ""),
  ("Reports and insights", "Reports your team can run, brand and share with clients.", R, ""),
 ]),
 ("transactions", "Multi-asset execution", "Orders through the exchanges and utilities your firm already uses.", [
  ("BSE StAR MF", "Purchases, SIPs and other systematic transactions, with BSE mandates.", R, ""),
  ("NSE", "Transactions, systematic transactions and mandates, plus UCC creation.", R, ""),
  ("MF Utilities", "Account opening, mandates, transactions and systematic transactions.", R, ""),
  ("SIP management", "Start, pause, step up and stop SIPs, and see every instalment.", R, ""),
  ("Order tracker", "Every order and its status, from placed to allotted.", R, ""),
  ("Client-side transactions", "Clients can buy, start a SIP or redeem themselves, where your firm switches it on.", R, ""),
  ("Execution centre", "Every order batch and what needs attention, in one view.", R, ""),
  ("Payment links and mandates", "Clients pay through payment links and mandates. The platform does not hold client money.", R, ""),
  ("Multi-client basket", "Place the same transaction for several clients in one go.", P, ""),
 ]),
 ("operations", "Back-office operations", "The back office, on one list your whole team shares.", [
  ("Task centre", "My tasks, client tasks and team tasks, in one place.", R, ""),
  ("Registrar feeds", "Daily CAMS and KFintech feeds bring holdings and transactions in.", R, ""),
  ("CAS import", "Read a client's consolidated account statement (CAS PDF) to bring holdings across.", R, ""),
  ("Reconciliation", "Match orders and holdings to registrar feeds, folio by folio.", R, ""),
  ("Exception queue", "Failed orders, reconciliation breaks and expiring mandates in one queue.", R, "new"),
  ("Master data", "Schemes, AMCs, team members and settings, maintained in one place.", R, ""),
 ]),
 ("engagement", "Client portal and engagement", "Everything your client needs from you, in your brand.", [
  ("Meeting centre", "Meetings and minutes of meeting, shared with the client.", R, ""),
  ("Advice centre", "Advice your adviser has written, kept with the client.", R, ""),
  ("Actions tab", "What the client needs to do next: tasks, meetings and, for advisory clients, advice.", R, ""),
  ("Document vault", "Statements, agreements and documents, kept with each client.", R, ""),
  ("Account aggregator", "With the client's consent, bring in accounts held elsewhere: bank selection, consent and data fetch.", R, "vendor"),
  ("Chat with your team", "A chat room between your team and the client.", R, "vendor"),
  ("Support and notifications", "Support and notifications for the client.", R, ""),
  ("Your firm's details", "The client sees who their adviser or distributor is.", R, ""),
  ("WhatsApp and email campaigns", "Plan and send campaigns to clients and leads, with approval before anything goes out.", P, ""),
  ("Content library", "Fund factsheets and approved content your team can share.", P, ""),
 ]),
 ("revenue", "Revenue and billing", "What your practice earns, and what it is owed.", [
  ("Business MIS", "AUM, flows and revenue trends across the book.", R, ""),
  ("Brokerage tracking", "Trail brokerage by AMC, scheme and client, from the registrar files.", R, ""),
  ("Fee engine and invoicing", "Advisory fees calculated, invoiced and tracked to collection.", R, ""),
  ("Sub-broker payouts", "Monthly payout reports for sub-brokers, with each sub-broker's share worked out.", P, ""),
 ]),
 ("compliance", "Compliance and admin", "Records that stand up, and access that fits each role.", [
  ("Role-based access", "Each person sees what their role needs, and nothing else.", R, ""),
  ("Warnings that stay on", "The identity block and the standard risk warning cannot be edited out of templates.", R, ""),
  ("Audit trail", "Who changed what, and when, across the firm.", P, ""),
  ("AML and PEP screening", "Screen clients against sanctions and politically exposed person lists.", P, ""),
  ("Regulatory reporting logs", "Logs of the reports your firm files, kept for inspection.", P, ""),
 ]),
 ("dashboard", "Practice intelligence dashboard", "The state of the whole book on one screen.", [
  ("Book at a glance", "Assets, client families, SIP book, net sales, flows and book composition.", R, "new"),
  ("Revenue and fee collection", "Revenue and, for advisory firms, fee collection.", R, "new"),
  ("At risk and concentration", "Families at risk, concentration and drift, so reviews start in the right place.", R, "new"),
  ("Onboarding funnel", "Where every new client is in onboarding.", R, "new"),
  ("Team, reviews and plan health", "Team workload, reviews due, plan health and data quality.", R, "new"),
  ("Shortcuts", "Add a client, place an order, renew mandates and export, from the dashboard.", R, "new"),
  ("Client home", "Net worth, goals, allocation, cover and loans, statements and next actions, in your client's view.", R, "new"),
 ]),
 ("sense", "Spring Sense AI", "Personalised AI agents. A person approves before anything reaches a client.", [
  ("Meeting prep and notes", "A client brief before the meeting, and a summary with actions after it.", R, "ai"),
  ("Review drafts", "Drafts the review for your team to edit and approve.", R, "ai"),
  ("Client follow-ups", "Drafts reminders, SIP and birthday messages for approval.", R, "ai"),
  ("Ops and compliance checks", "Flags reconciliation breaks, KYC expiry and missing documents.", R, "ai"),
  ("Ask Spring Sense", "Answers your team's questions from your firm's own client records.", R, "ai"),
 ]),
]

NOTE = {"vendor": "Needs your vendor account", "new": "Rolling out", "ai": "AI, approved by a person", "": ""}
STATUS = {R: "Live", P: "Coming soon"}

def count(status=None):
    return sum(1 for g in GROUPS for f in g[3] if status is None or f[2] == status)

def status_chip(st):
    return f'<span class="stt stt-{st}">{STATUS[st]}</span>'

def directory():
    groups_html = ""
    for gid, gname, glede, items in GROUPS:
        rows = ""
        for name, desc, st, note in items:
            n = f'<span class="fnote fn-{note}">{NOTE[note]}</span>' if note else ""
            rows += (f'<li class="feat{" is-planned" if st == P else ""}" data-st="{st}" data-text="{(name + " " + desc).lower()}">'
                     f'<div class="feat-h"><h4>{name}</h4>{status_chip(st)}</div><p>{desc}</p>{n}</li>')
        groups_html += (f'<section class="fgroup" id="f-{gid}" data-group><div class="fgroup-head"><h3>{gname}</h3><p>{glede}</p>'
                        f'<span class="fcount" data-gcount></span></div><ul class="feats">{rows}</ul></section>')
    nav = "".join(f'<a href="#f-{g[0]}">{g[1]}</a>' for g in GROUPS)
    return f'''<div class="fdir" data-fdir>
  <div class="fdir-bar">
    <label class="fsearch"><span class="sr">Search features</span><input type="search" placeholder="Search features, e.g. SIP, KYC, mandate" data-fq></label>
    <div class="ffilter" role="group" aria-label="Filter by status">
      <button class="fchip" type="button" data-fst="all" aria-pressed="true">All</button>
      <button class="fchip" type="button" data-fst="ready" aria-pressed="false">Live</button>
      <button class="fchip" type="button" data-fst="planned" aria-pressed="false">Coming soon</button>
    </div>
    <span class="fshown" role="status" data-fshown></span>
  </div>
  <div class="fdir-body">
    <nav class="fdir-nav" aria-label="Feature groups">{nav}</nav>
    <div class="fdir-groups">{groups_html}<p class="fempty" data-fempty hidden>No features match. Try another word, or clear the filters.</p></div>
  </div>
  <p class="fine">Coming soon features are in development and not live yet. Nothing here is a launch date.</p>
</div>'''
