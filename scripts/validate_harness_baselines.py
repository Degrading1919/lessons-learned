
#!/usr/bin/env python3
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "datasets" / "harness_baselines.jsonl"
REQUIRED = {
    "id", "as_of", "harness", "provider", "billing_mode",
    "best_roles", "overhead_risks", "cache_behavior",
    "efficiency_prior", "evidence_strength", "community_signal", "caveat"
}
STRENGTH = {"low", "medium", "medium-high", "high"}

def fail(message):
    raise SystemExit("ERROR: " + message)

def main():
    if not DATA.exists():
        fail("missing datasets/harness_baselines.jsonl")
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
        if row["evidence_strength"] not in STRENGTH:
            fail(f"line {line_number}: invalid evidence_strength")
        for field in ("best_roles", "overhead_risks"):
            value = row[field]
            if not isinstance(value, list) or not value or not all(isinstance(x, str) and x for x in value):
                fail(f"line {line_number}: {field} must be a non-empty list of strings")
        count += 1
    if not count:
        fail("harness_baselines.jsonl contains no records")
    print(f"Validated {count} harness baselines with unique IDs.")

if __name__ == "__main__":
    main()
