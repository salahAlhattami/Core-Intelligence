# Data Quality Specification

Validation must fail when:
1. `confirmed_current` lacks an official current-edition source.
2. A historical record is marked current-confirmed without current evidence.
3. An email/phone/WhatsApp has no public source URL.
4. A source-backed field lacks a verification date.
5. A duplicate official domain is assigned to conflicting company identities without review.
6. A generated or guessed email is present.
7. participation year/edition evidence is missing.
8. verification status is inconsistent with source type.

Validation should warn when:
- only one historical edition has been researched;
- fewer than two completed editions are covered;
- a third public historical edition exists but has not been processed;
- a candidate has conflicting country or legal-name evidence;
- contact enrichment remains blank rather than explicitly marked not found/pending.
