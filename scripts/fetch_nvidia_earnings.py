"""Fetch NVIDIA datacenter revenue and compute YoY growth.

Supports resolution of AV-001 (NVIDIA Q4 FY26 datacenter revenue YoY <50%).

Data source: NVIDIA Investor Relations press release index. This script
does NOT try to parse HTML earnings releases; it prints the URLs and a
manual-entry template. The reason: NVIDIA's press-release layout changes
each quarter and a scraper breaks quietly. A human-in-the-loop step here
is deliberate—prediction resolution demands auditable evidence.

Usage:
    python scripts/fetch_nvidia_earnings.py
    python scripts/fetch_nvidia_earnings.py --record \\
        --quarter Q4FY26 --datacenter 58800 --prior-year-datacenter 39200
"""
from __future__ import annotations

import argparse
import sys

from common import write_snapshot

IR_INDEX = "https://investor.nvidia.com/financial-info/financial-reports/default.aspx"
PRESS_URL_PATTERN = "https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-{quarter}-fiscal-{year}"


def print_manual_instructions(quarter_label: str) -> None:
    print("NVIDIA datacenter revenue fetcher (manual entry)")
    print("=" * 60)
    print(f"  Target quarter:  {quarter_label}")
    print(f"  IR index:        {IR_INDEX}")
    print(f"  Expected URL:    {PRESS_URL_PATTERN.format(quarter='fourth-quarter', year='2026')}")
    print()
    print("Retrieve the earnings release, find the Data Center segment")
    print("revenue in the 'Revenue by Market' table, and rerun with:")
    print()
    print("    --record --quarter Q4FY26 \\")
    print("      --datacenter <DC revenue in $M> \\")
    print("      --prior-year-datacenter <year-ago DC revenue in $M>")


def record(quarter: str, datacenter_m: float, prior_m: float) -> dict:
    yoy = (datacenter_m - prior_m) / prior_m
    data = {
        "quarter": quarter,
        "datacenter_revenue_musd": datacenter_m,
        "prior_year_datacenter_musd": prior_m,
        "yoy_growth": round(yoy, 4),
        "threshold_av001_correct": yoy < 0.50,
    }
    path = write_snapshot("nvidia-earnings", data)
    print(f"Snapshot written: {path}")
    print(f"  Datacenter {quarter}: ${datacenter_m:,.0f}M")
    print(f"  YoY growth:           {yoy * 100:.1f}%")
    print(f"  AV-001 (growth<50%):  {'CORRECT' if yoy < 0.50 else 'INCORRECT'}")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true")
    parser.add_argument("--quarter", default="Q4FY26")
    parser.add_argument("--datacenter", type=float, help="Datacenter revenue, USD millions")
    parser.add_argument("--prior-year-datacenter", type=float, help="Prior-year Q4 datacenter revenue, USD millions")
    args = parser.parse_args()

    if not args.record:
        print_manual_instructions(args.quarter)
        return 0

    if args.datacenter is None or args.prior_year_datacenter is None:
        parser.error("--record requires both --datacenter and --prior-year-datacenter")

    record(args.quarter, args.datacenter, args.prior_year_datacenter)
    return 0


if __name__ == "__main__":
    sys.exit(main())
