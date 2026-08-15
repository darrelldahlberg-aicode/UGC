#!/usr/bin/env python3
"""Validate UGC creator, campaign, performance, scorecard, and reference records."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = {
    "creator": ROOT / "schemas" / "creator.schema.json",
    "campaign": ROOT / "schemas" / "campaign.schema.json",
    "performance": ROOT / "schemas" / "performance.schema.json",
    "scorecard": ROOT / "schemas" / "scorecard.schema.json",
}


def load_schema(record_type: str) -> dict:
    """Load one of the four versioned JSON schemas."""
    if record_type not in SCHEMAS:
        raise ValueError(f"Unknown record type: {record_type}")
    path = SCHEMAS[record_type]
    return json.loads(path.read_text(encoding="utf-8"))


def _schema_errors(record_type: str, payload: dict[str, Any]) -> list[str]:
    schema = load_schema(record_type)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors: list[str] = []
    for error in sorted(validator.iter_errors(payload), key=lambda item: list(item.absolute_path)):
        location = ".".join(str(part) for part in error.absolute_path)
        if location:
            errors.append(f"schema {location}: {error.message}")
        else:
            errors.append(f"schema: {error.message}")
    return errors


def _parse_iso_date(value: str | None, field_name: str, errors: list[str]) -> date | None:
    if value is None:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        errors.append(f"{field_name} must be a valid ISO YYYY-MM-DD date")
        return None


def _validate_campaign(payload: dict[str, Any], *, as_of: str | None) -> list[str]:
    errors: list[str] = []
    rights = payload.get("rights") or {}
    approvals = payload.get("approvals") or {}

    start = _parse_iso_date(rights.get("start_date"), "rights.start_date", errors)
    end = _parse_iso_date(rights.get("end_date"), "rights.end_date", errors)

    approved_permissions = [
        name
        for name in ("organic_posting", "brand_usage", "paid_media", "whitelisting")
        if rights.get(name) == "approved"
    ]
    if approved_permissions and (start is None or end is None):
        errors.append("approved rights require both rights.start_date and rights.end_date")

    if start is not None and end is not None and end < start:
        errors.append("rights.end_date must not be before rights.start_date")

    destination = payload.get("deployment_destination")
    is_paid = destination in {"paid_media", "both"}
    is_launch = destination in {"organic", "paid_media", "both"}

    if is_paid and rights.get("paid_media") != "approved":
        errors.append("paid deployment requires rights.paid_media = approved")

    if is_launch and approvals.get("final") != "approved":
        errors.append("deployment requires approvals.final = approved")

    if is_paid and approvals.get("media") not in {"approved", "not_required"}:
        errors.append("paid deployment requires approvals.media to be approved or not_required")

    if is_launch and approvals.get("quality") not in {"approved", "not_required"}:
        errors.append("deployment requires approvals.quality to be approved or not_required")

    if as_of is not None:
        try:
            as_of_date = date.fromisoformat(as_of)
        except ValueError:
            errors.append("as_of must be a valid ISO YYYY-MM-DD date")
        else:
            if is_paid and end is not None and end < as_of_date:
                errors.append("paid-media rights are expired as of validation date")
            elif destination in {"organic", "both"} and end is not None and end < as_of_date:
                errors.append("required usage rights are expired as of validation date")

    return errors


def _validate_performance(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    metrics = payload.get("metrics") or {}
    unknown_metrics = payload.get("unknown_metrics") or []

    for metric_name in unknown_metrics:
        if metric_name not in metrics:
            errors.append(f"unknown metric {metric_name} must exist in metrics with value null")
        elif metrics.get(metric_name) is not None:
            errors.append(
                f"unknown metric {metric_name} must be null; do not replace missing data with zero or another value"
            )

    return errors


def _validate_reference(payload: dict[str, Any]) -> list[str]:
    if payload.get("reference_only") is not True:
        return ["reference metadata requires reference_only=true"]
    return []


def validate_record(record_type: str, payload: dict, *, as_of: str | None = None) -> list[str]:
    """Return a list of validation errors. Empty list means valid."""
    if record_type == "reference":
        return _validate_reference(payload)

    if record_type not in SCHEMAS:
        return [f"unknown record type: {record_type}"]

    errors = _schema_errors(record_type, payload)
    if errors:
        return errors

    if record_type == "campaign":
        errors.extend(_validate_campaign(payload, as_of=as_of))
    elif record_type == "performance":
        errors.extend(_validate_performance(payload))

    return errors


def _load_payload(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"record file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"record file is not valid JSON: {path}: {exc}") from exc

    if not isinstance(payload, dict):
        raise ValueError("record root must be a JSON object")
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate UGC structured records")
    parser.add_argument("record_type", choices=[*SCHEMAS.keys(), "reference"])
    parser.add_argument("record_path", type=Path)
    parser.add_argument("--as-of", dest="as_of", help="ISO YYYY-MM-DD date for rights expiration checks")
    args = parser.parse_args(argv)

    try:
        payload = _load_payload(args.record_path)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1

    errors = validate_record(args.record_type, payload, as_of=args.as_of)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
