#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "datasets" / "cases.jsonl"

REQUIRED = {
    "id",
    "date",
    "project",
    "model_family",
    "task_types",
    "prompt_pattern",
    "artifact",
    "verification",
    "human_signal",
    "outcome",
    "lesson",
    "evidence_level",
}
EVIDENCE_LEVELS = {"A", "B", "C"}


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def main() -> None:
    if not CASES.exists():
        fail(f"missing {CASES.relative_to(ROOT)}")

    seen = set()
    count = 0

    for line_number, raw in enumerate(CASES.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue

        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            fail(f"line {line_number}: invalid JSON: {exc}")

        if not isinstance(row, dict):
            fail(f"line {line_number}: case must be a JSON object")

        missing = sorted(REQUIRED - row.keys())
        if missing:
            fail(f"line {line_number}: missing required fields: {', '.join(missing)}")

        case_id = row["id"]
        if not isinstance(case_id, str) or not case_id.strip():
            fail(f"line {line_number}: id must be a non-empty string")
        if case_id in seen:
            fail(f"line {line_number}: duplicate id {case_id!r}")
        seen.add(case_id)

        try:
            date.fromisoformat(row["date"])
        except (TypeError, ValueError):
            fail(f"line {line_number}: date must be YYYY-MM-DD")

        if row["evidence_level"] not in EVIDENCE_LEVELS:
            fail(f"line {line_number}: evidence_level must be A, B, or C")

        for field in ("task_types", "verification"):
            value = row[field]
            if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
                fail(f"line {line_number}: {field} must be a list of strings")

        for field in ("project", "model_family", "prompt_pattern", "human_signal", "outcome", "lesson"):
            value = row[field]
            if not isinstance(value, str) or not value.strip():
                fail(f"line {line_number}: {field} must be a non-empty string")

        count += 1

    if count == 0:
        fail("cases.jsonl contains no cases")

    print(f"Validated {count} cases with {len(seen)} unique IDs.")


if __name__ == "__main__":
    main()
