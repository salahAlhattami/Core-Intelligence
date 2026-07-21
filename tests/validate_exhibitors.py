#!/usr/bin/env python3
"""Validate current exhibitor extraction outputs."""
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
    ROOT / "reports" / "2026-07-21-parallel-current-extraction-batch-1.md",
]
RAW_SNAPSHOTS = {
    "riyadh-2026-saudi-agriculture": ROOT / "database" / "raw" / "saudi-agriculture-2026-exhibitors-2026-07-18.csv",
    "riyadh-2026-leap": ROOT / "database" / "raw" / "leap-2026-exhibitors-2026-07-21.csv",
    "riyadh-2026-big5-construct-saudi": ROOT / "database" / "raw" / "big5-construct-saudi-2026-exhibitors-2026-07-21.csv",
    "riyadh-2026-saudi-build": ROOT / "database" / "raw" / "saudi-build-2026-exhibitors-2026-07-21.csv",
    "riyadh-2026-saudi-elenex": ROOT / "database" / "raw" / "saudi-elenex-2026-exhibitors-2026-07-21.csv",
}
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


def main():
    exhibitors = read_csv(EXHIBITORS)
    evidence = read_csv(EVIDENCE)
    raw_by_exhibition = {exhibition_id: read_csv(path) for exhibition_id, path in RAW_SNAPSHOTS.items()}
    raw_total = sum(len(rows) for rows in raw_by_exhibition.values())
    print(f"CSV parsing PASS exhibitors={len(exhibitors)} raw_total={raw_total} evidence={len(evidence)}")

    report_text = "\n".join(path.read_text(encoding="utf-8") for path in REPORTS if path.exists())
    require("Raw exhibitor names extracted: 222" in report_text, "Saudi Agriculture report raw count mismatch")
    require("Unique companies after dedupe: 222" in report_text, "Saudi Agriculture report unique count mismatch")
    require(f"Parallel current batch exhibitors added: {raw_total - 222}" in report_text, "Parallel batch report count mismatch")
    print("Report count matching PASS")

    ids = [row["record_id"] for row in exhibitors]
    duplicate_ids = [value for value, count in Counter(ids).items() if count > 1]
    require(not duplicate_ids, f"Duplicate exhibitor IDs: {duplicate_ids[:10]}")
    print("Duplicate exhibitor IDs PASS")

    valid_exhibition_ids = set(RAW_SNAPSHOTS)
    bad_exhibitions = [row["record_id"] for row in exhibitors if row["exhibition_id"] not in valid_exhibition_ids]
    require(not bad_exhibitions, f"Invalid exhibition_id in exhibitors.csv: {bad_exhibitions[:10]}")
    print("Exhibition ID validation PASS")

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
    contact_date_errors = [
        row["record_id"]
        for row in exhibitors
        if any(row.get(field, "").strip() for field in contact_fields)
        and not row.get("last_verified_at", "").strip()
    ]
    require(not contact_date_errors, f"Contact data without last_verified_at: {contact_date_errors[:10]}")
    print("Contact source/date validation PASS")

    # Dedupe policy: no merge may rely on normalized name only. Either domain-backed or raw-name/country exact key.
    domain_keys = [row["official_domain"] for row in exhibitors if row["official_domain"]]
    duplicate_domains = [value for value, count in Counter(domain_keys).items() if count > 1]
    require(not duplicate_domains, f"Duplicate domains require manual review: {duplicate_domains[:10]}")
    name_country_keys = [
        (re.sub(r"\W+", " ", row["company_name_raw"].lower()).strip(), row["country"].lower())
        for row in exhibitors if not row["official_domain"]
    ]
    duplicate_name_country = [value for value, count in Counter(name_country_keys).items() if count > 1]
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
