# Parallel Current Extraction Batch 1

Date: 2026-07-21
Branch/PR: `codex/extract-saudi-agriculture-2026-exhibitors` / Draft PR #5
Mode: Parallel multi-exhibition public-source research

## Scope
- Extract current confirmed exhibitors from several official 2026 exhibitor sources in the same run.
- Continue Saudi Agriculture public-source enrichment for selected high-yield records in `exh-saag-2026-0026` through `exh-saag-2026-0050`.
- Do not contact companies, infer contacts, merge by similar names, import CRM data, or merge to `main`.

## Current Extraction Results
| Exhibition | Raw snapshot | Rows added | Source status |
|---|---:|---:|---|
| LEAP 2026 | `database/raw/leap-2026-exhibitors-2026-07-21.csv` | 25 | Official current page; visible card names only |
| Big 5 Construct Saudi 2026 | `database/raw/big5-construct-saudi-2026-exhibitors-2026-07-21.csv` | 24 | Official current directory, first page rows 1-24 of 535 |
| Saudi Build 2026 | `database/raw/saudi-build-2026-exhibitors-2026-07-21.csv` | 25 | Official current list, first 25 visible rows |
| Saudi Elenex 2026 | `database/raw/saudi-elenex-2026-exhibitors-2026-07-21.csv` | 26 | Official current list, all 26 visible rows |

Parallel current batch exhibitors added: 100

## Data Counts After This Run
- Total exhibitor records: 322
- Saudi Agriculture current exhibitors: 222
- LEAP current exhibitors added: 25
- Big 5 Construct Saudi current exhibitors added: 24
- Saudi Build current exhibitors added: 25
- Saudi Elenex current exhibitors added: 26
- Evidence rows total: 785
- New 2026-07-21 evidence rows: 167
- Current-participation evidence rows added: 100
- Big 5 profile/detail evidence rows added: 32
- Saudi Agriculture enrichment evidence rows added: 35

## Saudi Agriculture Enrichment
- Enriched 10 higher-yield records from `exh-saag-2026-0026` through `exh-saag-2026-0050`.
- Records with contact source URLs in this slice after the update: 9.
- Added official company websites, public emails/phones where explicitly listed, LinkedIn public pages where matched to company context, and one exact-name supporting business directory.
- No guessed emails, generated phone numbers, inferred WhatsApp numbers, or named private contacts were added.

## Source Notes
- LEAP page exposes official 2026 exhibitor names, but the visible card text does not expose stand, country, sector, or company website fields.
- Big 5 first page exposes stand, hall, country, and official profile links; selected profile rows also exposed website and sector/category detail.
- Saudi Build and Saudi Elenex official pages expose table rows with company, stand, country, and some sector/product/website fields.
- Saudi Build agent did not finish before shutdown; the 25-row batch was extracted locally from the official page.

## Quality Notes
- All new current exhibitor rows are `confirmed_current`, `is_current_confirmed=true`, and source-backed by official current exhibitor pages.
- Extraction is intentionally partial for LEAP, Big 5, and Saudi Build; follow-up lanes should continue from the next visible row/page.
- This is not completed enrichment for any newly added exhibition.

## Next Action
- Continue Big 5 from row 25 onward.
- Continue Saudi Build after row 25.
- Continue LEAP through additional loaded/paginated batches.
- Continue Saudi Agriculture enrichment with remaining records in `0026`-`0050`, then proceed to `0051`-`0075`.
- Start cross-source enrichment for the newly added Big 5, Saudi Build, Saudi Elenex, and LEAP records only after raw/current extraction coverage is stable.
