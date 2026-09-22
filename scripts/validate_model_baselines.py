#!/usr/bin/env python3
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "datasets" / "model_baselines.jsonl"

REQUIRED = {
    "id", "provider", "model", "as_of", "availability",
    "baseline_roles", "strengths", "weaknesses",
    "community_signal", "confidence"
}
CONFIDENCE = {"low", "medium", "high"}


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def main() -> None:
    if not DATA.exists():
        fail(f"missing {DATA.relative_to(ROOT)}")

    seen = set()
    count = 0
    for line_number, raw in enumerate(DATA.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            row = json.loads(raw)
        except json.JSONDecodeError as exc:
            fail(f"line {line_number}: invalid JSON: {exc}")

        missing = sorted(REQUIRED - row.keys())
        if missing:
            fail(f"line {line_number}: missing fields: {', '.join(missing)}")

        if row["id"] in seen:
            fail(f"line {line_number}: duplicate id {row['id']!r}")
        seen.add(row["id"])

        try:
            date.fromisoformat(row["as_of"])
        except (TypeError, ValueError):
            fail(f"line {line_number}: as_of must be YYYY-MM-DD")

        if row["confidence"] not in CONFIDENCE:
            fail(f"line {line_number}: confidence must be low, medium, or high")

        for field in ("baseline_roles", "strengths", "weaknesses"):
            value = row[field]
            if not isinstance(value, list) or not value or not all(isinstance(x, str) and x for x in value):
                fail(f"line {line_number}: {field} must be a non-empty list of strings")

        index = row.get("independent_index")
        if index is not None:
            if not isinstance(index, dict) or not isinstance(index.get("source"), str):
                fail(f"line {line_number}: independent_index must be null or an object with source")
            if not isinstance(index.get("score"), (int, float)):
                fail(f"line {line_number}: independent_index.score must be numeric")

        count += 1

    if not count:
        fail("model_baselines.jsonl contains no records")

    print(f"Validated {count} public model baselines with unique IDs.")


if __name__ == "__main__":
    main()
