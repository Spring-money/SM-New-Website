# Website v2 brief (owner: Andy, id: web)

Set by AJ, 6 Oct 2026, 00:50. Written by Claude for AJ. **Run tonight.**

## Goal
A proper, in-depth B2B website for Spring Money: software for MFD firms, RIA firms and firms that run both. It must look and feel at least as good as Claude's draft in `work/web/revamp/` (read its README first) and go deeper on every page. This is a static site in `work/web/v2/`. It is not the repo and not the live site; never publish or deploy anything.

## Start from
- `work/web/revamp/`: copy it into `work/web/v2/` and extend it. Keep the design system (style.css tokens, Poppins/Inter, Evergreen `#0B6B53`, the hero "front door" stage, the licence label switcher, the brand kit, motion with reduced-motion support).
- Brand guideline v0.3 and section 12 (`work/brand/`), your own Stage 1 review (`work/web/01-site-review.md`), `knowledge/company.md`, `knowledge/product-manthan.md`, `knowledge/partnerships.md`, `knowledge/reference/partnerships-q4-2026.md`.

## Pages
1. Home: deeper than the draft. Add a Spring Sense section and the partner wall.
2. Platform: module by module (planner portal, client portal, mobile app). Each module gets a mock screen in the draft's style, using invented demo data only.
3. For MFD firms
4. For RIA firms
5. **Spring Sense**: its own page (see below), with the most ambitious visual and motion on the site.
6. Integrations and partners: the full wall (see below).
7. Security: only facts that are confirmed in `knowledge/` or by engineering. If none are confirmed, publish a short "how we handle data" page and list the questions for engineering in the README. Never invent certifications.
8. About: positioning, mission, "One house". No team size, funding or customer numbers (not known).
9. Book a demo (form, not wired).
10. Privacy, Terms and Grievances: placeholder pages, clearly marked "to be written by legal".

## Spring Sense (facts from AJ, 6 Oct 2026, `[told]`)
- **What it is:** personalised AI agents for MFD and RIA firms. **Live with firms today.**
- **For:** both MFD and RIA firms. Wording switches by licence.
- **Agents:**
  1. Meeting prep and notes: a client brief before the meeting, and a summary with actions after it.
  2. Portfolio review drafts: drafts the review; the adviser or distributor edits and approves it.
  3. Client follow-ups: drafts reminders and SIP or birthday messages for approval.
  4. Ops and compliance checks: flags reconciliation breaks, KYC expiry and missing documents.
  5. Ask Spring Sense: a generalist assistant that draws on the firm's historical and current client data to answer questions.
- **Rules for the copy (section 12.7 and `mfd-vs-ria.md`), not optional:**
  - A person approves before anything reaches a client. Say so on the page.
  - Every AI output is labelled as AI-generated, and the firm's adviser or distributor stays named as responsible.
  - On MFD wording: "suggestions" and "drafts", never "advice", "recommendations" or "AI advice". On RIA wording, recommendations remain the adviser's.
  - Don't promise accuracy, returns or "never wrong". Never say "AI adviser".
  - Data: don't state where data is processed, which models are used, or retention, until engineering confirms. Put these questions in the README for AJ.
- **Visual:** an "agents at work" scene, for example the planner portal with Spring Sense cards drafting a review and flagging a KYC expiry, in the same mock-UI style as the hero. Ask the brand designer for help only if needed.

## Partner wall (AJ decision, 6 Oct 2026)
- AJ confirms he holds logo permissions for all current and planned partners. Record this in `logo-permissions.md` as "AJ confirmed, 6 Oct 2026".
- **One wall with everyone together**, current and planned (AJ's choice). Wording above the wall: "Built with" or "Our partners", not "integrated with". Planned partners are not live integrations.
- **Current** (from `product-manthan.md`): BSE StAR MF, NSE, MF Utilities, CAMS, KFintech, CKYC (via Zoop), Digio, Signzy, OTPless, AiSensy, account aggregator (provider unnamed: leave it out until Arnav confirms).
- **Planned** (from `partnerships.md`, top 10): Appreciate, CMOTS, CAS Parser, Volt Money, Blostem, Nuvama, IndiaBonds, The Wealth Company, plus Exotel. Leave out the messaging bake-off candidates (Infobip, Gupshup, Kaleyra) until one is picked.
- **Logo files:** download each official logo from the partner's own website or press/brand kit only. Never redraw, trace or recolour a logo. Save to `work/web/v2/assets/partners/` and record the source URL and date for each in `logo-permissions.md`. Show logos in their original colours, or a single grey treatment if the brand rules allow it. If you can't find an official file, use a plain text tile and say so.

## Copy rules
- Section 12.2 banned words: best, No. 1, leading, guaranteed, unbiased, expert advice, free, "ensures compliance", return figures, customer/AUM numbers.
- Don't claim: EUIN handling, RIA agreement e-sign, client-OTP order rule, security certifications.
- Don't name tenant firms. Demo firms stay invented.
- Don't use "Manthan" in public (trademark check pending).

## Quality bar (check before reporting)
- Desktop 1440 and phone 390: no sideways scroll; render every page and look at it.
- WCAG AA contrast on every text pair; visible keyboard focus; reduced motion respected; no console errors.
- Fonts self-hosted, no trackers, no external scripts.
- Everything works by opening `index.html` and through `python3 -m http.server`.

## Report
Report in two stages, to Mike for AJ:
1. Sitemap plus Spring Sense and partner-wall copy (short).
2. The finished site, with screenshots of every page at both widths.

Compliance checks the Spring Sense page and the partner wall wording before AJ sees stage 2. Do not edit the repo, deploy, or contact any partner.
