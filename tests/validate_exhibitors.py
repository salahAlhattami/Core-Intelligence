#!/usr/bin/env python3
"""Validate Saudi Agriculture 2026 exhibitor extraction outputs."""
import csv
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
EXHIBITORS = ROOT / "database" / "exhibitors.csv"
EVIDENCE = ROOT / "database" / "evidence.csv"
RAW = ROOT / "database" / "raw" / "saudi-agriculture-2026-exhibitors-2026-07-18.csv"
REPORT = ROOT / "reports" / "2026-07-18-saudi-agriculture-2026-exhibitor-batch.md"
VALID_EXHIBITION_ID = "riyadh-2026-saudi-agriculture"
URL_FIELDS = [
    "best_known_website", "linkedin_company", "instagram", "facebook", "x_profile",
    "youtube", "other_public_profile", "google_business", "public_contact_profile",
    "participation_source_url", "contact_source_url",
]


def read_csv(path):
    with path.open(newline="") as handle:
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
    raw = read_csv(RAW)
    print(f"CSV parsing PASS exhibitors={len(exhibitors)} raw={len(raw)} evidence={len(evidence)}")

    report_text = REPORT.read_text()
    require(f"Raw exhibitor names extracted: {len(raw)}" in report_text, "Report raw count mismatch")
    require(f"Unique companies after dedupe: {len(exhibitors)}" in report_text, "Report unique count mismatch")
    print("Report count matching PASS")

    ids = [row["record_id"] for row in exhibitors]
    duplicate_ids = [value for value, count in Counter(ids).items() if count > 1]
    require(not duplicate_ids, f"Duplicate exhibitor IDs: {duplicate_ids[:10]}")
    print("Duplicate exhibitor IDs PASS")

    require(all(row["exhibition_id"] == VALID_EXHIBITION_ID for row in exhibitors), "Invalid exhibition_id in exhibitors.csv")
    print("Exhibition ID validation PASS")

    evidence_ids = {row["entity_id"] for row in evidence if row["entity_type"] == "exhibitor"}
    orphan_exhibitors = [row["record_id"] for row in exhibitors if row["record_id"] not in evidence_ids]
    require(not orphan_exhibitors, f"Exhibitor records without evidence: {orphan_exhibitors[:10]}")
    print("No orphan exhibitor evidence PASS")

    for row in exhibitors:
        for field in URL_FIELDS:
            require(valid_url(row.get(field, "")), f"Invalid URL in {field}: {row['record_id']} {row.get(field)}")
    print("URL format validation PASS")

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

    require(len(raw) == len(exhibitors), "Unexpected dedupe delta; review raw vs unique counts")
    print("Raw-to-unique count validation PASS")


if __name__ == "__main__":
    main()
