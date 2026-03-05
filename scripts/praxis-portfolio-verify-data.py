#!/usr/bin/env python3
"""Verify committed portfolio data files are present and valid JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REQUIRED_FILES = {
    "landing.json",
    "projects.json",
    "essays.json",
    "graph.json",
    "about.json",
    "rss-meta.json",
    "system-metrics.json",
}


def verify_data_dir(data_dir: Path) -> int:
    missing = sorted(name for name in REQUIRED_FILES if not (data_dir / name).exists())
    if missing:
        print("ERROR: Missing required portfolio data files:")
        for name in missing:
            print(f"  - {data_dir / name}")
        print("Run `npm run generate-data` from `portfolio-site/` and commit the refreshed data.")
        return 1

    failed: list[Path] = []
    for name in sorted(REQUIRED_FILES):
        path = data_dir / name
        try:
            with open(path, encoding="utf-8") as f:
                json.load(f)
        except (OSError, json.JSONDecodeError):
            failed.append(path)

    if failed:
        print("ERROR: Invalid JSON in portfolio data files:")
        for path in failed:
            print(f"  - {path}")
        return 1

    print(f"OK: verified {len(REQUIRED_FILES)} portfolio data files in {data_dir}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify portfolio-site data snapshot.")
    parser.add_argument(
        "--data-dir",
        type=Path,
        default=Path("portfolio-site/src/data"),
        help="Directory containing generated JSON data files.",
    )
    args = parser.parse_args()
    return verify_data_dir(args.data_dir)


if __name__ == "__main__":
    sys.exit(main())
