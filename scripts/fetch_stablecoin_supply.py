"""Fetch aggregate USDT + USDC supply (circulating) for a date.

Supports DA-003 (combined USDT+USDC supply exceeds $300B in 2026) and
DA-004 (no US-regulated stablecoin >2% peg break for >24 hours in 2026).

Data source: DeFiLlama public stablecoins API.
  https://stablecoins.llama.fi/stablecoin/{id}?includePrices=true

DeFiLlama assigns numeric IDs to each stablecoin:
  - Tether (USDT) = 1
  - USDC = 2
  - PYUSD = 44 (approx; verify before use)
  - DAI = 5

We use `/stablecoins` to list and `/stablecoincharts/all` or per-coin
history for time series. For a point-in-time snapshot, the summary
endpoint at `/stablecoins?includePrices=true` returns current circulating
and a price check in one call.

No API key required. Polite: one request per coin, UA set in common.py.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from datetime import date

from common import requests_headers, write_snapshot

STABLECOINS_SUMMARY_URL = "https://stablecoins.llama.fi/stablecoins?includePrices=true"

# DeFiLlama stablecoin IDs we care about for DA-003 / DA-004.
STABLECOINS = {
    "USDT": 1,
    "USDC": 2,
    "PYUSD": 44,
    "DAI": 5,
    "FDUSD": 100,  # verify; placeholder
}

# For DA-004, focus on "US-regulated" stablecoins. This is a judgment call.
# Treatment: USDC (Circle, Coinbase), PYUSD (Paxos/PayPal), FDUSD (FirstDigitalTrust).
# USDT is excluded — Tether is not US-regulated in the DA-004 sense.
US_REGULATED_SET = {"USDC", "PYUSD", "FDUSD"}


def _http_get(url: str) -> dict:
    req = urllib.request.Request(url, headers=requests_headers())
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code} fetching {url}: {exc.reason}") from exc
    return json.loads(body)


def fetch_current_supply() -> dict:
    """Return circulating supply and current price for tracked stablecoins."""
    data = _http_get(STABLECOINS_SUMMARY_URL)
    by_symbol: dict[str, dict] = {}

    # DeFiLlama returns a list under "peggedAssets" with {id, symbol, circulating, price}.
    assets = data.get("peggedAssets", [])
    for asset in assets:
        sym = asset.get("symbol", "").upper()
        if sym in STABLECOINS:
            circ_field = asset.get("circulating", {})
            # circulating is a dict keyed by peg (e.g., {"peggedUSD": 123456789})
            circ_usd = None
            if isinstance(circ_field, dict):
                circ_usd = circ_field.get("peggedUSD")
            price = asset.get("price")
            by_symbol[sym] = {
                "symbol": sym,
                "circulating_usd": circ_usd,
                "price_usd": price,
                "depeg_2pct": price is not None and abs(price - 1.0) >= 0.02,
            }

    # Compute DA-003 aggregate
    usdt = by_symbol.get("USDT", {}).get("circulating_usd") or 0
    usdc = by_symbol.get("USDC", {}).get("circulating_usd") or 0
    combined = usdt + usdc

    # Compute DA-004 depeg check
    us_regulated_depegged = [
        s for s, info in by_symbol.items()
        if s in US_REGULATED_SET and info.get("depeg_2pct")
    ]

    return {
        "as_of": date.today().isoformat(),
        "by_symbol": by_symbol,
        "analysis": {
            "usdt_circulating": usdt,
            "usdc_circulating": usdc,
            "usdt_usdc_combined": combined,
            "da003_threshold_300b": 300_000_000_000,
            "da003_correct_if_combined_ge_300b": bool(combined >= 300_000_000_000),
            "us_regulated_depegged_now": us_regulated_depegged,
            "da004_intraday_depeg_detected": bool(us_regulated_depegged),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print result without writing a snapshot.",
    )
    args = parser.parse_args()

    result = fetch_current_supply()

    a = result["analysis"]
    print(f"As of {result['as_of']}:")
    print(f"  USDT circulating: ${a['usdt_circulating'] / 1e9:.1f}B")
    print(f"  USDC circulating: ${a['usdc_circulating'] / 1e9:.1f}B")
    print(f"  Combined:         ${a['usdt_usdc_combined'] / 1e9:.1f}B")
    print(f"  DA-003 threshold: $300.0B")
    print(f"  DA-003 crossed:   {a['da003_correct_if_combined_ge_300b']}")
    if a["us_regulated_depegged_now"]:
        print(f"  DA-004 WARNING: intraday depeg on {a['us_regulated_depegged_now']}")
        print("  Note: DA-004 requires >24h; one-shot snapshot detects the event only,")
        print("  not duration. Run repeatedly or correlate with historical data to confirm.")
    else:
        print("  DA-004 depeg:     None (at snapshot time)")

    if not args.dry_run:
        path = write_snapshot("stablecoin-supply", result)
        print(f"Snapshot written: {path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
