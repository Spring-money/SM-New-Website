"""Multi-asset section and SEO FAQ page (Claude, 6 Oct 2026)."""
import json

# status: live = transact today; track = tracked in the family picture; soon = with a planned partner; no = not offered
ASSETS = [
 ("Mutual funds", "Transact and track", "live", "Orders through BSE StAR MF, NSE and MF Utilities, with SIPs, redemptions and mandates. Holdings from CAMS and KFintech feeds and CAS."),
 ("Stocks and ETFs", "Track", "track", "Equity holdings sit in the family picture, so reviews see the whole portfolio."),
 ("Bonds", "Track \u00b7 transact coming", "soon", "Tracked today. A bond shelf is planned with our bond partners."),
 ("Fixed deposits", "Track \u00b7 transact coming", "soon", "Tracked today. Fixed deposits are planned with our deposits partner."),
 ("Global investing", "Coming", "soon", "Planned through GIFT City with our global investing partner."),
 ("Alternates (AIF, PMS)", "Track", "track", "Recorded as assets so the family's allocation is complete."),
 ("Insurance and loans", "Track", "track", "Cover and liabilities sit alongside investments, for plans that start from the full balance sheet."),
 ("Loans against mutual funds", "Coming", "soon", "Planned with our lending partner, where the rules allow."),
 ("Digital gold", "Not on the platform", "no", "Digital gold is unregulated, so we leave it out."),
]
STATUS = {"live": "Transact", "track": "Track", "soon": "Coming", "no": "Not offered"}

def assets_section(headline):
    tiles = "".join(f'<li class="as as-{s}"><div class="as-h"><h3>{n}</h3><span class="as-st">{st}</span></div><p>{d}</p></li>' for n, st, s, d in ASSETS)
    return f'''  <section class="section assets-sec" id="assets"><div class="wrap">
    <div class="assets-head reveal"><h2 class="mfsh">{headline}</h2>
      <p class="lede">Mutual funds are where most Indian firms start. They are rarely where a family's money ends. Spring Money puts the whole family in one picture, with everything they own in orbit around them.</p></div>
    <ul class="as-grid">{tiles}</ul>
    <p class="small muted" style="margin-top:16px">Coming = planned with a partner, not live today. What a firm can transact depends on its own registrations.</p>
  </div></section>
'''

FAQ_ALL = [
 ("About Spring Money", [
  ("What is Spring Money?", "Spring Money is the technology partner for India's wealth advisors: firms that advise, distribute or both. Its platform, Manthan, gives them integrated intelligence, their own brand in front of clients and a platform customised to how they work."),
  ("Is Spring Money an investment adviser or a mutual fund distributor?", "No. Spring Money is a technology provider. Your firm advises or distributes under its own registration. We build the tools your team and your clients use."),
  ("How does Spring Money make money?", "Firms pay 3 basis points (0.03%) of the assets they manage on Manthan, calculated annually and billed monthly. We take no commission or sales-linked payment from fund houses or other product makers."),
  ("Where is Spring Money based?", "Pune, at MIT TBI on the MIT WPU campus in Kothrud. The company is 2AN Technologies Private Limited."),
 ]),
 ("For mutual fund distributors", [
  ("What should a mutual fund distributor look for in software?", "That depends on the firm. Spring Money is built for firms that want onboarding, orders on BSE StAR MF, NSE and MF Utilities, reconciliation and portfolio reviews, in their own brand, on one platform."),
  ("Can I place mutual fund orders through BSE StAR MF, NSE and MFU?", "Yes. Purchases, SIPs, redemptions and mandates run through BSE StAR MF, NSE and MF Utilities, with an execution centre that shows every order batch."),
    ("Can we upgrade from our current system?", "Yes. We bring your clients, holdings and history across, and show your team what changes on day one. Holdings come in from CAMS and KFintech feeds and CAS statements."),
 ]),
 ("For investment advisers", [
  ("What software do SEBI-registered investment advisers use?", "Advisers need onboarding with an agreement, risk profiling, financial plans, recommendations, reviews and fee management. Spring Money brings these together, with the adviser's SEBI registration details where they belong."),
  ("Does Spring Money support fee-only advice?", "Yes. Advisory firms get fees and invoices, with fee collection through UPI AutoPay or bank transfer, and partners come in a no-payout mode that fits fee-only advice."),
  ("Can one firm both advise and distribute?", "Yes. Firms with both an RIA registration and an ARN run each client family in the right lane."),
 ]),
 ("Clients and brand", [
  ("Will my clients see my firm's brand?", "Yes. Your clients see your name, logo, colours and font. Spring Money appears only as a small technology credit."),
  ("Can clients see all their investments in one place?", "Yes. Everything a family owns, owes and is protected by sits in one picture. With the client's consent, accounts held elsewhere can come in through the account aggregator."),
  ("Does the platform hold client money?", "No. Clients pay through payment links and mandates. The platform never holds client money or units."),
 ]),
 ("Spring Sense", [
  ("What is Spring Sense?", "Personalised AI agents, rolling out to firms now. They prepare meeting briefs, draft portfolio reviews and client follow-ups, flag KYC expiry and reconciliation breaks, and answer questions from the firm's own records."),
  ("Does Spring Sense give investment advice?", "No. It drafts and flags for your team. Your adviser or distributor approves anything before it reaches a client, and every output is labelled AI-generated."),
 ]),
 ("Assets and products", [
  ("Which assets does Spring Money cover?", "The whole net worth. Mutual funds can be transacted today. Equities, ETFs, bonds, deposits, retirement savings (EPF, PPF, NPS), alternatives, physical assets, insurance and loans are tracked, through the account aggregator, registrar and exchange feeds, CAS statements or manual entry. Bonds, fixed deposits and loans against mutual funds are planned with partners."),
  ("Does Spring Money offer digital gold?", "No. Digital gold is unregulated, so it is not on the platform."),
 ]),
]

def faq_jsonld(pairs):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in pairs]}, ensure_ascii=False) + '</script>'

ORG_JSONLD = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "Organization", "name": "Spring Money",
    "legalName": "2AN Technologies Private Limited", "url": "https://www.springmoney.in", "logo": "https://www.springmoney.in/assets/logo.svg",
    "address": {"@type": "PostalAddress", "streetAddress": "MIT TBI, MIT WPU Campus, Kothrud", "addressLocality": "Pune", "addressRegion": "Maharashtra", "addressCountry": "IN"},
    "sameAs": ["https://www.youtube.com/@springmoney", "https://www.linkedin.com/company/springmoney/"]}) + '</script>'

def faq_page_body():
    nav = "".join(f'<a href="#q-{i}">{g}</a>' for i, (g, _) in enumerate(FAQ_ALL))
    groups = ""
    for i, (g, items) in enumerate(FAQ_ALL):
        qs = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items)
        groups += f'<section class="fqg" id="q-{i}"><h2>{g}</h2><div class="faq">{qs}</div></section>'
    allpairs = [p for _, items in FAQ_ALL for p in items]
    return f'''  <section class="page-hero"><div class="hero-bg" aria-hidden="true"></div><div class="wrap load"><p class="who">FAQ</p>
    <h1>Questions firms ask us.</h1>
    <p class="lede">About Spring Money, Manthan, Spring Sense and the assets we cover.</p></div></section>
  <section class="section" style="padding-top:0"><div class="wrap fq-wrap"><nav class="fdir-nav fq-nav" aria-label="FAQ groups">{nav}</nav><div>{groups}</div></div></section>
  {faq_jsonld(allpairs)}'''
