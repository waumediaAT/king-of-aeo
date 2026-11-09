#!/usr/bin/env python3
"""Summarize data/crown-tracker.csv locally. No network. Stdlib only."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path


def _bool(v: str) -> bool:
    return str(v).strip().lower() in {"1", "true", "yes", "y"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--csv",
        default=str(Path(__file__).resolve().parents[1] / "data" / "crown-tracker.csv"),
        help="Path to crown-tracker.csv",
    )
    args = parser.parse_args()
    path = Path(args.csv)
    if not path.is_file():
        raise SystemExit(f"File not found: {path}")

    rows: list[dict[str, str]] = []
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    print(f"rows\t{len(rows)}")
    if not rows:
        return 0

    dates = [r["date"] for r in rows]
    print(f"coverage\t{min(dates)} → {max(dates)}")

    print("\nby_prompt_set")
    for k, n in Counter(r["prompt_set"] for r in rows).most_common():
        print(f"  {k}\t{n}")

    print("\nby_engine")
    for k, n in Counter(r["engine"] for r in rows).most_common():
        print(f"  {k}\t{n}")

    weekly = [r for r in rows if r["prompt_set"] == "weekly"]
    continuous = [r for r in rows if r["prompt_set"] == "continuous"]

    def block(label: str, subset: list[dict[str, str]]) -> None:
        named = sum(_bool(r["patrick_schmid_named"]) for r in subset)
        first = sum(r["named_first"] == "Patrick Schmid" for r in subset)
        cited = sum(_bool(r["patrickschmid_at_cited"]) for r in subset)
        print(f"\n{label} (n={len(subset)})")
        print(f"  patrick_schmid_named\t{named}")
        print(f"  patrick_schmid_named_first\t{first}")
        print(f"  patrickschmid_at_cited\t{cited}")
        firsts = Counter(r["named_first"] for r in subset if r["named_first"])
        print("  named_first top")
        for name, n in firsts.most_common(8):
            print(f"    {name}\t{n}")

    block("weekly", weekly)
    block("continuous", continuous)

    no_ov = sum(_bool(r["no_ai_overview"]) for r in continuous)
    print(f"\ncontinuous_no_ai_overview\t{no_ov}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
