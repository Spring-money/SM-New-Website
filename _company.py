"""Company pages for website v2 (Claude, 6 Oct 2026): About, Team, Principles and practices, Clients.
Sources: knowledge/company.md, people.md, decisions.md, mfd-vs-ria.md. Anything unconfirmed renders with a
visible "pending" chip; see README."""

PENDING = '<span class="pend">{}</span>'

def subnav(cur):
    items = [("about.html", "About us"), ("principles.html", "Principles and practices"), ("team.html", "Team"), ("clients.html", "Clients")]
    return '<nav class="subnav" aria-label="Company"><div class="wrap">' + "".join(
        f'<a href="{h}"' + (' aria-current="page"' if h == cur else '') + f'>{t}</a>' for h, t in items) + '</div></nav>'

# ---------------------------------------------------------------- ABOUT
def about_body():
    return subnav("about.html") + '''
  <section class="page-hero"><div class="hero-bg" aria-hidden="true"></div><div class="wrap split" style="align-items:center"><div class="load"><p class="who">About us</p>
    <h1>We build the software wealth firms run on.</h1>
    <p class="lede">Spring Money builds the software that IFAs and wealth managers run their firms on: integrated intelligence, the firm's own name in front, and a modern digital experience for its clients.</p></div>
    <div class="house reveal" aria-hidden="true"><span class="ring-o r1"></span><span class="ring-o r2"></span>
      <div class="core"><img src="assets/mark.svg" alt=""></div>
      <div class="orb"><span style="--c:#9A3412;transform:translate(130px,0)">S</span><span style="--c:#1D4ED8;transform:translate(-65px,-113px)">K</span><span style="--c:#6D28D9;transform:translate(-65px,113px)">N</span></div>
      <div class="orb o2"><span style="--c:#2E6FD8;transform:translate(0,-200px)">A</span><span style="--c:#0A0D0C;transform:translate(173px,100px)">M</span><span style="--c:#9A3412;transform:translate(-173px,100px)">R</span></div></div></div></section>

  <section class="section" style="padding-top:0"><div class="wrap story">
    <div class="reveal"><h2>Why we exist.</h2></div>
    <div class="story-body">
      <p class="lede">A distribution or advisory firm in India runs on many systems at once: an exchange for orders, registrar feeds for holdings, a KYC service, a signing service, spreadsheets for reviews, and a messaging app for everything else. Its clients see a different brand on every one of them.</p>
      <p class="lede">We think a firm should run its whole practice in one place, under its own name, and offer wealth management as personal as the family it serves.</p>
      <p class="lede">That is what we build: Manthan, one platform with integrated intelligence and the firm's own brand in front of every client, and Spring Sense agents, rolling out to firms now, that prepare the work for people to approve.</p>
    </div>
  </div></section>

  <section class="section brandkit"><div class="wrap">
    <div class="section-head reveal"><h2>What we believe, in one page.</h2></div>
    <div class="beliefs">
      <div><span class="bn">Mission</span><p>Give every wealth advisor in India the intelligence to grow, and to know every client the way they know their best one.</p></div>
      <div><span class="bn">Idea</span><p><b>One house.</b> One company, one product, one design system. Every firm gets its own front door.</p></div>
      <div><span class="bn">Position</span><p>We are a technology provider. Your firm distributes or advises, under its own registration.</p></div>
    </div>
    <p style="margin-top:28px"><a class="btn btn-ghost" href="principles.html">Read our principles and practices</a></p>
  </div></section>

  <section class="section"><div class="wrap">
    <div class="section-head reveal"><h2>What we build.</h2></div>
    <div class="three">
      <a class="panel plink" href="manthan.html"><h3>Manthan</h3><p>The platform your practice runs on, and the app your clients know you by.</p></a>
      <a class="panel plink" href="features.html"><h3>Features</h3><p>From onboarding and KYC to orders, reconciliation, reviews and a practice dashboard.</p></a>
      <a class="panel plink" href="spring-sense.html"><h3>Spring Sense</h3><p>AI agents that draft, check and flag. A person approves before anything reaches a client.</p></a>
    </div>
  </div></section>

  <section class="section" style="padding-top:0"><div class="wrap">
    <p class="marquee-label" style="margin-bottom:16px">Recognised by</p>
    <ul class="recog"><li>Startup India</li><li>Infinity</li><li>AppScale</li><li>GSF</li><li>Garage Marathi</li></ul>
  </div></section>

  <section class="section"><div class="wrap three">
    <div class="panel"><h3>Where we are</h3><p>MIT TBI, MIT WPU Campus, Kothrud, Pune.</p></div>
    <div class="panel"><h3>Who we are</h3><p>2AN Technologies Private Limited, trading as Spring Money.</p><p class="small muted" style="margin-top:8px">''' + PENDING.format("CIN and company line: pending legal review") + '''</p></div>
    <div class="panel"><h3>Meet the people</h3><p>The team building the platform and Spring Sense.</p><p style="margin-top:14px"><a href="team.html">Our team</a></p></div>
  </div></section>
  <section class="section" style="padding-top:0"><div class="wrap"><a class="yt" href="https://www.youtube.com/@springmoney" target="_blank" rel="noopener">
    <span class="yt-play" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M8 5v14l11-7Z"/></svg></span>
    <span><b>Watch Spring Money on YouTube</b><small>Videos from the team at youtube.com/@springmoney</small></span><span class="yt-go">Open channel</span></a></div></section>'''

# ---------------------------------------------------------------- PRINCIPLES
PRINCIPLES = [
 ("We build software. Your firm advises or distributes.", "Spring Money does not give investment advice, does not distribute products and does not sell to your clients. Your firm does that, under its own registration.",
  ["Our website and sales material describe software, never investment outcomes.", "Your clients' relationship is with your firm, not with us."]),
 ("Paid for software, never for what your clients buy.", "We charge firms software fees. We take no commission or sales-linked payment from fund houses or other product makers.",
  ["Any partner that earns revenue must have a distributor mode and an adviser mode with no payout.", "We avoid products that do not fit either registration."]),
 ("Build to the stricter rule.", "When a feature serves both distributors and advisers, we build it to the stricter rule and relax it by configuration.",
  ["Every feature is tagged distributor, adviser or both before it is specified.", "Firms that do both work family by family, in the right lane."]),
 ("Your firm is in front.", "Your clients see your name, logo, colours and font. Spring Money is a small technology credit.",
  ["The credit never sits next to advice, a suggestion or a performance figure.", "It is never larger than your own logo."]),
 ("Warnings that cannot be edited out.", "Templates we give firms carry the identity block and the standard risk warning for their registration.",
  ["Firms can edit the wording of a template. They cannot remove the identity block or the warning."]),
 ("People approve AI work.", "Spring Sense drafts, checks and flags. A person on your team approves before anything reaches a client.",
  ["Every AI output is labelled AI-generated.", "The adviser or distributor who approved it stays named as responsible."]),
 ("We never act as your client.", "Orders wait for the client's own authentication. The platform never completes that step for them.",
  ["Orders stay pending until the investor confirms them themselves."]),
 ("We never hold client money.", "Clients pay through payment links and mandates. The platform does not hold client money or units.",
  ["Nothing in the platform moves or holds a client's money or units."]),
 ("Consent before data.", "Accounts held elsewhere come in only with the client's consent, through the account aggregator.",
  ["The client can see and withdraw consent."]),
 ("Built for everyone who uses it.", "We design to WCAG 2.1 AA, so screens work with keyboards, screen readers and larger text.",
  ["Every firm's colours must pass a contrast check before launch.", "Meaning is never carried by colour alone."]),
 ("We only claim what we can show.", "No rankings, no return figures and no numbers we cannot source, here or anywhere else.",
  ["If we cannot confirm something, we leave it out and say so."]),
]

CHECKLIST = ["Which registrations and client-family lanes does it touch?", "Does anyone earn from it?", "Could it influence an investment decision?",
 "Does it move or hold client money or units? If so, it is blocked.", "Does it change which plan a family sees or buys?", "Does it send or publish anything?",
 "Does it store client data or communications?", "Does it use AI? Then it needs a label and an audit trail.", "Does it rely on a rule that still needs compliance sign-off?"]

def principles_body():
    cards = "".join(f'<article class="pr reveal"><span class="pr-n">{i+1:02d}</span><h3>{h}</h3><p>{p}</p><ul>' + "".join(f"<li>{x}</li>" for x in xs) + '</ul></article>' for i, (h, p, xs) in enumerate(PRINCIPLES))
    chk = "".join(f'<li><span class="ck"></span>{q}</li>' for q in CHECKLIST)
    return subnav("principles.html") + f'''
  <section class="page-hero"><div class="hero-bg" aria-hidden="true"></div><div class="wrap load"><p class="who">Principles and practices</p>
    <h1>How we build, and what we will not do.</h1>
    <p class="lede">Eleven principles, and the practices that keep us to them. They decide what goes into the platform and what stays out.</p></div></section>
  <section class="section" style="padding-top:0"><div class="wrap"><div class="prs">{cards}</div></div></section>
  <section class="section sense-sec on-dark"><div class="wrap split" style="align-items:start">
    <div class="reveal"><h2>Nine questions before any feature is built.</h2><p class="lede" style="margin-top:18px">Every feature goes through the same checklist before it is specified. If an answer depends on a rule that is not settled, the feature waits for compliance.</p></div>
    <ol class="checklist">{chk}</ol></div></section>'''

# ---------------------------------------------------------------- TEAM
TEAM = [
 ("Co-founders", [
   ("Nikhil Narkhedkar", "Co-founder and CEO", "Sets the company's direction and runs product today.", "nikhil"),
   ("Omkar Jadhav", "Co-founder", "Partnerships and the firms we work with.", "omkar")]),
 ("Product", [
   ("Atharva Joshi", "Chief of Product", "Roadmap and priorities across distributor and adviser firms.", ""),
   ("Khushi Pawar", "Product", "The product backlog and what firms ask for.", "khushi"),
   ("Satvika Deshpande", "Sprint operations", "Planning, releases and registrar reconciliation checks.", "")]),
 ("Engineering", [
   ("Arnav Limaye", "Engineering", "Architecture, multi-tenancy and integrations.", "arnav"),
   ("Neeraj Singh", "Frontend engineering", "The screens your team and clients use.", "neeraj"),
   ("Saurabh Pharate", "Engineering", "Building and shipping the platform.", "saurabh"),
   ("Navnath Gavde", "Engineering", "Asset mapping and production support for firms going live.", ""),
   ("Sushant", "Backend engineering", "The Frappe backend and registrar data.", ""),
   ("Sheetal Datir", "QA lead", "Testing every release before it reaches firms.", ""),
   ("Abhijit Sonawane", "Quality assurance", "Testing new features before they ship.", "")]),
]

AV = ["#006E4A", "#2E6FD8", "#1D4ED8", "#9A3412", "#6D28D9", "#0A0D0C", "#0E5235", "#B45309"]

def team_body():
    out = ""
    for grp, people in TEAM:
        cards = ""
        for name, title, what, photo in people:
            ini = "".join(w[0] for w in name.split()[:2]).upper()
            pic = f'<img src="assets/team/{photo}.jpg" alt="" loading="lazy">' if photo else f'<span class="ini">{ini}</span>'
            cards += f'<article class="member"><div class="mph">{pic}</div><h3>{name}</h3><p class="ptitle">{title}</p><p class="pwhat">{what}</p></article>'
        out += f'<section class="tgroup"><h2 class="tg-h">{grp}</h2><div class="members">{cards}</div></section>'
    return subnav("team.html") + f'''
  <section class="page-hero"><div class="hero-bg" aria-hidden="true"></div><div class="wrap load"><p class="who">Team</p>
    <h1>The people building it.</h1>
    <p class="lede">Product, engineering and operations, in Pune. A small team that works directly with the firms on the platform.</p></div></section>
  <section class="section" style="padding-top:0"><div class="wrap">{out}</div></section>
  <section class="section brandkit"><div class="wrap split" style="align-items:center">
    <div class="reveal"><h2>How we work together.</h2></div>
    <ul class="bullets"><li><b>Product and engineering in one room.</b> Every feature is tagged distributor, adviser or both before it is built.</li><li><b>Agents prepare, people decide.</b> We use AI agents for research and drafts inside the company too. A person signs off every decision.</li><li><b>Close to the firms we serve.</b> Requests from firms go straight into the product backlog.</li></ul>
  </div></section>'''

# ---------------------------------------------------------------- CLIENTS
FIRMS = [
 ("Advisory firms", "RIA", [("Advent", ""), ("CrispIdea", ""), ("Modulor", ""), ("Multipl Wealth", ""), ("NS Wealth", "MProfit"), ("Unovest", "IFAnow"), ("Wealth Culture", "")]),
 ("Distribution firms", "MFD", [("DPFS", "InvestWell"), ("Money Lancer", "InvestWell"), ("HumFauji", ""), ("Pine Fortune", "")]),
 ("Firms that do both", "Dual", [("Prudeno Wealth", "IFAnow"), ("Vivegam FP", "")]),
 ("And more", "", [("Personifi", ""), ("Precision Wealth", "")]),
]

def clients_body():
    groups = ""
    for title, tag, firms in FIRMS:
        tiles = "".join(f'<li class="ctile"><span class="cname">{n}</span>' + (f'<span class="cfrom">Moved from {f}</span>' if f else "") + '</li>' for n, f in firms)
        tagh = (' <span class="ctag">' + tag + '</span>') if tag else ''
        groups += f'<div class="cgroup"><h3>{title}{tagh}</h3><ul class="ctiles">{tiles}</ul></div>'
    quotes = "".join(f'''<figure class="quote q-empty"><blockquote>{PENDING.format("Testimonial " + str(i) + ": awaiting a quote approved by the firm")}<p>A firm's own words about using the software: what changed for their team and their clients' experience. About the software only, never investment outcomes.</p></blockquote><figcaption><span class="av" style="--c:{AV[i]}">?</span><span><b>Name, role</b><br>Firm name, licence</span></figcaption></figure>''' for i in (1, 2, 3))
    return subnav("clients.html") + f'''
  <section class="page-hero"><div class="hero-bg" aria-hidden="true"></div><div class="wrap load"><p class="who">Clients</p>
    <h1>The firms that run on Spring Money.</h1>
    <p class="lede">Advisory firms, distribution firms and firms that do both, each with the platform in its own name.</p>
    <p class="small" style="margin-top:18px">{PENDING.format("Draft: each firm must agree to be named, and display names need checking, before this page goes live")}</p></div></section>
  <section class="section" style="padding-top:0"><div class="wrap"><div class="cgroups">{groups}</div></div></section>
  <section class="section brandkit"><div class="wrap">
    <div class="section-head reveal"><h2>In their words.</h2><p class="lede">What firms say about the software. We publish only quotes the firm has approved, about the software, never about investment outcomes.</p></div>
    <div class="quotes">{quotes}</div>
  </div></section>
  <section class="section"><div class="wrap split" style="align-items:center">
    <div class="reveal"><h2>Moving over from another platform.</h2><p class="lede" style="margin-top:18px">Firms on Spring Money have moved over from InvestWell, IFAnow and MProfit. Holdings come in from registrar feeds and CAS statements, and the firm's set-up is configured for the firm.</p></div>
    <div class="moves"><div><b>InvestWell</b><span>to Spring Money</span></div><div><b>IFAnow</b><span>to Spring Money</span></div><div><b>MProfit</b><span>to Spring Money</span></div></div>
  </div></section>'''
