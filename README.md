# Spring Money website v2

Built 6 Oct 2026 by Andy (web) for AJ, from `work/web/revamp/`. **Draft. Not published, not deployed.** Nothing on springmoney.in or spring.money, and nothing in the repo, was touched. No partner was contacted.

## Open it
Double-click `index.html`, or run `python3 -m http.server` in this folder. No internet, no libraries, no trackers, fonts self-hosted.
`build.py` regenerates the pages (`python3 build.py`); the HTML files are plain and work without it. `_check.py`, `_scenes.py` and `_contrast.py` are the test scripts (Playwright with local Chrome).

## Pages (12)
`index` · `platform` · `for-mfd` · `for-ria` · `spring-sense` · `partners` · `security` · `about` · `demo` · `privacy`, `terms`, `grievances` (placeholders, marked "to be written by legal").
Stage 1 sitemap and copy: `01-sitemap-and-copy.md`. Screenshots of every page at 1440 and 390 px: `shots/`. Each Spring Sense scene: `shots/sense-*`.

## What is new on top of the revamp draft
- **Spring Sense** (home section and its own page): an animated planner-portal scene with five agents that cycle (meeting prep, review drafts, follow-ups, ops checks, Ask). Pause button, click-to-pick agent, MFD/RIA wording switch. Reduced-motion shows the finished state.
- **Partner wall**: one wall, each tile marked "In the platform" or "Planned", with a filter. Logos are the files as served by each partner (`assets/partners/`, `logo-permissions.md`). Four partners have no usable official file and show a plain text tile: CAMS, KFintech, Blostem, The Wealth Company. Volt Money and IndiaBonds logos are white, so they sit on a dark tile. Account aggregator is left out until the provider is confirmed.
- **Platform** page with a mock screen per module; deeper MFD and RIA pages; Security, About, legal placeholders.

## Checks run (6 Oct 2026)
See "Report" in `02-build-report.md`.

## For compliance (check before AJ sees it)
1. `spring-sense.html` and the Spring Sense section on the home page, MFD and RIA pages.
2. The partner wall wording ("Built with the rails and partners...", "In the platform", "Planned", the footnote), on `partners.html` and the home page.
3. Statements carried over from the revamp and still needing a view: "The platform does not hold client money", "We take no commission or sales-linked payment", "Distribution and advice kept apart", "advisory agreement step", "fee mandates".
4. "Firms are moving over from InvestWell, IFAnow and MProfit" (from `product-manthan.md`, told).

## Questions for engineering / AJ (not answered on the site)
1. Spring Sense: where is data processed? Which models are used, and do they train on firm data? What is retained, and for how long? Is there an audit log of who approved what? (None of this is stated on the site.)
2. Spring Sense: is "in use with firms today" true for both MFD and RIA firms, and for all five agents? (From AJ, 6 Oct 2026, told.)
3. Account aggregator provider (Arnav). Add it to the wall when confirmed.
4. Security: any certification, penetration test or policy that can be named? None is claimed. The Security page lists only: one-time-code sign-in, per-firm configuration, admin area, documents with the client, no client money held, AI labels and approval. Please confirm each.
5. Facts to confirm from the revamp list: KYC status via MFU, eNACH/NACH mandates, fee mandates for RIA clients, WhatsApp messaging, document vault, execution centre, "Investor charter" in the app.
6. CAMS and KFintech logos: their sites block plain downloads. Ask AJ for the files, or keep the text tiles.
7. CKYC tile shows the Zoop logo with "via Zoop". Confirm that is how AJ wants it shown.
8. CMOTS file is its 192 px app icon; Exotel is 120 px wide. Better files may exist in their brand kits.

## Not claimed on purpose
EUIN handling, RIA agreement e-sign, the client one-time-code order rule, any security certification, any customer or AUM number, team size, funding, any tenant firm name, "Manthan".

## Before it goes live
Same list as the revamp README: compliance review, company line and CIN in the footer, a decision on the one domain, the demo form wired to a Spring Money inbox, legal pages written, then a port into the Next.js site by an engineering ticket. No agent edits the repo.


## Claude's depth pass (6 Oct 2026, 01:10–01:45)
Andy's original is backed up in `work/web/_v2-andy-backup/`. Rebuild with `python3 build.py` (it imports `_features.py` and `_depth.py`).

**Added**
- **`features.html`**: a feature directory with 59 features in 8 groups. It has search, licence and screen filters, and a group nav that follows your scroll.
  - The source is `work/product-map/manthan-inventory.md`, the mapper's reading of the repo code.
  - Only features that are on for real firms are listed. Demo-only features (CRM deals, contacts and call logs, the AML check) are left out.
  - Features that depend on the firm's own vendor accounts are tagged "Needs your vendor account".
- **Platform page**:
  - a practice dashboard mock: counting KPIs, sparklines, an exception queue and the onboarding funnel
  - a 7-step client onboarding walk-through, with a phone that updates at each step
  - "who uses it" by role
  - set-ups by licence
  - an FAQ
- **Home**: a partner logo marquee, Spring Sense pop-ups in the hero, a teaser for the feature directory, and an FAQ.
- **Spring Sense page**: an approval-gate bar in the demo, and an FAQ.
- A "Features" link in the nav and the footer.

**Confirm before going live**
- **The practice dashboard is labelled "Rolling out".** In code, `dashboard_v2` is on only for Spring Money's own ID, plus Prudeno UAT. AJ to confirm that wording, or remove the section.
- **Three features are on for only one or two firms:** MFU transactions (NS Wealth only), CAS import and RTA feed flags (demo only, though the CAS parsing backend exists), and leads. They're described as things a firm can switch on. Engineering should confirm.
- **The "Investor charter" label applies to both licences.** Compliance should check that.
- **The dashboard figures are invented demo data** and are labelled as such.

## Company pages (Claude, 6 Oct 2026, ~01:40)
`about.html`, `principles.html`, `team.html` and `clients.html` share one Company sub-nav. The source is `_company.py`.
- **Team.** Names and titles come from the current springmoney.in/meet-the-team page and from Slack profiles. Photos are the black-and-white portraits from the current site, resized.
  - Website people not found in Slack were left out, as likely no longer here: Rishabh Shetty, Ravinder Singh, Sahil Panda, Nirmal Nehra, Akhilesh Patidar.
  - Added from Slack: Atharva, Satvika, Sushant, Navnath Gavde and Abhijit Sonawane. They have initials instead of photos. Titles for Navnath and Abhijit are inferred from their work in #general.
  - AJ to confirm with each person before going live, especially those who are new to the page.
- **Clients.** The list combines the firms in the repo with Slack, which added Money Lancer and HumFauji and the name "Prudeno Wealth". "Moved from" comes from Nikhil's note in #rta-recon-reports. Each firm must agree to be named, so the page shows a draft chip.
- **Testimonials.** There are three empty quote slots. We need real quotes, approved by each firm, about the software only.
- **About.** "Recognised by" lists Startup India, Infinity, AppScale, GSF and Garage Marathi, taken from the current site. They're shown as text; logos to follow.
- **Principles.** Principle 8 ("We never act as your client": orders wait for the investor's own authentication) is a working decision that still needs compliance sign-off.

## Pass 4 (Claude, 6 Oct 2026, ~01:55)
- **Richer illustrated UI.**
  - Hero: KPI tiles with figures and sparklines, named demo families with next steps and owners, and a client app showing net worth, asset mix, goals and the next SIP. All of these switch with each demo firm.
  - The platform phones and the brand-kit phone show real-looking screens (goals, home, document vault) instead of grey placeholder bars.
  - All figures and names are invented demo data.
- **Multi-asset section** (home, `#assets`), from `_assets.py`.
  - Headline: "Mutual Funds Sahi Hai. Par kya sirf wahi hai?" **Legal check needed:** "Mutual Funds Sahi Hai" is AMFI's campaign line. A safer alternative is "Mutual funds are the start. Not the whole picture." It's a one-line swap in `build.py`.
  - Each asset is labelled Transact, Track, Coming or Not offered. Only mutual funds are transacted today. "Coming" items depend on planned partners.
  - **Digital gold is shown as "Not on the platform: unregulated"**, per AJ's decision of 1 Oct 2026.
- **SEO.**
  - New `faq.html` with 20 questions in 6 groups.
  - FAQPage JSON-LD on home, platform, Spring Sense and the FAQ page; Organization JSON-LD on home.
  - A FAQ link in the footer.
- **YouTube.** Links to youtube.com/@springmoney in the footer (with LinkedIn) and as a card on About.
  - **Check before going live:** the channel currently carries consumer videos, including investor testimonials, which were Andy's P0 item #3. Review the channel before linking it from the B2B site.
- **Spring Sense icon.** Three concepts are in `work/brand/spring-sense-icon/concepts.html`. Concept A (spark and sprout) is used in the nav and the Spring Sense badges for now. Search the "Spring Sense" trademark before launch.
