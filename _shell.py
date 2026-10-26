"""Page shell for the website: head, header with dropdowns, footer (revision brief sections 9 and 6.7)."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

WA = "https://wa.me/918668484607?text=Hi%2C%20I%27d%20like%20to%20know%20more%20about%20Manthan"
MAIL = "mailto:sayhi@spring.money?subject=Manthan%20enquiry"
GIT = "get-in-touch.html"
# Open item 5: Spring Sense status. One switch for the whole site.
SENSE_STATUS = "Rolling out to firms now"

def soon(label="Coming soon"):
    return f'<span class="soon">{label}</span>'

def dd(label, items, key):
    li = ""
    for it in items:
        if it[1] is None:
            li += f'<li><span class="dd-soon" aria-disabled="true"><span>{it[0]}<small>{it[2]}</small></span>{soon()}</span></li>'
        else:
            li += f'<li><a href="{it[1]}"><span>{it[0]}<small>{it[2]}</small></span></a></li>'
    return (f'      <li class="dd" data-dd="{key}"><button type="button" class="dd-btn" aria-expanded="false" aria-controls="dd-{key}">{label}</button>'
            f'<ul class="dd-menu" id="dd-{key}">{li}</ul></li>\n')

ADVISORS = [("RIA", "for-ria.html", "SEBI-registered investment advisers"), ("MFD", "for-mfd.html", "Mutual fund distributors"),
            ("PMS", None, "Portfolio managers"), ("RA", None, "Research analysts")]
RESOURCES = [("Calculators", "calculators.html", "Illustrative tools for client meetings")]

def head(title, desc, robots=""):
    nav = ('      <li><a href="manthan.html">Manthan</a></li>\n'
           '      <li><a href="spring-sense.html"><img class="ss-nav" src="assets/spring-sense.svg" alt="">Spring Sense</a></li>\n'
           + dd("For wealth advisors", ADVISORS, "advisors")
           + '      <li><a href="partners.html">Partners</a></li>\n'
           + dd("Resources", RESOURCES, "resources")
           + f'      <li class="nav-cta"><a class="btn btn-primary" href="{GIT}">Get in touch</a></li>\n')
    rb = f'<meta name="robots" content="{robots}">\n' if robots else ""
    return f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{rb}<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#FCFFFE">
<link rel="icon" href="assets/mark.svg" type="image/svg+xml">
<link rel="stylesheet" href="fonts.css">
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="v2.css">
<link rel="stylesheet" href="brand.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <nav class="wrap nav" aria-label="Main">
    <a class="brand" href="index.html" aria-label="Spring Money home"><img src="assets/logo.svg" alt="Spring Money" width="150" height="25"></a>
    <ul class="nav-links" id="nav-links">
{nav}    </ul>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false" aria-controls="nav-links"><span></span><span></span><span></span></button>
  </nav>
</header>
<main id="main">
'''

ICON = {
 "wa": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3.5 20.5l1.2-4.1A8.5 8.5 0 1 1 8 19.6Z"/><path d="M9 8.5c0 3.5 3 6.5 6.5 6.5l1-1.6-2-1.2-1 .9c-1-.4-2.1-1.5-2.5-2.5l.9-1-1.2-2Z"/></svg>',
}

FOOT = f'''</main>
<footer class="site-footer on-dark">
  <div class="wrap">
    <div style="margin-bottom:40px"><img src="assets/logo-reversed.svg" alt="Spring Money" width="150" height="25"><p style="margin-top:14px;max-width:30em">The technology partner for India's wealth advisors.</p></div>
    <div class="foot-grid">
      <div><h4>Manthan</h4><ul><li><a href="manthan.html">Overview</a></li><li><a href="features.html">Features</a></li><li><a href="manthan.html#pricing">Pricing</a></li><li><a href="partners.html">Partners</a></li><li><a href="spring-sense.html">Spring Sense</a></li><li><a href="security.html">How we handle data</a></li></ul></div>
      <div><h4>For wealth advisors</h4><ul><li><a href="for-ria.html">RIA</a></li><li><a href="for-mfd.html">MFD</a></li><li><span class="na">PMS</span>{soon()}</li><li><span class="na">RA</span>{soon()}</li><li><span class="na">AMCs</span>{soon()}</li></ul></div>
      <div><h4>Resources</h4><ul><li><a href="calculators.html">Calculators</a></li><li><a href="faq.html">FAQ</a></li><li><a href="https://www.youtube.com/@springmoney" target="_blank" rel="noopener">YouTube<span class="sr"> (opens in a new tab)</span></a></li></ul></div>
      <div><h4>About us</h4><ul><li><a href="about.html">About</a></li><li><a href="principles.html">Principles and practices</a></li><li><a href="team.html">Team</a></li><li><span class="na">Clients</span>{soon()}</li><li><a href="{GIT}">Contact</a></li></ul></div>
      <div><h4>Legal</h4><ul><li><a href="privacy.html">Privacy policy</a></li><li><a href="terms.html">Terms of use</a></li><li><a href="grievances.html">Grievances</a></li><li><a href="takedown.html">Takedown policy</a></li></ul></div>
      <div><h4>Connect</h4><ul><li><a href="{WA}" target="_blank" rel="noopener">WhatsApp<span class="sr"> (opens WhatsApp)</span></a></li><li><a href="{MAIL}">Email</a></li><li><a href="https://www.linkedin.com/company/springmoney/" target="_blank" rel="noopener">LinkedIn<span class="sr"> (opens in a new tab)</span></a></li><li><a href="https://www.youtube.com/@springmoney" target="_blank" rel="noopener">YouTube<span class="sr"> (opens in a new tab)</span></a></li><li><a href="https://www.instagram.com/springmoneyapp/" target="_blank" rel="noopener">Instagram<span class="sr"> (opens in a new tab)</span></a></li></ul></div>
    </div>
    <div class="foot-company">
      <div><p><b style="color:var(--sm-paper)">2AN Technologies Private Limited</b></p>
        <address>5th Floor, MIT TBI, Kashyap Building, MIT WPU Campus, Rambaug Colony, Kothrud, Pune, Maharashtra 411038</address></div>
      <div><p><a href="mailto:sayhi@spring.money">sayhi@spring.money</a></p><p><a href="{WA}" target="_blank" rel="noopener">WhatsApp +91 86684 84607</a></p></div>
      <p style="grid-column:1/-1;margin-top:8px">&copy; <span data-year>2026</span> 2AN Technologies Private Limited. Spring Money is a technology provider. It does not give investment advice or manage money.</p>
    </div>
  </div>
</footer>
<script src="site.js"></script>
<script src="v2.js"></script>
<script src="brand.js"></script>
</body>
</html>
'''

def page(name, title, desc, body, robots=""):
    with open(os.path.join(ROOT, name), "w") as f:
        f.write(head(title, desc, robots) + body + FOOT)

def cta(h="See Manthan in your own firm's brand.", extra=""):
    return f'''  <section class="cta"><div class="wrap"><div class="cta-box"><h2>{h}</h2><div class="hero-actions"><a class="btn btn-primary" href="{GIT}">Get in touch</a>{extra}</div></div></div></section>
'''

def faq(items):
    return '<div class="faq">' + "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'

def redirect_stub(name, target, title):
    with open(os.path.join(ROOT, name), "w") as f:
        f.write(f'''<!doctype html>
<html lang="en-IN"><head><meta charset="utf-8"><meta name="robots" content="noindex">
<title>{title}</title><link rel="canonical" href="{target}"><meta http-equiv="refresh" content="0; url={target}"></head>
<body><p>This page has moved to <a href="{target}">{target}</a>.</p></body></html>
''')
