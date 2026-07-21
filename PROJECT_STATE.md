# Project State

Last updated: 2026-07-21
Status: Parallel multi-exhibition public-source research mode active

## Current objective
Run the Riyadh exhibition intelligence pipeline across multiple exhibitions in parallel, using current confirmed exhibitors plus the last two or three completed editions, with comprehensive collection across all relevant public sources.

## Operational mode
- Use several bounded research lanes at the same time; do not wait to finish one exhibition before starting source discovery or extraction for the next.
- Keep each agent on a non-overlapping lane: one current directory extraction, one historical-source lane, or one company-enrichment slice.
- Centralize final normalization, evidence IDs, duplicate checks, report counts, branch pushes, and PR updates in the coordinator workflow.
- Use `config/parallel-research-lanes.yaml` as the active lane map for daily work allocation.
- Keep Saudi Agriculture PR #5 as the active extraction/enrichment PR until reviewed or merged; launch LEAP, Saudi Event Show, Hotel & Hospitality, and historical-candidate lanes in parallel without external outreach.

## Priority queue
- [x] P0 — Establish the CIP operating model, canonical schemas, source policy, and quality rules.
- [x] P0 — Expand collection policy to official, third-party, unofficial, and unverified public sources with clear source labels.
- [ ] P0 — Validate the initial Riyadh exhibition calendar and classify exhibition vs conference-only events. _(partial/in progress; 18 Jul–31 Dec 2026 scope corrected, but category coverage gaps remain)_
- [ ] P0 — Register current and historical source URLs across official and third-party public sources.
- [ ] P0 — Start historical candidate collection immediately where 2026 directories are unavailable.
- [ ] P1 — Import/normalize the existing Riyadh exhibitions workbook into canonical CSV datasets.
- [ ] P1 — Build confirmed-current and historical-candidate records without mixing statuses.
- [ ] P1 — Enrich public business contacts from the full source universe in parallel lanes of about 15-25 companies per target per run.
- [ ] P2 — Implement deduplication, source-relationship labelling, evidence coverage, and quality validation scripts.
- [ ] P2 — Produce opportunity rankings for Core Media.
- [ ] P3 — Add recurring monitoring only after the initial normal Codex task and schemas are stable.
- [!] Any automatic external outreach, CRM import, publishing, or messaging requires Salah's explicit approval.

## Initial named discovery targets
LEAP, Cityscape Global, BAPEX, HR-focused exhibitions, and every other qualifying Riyadh exhibition through 31 December 2026. Names, dates, and eligibility must be verified before being treated as canonical.

## Daily log
### 2026-07-21 - Parallel current extraction continuation batch 4
- Continued the all-exhibitions workflow with BIO Middle East, LEAP, Big 5 Construct Saudi, Saudi Agriculture enrichment, and broad source discovery running in parallel.
- Added 224 additional current public-source company records: 126 BIO Middle East 2026, 50 LEAP 2026 rows, and 48 Big 5 Construct Saudi 2026 rows.
- Continued Saudi Agriculture enrichment for 26 records in the `exh-saag-2026-0075` through `exh-saag-2026-0100` range using public company, government/chamber, association, partner, social, and directory sources.
- Registered new source lanes for Saudi Warehousing & Logistics 2026 official exhibitor directory, HRSE KSA 2026 current sponsors/exhibitors, CPHI exhibitor essentials, Cityscape 2025 official event-app directory, Global Health 2026 app landing, and Black Hat MEA 2025 official historical directory.
- Upgraded HRSE KSA from a date-unconfirmed HR/recruitment candidate to an upcoming confirmed current target based on official 2026 HRSE pages.
- `database/exhibitors.csv` now contains 779 records, `database/evidence.csv` contains 1648 rows, and `database/exhibition-sources.csv` contains 93 source rows in the local branch before publication verification.
- No outreach, CRM import, automatic messaging, guessed contacts, or name-only merges were performed.

### 2026-07-21 - Parallel current extraction continuation batch 3
- Continued the approved all-exhibitions workflow rather than focusing on a single exhibition.
- Added 98 additional current public-source company records: 50 LEAP 2026 rows and 48 Big 5 Construct Saudi 2026 rows.
- Continued Saudi Agriculture enrichment for 15 records in the `exh-saag-2026-0051` through `exh-saag-2026-0074` range using public company/contact sources only.
- Added public-source enrichment for selected Saudi Event Show 2026 and Hotel & Hospitality Expo Saudi Arabia 2026 sponsor, partner, logo-strip, and company-public participants while preserving their source relationships.
- Registered additional broad source-scan findings for BIO Middle East, CPHI Middle East, Cityscape Global, Global Health, INDEX Saudi, Money20/20 Middle East, Saudi Warehousing & Logistics Expo, LIGHTSPACE Saudi Arabia, Saudi Food Expo, FABEX Saudi Arabia, HRSE KSA, Black Hat MEA, Industrial Transformation Saudi Arabia, and related candidates.
- Corrected BIO Middle East 2026 and CPHI Middle East 2026 from completed/historical May status to upcoming confirmed 14-16 Dec 2026 current targets based on current official pages.
- `database/exhibitors.csv` now contains 555 records, `database/evidence.csv` contains 1254 rows, and `database/exhibition-sources.csv` contains 86 source rows in the local branch before publication verification.
- No outreach, CRM import, automatic messaging, guessed contacts, or name-only merges were performed.

### 2026-07-21 - Parallel current extraction continuation batch 2
- Continued the approved multi-exhibition workflow across LEAP 2026, Big 5 Construct Saudi 2026, Saudi Build 2026, Saudi Event Show 2026, Hotel & Hospitality Expo Saudi Arabia 2026, and Saudi Agriculture enrichment.
- Added 135 additional current public-source company/participant records: 50 LEAP, 24 Big 5, 23 Saudi Build, 21 Saudi Event Show sponsor/partner participants, and 17 Hotel & Hospitality public-source participants/candidates.
- Expanded raw snapshots to include Saudi Event Show current sponsor/partner participants and Hotel & Hospitality current public-source candidates.
- Continued Saudi Agriculture enrichment for 9 additional records in the `exh-saag-2026-0038` through `exh-saag-2026-0050` range using official, affiliate, LinkedIn, company, and registry-mirror public sources.
- `database/exhibitors.csv` now contains 457 records and `database/evidence.csv` contains 1023 rows in the local branch before publication verification.
- Saudi Event Show and Hotel & Hospitality rows preserve sponsor, partner, logo-strip, public-social, company-calendar, media-partner, and advisory relationships explicitly; booth exhibitor status is not inferred from those rows.
- No outreach, CRM import, automatic messaging, guessed contacts, or name-only merges were performed.

### 2026-07-21 - Parallel current extraction batch 1
- Ran the approved multi-exhibition workflow across LEAP 2026, Big 5 Construct Saudi 2026, Saudi Build 2026, Saudi Elenex 2026, and Saudi Agriculture enrichment.
- Added 100 current confirmed exhibitor records from official 2026 sources: 25 LEAP, 24 Big 5 Construct Saudi, 25 Saudi Build, and 26 Saudi Elenex.
- Added raw snapshots for the four new current-extraction lanes.
- Continued Saudi Agriculture enrichment for 10 higher-yield records within `exh-saag-2026-0026` through `exh-saag-2026-0050`.
- Added 167 evidence rows for the 2026-07-21 extraction/enrichment work, bringing `database/evidence.csv` to 785 rows and `database/exhibitors.csv` to 322 rows.
- Saudi Build agent did not complete before shutdown; the batch was extracted locally from the official Saudi Build page.
- No outreach, CRM import, automatic messaging, guessed contacts, or name-only merges were performed.

### 2026-07-20 - Parallel multi-exhibition research mode launched
- Switched daily operation from single-exhibition sequencing to parallel multi-agent lanes across all qualifying Riyadh exhibitions.
- Added `config/parallel-research-lanes.yaml` to define active lanes, daily batch size, source priorities, coordination rules, and quality gates.
- Started read-only parallel agent scouting for LEAP 2026, The Saudi Event Show 2026, Hotel & Hospitality Expo Saudi Arabia 2026, Saudi Agriculture enrichment continuation, and the remaining calendar/historical-candidate backlog.
- Registered newly verified official current-directory lanes for Big 5 Construct Saudi 2026, Saudi Build 2026, and Saudi Elenex 2026.
- Corrected Saudi Event Show and Hotel & Hospitality 10Times pages from current-directory assumptions to historical/discovery-only because both pages state current-edition exhibitors are unavailable.
- Added 8 field-level evidence rows for the source-status corrections, newly located current-directory URLs, and Big 5 venue correction, bringing `database/evidence.csv` to 618 rows.
- Current GitHub state before this coordination update: Draft PR #5 is open, based on `main` commit `01136d944d408f522eb1887170a8f9b7a4a46f9a`, with Saudi Agriculture extraction plus enrichment batch 1 at head `0d7bad11215fae1a475463c8ffa252b5396472fe`.
- Coordination decision: continue publishing through Draft PRs, do not merge, do not contact companies, do not import to CRM, and keep every material fact source-backed with source relationship, page status, verification status, confidence, URL, and access date.

### 2026-07-20 - Saudi Agriculture 2026 enrichment batch 1
- Enriched the first 25 Saudi Agriculture 2026 exhibitor records using public sources only.
- Added official/company-site, LinkedIn/public company page, partner-directory, business-directory, and registry-preview evidence where stable sources were found.
- Captured public business contacts only when explicitly published; no guessed emails, phone numbers, WhatsApp numbers, or named contacts were added.
- Added 158 enrichment evidence rows, bringing `database/evidence.csv` from 452 to 610 rows while preserving all prior evidence.
- Key gaps remain: several early records still have no stable public website/contact source, LinkedIn coverage is partial, Google Business/Maps coverage was not captured in this batch, and no company has a verified named sales/marketing contact yet.

### 2026-07-18 — Saudi Agriculture 2026 exhibitor extraction batch 1
- Extracted all 222 visible raw exhibitor rows from the official Saudi Agriculture 2026 exhibitors-list table.
- Normalized 222 unique current exhibitor company records into `database/exhibitors.csv` without fuzzy/name-only merges.
- Added 222 exhibitor participation evidence rows and preserved a raw/source snapshot.
- Added exhibitor validation covering duplicate IDs, orphan evidence, exhibition ID, URL format, report counts, and no name-only merge behavior.
- Historical source coverage remains: 2025 explicit list `not_found`; 2024 third-party list source available in registry source map but company-level historical extraction not yet performed.

### 2026-07-18 — PR #3 final duplicate-source cleanup
- Removed duplicate Saudi Agriculture 2026 current source rows for the same exhibitors-list URL.
- Kept one Lighting Design & Technology 2023 historical exhibitor source and corrected the erroneous source id that implied a 2026 official current source.
- Downgraded Saudi Agriculture 2025 historical coverage to `not_found` because the reused exhibitors-list URL was not captured with explicit 2025 dating.
- Added registry validation for duplicate source composites: `exhibition_id + edition_year + source_url + current_or_historical`.

### 2026-07-18 — PR #3 registry correction pass
- Corrected the operational upcoming scope to 18 July 2026 through 31 December 2026.
- Reclassified seven pre-18-July events as `completed_historical` / `historical_2026_completed` so they remain available for historical extraction but are excluded from upcoming sales-pipeline totals.
- Expanded the registry to 32 rows across upcoming B2B exhibitions, completed historical 2026 exhibitions, secondary consumer/commercial opportunities, and date-unconfirmed candidates.
- Recorded 71 audited source-map rows and 230 field-level evidence rows with corrected source relationships, primary/third-party classification, lifecycle status, and current/historical classification.
- Reopened the P0 calendar-validation item as partial/in progress because HR/recruitment, BAPEX/FAPEX, equestrian, back-to-school, and other category gaps require further research before comprehensive validation can be claimed complete.
- [!] Salah to decide whether secondary consumer/commercial opportunities such as DUNES Expo, shopping/fashion pop-up markets, horse/equestrian events, and back-to-school retail fairs should enter the B2B Core Media pipeline.


### 2026-07-17 — Source expansion approved
- Completed final review of PR #2 across six files.
- Approved comprehensive collection from official, third-party, unofficial, and unverified public sources.
- Confirmed that discovery-only data remains usable when clearly labelled by source relationship, confidence, and verification status.
- Approved the expanded schemas and source configuration for operational use.

### 2026-07-17 — Comprehensive source expansion
- Expanded collection from official sources to all relevant publicly accessible sources.
- Explicitly added Eye of Riyadh, Saudi/international company directories, B2B/industry directories, Google Business/Maps, LinkedIn, social platforms, public news, and other public pages.
- Removed any requirement that a social account or public page be official or verification-badged.
- Required source relationship, verification status, confidence, URL, and access date so discovery-only data remains usable without being misrepresented.

### 2026-07-17 — Final review
- Completed final review of PR #1 across 13 files.
- Confirmed separation of current confirmed exhibitors from historical candidates.
- Confirmed the minimum two-edition and target three-edition historical collection rules.
- Confirmed source, privacy, validation, and no-automatic-outreach safeguards.
- Approved the bootstrap for merge and operation.

### 2026-07-17 — Bootstrap
- Bootstrapped CIP operating rules, schemas, source policy, historical-edition workflow, and review process.
- Added the mandatory last-two-editions rule with a third edition targeted whenever available.
- Confirmed that historical exhibitors are candidates, not current confirmed exhibitors.
