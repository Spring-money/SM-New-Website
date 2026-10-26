# Website v1.1: changelog

Andy (web), 7 Oct 2026. Draft for AJ. Applies Omkar's feedback and direction (`work/web/2026-10-07-omkar-feedback.md`). Nothing sent or published. Build: `python3 build.py` in `work/web/v2/` (the build files also needed a small fix to run on Python 3.9; output is unchanged).
Preview package: `work/web/Spring-Money-Website-v1.1-preview.zip` (same file set as the v1 zip, with an updated `PREVIEW-README.txt`).

## Omkar's points 1a to 1m
| # | Change | Where |
|---|---|---|
| 1a | Hero is value-led: "Hyper-personalise personal finance for your clients." New "Four reasons wealth firms choose Spring Money" section: integrated intelligence, your own brand, a modern digital experience, configured to your firm. White-labelling is one of the four, no longer the whole hero | `index.html` hero and `#value` |
| 1b | Licence banners removed from the home page. Audience line reads "For IFAs and wealth managers". Hero demo firms say "Wealth manager" instead of ARN or INA badges. Footer, FAQ and meta text say IFAs and wealth managers | `index.html`, footer on every page |
| 1c | Hero line "A planner portal for your team. A client portal and mobile app in your brand." removed. Now: integrated intelligence, a modern digital experience, a platform configured to the firm, under its own brand | hero |
| 1d | Firm-level figures between Rs 300 Cr and 1,000 Cr: hero Assets Rs 468.4 Cr, 742.9 Cr, 931.5 Cr; practice dashboard Rs 412.6 Cr. SIP book now in Cr a month (2.1, 3.4, 4.6). Family net worth (a client, not a firm) is unchanged | `site.js` demo firms, `_home_hero.html`, `_depth.py` |
| 1e | "One platform. Wording that follows your licence." section and the MFD/RIA/Both toggle removed from the home page. The MFD/RIA label boards are gone from the for-mfd and for-ria pages | `index.html`, `for-mfd.html`, `for-ria.html` |
| 1f | "Mutual Funds Sahi Hai. Par kya sirf wahi hai?" kept (legal check still open). The "Your firm" and "Your family" characters in the orbit are replaced by new original icons (a building and a family group). The two "For MFD firms / For RIA firms" lanes under the orbit are removed | `_orbit.py`, `_assets.py` |
| 1g | Flow now starts before onboarding: Meet, Onboard, Bring holdings in, Transact, Run operations, Review. Heading "From first conversation to yearly review". Removed "Your team works in the planner portal...". Onboarding: "Compliant onboarding, guided step by step." Holdings: "from multiple sources". Transact: "Place and track orders in one place, with more products on the way" (no MF-only wording) | `index.html` `#practice` |
| 1h | "Three screens. One record." section removed | `index.html` |
| 1i | Spring Sense badge says "launching soon" everywhere. "In use with firms today" is gone. MFD/RIA wording toggle removed from every Spring Sense scene. The demo uses neutral wording (review draft, suggestions, your team) | `index.html`, `spring-sense.html`, for-mfd, for-ria, features, FAQ |
| 1j | Form-factor and client-app mentions removed or reworded: brand section, phone preview label, documents line ("kept with each client, in one vault"), client onboarding steps, role list, feature descriptions, FAQ | home, platform, features, FAQ, About, Team, Clients |
| 1k | Partner wording: "Integrated with rails and partners built for modern wealth management." (home heading, marquee label, partners page H1) | `index.html`, `partners.html` |
| 1l | "One wall, two states. Each name is marked..." removed. The tiles still show "In the platform" or "Planned", and the footnote still says planned partners are not live | home, partners |
| 1m | "We're paid for software. Never for what your clients buy." section removed from the home page, About and the partners panel. It remains in the FAQ answer and on the Principles page (see questions) | home, About, partners |

## Other pages: carried through
- **Platform:** new H1 "One platform to hyper-personalise personal finance". The three modules (planner portal, client portal, mobile app) become "Your team's workspace" and "Your clients' experience"; phone mock-up dropped. "Set up for your licence" is now "Configured for your firm" (three cards: start with what you need, add as you go, bring your own accounts). "Across all three" is now "Across the platform". FAQ rewritten.
- **Features:** licence and screen filters and tags removed (search and groups stay). All descriptions drop portal and app wording.
- **Spring Sense:** launching soon; one description per agent (no MFD/RIA wording); "Review drafts" replaces "Portfolio review drafts" in the page text; new first FAQ "When is Spring Sense available?".
- **For MFD firms, For RIA firms:** wording toggles, lanes section and "Advise and distribute? Built for that too." removed; ARN and INA badges removed; launching-soon Spring Sense blocks.
- **About, Principles, Team, Clients, FAQ, Security, Demo, footer:** neutral audience wording, no portal or app talk. The "Your licence decides the words on the screen" principle is removed (Principles is now eleven). The old FAQ question with "best" is reworded. The orbit's lending line no longer says "distributor firms only".
- **Home CTA:** the MFD and RIA doors are replaced by "Explore the platform" and "Meet Spring Sense".

## Proposal for AJ: the for-mfd and for-ria pages (superseded: AJ decided on 15 Oct, see the PRM-37 section below)
They are still in the navigation and footer because only AJ can decide. They are the last place the site splits the story by licence, which Omkar asked us to stop. Options:
1. **Merge (my recommendation):** one page, "For IFAs and wealth managers", with the workflow and Spring Sense blocks. Redirect both old pages. Nav and footer lose two links.
2. **Reframe:** keep two pages, retitled by use case (for example "Run orders and operations" and "Plan and review") instead of by licence.
3. **Keep as reworded now:** lowest effort, but the nav still shows "For MFD firms / For RIA firms" next to a home page that avoids them.

## Copy to check (nothing claims a feature we lack, but these need a decision)
- "Compliant onboarding" (Omkar's wording): a compliance claim. The platform has CKYC and KYC status; nothing in `knowledge/product-manthan.md` says it is compliant.
- "Designed to the standard clients now expect from consumer fintech": a comparison. It is Omkar's direction, not a measured claim.
- "with more products on the way" and the planned partners: forward-looking, from `partnerships.md`; none is live.
- "Meet: capture prospects": rests on the CRM in the planner portal (`product-manthan.md`).
- "Warnings that stay on" and "cannot be edited out": the AJ decision of 5 Oct 2026 (`decisions.md`). `product-manthan.md` does not say it is built.
- Spring Sense "launching soon": AJ said on 6 Oct that it was live with firms. Omkar asks for "launching soon". Please confirm which is right.
- Unchanged from v1 and still pending: "does not hold client money", "advisory agreement step", fee mandates, the demo form's "Your firm is MFD / RIA / Both" field (kept for lead data only).

## Checks (headless Chrome, local files, 7 Oct 2026)
- 17 pages rendered at 1440 px and 390 px: page width equals window width everywhere (no sideways scroll); no console errors or failed requests.
- Contrast was not re-audited. New blocks reuse existing colour tokens only.
- Not touched: `_v2-andy-backup`, the v1 zip.

## Open questions for AJ
1. Merge, reframe or keep the MFD and RIA pages?
2. Spring Sense: "launching soon" (Omkar) or "live with firms" (AJ, 6 Oct)?
3. Keep the "paid for software" line in the FAQ and Principles?
4. The four value pillars include "configured to your firm", which Omkar said the team has stopped talking about. Keep it?

## PRM-37: AJ's decisions applied (15 Oct 2026)
1. **for-mfd and for-ria kept separate and reframed.**
   - MFD page (`for-mfd.html`): distribution framing only. The hero says the firm distributes under its own AMFI registration and Spring Money supplies the software. "Portfolio reviews" became "portfolio statements and service reviews", plus "scheme suggestions for your team to offer". Spring Sense block: "Drafts for your team, approved by a person", with "service-meeting briefs" and "portfolio summaries", and "They do not give advice". Nothing on the page describes the MFD as giving advice.
   - RIA page (`for-ria.html`): unchanged advisory framing. Its FAQ "We advise and distribute" now reads "Our firm holds both registrations. Can one platform handle both?" (no "lane").
2. **Spring Sense wording:** "launching soon" is now "live and rolling out to firms now" (badges, home, platform, features, FAQs, meta descriptions, About). This is modest on purpose, and Omkar may override it.
3. **"Paid for software" kept** in the FAQ and Principles. No change.
4. **"Configured to your firm" pillar kept.** No change.
5. **Copy fixes everywhere:** "compliant onboarding" is now "onboarding and KYC flows built around SEBI and AMFI requirements"; "consumer fintech standard" is now "consumer-app quality design" (home hero, value pillar, About).
Rebuilt with `python3 build.py`; a pre-edit copy is in `work/web/_v11-pre-prm37`. Compliance-analyst to check both audience pages before AJ's last look.

**Render not checked** after the PRM-37 edits (no browser tooling available; god asked not to reinstall). The pages rebuilt cleanly from `build.py` and a text search found no leftover old wording. The earlier 7 Oct render check covered the layout; the PRM-37 edits change text only.

## Compliance fixes applied (15 Oct 2026, work/compliance/2026-10-15-website-v1.1-check.md)
- RIA FAQ: "Our firm holds both registrations" is now "Our group has an advisory business and a distribution business. Can one platform handle both? Yes, kept apart. Each client family sits under one registration only, and advisory and distribution records stay separate."
- "Fee mandates" is now "fee collection through UPI AutoPay or bank transfer" (RIA page, FAQ, features list).

## Open for AJ (listed only, not changed)
1. Who drafts the "scheme suggestions" on the MFD page: if the platform or Spring Sense drafts them, the MFD FAQ "No" must change. Needs product confirmation and sign-off.
2. "An AI-generated label on every output": keep only if the label ships with Spring Sense.
3. "The platform does not hold client money" (MFD page, twice): needs product or tech to confirm the payment flow.
4. "Firms are moving over from InvestWell, IFAnow and MProfit": needs evidence, or use the compliance wording "Moving from another platform such as InvestWell, IFAnow or MProfit?"
5. Footer "Company line and CIN: pending legal review": placeholder; fill in or leave unpublished.

**Render check update (15 Oct):** the Playwright reinstall finished in the background (a Python package only; it used the installed Chrome, no browser download). `_check.py` ran on the build after the PRM-37 copy edits and before the compliance fixes: 390 px page width equals window width on the pages listed, same element-overflow list as 7 Oct (intentional scroll containers). The compliance fixes change text only. The earlier 'Render not checked' line is superseded.
