# Riyadh Exhibition Registry and Historical Source Map Corrections

Date: 2026-07-18
Branch/PR: PR #3 update / managed Codex Cloud task
Operator: Codex

## Scope correction
The operational upcoming-exhibition registry now covers exhibitions occurring from **18 July 2026 through 31 December 2026**. Seven events that ended before 18 July 2026 were retained as `completed_historical` / `historical_2026_completed` and are excluded from upcoming sales-pipeline totals.

## Corrected pipeline counts
- Upcoming qualifying B2B exhibitions: 18
- Completed 2026 exhibitions retained for historical extraction: 7
- Secondary consumer/commercial opportunities: 4
- Date-unconfirmed candidates requiring more calendar research: 3
- Excluded non-exhibition events/categories documented: 3
- Current 2026 exhibitor/company directories found for upcoming B2B pipeline: 4
- Upcoming B2B current-directory gaps: 14
- Upcoming B2B exhibitions with one historical exhibitor/list edition found: 5
- Upcoming B2B exhibitions with two historical exhibitor/list editions found: 2
- Upcoming B2B exhibitions with three historical exhibitor/list editions found: 0
- `database/exhibitions.csv` rows: 32
- `database/exhibition-sources.csv` rows: 71
- `database/evidence.csv` rows: 230

## Upcoming qualifying B2B exhibitions
| Exhibition | Dates | Lifecycle | Priority | Sector | Current list | Historical list editions | Verification | Confidence |
|---|---|---|---:|---|---|---:|---|---|
| LEAP 2026 | 2026-08-31–2026-09-03 | upcoming_confirmed | A+ | technology_ai | yes | 1 | verified_primary | high |
| Cityscape Global 2026 | 2026-11-16–2026-11-19 | upcoming_confirmed | A+ | real_estate | no | 0 | verified_cross_source | high |
| Global Health Exhibition 2026 | 2026-10-26–2026-10-29 | upcoming_confirmed | A+ | healthcare | no | 2 | verified_primary | high |
| Saudi Build 2026 | 2026-11-02–2026-11-05 | upcoming_confirmed | A | construction | no | 0 | verified_cross_source | medium |
| Big 5 Construct Saudi 2026 | 2026-08-30–2026-09-02 | upcoming_confirmed | A | construction | no | 0 | verified_cross_source | medium |
| INDEX Saudi Arabia 2026 | 2026-09-06–2026-09-08 | upcoming_confirmed | A | interiors_design | no | 1 | verified_primary | high |
| Saudi Warehousing & Logistics Expo 2026 | 2026-08-30–2026-09-01 | upcoming_confirmed | A | logistics_supply_chain | no | 0 | verified_cross_source | high |
| The Saudi Event Show 2026 | 2026-09-09–2026-09-10 | upcoming_confirmed | A | events_mice_production | yes | 1 | verified_cross_source | high |
| Money20/20 Middle East 2026 | 2026-09-14–2026-09-16 | upcoming_confirmed | A | fintech | no | 0 | verified_primary | high |
| Hotel & Hospitality Expo Saudi Arabia 2026 | 2026-09-15–2026-09-17 | upcoming_confirmed | A | hospitality | yes | 1 | verified_cross_source | medium |
| Lighting Design & Technology Expo 2026 | 2026-09-06–2026-09-08 | upcoming_discovery | B | lighting_design_technology | no | 1 | discovery_only | low |
| ORGATEC WORKSPACE Saudi Arabia 2026 | 2026-09-13–2026-09-15 | upcoming_discovery | B | workspace_interiors | no | 0 | conflict_needs_review | medium |
| Saudi Agriculture 2026 | 2026-10-19–2026-10-22 | upcoming_confirmed | A | agriculture_foodpack_aquaculture | yes | 2 | verified_primary | high |
| Saudi Food Expo 2026 | 2026-11-15–2026-11-18 | upcoming_discovery | B | food_hospitality | no | 0 | discovery_only | low |
| Saudi Elenex 2026 | 2026-11-02–2026-11-05 | upcoming_confirmed | A | energy_electricity_hvac | no | 0 | verified_primary | high |
| LIFT CITY EXPO Riyadh 2026 | 2026-11-26–2026-11-28 | upcoming_confirmed | B | elevators_vertical_transport | no | 0 | discovery_only | medium |
| Industrial Transformation Saudi Arabia 2026 | 2026-11-30–2026-12-02 | upcoming_confirmed | A | industrial_manufacturing | no | 0 | discovery_only | medium |
| Black Hat Middle East and Africa 2026 | 2026-12-01–2026-12-03 | upcoming_confirmed | A | cybersecurity_security | no | 0 | verified_cross_source | medium |

## Completed 2026 exhibitions retained for historical extraction
| Exhibition | Dates | Classification | Note |
|---|---|---|---|
| World Defense Show 2026 | 2026-02-08–2026-02-12 | historical_2026_completed | Excluded from upcoming totals; useful for historical extraction. |
| WAM Saudi Expo 2026 | 2026-02-15–2026-02-17 | historical_2026_completed | Excluded from upcoming totals; useful for historical extraction. |
| Automechanika Riyadh 2026 | 2026-05-04–2026-05-06 | historical_2026_completed | Excluded from upcoming totals; useful for historical extraction. |
| CPHI Middle East 2026 | 2026-05-11–2026-05-13 | historical_2026_completed | Excluded from upcoming totals; useful for historical extraction. |
| BIO Middle East 2026 | 2026-05-11–2026-05-13 | historical_2026_completed | Excluded from upcoming totals; useful for historical extraction. |
| Saudi Travel Market 2026 | 2026-05-11–2026-05-13 | historical_2026_completed | Excluded from upcoming totals; useful for historical extraction. |
| Beautyworld Saudi Arabia 2026 | 2026-05-18–2026-05-20 | historical_2026_completed | Excluded from upcoming totals; useful for historical extraction. |

## Secondary consumer/commercial opportunities
| Candidate | Classification | Reason |
|---|---|---|
| DUNES Expo 2026 | upcoming_discovery / secondary_consumer_opportunity | Secondary consumer opportunity; not counted in primary B2B total pending Salah decision. |
| Shopping and fashion pop-up markets 2026 | date_unconfirmed / secondary_consumer_opportunity | Retained only as Salah-review secondary opportunity category; not a specific qualifying exhibition record for extraction. |
| Horse and equestrian exhibition candidates 2026 | date_unconfirmed / secondary_consumer_opportunity | Could overlap consumer/sport events; not counted as primary B2B. |
| Back-to-school exhibition candidates 2026 | date_unconfirmed / secondary_consumer_opportunity | Likely retail/consumer if found; not counted as primary B2B. |

## Date-unconfirmed candidates
| Candidate | Status | Research finding |
|---|---|---|
| Foodex Saudi 2026 | date_unconfirmed | Date-unconfirmed Riyadh candidate; not counted as upcoming confirmed pipeline until exact Riyadh dates are verified. |
| HR and recruitment exhibitions in Riyadh 2026 | date_unconfirmed | Explicitly investigated; no qualifying upcoming exhibition source captured in this pass. |
| BAPEX/FAPEX Riyadh 2026 candidate | date_unconfirmed | Name requires user/Salah clarification or deeper Arabic search; not counted as upcoming. |

## Excluded non-exhibition events/categories
| Event/category | Reason |
|---|---|
| Riyadh Season consumer activations | Entertainment/festival activations, not stable B2B trade exhibitions. |
| General conference-only HR or education summits | Excluded unless a meaningful exhibitor floor and dates are evidenced. |
| Webinar/lecture/networking-only listings | No qualifying exhibition floor. |

## Source coverage and corrections
- General events-directory homepages were removed from source-map rows where specific event URLs or explicit `not_found` investigation rows were more appropriate.
- Global Health's public exhibitor-list page is classified as a 2025 historical source unless a page itself demonstrably lists 2026 exhibitors.
- Official URLs are no longer labelled as third-party directory sources, and third-party rows such as Eye of Riyadh/10Times/ExpoFP/Expolista are not marked primary.
- `exhibitor_list_available=yes` is used only when the source is an actual exhibitor/company list, not merely an exhibit-sales page, sponsor page, venue page, or search result.
- Search-result URLs alone are not counted as historical sources; `not_found` rows use `multi_source_review` notes describing the source types/queries checked.

## Historical research approach
For upcoming qualifying B2B exhibitions, historical source checks used event-appropriate English and Arabic patterns: event name + exhibitors/list/catalogue/floor plan/sponsors + year, Arabic `العارضين` and `قائمة الشركات`, official-domain year queries, Eye of Riyadh event-specific pages, 10Times/Expolista/Eventseye-style directory pages, LinkedIn/public social announcements, and public event/news pages. `not_found` records are retained only where multiple source types were checked and no stable public exhibitor/company list was captured.

## Conflicts and low-confidence records
- Saudi Warehousing & Logistics Expo has a date conflict between venue/calendar-style sources and snippets of official pages; retained with medium confidence.
- ORGATEC WORKSPACE Saudi Arabia has a 2026 social/third-party trail but the official site now emphasizes 2027; marked `conflict_needs_review`.
- Saudi Food Expo is retained as discovery-only because similarly named food events show conflicting cities/dates.
- Foodex Saudi Riyadh 2026 remains date-unconfirmed because the official site mentions Riyadh/Jeddah November 2026 without exact Riyadh dates/venue.
- HR/recruitment, BAPEX/FAPEX, horse/equestrian, and back-to-school categories were explicitly investigated but no qualifying primary B2B upcoming exhibition was verified in this correction pass.

## A+ and A recommended extraction order
1. LEAP 2026
2. Cityscape Global 2026
3. Global Health Exhibition 2026
4. Saudi Agriculture 2026
5. Saudi Event Show 2026
6. Saudi Warehousing & Logistics Expo 2026
7. Hotel & Hospitality Expo Saudi Arabia 2026
8. Money20/20 Middle East 2026
9. Saudi Build 2026 / Saudi Elenex 2026
10. Big 5 Construct Saudi 2026 / INDEX Saudi Arabia 2026
11. Black Hat MEA 2026
12. Industrial Transformation Saudi Arabia 2026

## Limitations and remaining gaps
- This correction still does not claim comprehensive calendar validation is complete; the P0 calendar item is reopened as partial/in progress.
- Some 2026 exhibitor directories may be unpublished, JavaScript/app-gated, registration-gated, or renamed.
- No individual exhibitor extraction or contact enrichment was performed in this PR.
- No private personal data, guessed contacts, outreach, CRM import, external publishing, or merge was performed.

## Recommended next task
Run focused exhibitor extraction for the four upcoming B2B sources with current 2026 exhibitor/company lists first, then continue historical source deepening for Cityscape, Global Health, construction/interiors, logistics, and food/hospitality targets.
