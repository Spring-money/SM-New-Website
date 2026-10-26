# Website v2: build report

Andy (web), 6 Oct 2026. Draft only: nothing published, deployed or sent; no live site, repo or partner touched. Read `README.md` first (pages, compliance list, engineering questions).

## For compliance (tomorrow morning)
1. **Spring Sense**: `spring-sense.html`, plus the Spring Sense sections on `index.html`, `for-mfd.html`, `for-ria.html`.
2. **Partner wall wording**: `partners.html` and the wall on `index.html` ("Built with the rails and partners...", "In the platform" / "Planned", footnote).
3. **Carried-over statements**: "does not hold client money", "no commission or sales-linked payment", "distribution and advice kept apart", "advisory agreement step", "fee mandates", "firms are moving over from InvestWell, IFAnow and MProfit". Also `security.html`.

## Fixes made on AJ's request (6 Oct 2026)
- Partner logos now sit inside their tiles at similar visual weight (IndiaBonds no longer clipped; CMOTS and MFU enlarged on screen only, files unchanged).
- Spring Sense mock-up label is "Agents" (sentence case).

## Checks run (headless Chrome, local files, 6 Oct 2026)
| Check | Result |
|---|---|
| 12 pages at 1440 px and 390 px, rendered and viewed | Done; screenshots below |
| Sideways scroll (page width equals window width, no element past the edge) | None on all 24 renders |
| Console errors and failed requests | None on all 24 renders (one script bug found and fixed on the way) |
| Text contrast, WCAG AA, computed for every text and background pair, incl. each Spring Sense scene in MFD and RIA wording | Two real failures fixed (white on translucent green behind the firm initial and the "Dashboard" tab, 4.38:1, now on a darker tile). Other flags were hidden states and the toggle pill, not visible text. Re-run after the fix was not repeated |
| Keyboard focus | Visible focus ring comes from `style.css` (evergreen, lime on dark); not re-tested key by key |
| Reduced motion | Scenes, orbit and entrance effects stop; Spring Sense shows its finished state (contrast audit ran in this mode) |
| Fonts, scripts, trackers | Poppins, Inter and Montserrat are self-hosted; no external scripts, no trackers |
| Opens by double-click and by `python3 -m http.server` | Pages render from `file://`; the server route was not run separately (all links are relative) |

## Screenshot list (`work/web/v2/shots/`)
Every page, both widths (`<page>-1440.png`, `<page>-390.png`): index, platform, spring-sense, for-mfd, for-ria, partners, security, about, demo, privacy, terms, grievances.
Spring Sense scenes (`sense-mfd-agent1..5-{1440,390}.png`, and `sense-ria-agent2-{1440,390}.png` for the RIA wording of the review draft).

## Known gaps
- Four partners have no official logo file and show text tiles: CAMS, KFintech, Blostem, The Wealth Company (`logo-permissions.md`).
- Contrast and screenshots of the last two small CSS tweaks were not re-audited line by line (budget).
- Phone check covers layout and overflow, not every touch target.
- Open questions for engineering and AJ are in `README.md`.
