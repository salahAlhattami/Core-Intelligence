# AGENTS.md — Core Intelligence Platform

## Mission
Build a comprehensive, source-backed sales intelligence database for Core Media covering exhibitions with exhibitors in Riyadh, initially through the end of 2026.

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
1. Collect confirmed current-edition exhibitors when evidence exists.
2. If the current directory is absent or incomplete, do not wait. Collect exhibitors from at least the last two completed editions.
3. Target three completed editions whenever public lists/directories are available.
4. Keep historical participants as return-likelihood candidates, never label them confirmed without current-edition evidence.
5. Record each participation year/edition separately and preserve its source URL.
6. Repeated historical participation raises return likelihood but does not prove current participation.

## Comprehensive public-source collection
- Search broadly across every relevant publicly accessible source; do not limit research to official or verified accounts.
- Include official event sources, historical catalogues, exhibitor lists, floor plans, websites, search results, chambers, government registries, Google Business/Maps, Eye of Riyadh (عين الرياض), other Saudi and international company directories, B2B directories, distributor directories, LinkedIn, Instagram, Facebook, X, YouTube, and other public profiles or pages.
- Unofficial, unverified, third-party, and directory sources are allowed for discovery and enrichment.
- Do not discard a useful public page merely because it lacks a verification badge or cannot be proven official.
- Label every source by relationship/type and confidence. Keep observed public data separate from confirmed facts.
- Cross-check important contact or participation claims when possible, but retain a discovery-only lead when cross-verification is not yet available.
- Preserve the exact source URL, source name, access date, and notes for every collected value.

## Public-data and safety rules
- Use publicly accessible business information.
- Never guess, infer, pattern-generate, or fabricate email addresses or phone numbers.
- Never collect private personal contact information.
- A named professional contact is allowed when publicly published with a business role/source.
- Public social profiles may be inspected; do not use prohibited bulk scraping of restricted platforms.
- Every material fact or lead must carry a source URL and collection/verification date.
- Deduplicate primarily by domain, normalized legal/company name, phone, and contextual evidence.
- Keep `not_found`, `pending`, and `discovery_only` distinct.

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

Allowed source relationships:
- `official`
- `organizer_or_event`
- `government_or_chamber`
- `third_party_directory`
- `unofficial_social_or_public_page`
- `search_discovery`
- `unknown`

## Definition of done
A task is complete only when records are normalized, source-backed, deduplicated, status-labelled, logged, and summarized in a PR. Discovery-only data is acceptable when clearly labelled and not misrepresented as verified.
