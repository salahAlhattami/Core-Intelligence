# Non-LEAP Current Exhibition Extraction Batch

Date: 2026-07-23
Branch: codex/extract-non-leap-current-exhibitors
Mode: Current exhibitor/company extraction with LEAP intentionally skipped

## Scope
This batch continues the current exhibitor/company extraction workflow after Saudi Agriculture 2026 while intentionally excluding LEAP 2026. It restores source-backed current rows for the remaining available non-LEAP exhibition lists and keeps sponsor/partner/logo-strip records labelled according to the public source relationship. This is a current extraction batch, not completed enrichment.

## LEAP skip
- `riyadh-2026-leap` rows added in this batch: 0
- `database/raw/leap-2026-exhibitors-2026-07-21.csv` is not included in this batch.
- Existing registry/source-map references to LEAP remain unchanged, but no LEAP company records are added to `database/exhibitors.csv`.

## Counts
- Non-LEAP current batch records added: 382
- Total current company records after this run: 604
- Total evidence rows after this run: 1157
- Total registered exhibition-source rows after this run: 93
- Raw snapshot total after this run: 604
- Company records with websites: 175
- Email-bearing company records: 9
- Phone or WhatsApp-bearing company records: 11
- LinkedIn-bearing company records: 11

## Records by exhibition
| Exhibition | Rows | Source status |
|---|---:|---|
| Saudi Agriculture 2026 | 222 | Existing official current extraction batch |
| Big 5 Construct Saudi 2026 | 144 | Official current directory partial extraction |
| BIO Middle East 2026 | 126 | Official current exhibitor list |
| Saudi Build 2026 | 48 | Official current exhibitor list |
| Saudi Elenex 2026 | 26 | Official current exhibitor list |
| Saudi Event Show 2026 | 21 | Official sponsor/partner participant pages; booth exhibitor status is not inferred |
| Hotel & Hospitality Expo Saudi Arabia 2026 | 17 | Official logo strip plus public-source participants/candidates; relationship preserved |

## Raw snapshots
- `database/raw/saudi-agriculture-2026-exhibitors-2026-07-18.csv` — 222 rows
- `database/raw/big5-construct-saudi-2026-exhibitors-2026-07-21.csv` — 144 rows
- `database/raw/bio-middle-east-2026-exhibitors-2026-07-21.csv` — 126 rows
- `database/raw/saudi-build-2026-exhibitors-2026-07-21.csv` — 48 rows
- `database/raw/saudi-elenex-2026-exhibitors-2026-07-21.csv` — 26 rows
- `database/raw/saudi-event-show-2026-current-sponsors-partners-2026-07-21.csv` — 21 rows
- `database/raw/hotel-hospitality-expo-saudi-2026-current-public-candidates-2026-07-21.csv` — 17 rows

## Source handling
- Official current directories are marked `verified_primary` where the source exposes named current exhibitors.
- Saudi Event Show sponsor/partner records are retained as current public participants from official sponsor/partner pages; booth exhibitor status is not inferred.
- Hotel & Hospitality rows are retained from the official 2026 logo strip and public-source candidates with relationship/confidence preserved.
- No guessed emails, phone numbers, WhatsApp numbers, LinkedIn URLs, or private contacts were added.

## Validation
- `python tests/validate_registry.py`
- `python tests/validate_exhibitors.py`
- `git diff --check`

## Next extraction lanes
- Saudi Warehousing & Logistics Expo 2026 official directory.
- HRSE KSA 2026 sponsor/exhibitor list, with sponsor, partner, and exhibitor roles kept separate.
- Cityscape, Global Health, INDEX, CPHI, Black Hat, Saudi Food, Industrial Transformation, and historical-only lists as their public sources become extractable.
