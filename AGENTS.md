# AGENTS.md — Core Intelligence Platform

## Mission
Build a verified, source-backed sales intelligence database for Core Media covering exhibitions with exhibitors in Riyadh, initially through the end of 2026.

## Roles
- Codex executes collection, normalization, enrichment, validation, tests, reports, and pull requests.
- ChatGPT defines tasks, reviews strategy and evidence, audits quality, and reviews pull requests.
- Salah approves blocked/sensitive decisions and final merges.
- GitHub is the single source of truth. Do not rely on chat-only decisions.

## Mandatory run protocol
1. Read `MASTER_PROMPT.md`, `PROJECT_STATE.md`, and relevant config before work.
2. Work on the next open `[ ]` item by priority.
3. Never execute items marked `[!]`; they require Salah's explicit approval.
4. Update data, evidence, validation state, and reports in the same PR.
5. Update `PROJECT_STATE.md` with a dated newest-first log entry.
6. Open a focused PR; do not merge it.

## Exhibitor history rule
For every target exhibition:
1. Collect confirmed current-edition exhibitors when an official directory exists.
2. If the current directory is absent or incomplete, do not wait. Collect exhibitors from at least the last two completed editions.
3. Target three completed editions whenever public lists/directories are available.
4. Keep historical participants as return-likelihood candidates, never label them confirmed without current-edition evidence.
5. Record each participation year/edition separately and preserve its source URL.
6. Repeated historical participation raises return likelihood but does not prove current participation.

## Public-data and safety rules
- Use only publicly published business information.
- Never guess, infer, pattern-generate, or fabricate email addresses or phone numbers.
- Never collect private personal contact information.
- A named professional contact is allowed only when publicly published with a business role/source.
- Social profiles may be checked manually as public pages; do not bulk scrape restricted platforms.
- Secondary directories are discovery sources, not final proof unless cross-verified.
- Every material fact must carry a source URL and verification date.
- Deduplicate primarily by official domain plus normalized legal/company name.
- Keep "not found" distinct from blank/not-yet-researched.

## Evidence and status
Allowed participation statuses:
- `confirmed_current`
- `historical_repeat_candidate`
- `historical_single_candidate`
- `sponsor_or_partner_only`
- `unverified`

Allowed verification statuses:
- `verified_primary`
- `verified_cross_source`
- `discovery_only`
- `conflict_needs_review`
- `not_found`

## Definition of done
A task is complete only when records are normalized, source-backed, deduplicated, validated, logged, and summarized in a PR.
