"""Fetch hyperscaler quarterly capex figures.

Supports resolution of HC-001 (combined quarterly capex peaks <$150B),
HC-002 (guidance reduction), AV-002 (language moderation), and AV-007
(absolute capex reduction YoY).

Like the NVIDIA fetcher, this script intentionally uses manual entry.
Capex disclosures vary: some companies report "purchases of property
and equipment," others add finance-lease additions, others break out
datacenter vs. other. Auto-scraping these fields is fragile and often
wrong. Instead we capture the numbers a human has pulled from the
10-Q/10-K/press release and normalize them.
"""
from __future__ import annotations

import argparse
import sys

from common import write_snapshot

COMPANIES = {
    "MSFT": "Microsoft",
    "GOOG": "Alphabet",
    "AMZN": "Amazon",
    "META": "Meta",
}

IR_URLS = {
    "MSFT": "https://www.microsoft.com/en-us/investor",
    "GOOG": "https://abc.xyz/investor/",
    "AMZN": "https://ir.aboutamazon.com/",
    "META": "https://investor.atmeta.com/",
}


def print_manual_instructions(company: str) -> None:
    print(f"Hyperscaler capex fetcher — {COMPANIES[company]} ({company})")
    print("=" * 60)
    print(f"  IR site: {IR_URLS[company]}")
    print()
    print("Find the most recent quarterly earnings release. Extract:")
    print("  - Purchases of property and equipment (cash flow statement)")
    print("  - Finance-lease additions (if disclosed separately)")
    print("  - Any full-year capex guidance commentary")
    print()
    print("Rerun with:")
    print(f"    --record --company {company} --quarter <YYYY-QN> \\")
    print("      --capex-musd <capex in $M> \\")
    print("      --guidance-musd <FY guidance midpoint in $M> \\")
    print("      --language-tone [aggressive|neutral|moderating]")


def record(
    company: str,
    quarter: str,
    capex_musd: float,
    guidance_musd: float | None,
    language_tone: str,
) -> dict:
    data = {
        "company": company,
        "company_name": COMPANIES[company],
        "quarter": quarter,
        "capex_musd": capex_musd,
        "fy_guidance_midpoint_musd": guidance_musd,
        "language_tone": language_tone,
    }
    path = write_snapshot(f"hyperscaler-capex-{company.lower()}", data)
    print(f"Snapshot written: {path}")
    print(f"  {company} {quarter} capex: ${capex_musd:,.0f}M  (tone: {language_tone})")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true")
    parser.add_argument("--company", choices=list(COMPANIES), required=True)
    parser.add_argument("--quarter", help="e.g. 2026-Q1")
    parser.add_argument("--capex-musd", type=float)
    parser.add_argument("--guidance-musd", type=float)
    parser.add_argument(
        "--language-tone",
        choices=["aggressive", "neutral", "moderating"],
        default="neutral",
    )
    args = parser.parse_args()

    if not args.record:
        print_manual_instructions(args.company)
        return 0

    if args.quarter is None or args.capex_musd is None:
        parser.error("--record requires --quarter and --capex-musd")

    record(
        args.company,
        args.quarter,
        args.capex_musd,
        args.guidance_musd,
        args.language_tone,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
