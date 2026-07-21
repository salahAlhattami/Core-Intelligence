# Parallel Current Extraction Batch 3

Date: 2026-07-21
Branch/PR: `codex/extract-saudi-agriculture-2026-exhibitors` / Draft PR #5
Mode: Parallel multi-exhibition public-source research

## Scope
- Continue current public-source extraction across multiple Riyadh exhibitions in the same run.
- Add LEAP 2026 rows 76-125 and Big 5 Construct Saudi 2026 rows 49-96.
- Continue public-source enrichment for Saudi Agriculture, Saudi Event Show, and Hotel & Hospitality Expo Saudi Arabia in parallel.
- Scan remaining priority exhibitions for current, historical, official, third-party, sponsor, event-app, and directory sources without treating discovery-only records as confirmed exhibitors.
- Do not contact companies, infer contacts, merge by similar names, import CRM data, or merge to `main`.

## Current Extraction Results
| Exhibition | Raw snapshot | Current rows after batch | Batch 3 increase | Source status |
|---|---:|---:|---:|---|
| Saudi Agriculture 2026 | `database/raw/saudi-agriculture-2026-exhibitors-2026-07-18.csv` | 222 | 0 | Official current directory; enrichment continued separately |
| LEAP 2026 | `database/raw/leap-2026-exhibitors-2026-07-21.csv` | 125 | 50 | Public LEAP 2026 exhibitor page and loaded page; visible card names only |
| Big 5 Construct Saudi 2026 | `database/raw/big5-construct-saudi-2026-exhibitors-2026-07-21.csv` | 96 | 48 | Public official directory AJAX rows 49-96 |
| Saudi Build 2026 | `database/raw/saudi-build-2026-exhibitors-2026-07-21.csv` | 48 | 0 | Current official table rows already captured in earlier parallel batch |
| Saudi Elenex 2026 | `database/raw/saudi-elenex-2026-exhibitors-2026-07-21.csv` | 26 | 0 | Official current list already fully visible |
| Saudi Event Show 2026 | `database/raw/saudi-event-show-2026-current-sponsors-partners-2026-07-21.csv` | 21 | 0 | Official sponsor/partner pages; booth exhibitor status not inferred |
| Hotel & Hospitality Expo Saudi Arabia 2026 | `database/raw/hotel-hospitality-expo-saudi-2026-current-public-candidates-2026-07-21.csv` | 17 | 0 | Official logo strip plus public social/company/event sources; relationship preserved |

Parallel current batch exhibitors added: 333
Total current company records after this run: 555

## Data Counts After This Run
- Total exhibitor/company records: 555
- Total evidence rows: 1254
- Total registered exhibition-source rows: 86
- New evidence rows in this continuation: 231
- New current/company records in this continuation: 98
- Contact-bearing company records: 47 email-bearing, 33 phone/WhatsApp-bearing, 27 LinkedIn-bearing, and 184 website-bearing.

## Enrichment Added
- Saudi Agriculture enrichment continued for 15 records in the `exh-saag-2026-0051` through `exh-saag-2026-0074` range.
- Saudi Event Show enrichment added event relationship, website, LinkedIn or social page, and public business contact fields for selected sponsor/partner participants where public pages supported the value.
- Hotel & Hospitality enrichment added websites, LinkedIn pages, and public contact channels for selected logo-strip/public-source participants where public company pages supported the value.
- Sponsor, partner, logo-strip, and public-social relationships are retained in Evidence and notes; booth exhibitor status is not inferred from those source types.

## Broad Source Scan
- BIO Middle East 2026 was corrected from historical/completed status to current/upcoming confirmed after its official 2026 exhibitor-list page showed a 126-company current list and 14-16 Dec 2026 dates at RECC Malham.
- CPHI Middle East 2026 was corrected from historical/completed status to current/upcoming confirmed after its official current site showed 14-16 Dec 2026 at RECC Malham.
- Cityscape Global, Global Health, INDEX Saudi, Money20/20 Middle East, Saudi Warehousing & Logistics Expo, LIGHTSPACE Saudi Arabia, Saudi Food Expo, FABEX Saudi Arabia, HRSE KSA, Black Hat MEA, Industrial Transformation Saudi Arabia, and related candidates were scanned and recorded as official, historical, discovery-only, or conflict-needs-review sources as appropriate.
- Discovery-only and historical-only source rows remain source leads, not confirmed current exhibitor records.

## Quality Notes
- This is a current exhibitor/company extraction batch plus public-source enrichment, not completed enrichment.
- Cross-exhibition repeat companies remain allowed only when each event relationship is separately source-backed.
- No guessed emails, phone numbers, WhatsApp numbers, or named contacts were added.
- No automatic outreach, CRM import, or GitHub merge was performed.

## Next Action
- Start BIO Middle East 2026 current exhibitor extraction because a 126-company official list is now available.
- Continue LEAP after row 125 and Big 5 after row 96.
- Continue Saudi Agriculture enrichment from `exh-saag-2026-0075` onward.
- Probe official/list endpoints for CPHI, Saudi Warehousing, INDEX/LIGHTSPACE, Cityscape, Global Health, and Saudi Food while extracting historical candidates where 2026 current lists are unavailable.
