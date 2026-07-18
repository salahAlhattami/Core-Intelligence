# Riyadh Exhibition Registry and Historical Source Map

Date: 2026-07-17
Branch/PR: managed Codex Cloud task / draft PR metadata
Operator: Codex

## Scope and rerun status
This is a rerun because the prior local commit `d8fe209` and prior registry artifacts were not available in this managed checkout. The run built a source-backed foundational registry for qualifying Riyadh exhibitions from 2026-07-17 through 2026-12-31, using official, organizer/event, third-party directory, search-discovery, and other public sources.

## Results
- Total qualifying exhibitions: 16
- Total excluded / review-only events documented: 4
- Current 2026 exhibitor directories found: 4
- No current 2026 exhibitor directory found: 12
- Exhibitions with one located historical edition source/list: 6
- Exhibitions with two located historical edition sources/lists: 0
- Exhibitions with three located historical edition sources/lists: 0
- Source-map rows: 70
- Field-level evidence rows: 86

Counts match the previous unavailable run checkpoints because this rerun rebuilt the same foundational scale: 16 exhibitions, 70 source-map records, and 86 evidence records. The exact exhibition mix should still be reviewed in the next pass because several newer 2026 shows were retained as discovery-only leads.

## Qualifying exhibitions
| Exhibition | Priority | Sector | Current directory | Source rows | Verification | Confidence |
|---|---:|---|---|---:|---|---|
| LEAP 2026 | A+ | technology | yes | 5 | verified_primary | high |
| Cityscape Global 2026 | A+ | real_estate | no | 5 | verified_cross_source | high |
| Global Health Exhibition 2026 | A+ | healthcare | yes | 5 | verified_primary | high |
| Saudi Build 2026 | A | construction | no | 5 | verified_cross_source | medium |
| Big 5 Construct Saudi 2026 | A | construction | no | 4 | verified_cross_source | medium |
| INDEX Saudi Arabia 2026 | A | interiors_design | yes | 5 | verified_primary | high |
| Automechanika Riyadh 2026 | A | automotive_aftermarket | no | 5 | verified_cross_source | medium |
| CPHI Middle East 2026 | A | pharmaceuticals | no | 4 | verified_cross_source | medium |
| BIO Middle East 2026 | A | biotech | yes | 4 | verified_primary | high |
| Saudi Travel Market 2026 | B | tourism | no | 4 | discovery_only | low |
| Beautyworld Saudi Arabia 2026 | B | beauty | no | 4 | verified_cross_source | medium |
| Saudi Wood Expo 2026 | B | wood_construction | no | 4 | verified_cross_source | medium |
| Saudi Industrial Series 2026 | A | industrial_manufacturing | no | 4 | verified_cross_source | medium |
| WAM Saudi Expo 2026 | A | advanced_manufacturing_logistics | no | 4 | verified_cross_source | medium |
| Smart Cities Saudi Expo 2026 | B | smart_cities | no | 4 | discovery_only | low |
| World Defense Show 2026 | A | defense_security | no | 4 | verified_primary | high |

## Excluded and Salah-review events
| Event | Status | Reason |
|---|---|---|
| DUNES Expo 2026 | [!] Salah review | Outdoor lifestyle/consumer-facing event with exhibitor floor; unclear B2B priority for Core Media. |
| Riyadh Season consumer activations | excluded | Entertainment/festival activations, not a stable trade exhibition registry target. |
| General HR conferences without exhibitor lists | excluded | Conference/networking-only sources were not included unless an exhibition floor was evidenced. |
| Shopping/fashion pop-up markets | [!] Salah review | Potential booth/design opportunity but not clearly qualifying B2B/professional exhibition. |

## Current and historical research gaps
- Current directories were located for LEAP, Global Health, INDEX Saudi Arabia, and BIO Middle East.
- Most 2026 construction, automotive, industrial, travel, beauty, wood, smart-city, and defense/security targets have exhibit/registration or event pages but no open current exhibitor directory found in this pass.
- Explicit `not_found` source rows were recorded for baseline 2025 and 2024 historical searches where no stable public historical exhibitor list was captured.
- Historical records remain source-map records only; no historical exhibitor is treated as a 2026 confirmed exhibitor.

## A+ and A priority extraction order
1. LEAP 2026
2. Global Health Exhibition 2026
3. Cityscape Global 2026
4. BIO Middle East 2026
5. INDEX Saudi Arabia 2026
6. Saudi Build 2026
7. Big 5 Construct Saudi 2026
8. Saudi Industrial Series 2026
9. World Defense Show 2026
10. Automechanika Riyadh 2026
11. CPHI Middle East 2026
12. WAM Saudi Expo 2026

## Conflicts and low-confidence records
- LEAP exhibitor counts vary across official/event and third-party list pages; the registry records the official-style public claim and flags variance in notes.
- Global Health has a 2026 event homepage and a public exhibitor-list page whose page copy references 2025; retained with notes for follow-up.
- Saudi Travel Market and Smart Cities Saudi Expo are discovery-only until official event pages are cross-checked.
- WAM Saudi Expo dates/venue need primary-source reconfirmation despite strong third-party/event-directory evidence.

## Limitations
- This rerun did not extract individual exhibitor companies; it created the registry and source map that should drive the next extraction tasks.
- Search-result URLs are preserved only as discovery/not-found audit records and must not be treated as evidence of exhibitor participation.
- Several current directories may require JavaScript, app access, registration, or later publication.
- No private personal data, guessed contacts, outreach, CRM import, or external publishing was performed.

## Exact output row counts
- `database/exhibitions.csv`: 16 data rows
- `database/exhibition-sources.csv`: 70 data rows
- `database/evidence.csv`: 86 data rows

## Recommended next task
Start exhibitor extraction for the four exhibitions with current 2026 directory/list coverage first, beginning with LEAP 2026 and Global Health Exhibition 2026, then process BIO Middle East and INDEX Saudi Arabia.
