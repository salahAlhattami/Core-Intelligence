# Saudi Agriculture 2026 Current Exhibitor Extraction Batch

Date: 2026-07-18
Branch: codex/extract-saudi-agriculture-2026-exhibitors
Exhibition ID: riyadh-2026-saudi-agriculture
Source: https://saudi-agriculture.com/exhibitors-list/

## Scope
This current exhibitor extraction batch extracts every visible company row from the current Saudi Agriculture 2026 official exhibitors-list table. The extraction preserves raw exhibitor names, stand numbers, sectors, product text, country, listed websites, and official table details before normalization. No guessed emails, phone numbers, personal data, or outreach actions were added.

## Counts
- Raw exhibitor names extracted: 222
- Unique companies after dedupe: 222
- Companies with websites: 116
- Companies with LinkedIn: 0
- Public contact methods captured: 0
- Named public contacts captured: 0
- Conflicts: 0
- Evidence rows added for current participation: 222

## Deduplication
Deduplication used official domain when listed, otherwise exact normalized raw company name plus country. No companies were merged using name similarity alone. This produced no duplicates requiring merge review in this batch.

## Historical coverage
- 2025: not_found for explicit exhibitor-list coverage. The reused current exhibitors-list URL was not captured with explicit 2025 dating and is not counted as a 2025 list.
- 2024: one third-party/event-directory exhibitor source remains available from the registry source map, but company-level historical extraction was not performed in this batch.

## Source relationship and verification
- Participation evidence comes from the official Saudi Agriculture exhibitors-list page and is marked `verified_primary`.
- Company websites listed inside the official directory are preserved as listed public URLs, but contact fields remain blank unless a public source explicitly provides them.
- LinkedIn/social/profile fields are left blank in this batch because no stable public social URL was captured from the official exhibitor table itself.

## Files changed
- database/exhibitors.csv
- database/evidence.csv
- database/raw/saudi-agriculture-2026-exhibitors-2026-07-18.csv
- reports/2026-07-18-saudi-agriculture-2026-exhibitor-batch.md
- tests/validate_exhibitors.py
- PROJECT_STATE.md

## Validation
- `python3 tests/validate_registry.py`
- `python3 tests/validate_exhibitors.py`
- `git diff --check`

## Limitations
This is a current exhibitor extraction batch, not completed enrichment. It captures the full current official exhibitor list, but does not yet perform broad per-company contact enrichment across LinkedIn, social pages, chambers, directories, news, PDF catalogues, distributor pages, or company websites. That should follow in smaller enrichment batches.

## Recommended next task
Enrich the first 25 Saudi Agriculture 2026 exhibitors with company websites, LinkedIn/company social pages, public business emails/phones, public named sales/marketing/business-development contacts, and cross-source verification.
