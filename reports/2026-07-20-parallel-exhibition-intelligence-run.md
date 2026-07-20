# Parallel Exhibition Intelligence Run

Date: 2026-07-20
Branch/PR: `codex/extract-saudi-agriculture-2026-exhibitors` / Draft PR #5
Operator: Codex coordinator with parallel read-only research agents

## Scope
- Mode change: run multiple exhibition lanes in parallel instead of sequencing all work through one exhibition.
- Repository: `salahAlhattami/Core-Intelligence`
- GitHub main source of truth: `origin/main` at `01136d944d408f522eb1887170a8f9b7a4a46f9a`
- Active Draft PR at start of run: #5, head `0d7bad11215fae1a475463c8ffa252b5396472fe`

## Parallel Lanes Started
| Lane | Exhibition scope | First deliverable | Status |
|---|---|---|---|
| Saudi Agriculture enrichment | `riyadh-2026-saudi-agriculture` records `0026`-`0050` | Public-source enrichment plan and next batch | Started |
| LEAP current extraction | `riyadh-2026-leap` | Current-directory extraction feasibility and source map | Started |
| Saudi Event Show current extraction | `riyadh-2026-saudi-event-show` | Third-party/current directory assessment and sample leads | Started |
| Hotel & Hospitality current extraction | `riyadh-2026-hotel-hospitality-expo` | Third-party/current directory assessment and sample leads | Started |
| Calendar and historical backlog | Multiple Riyadh exhibitions | Prioritized lane matrix for current vs historical work | Started |

## Current Data Baseline
- Primary B2B upcoming exhibitions currently registered: 18
- Completed-historical 2026 exhibitions currently registered: 7
- Current exhibitor-list/logo sources marked available after this run: 6
- Current exhibitor-list source tracked as `unknown` pending current-year verification: 1
- Historical exhibitor-list sources marked available: 9
- Saudi Agriculture exhibitors currently in PR #5: 222
- Saudi Agriculture raw snapshot rows currently in PR #5: 222
- Evidence rows after this coordination/source update: 618

## Agent Findings Logged This Run
### Saudi Agriculture Enrichment Continuation
- Recommended next contiguous slice: `exh-saag-2026-0026` through `exh-saag-2026-0050`.
- Higher-yield Saudi records with listed websites or stronger public-source prospects: Al Muneef, Al Ousaimi Group, Al Rajhi and Al-Misfer Agricultural, Al Rawda Factory, Al Taleb Group, Al Wasail Industrial, Al Watania Agriculture, Al Yaseen Agriculture, Almarai, Artat Enterprise, and Asasiat.
- Trickier Saudi records needing Arabic/chamber/registry follow-up: Al Rajhia Dates/RAPCO, Al Raya Specialities Industrial, Al Tanseeq, ARASCO, and Areen Najd.
- International records needing exact-entity checks: Al Rafiq Greenhouses, Alliance Food Security Holding, Andritz Feed & Biofuel, Artigianfer, and Ashapura International.
- Evidence IDs should continue after `ev-saag-enrich-20260720-0158`.

### Saudi Event Show 2026
- Official Informa page confirms the 2026 event and sponsor/partner ecosystem but does not expose a named 2026 exhibitor directory.
- 10Times exposes a third-party exhibitor page with a visible count of 76, but also states current-edition exhibitors are not available and appears to include past-edition exhibitors.
- Official 2025 exhibitor/partner directory is extractable as historical coverage; 2024 has public press/social/directory evidence but no stable full official directory found in this pass.
- Classification decision: use official 2026 sponsor/partner entries only as sponsor/partner records unless exhibitor status is explicit; treat 10Times company names as `discovery_only` or historical/third-party leads until cross-verified.

### Hotel & Hospitality Expo Saudi Arabia 2026
- Official 2026 event page is active and confirms the event, but the publicly visible exhibitor evidence is a logo strip rather than a structured directory.
- Approximately 14 official 2026 logos were visible in the scouting pass; sample names included RAK Porcelain, Roasting House, UNOX, Ozti, Back Care, Wooden Coffee, Black Knight, CUPTIME, Breehant Coffee & Roastery, and Port Stores.
- 10Times explicitly says current-edition exhibitors are not available and shows past-edition exhibitors; do not classify those names as 2026 `confirmed_current`.
- Official 2025 directory appears extractable with 138 records; 2024 has AUMA/official co-located evidence but needs careful status labelling.
- Classification decision: treat official visible 2026 logos as `confirmed_current` only when the company name can be read and source-backed; treat 10Times rows as historical/discovery leads.

### Calendar Backlog and Newly Verified Current Directories
- Newly verified official current directory lanes were registered for Big 5 Construct Saudi 2026, Saudi Build 2026, and Saudi Elenex 2026.
- Big 5 Construct Saudi official directory is extractable and shows 535 exhibitor rows on the first page set.
- Saudi Build official list is extractable with named companies, stand numbers, countries, sectors, products, details, and website fields.
- Saudi Elenex official list is extractable with named companies, stand numbers, countries, sectors, products/details, and website fields.
- Saudi Food Expo official homepage confirms the 2026 event and links an exhibitors page with named companies, but row-level current-year labelling still needs verification before confirmed-current extraction.
- Historical/watch lanes remain appropriate for Cityscape Global, Global Health, INDEX Saudi Arabia, Money20/20 Middle East, Black Hat MEA, Industrial Transformation Saudi, Foodex, Lift City, and ORGATEC until a stable current 2026 directory is verified.

## Data Corrections Made
- Added `config/parallel-research-lanes.yaml`.
- Updated `database/exhibitions.csv` for newly located official current directories and corrected Saudi Event Show/Hotel current-directory assumptions.
- Updated `database/exhibition-sources.csv` with source rows/corrections, raising source-map rows to 73 after merging a duplicate Hotel 10Times historical row.
- Added 8 field-level evidence rows for the new directory findings, source-status corrections, and Big 5 venue correction, raising `database/evidence.csv` to 618 rows.
- Downgraded 10Times Saudi Event Show and Hotel exhibitor pages from current-directory use to historical/discovery-only because each page states current-edition exhibitors are not available.

## Coordination Rules
- Do not use one exhibition as a bottleneck for the whole research program.
- Assign each agent one non-overlapping lane: current-directory extraction, historical candidate collection, or company enrichment slice.
- Keep final CSV normalization, evidence IDs, duplicate checks, report counts, commits, pushes, and PR updates in one coordinator workflow.
- Preserve `confirmed_current`, `historical_repeat_candidate`, `historical_single_candidate`, `sponsor_or_partner_only`, and `unverified` as separate statuses.
- Keep third-party and unofficial public sources usable but explicitly labelled by `source_relationship`, `account_or_page_status`, `verification_status`, `confidence`, URL, and access date.
- Do not guess emails, phone numbers, WhatsApp numbers, or named contacts.
- Do not merge companies by similar name alone.
- Do not merge PRs, contact companies, or import records into CRM.

## Immediate Work Allocation
| Priority | Work package | Recommended agent output |
|---|---|---|
| P0 | LEAP 2026 official current directory | Raw source snapshot, normalized current exhibitors, evidence, report |
| P0 | Big 5 Construct Saudi official current directory | Raw source snapshot, normalized current exhibitors, evidence, report |
| P0 | Saudi Build official current directory | Raw source snapshot, normalized current exhibitors, evidence, report |
| P0 | Saudi Elenex official current directory | Raw source snapshot, normalized current exhibitors, evidence, report |
| P0 | Saudi Agriculture enrichment continuation | Enrich records `0026`-`0050` with public business sources |
| P0 | Saudi Event Show 2026 official sponsors and historical directory | Extract sponsor/partner-only records separately from historical/discovery exhibitor leads |
| P0 | Hotel & Hospitality 2026 logo strip and 2025 directory | Extract official 2026 logo-only records separately from 2025 historical candidates |
| P0 | Saudi Food Expo current-year verification | Verify whether the populated exhibitors page is explicitly 2026 before extracting as confirmed-current |
| P1 | Historical candidates for targets without current directories | Last two completed editions first; target third edition when public sources are reliable |

## Quality Gate
- `python tests/validate_registry.py`
- `python tests/validate_exhibitors.py` when exhibitor data changes
- `git diff --check`
- Duplicate exhibitor IDs: 0 required
- Duplicate evidence IDs: 0 required
- Orphan exhibitor evidence: 0 required
- Report counts must reconcile with CSV row counts

## Decision
Parallel multi-exhibition operation is now active. The next data-producing PR updates should come from multiple lanes instead of continuing Saudi Agriculture alone.
