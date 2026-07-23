#!/usr/bin/env python3
"""Validate current exhibitor extraction outputs with LEAP intentionally skipped."""
import csv
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
EXHIBITORS = ROOT / "database" / "exhibitors.csv"
EVIDENCE = ROOT / "database" / "evidence.csv"
REPORTS = [
    ROOT / "reports" / "2026-07-18-saudi-agriculture-2026-exhibitor-batch.md",
    ROOT / "reports" / "2026-07-23-non-leap-current-exhibition-batch.md",
]
RAW_SNAPSHOTS = {
    "riyadh-2026-saudi-agriculture": ROOT / "database" / "raw" / "saudi-agriculture-2026-exhibitors-2026-07-18.csv",
    "riyadh-2026-big5-construct-saudi": ROOT / "database" / "raw" / "big5-construct-saudi-2026-exhibitors-2026-07-21.csv",
    "riyadh-2026-saudi-build": ROOT / "database" / "raw" / "saudi-build-2026-exhibitors-2026-07-21.csv",
    "riyadh-2026-saudi-elenex": ROOT / "database" / "raw" / "saudi-elenex-2026-exhibitors-2026-07-21.csv",
    "riyadh-2026-saudi-event-show": ROOT / "database" / "raw" / "saudi-event-show-2026-current-sponsors-partners-2026-07-21.csv",
    "riyadh-2026-hotel-hospitality-expo": ROOT / "database" / "raw" / "hotel-hospitality-expo-saudi-2026-current-public-candidates-2026-07-21.csv",
    "riyadh-2026-bio-middle-east": ROOT / "database" / "raw" / "bio-middle-east-2026-exhibitors-2026-07-21.csv",
}
SKIPPED_EXHIBITION_IDS = {"riyadh-2026-leap"}
URL_FIELDS = [
    "best_known_website", "linkedin_company", "instagram", "facebook", "x_profile",
    "youtube", "other_public_profile", "google_business", "public_contact_profile",
    "participation_source_url", "contact_source_url",
]


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def valid_url(value):
    if not value:
        return True
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def normalized_name(value):
    return re.sub(r"\W+", " ", value.lower()).strip()


def main():
    exhibitors = read_csv(EXHIBITORS)
    evidence = read_csv(EVIDENCE)
    raw_by_exhibition = {exhibition_id: read_csv(path) for exhibition_id, path in RAW_SNAPSHOTS.items()}
    raw_total = sum(len(rows) for rows in raw_by_exhibition.values())
    print(f"CSV parsing PASS exhibitors={len(exhibitors)} raw_total={raw_total} evidence={len(evidence)}")

    report_text = "\n".join(path.read_text(encoding="utf-8") for path in REPORTS if path.exists())
    require("Raw exhibitor names extracted: 222" in report_text, "Saudi Agriculture report raw count mismatch")
    require("Unique companies after dedupe: 222" in report_text, "Saudi Agriculture report unique count mismatch")
    require(f"Non-LEAP current batch records added: {raw_total - 222}" in report_text, "Non-LEAP batch count mismatch")
    require(f"Total current company records after this run: {len(exhibitors)}" in report_text, "Current company total report mismatch")
    print("Report count matching PASS")

    ids = [row["record_id"] for row in exhibitors]
    duplicate_ids = [value for value, count in Counter(ids).items() if count > 1]
    require(not duplicate_ids, f"Duplicate exhibitor IDs: {duplicate_ids[:10]}")
    print("Duplicate exhibitor IDs PASS")

    valid_exhibition_ids = set(RAW_SNAPSHOTS)
    bad_exhibitions = [row["record_id"] for row in exhibitors if row["exhibition_id"] not in valid_exhibition_ids]
    require(not bad_exhibitions, f"Invalid exhibition_id in exhibitors.csv: {bad_exhibitions[:10]}")
    skipped_rows = [row["record_id"] for row in exhibitors if row["exhibition_id"] in SKIPPED_EXHIBITION_IDS]
    require(not skipped_rows, f"Skipped LEAP rows present in exhibitors.csv: {skipped_rows[:10]}")
    print("Exhibition ID validation PASS")
    print("LEAP skip validation PASS")

    evidence_ids = {row["entity_id"] for row in evidence if row["entity_type"] == "exhibitor"}
    orphan_exhibitors = [row["record_id"] for row in exhibitors if row["record_id"] not in evidence_ids]
    require(not orphan_exhibitors, f"Exhibitor records without evidence: {orphan_exhibitors[:10]}")
    print("No orphan exhibitor evidence PASS")

    for row in exhibitors:
        for field in URL_FIELDS:
            require(valid_url(row.get(field, "")), f"Invalid URL in {field}: {row['record_id']} {row.get(field)}")
    print("URL format validation PASS")

    contact_fields = [
        "general_email", "sales_email", "marketing_email", "other_public_email",
        "public_phone", "public_whatsapp", "public_contact_name", "public_contact_profile",
    ]
    contact_source_errors = [
        row["record_id"]
        for row in exhibitors
        if any(row.get(field, "").strip() for field in contact_fields)
        and not row.get("contact_source_url", "").strip()
    ]
    require(not contact_source_errors, f"Contact data without contact_source_url: {contact_source_errors[:10]}")
    print("Contact source validation PASS")

    # Cross-exhibition repeats are valid only when each participation is source-backed.
    domain_keys = [
        (row["exhibition_id"], row["official_domain"])
        for row in exhibitors if row["official_domain"]
    ]
    duplicate_domains = [value for value, count in Counter(domain_keys).items() if count > 1]
    require(not duplicate_domains, f"Duplicate domains require manual review: {duplicate_domains[:10]}")

    name_country_keys = [
        (row["exhibition_id"], normalized_name(row["company_name_raw"]), row["country"].lower())
        for row in exhibitors if not row["official_domain"]
    ]
    duplicate_name_country = []
    for value, count in Counter(name_country_keys).items():
        if count <= 1:
            continue
        matching = [
            row for row in exhibitors
            if (
                row["exhibition_id"],
                normalized_name(row["company_name_raw"]),
                row["country"].lower(),
            ) == value
        ]
        reviewed = all("duplicate_same_name_reviewed" in row.get("notes", "") for row in matching)
        distinct_booths = len({row.get("booth_or_sponsor_notes", "") for row in matching}) == len(matching)
        profile_urls = set()
        for row in matching:
            profile_match = re.search(r"Official .*? profile URL: (\S+)", row.get("notes", ""))
            if profile_match:
                profile_urls.add(profile_match.group(1))
        distinct_profiles = len(profile_urls) == len(matching)
        if not (reviewed and (distinct_booths or distinct_profiles)):
            duplicate_name_country.append(value)
    require(not duplicate_name_country, f"Name/country duplicate requires review: {duplicate_name_country[:10]}")
    print("No name-only merge validation PASS")

    exhibitor_counts = Counter(row["exhibition_id"] for row in exhibitors)
    raw_counts = {exhibition_id: len(rows) for exhibition_id, rows in raw_by_exhibition.items()}
    count_mismatches = [
        (exhibition_id, raw_counts[exhibition_id], exhibitor_counts[exhibition_id])
        for exhibition_id in raw_counts
        if raw_counts[exhibition_id] != exhibitor_counts[exhibition_id]
    ]
    require(not count_mismatches, f"Raw-to-exhibitor count mismatch: {count_mismatches}")
    print("Raw-to-unique count validation PASS")


if __name__ == "__main__":
    main()
