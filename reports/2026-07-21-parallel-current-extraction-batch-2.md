# Parallel Current Extraction Batch 2

Date: 2026-07-21
Branch/PR: `codex/extract-saudi-agriculture-2026-exhibitors` / Draft PR #5
Mode: Parallel multi-exhibition public-source research

## Scope
- Continue current company extraction across several Riyadh exhibitions in the same run.
- Use all public source types approved for the project: official pages, public event pages, company self-published pages, LinkedIn/public social pages, and public marketplace/directory pages.
- Preserve source relationship and confidence when a company is a sponsor, partner, logo-strip exhibitor, advisory participant, or public-source candidate rather than a structured booth exhibitor.
- Continue Saudi Agriculture enrichment for selected records from `exh-saag-2026-0038` through `exh-saag-2026-0050`.
- Do not contact companies, infer contacts, merge by similar names, import CRM data, or merge to `main`.

## Current Extraction Results
| Exhibition | Raw snapshot | Current rows after batch | Batch 2 increase | Source status |
|---|---:|---:|---:|---|
| Saudi Agriculture 2026 | `database/raw/saudi-agriculture-2026-exhibitors-2026-07-18.csv` | 222 | 0 | Official current directory; enrichment continued separately |
| LEAP 2026 | `database/raw/leap-2026-exhibitors-2026-07-21.csv` | 75 | 50 | Official current page; visible card names only |
| Big 5 Construct Saudi 2026 | `database/raw/big5-construct-saudi-2026-exhibitors-2026-07-21.csv` | 48 | 24 | Public official directory page 2 via AJAX listing |
| Saudi Build 2026 | `database/raw/saudi-build-2026-exhibitors-2026-07-21.csv` | 48 | 23 | Public official table rows visible on page |
| Saudi Elenex 2026 | `database/raw/saudi-elenex-2026-exhibitors-2026-07-21.csv` | 26 | 0 | Official current list already fully visible |
| Saudi Event Show 2026 | `database/raw/saudi-event-show-2026-current-sponsors-partners-2026-07-21.csv` | 21 | 21 | Official current sponsor/partner pages; booth exhibitor status not inferred |
| Hotel & Hospitality Expo Saudi Arabia 2026 | `database/raw/hotel-hospitality-expo-saudi-2026-current-public-candidates-2026-07-21.csv` | 17 | 17 | Official logo strip plus public social/company/event sources; relationship preserved per row |

Parallel current batch exhibitors added: 235
Total current company records after this run: 457

## Data Counts After This Run
- Total exhibitor/company records: 457
- Total evidence rows: 1023
- New evidence rows in this continuation: 238
- New current/company records in this continuation: 135
- Contact-bearing company records: 25 email-bearing, 21 phone-bearing, 16 LinkedIn-bearing.

## Saudi Agriculture Enrichment
- Added public-source enrichment for 9 additional Saudi Agriculture records in the `0038`-`0050` slice.
- Captured official/company websites, public emails, public phones, public LinkedIn pages, group/affiliate pages, and one registry mirror where the source matched the exact entity context.
- No guessed email, phone, WhatsApp, or personal contact was added.

## Source Notes
- LEAP still exposes only company names in the public card text; stand, country, sector, and website remain gaps for the extracted LEAP rows.
- Big 5 page 2 exposes company name, stand, hall, country, and directory profile URL; deeper profile enrichment was not completed for this page.
- Saudi Build public page exposes 48 current rows in this run; no additional visible rows were captured from the page during this pass.
- Saudi Event Show rows are current official sponsor/partner participants, not necessarily booth exhibitors.
- Hotel & Hospitality rows mix official logo-strip signals, company self-published exhibition calendars, event LinkedIn posts, and official partner/advisory pages. Relationship detail is retained in `booth_or_sponsor_notes` and Evidence.

## Quality Notes
- This is a current exhibitor/company extraction batch, not completed enrichment.
- Cross-exhibition repeat companies are allowed when each event relationship is separately source-backed.
- Historical-only leads from Saudi Event Show 2025 and Hotel & Hospitality 2025 were not added to current records in this batch.

## Next Action
- Continue LEAP after row 75.
- Continue Big 5 from row 49 onward and enrich page 2 profiles.
- Verify whether Saudi Build has hidden/paginated rows beyond the 48 visible rows.
- Continue Saudi Agriculture enrichment from `0051`-`0075`.
- Convert Saudi Event Show and Hotel & Hospitality sponsor/logo/advisory participants into fuller public-source company records, while keeping booth exhibitor status separate unless directly confirmed.
