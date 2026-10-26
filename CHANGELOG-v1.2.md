# Website v1.2: phase 1 of Omkar's revision brief (19 Oct 2026)

Built 26 Oct 2026 from `work/web/v2` (backup of the previous build: `work/web/_v12-pre-brief`). Build: `python3 build.py`.
Nothing is published. The contact form is not connected (it says so when submitted).

## Done (brief section → where)
| Brief | Change |
|---|---|
| 3 Brand | Lora 600 for display/H1/H2 only, Inter everywhere else with tabular numbers; `tokens.css` added as is; `brand.css` maps the old variables to the tokens. Action Green #006E4A buttons (44px, radius 8), Paper/Ink, borders instead of shadows, radius 8/12/16, chart colours #149B72 / #2E6FD8 / #7D8180, calm motion, reduced-motion respected. Poppins only in the "Try your brand" font picker. Dark panels use Spring Night with Spring Green as the accent (dark-mode rule). |
| 4 Voice | Section headings rewritten as observations; "Four reasons…" and "One idea runs through…" removed; no feature count in headlines. |
| 5 Audience | "Wealth advisor"/IFA throughout. RIA and MFD only inside the "For wealth advisors" dropdown; PMS and RA "Coming soon". AMCs: footer only, coming soon. |
| 6.1 Home | New hero (headline A; preview B–F with `index.html?h=B` … `?h=F`), sub-headline, "Get in touch" + "See Manthan". Three panels (Growth / Your brand / Customised, each with a live mock-up; the feature switches are clickable). Net-worth orbit widened to 7 groups with how each item arrives. New self-onboarding + CRM walkthrough (8 steps, client app on the left, CRM funnel and tasks on the right, in sync). Workflow step 1 is CRM. |
| 6.2/6.3 Manthan | `/platform` → `/manthan` (redirects in `_redirects` and a stub page). Pricing: 3 bps of managed assets, calculated annually, billed monthly; slider from ₹25 crore to ₹1,000 crore (₹100 crore = ₹3,00,000 a year, ₹25,000 a month); include list; no trial or starting-price copy. |
| 6.4 Get in touch | Every CTA says "Get in touch" → `get-in-touch.html` (`/demo` redirects). "Other" added, platform dropdown removed, step 3 reworded, WhatsApp and email as secondary buttons. |
| 6.6 Resources | Calculators page with 15 calculators: SIP, lumpsum, step-up SIP, SIP target, step-up SIP target, SIP to SWP, retirement, child education, FD-based retirement, capital gains tax, EMI, buy vs rent, car vs commute, FD vs RD, endowment vs term. Each is labelled illustrative and shows its assumptions; disclaimer at the foot. Works at phone width. |
| 6.7 / 9 Footer | About us moved to the footer; company block with 2AN Technologies, full address, email, WhatsApp. Footer columns as in section 9, with Takedown policy (placeholder page). |
| 7 Copy | No "personal finance", no competitor names, no `.example` URLs (all `yourfirm.manthan.money`, team side `/admin`). |
| 8 Ready/Planned | Features page and partner wall both use All / Ready / Planned. springmoney.ai items added. |
| Phase 2 slots | Routes exist, noindexed, "Coming soon": `for-pms`, `for-ra`, `for-amc`, `clients` (client names removed until consents), `find-an-advisor`. |

## Checks
All 27 pages at 1440 px and 390 px: no sideways scroll, no console errors. Calculators and the pricing slider checked by script. Copy scan: no banned words, competitor names or "personal finance".

## For AJ to confirm (brief section 10)
1. **Headline** (open item 1): A is live; B–F preview with `?h=`.
2. **GST** on pricing (item 2): shown as a visible placeholder under the calculator.
3. **Net-worth sources** (item 3): the brief's "likely source" per item is shown; confirm each.
4. **Ready/Planned** (item 4). Marked Planned: lead scoring, video KYC, multi-client basket, WhatsApp and email campaigns, content library, sub-broker payouts, firm-wide audit trail, AML/PEP screening, regulatory reporting logs. Everything else Ready, including Aadhaar e-sign, UCC/CAN, NACH/UPI AutoPay, XIRR, CAS import, business MIS, brokerage tracking and fee invoicing. Partners: Account Aggregator Ready; DigiLocker and MF Central Planned. Left out until accurate and permitted: Razorpay, PayU, smallcase, Morningstar. "Real-time valuation" became "Daily valuation"; "upfront" brokerage dropped (trail-only).
5. **Spring Sense status** (item 5): one switch, `SENSE_STATUS` in `_shell.py`, now "Rolling out to firms now".
6. Calculator tax rules are 2025-26 (equity: 20% short-term, 12.5% long-term above ₹1.25 lakh; debt funds from April 2023 at slab). Check before launch.
