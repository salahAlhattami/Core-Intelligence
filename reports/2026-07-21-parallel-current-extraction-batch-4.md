# Parallel Current Extraction Batch 4

Date: 2026-07-21
Branch/PR: `codex/extract-saudi-agriculture-2026-exhibitors` / Draft PR #5
Mode: Parallel multi-exhibition public-source research

## Scope
- Extract BIO Middle East 2026 because its official current exhibitor list is now public.
- Continue LEAP 2026 after row 125 and Big 5 Construct Saudi 2026 after row 96.
- Continue Saudi Agriculture public-source enrichment for `exh-saag-2026-0075` through `exh-saag-2026-0100`.
- Register newly found current/historical source lanes for Saudi Warehousing & Logistics, HRSE KSA, CPHI, Cityscape, Global Health, and Black Hat MEA.
- Do not contact companies, infer contacts, merge by similar names, import CRM data, or merge to `main`.

## Current Extraction Results
| Exhibition | Raw snapshot | Current rows after batch | Batch 4 increase | Source status |
|---|---:|---:|---:|---|
| Saudi Agriculture 2026 | `database/raw/saudi-agriculture-2026-exhibitors-2026-07-18.csv` | 222 | 0 | Official current directory; enrichment continued separately |
| LEAP 2026 | `database/raw/leap-2026-exhibitors-2026-07-21.csv` | 175 | 50 | Public LEAP 2026 exhibitor page/load-more page; visible card names only |
| Big 5 Construct Saudi 2026 | `database/raw/big5-construct-saudi-2026-exhibitors-2026-07-21.csv` | 144 | 48 | Public official directory AJAX rows 97-144 |
| Saudi Build 2026 | `database/raw/saudi-build-2026-exhibitors-2026-07-21.csv` | 48 | 0 | Current official table rows already captured |
| Saudi Elenex 2026 | `database/raw/saudi-elenex-2026-exhibitors-2026-07-21.csv` | 26 | 0 | Official current list already fully visible |
| Saudi Event Show 2026 | `database/raw/saudi-event-show-2026-current-sponsors-partners-2026-07-21.csv` | 21 | 0 | Official sponsor/partner pages; booth exhibitor status not inferred |
| Hotel & Hospitality Expo Saudi Arabia 2026 | `database/raw/hotel-hospitality-expo-saudi-2026-current-public-candidates-2026-07-21.csv` | 17 | 0 | Official logo strip plus public sources; relationship preserved |
| BIO Middle East 2026 | `database/raw/bio-middle-east-2026-exhibitors-2026-07-21.csv` | 126 | 126 | Official current exhibitor list; stand/profile URLs captured where visible |

Parallel current batch exhibitors added: 557
Total current company records after this run: 779

## Data Counts After This Run
- Total exhibitor/company records: 779
- Total evidence rows: 1648
- Total registered exhibition-source rows: 93
- New evidence rows in this continuation: 394
- New current/company records in this continuation: 224
- Contact-bearing company records: 66 email-bearing, 55 phone/WhatsApp-bearing, 35 LinkedIn-bearing, and 195 website-bearing.

## Enrichment Added
- Saudi Agriculture enrichment continued for 26 records from `0075` through `0100`.
- Captured public company websites, public emails, phone/WhatsApp values, LinkedIn/public social pages, and selected context evidence only when explicitly visible in public sources.
- Some exact-name or social/directory values remain `discovery_only` or `verified_cross_source`; they are not treated as stronger than the source supports.
- Public named contact emails that appeared on source pages were retained as source-backed public evidence/contact text; no private or guessed contact data was added.

## Broad Source Scan
- Saudi Warehousing & Logistics 2026 now has a current official public exhibitor directory source recorded for next extraction.
- HRSE KSA was upgraded from a date-unconfirmed HR/recruitment candidate to an upcoming confirmed current target because official pages list 2026 event/exhibition context and named sponsors/exhibitors.
- CPHI exhibitor essentials, Cityscape 2025 official event-app directory, Global Health 2026 app landing, and Black Hat MEA 2025 official historical directory were recorded as supporting source lanes.
- Historical-only and discovery-only sources remain labelled as such and are not converted into confirmed current exhibitors.

## Quality Notes
- This is a current exhibitor/company extraction batch plus public-source enrichment, not completed enrichment.
- BIO duplicate names visible in the official list were kept as separate listing occurrences only when source profile context was preserved and marked for duplicate-name review.
- Cross-exhibition repeat companies remain allowed only when each event relationship is separately source-backed.
- No guessed emails, phone numbers, WhatsApp numbers, or named private contacts were added.
- No automatic outreach, CRM import, or GitHub merge was performed.

## Next Action
- Extract Saudi Warehousing & Logistics 2026 current official directory, starting with its public 129-exhibitor list.
- Continue Big 5 after row 144 and LEAP after row 175.
- Continue Saudi Agriculture enrichment from `exh-saag-2026-0101` onward.
- Begin HRSE KSA current sponsor/exhibitor extraction while keeping sponsor, partner, and exhibitor labels separate.
