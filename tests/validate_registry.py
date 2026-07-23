#!/usr/bin/env python3
"""Validate Riyadh exhibition registry CSV outputs."""
import csv
import datetime as dt
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "exhibitions": ROOT / "database" / "exhibitions.csv",
    "sources": ROOT / "database" / "exhibition-sources.csv",
    "evidence": ROOT / "database" / "evidence.csv",
}
REQUIRED = {
    "exhibitions": [
        "exhibition_id", "canonical_name", "organizer", "venue", "city", "country",
        "current_edition_year", "start_date", "end_date", "event_type",
        "has_exhibition_floor", "official_url", "current_directory_url", "priority",
        "verification_status", "last_verified_at", "notes", "lifecycle_status", "pipeline_tier",
    ],
    "sources": [
        "source_id", "exhibition_id", "edition_year", "source_type", "source_relationship",
        "source_name", "source_url", "current_or_historical", "exhibitor_list_available",
        "source_format", "verification_status", "confidence", "accessed_at", "notes",
    ],
    "evidence": [
        "evidence_id", "entity_type", "entity_id", "field_name", "claimed_value",
        "source_type", "source_relationship", "source_name", "source_url",
        "account_or_page_status", "edition_year", "published_at", "accessed_at",
        "is_primary", "verification_status", "confidence", "notes",
    ],
}
VALID_STATUS = {"verified_primary", "verified_cross_source", "discovery_only", "conflict_needs_review", "not_found"}
VALID_REL = {"official", "organizer_or_event", "government_or_chamber", "third_party_directory", "unofficial_social_or_public_page", "search_discovery", "unknown"}
VALID_CONF = {"high", "medium", "low"}
VALID_LIFECYCLE = {"upcoming_confirmed", "upcoming_discovery", "completed_historical", "postponed", "cancelled", "date_unconfirmed"}
VALID_TIERS = {"primary_b2b", "historical_2026_completed", "secondary_consumer_opportunity", "date_unconfirmed_candidate", "excluded_non_exhibition"}
CUTOVER = dt.date(2026, 7, 18)


def read_csv(name):
    with FILES[name].open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise AssertionError(f"{FILES[name]} has no data rows")
    print(f"CSV parsing PASS {FILES[name].relative_to(ROOT)}: {len(rows)} rows, {len(rows[0])} columns")
    return rows


def assert_no_duplicates(values, label):
    duplicates = [value for value, count in Counter(values).items() if count > 1]
    if duplicates:
        raise AssertionError(f"Duplicate {label}: {duplicates[:10]}")


def main():
    data = {name: read_csv(name) for name in FILES}
    for name, columns in REQUIRED.items():
        missing = [column for column in columns if column not in data[name][0]]
        if missing:
            raise AssertionError(f"{name} missing required columns: {missing}")
        print(f"Required columns PASS {name}")

    for name, path in FILES.items():
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.reader(handle)
            header = next(reader)
            bad_rows = [(idx, len(row)) for idx, row in enumerate(reader, 2) if len(row) != len(header)]
        if bad_rows:
            raise AssertionError(f"Inconsistent row lengths in {path}: {bad_rows[:10]}")
        print(f"Consistent row lengths PASS {name}")

    assert_no_duplicates([row["exhibition_id"] for row in data["exhibitions"]], "exhibition_id")
    assert_no_duplicates([row["source_id"] for row in data["sources"]], "source_id")
    assert_no_duplicates([row["evidence_id"] for row in data["evidence"]], "evidence_id")
    print("Duplicate IDs PASS")

    composite = [
        (row["exhibition_id"], row["edition_year"], row["source_url"], row["current_or_historical"])
        for row in data["sources"]
    ]
    assert_no_duplicates(composite, "source composite exhibition_id + edition_year + source_url + current_or_historical")
    print("Source composite duplicate validation PASS")

    names = [re.sub(r"\b2026\b", "", row["canonical_name"].lower()).strip() for row in data["exhibitions"]]
    assert_no_duplicates(names, "duplicate/rebranded exhibition names")
    print("Duplicate/rebranded exhibition review PASS")

    exhibitions_by_id = {row["exhibition_id"]: row for row in data["exhibitions"]}
    for row in data["exhibitions"]:
        if row["lifecycle_status"] not in VALID_LIFECYCLE:
            raise AssertionError(f"Invalid lifecycle status: {row}")
        if row["pipeline_tier"] not in VALID_TIERS:
            raise AssertionError(f"Invalid pipeline tier: {row}")
        if row["start_date"]:
            start = dt.date.fromisoformat(row["start_date"])
            dt.date.fromisoformat(row["end_date"])
            if start < CUTOVER and row["lifecycle_status"] != "completed_historical":
                raise AssertionError(f"Pre-cutover event not completed_historical: {row['exhibition_id']}")
            if row["pipeline_tier"] == "primary_b2b" and row["lifecycle_status"].startswith("upcoming") and start < CUTOVER:
                raise AssertionError(f"Upcoming primary event before cutover: {row['exhibition_id']}")
        elif row["lifecycle_status"] != "date_unconfirmed":
            raise AssertionError(f"Undated row must be date_unconfirmed: {row['exhibition_id']}")
    print("Date-scope validation PASS")
    print("Lifecycle/status validation PASS")

    for row in data["sources"]:
        if row["exhibition_id"] not in exhibitions_by_id:
            raise AssertionError(f"Unknown source exhibition_id: {row['source_id']}")
        if row["current_or_historical"] not in {"current", "historical"}:
            raise AssertionError(f"Bad current/historical value: {row['source_id']}")
        if row["exhibitor_list_available"] not in {"yes", "no", "not_found", "unknown"}:
            raise AssertionError(f"Bad exhibitor_list_available: {row['source_id']}")
        if row["verification_status"] not in VALID_STATUS or row["source_relationship"] not in VALID_REL or row["confidence"] not in VALID_CONF:
            raise AssertionError(f"Bad source metadata: {row['source_id']}")
        if row["source_url"] != "not_found" and not row["source_url"].startswith("http"):
            raise AssertionError(f"Bad source URL: {row['source_id']}")
        if row["source_relationship"] == "official" and row["source_type"] in {"eye_of_riyadh", "public_business_directory", "google_search", "venue_calendar"}:
            raise AssertionError(f"Official relationship with third-party type: {row['source_id']}")
        if row["source_type"] == "eye_of_riyadh" and "eyeofriyadh.com/events/details/" not in row["source_url"]:
            raise AssertionError(f"Eye of Riyadh row lacks event-specific URL: {row['source_id']}")
        if any(domain in row["source_url"] for domain in ["10times.com", "eyeofriyadh.com", "expofp.com", "expolista.com"]):
            if row["source_relationship"] != "third_party_directory":
                raise AssertionError(f"Third-party URL not labelled third_party_directory: {row['source_id']}")
        if exhibitions_by_id[row["exhibition_id"]]["pipeline_tier"] == "historical_2026_completed" and row["current_or_historical"] != "historical":
            raise AssertionError(f"Completed-historical source marked current: {row['source_id']}")
        if row["exhibitor_list_available"] == "yes":
            is_directory_type = "exhibitor_directory" in row["source_type"] or row["source_type"] == "public_business_directory"
            if not is_directory_type and "exhibitor" not in row["source_name"].lower():
                raise AssertionError(f"List availability yes without list evidence: {row['source_id']}")
    print("Source URL/source-name consistency PASS")
    print("Primary/third-party classification consistency PASS")
    print("Current vs historical classification PASS")
    print("Exhibitor-list availability validation PASS")

    for row in data["evidence"]:
        if row["verification_status"] not in VALID_STATUS or row["confidence"] not in VALID_CONF:
            raise AssertionError(f"Bad evidence metadata: {row['evidence_id']}")
        if row["is_primary"] == "true" and not (row["source_relationship"] == "official" and row["verification_status"] == "verified_primary"):
            raise AssertionError(f"Primary evidence not verified official: {row['evidence_id']}")
        if row["source_url"] != "not_found" and not row["source_url"].startswith("http"):
            raise AssertionError(f"Bad evidence URL: {row['evidence_id']}")
    print("Verification-status and confidence consistency PASS")

    covered = {row["exhibition_id"] for row in data["sources"]}
    missing = set(exhibitions_by_id) - covered
    if missing:
        raise AssertionError(f"Exhibitions with no source row: {sorted(missing)}")
    print("Missing-source validation PASS")


if __name__ == "__main__":
    main()
