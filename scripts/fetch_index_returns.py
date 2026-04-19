"""Fetch SOX and S&P 500 total returns for a date range.

Supports SC-002 (SOX underperforms S&P H1 2026), SC-005 (SOX 20%+
correction in 2027), and AV-005 (NVIDIA+AMD+Arm market cap lower by
Dec 31, 2026).

Uses yfinance for adjusted-close prices. Adjusted close includes
dividend reinvestment and splits, so ratioing first and last adjusted
closes gives total return.
"""
from __future__ import annotations

import argparse
import sys
from datetime import date

from common import write_snapshot

try:
    import yfinance as yf
except ImportError:
    yf = None  # type: ignore

TICKERS_INDEX = {
    "SOX": "^SOX",       # PHLX Semiconductor (price return only)
    "SOXX": "SOXX",      # iShares ETF proxy for SOX total return
    "SP500TR": "^SP500TR",  # S&P 500 Total Return
}

TICKERS_MARKET_CAP = {
    "NVDA": "NVDA",
    "AMD": "AMD",
    "ARM": "ARM",
}


def total_return(ticker: str, start: str, end: str) -> dict:
    if yf is None:
        raise RuntimeError("yfinance is not installed. Run `pip install -r scripts/requirements.txt`.")
    hist = yf.Ticker(ticker).history(start=start, end=end, auto_adjust=False)
    if hist.empty:
        raise RuntimeError(f"No data returned for {ticker} between {start} and {end}")
    start_adj = float(hist["Adj Close"].iloc[0])
    end_adj = float(hist["Adj Close"].iloc[-1])
    ret = (end_adj / start_adj) - 1.0
    return {
        "ticker": ticker,
        "start": start,
        "end": end,
        "start_adj_close": round(start_adj, 4),
        "end_adj_close": round(end_adj, 4),
        "total_return": round(ret, 6),
    }


def fetch_index_returns(start: str, end: str) -> dict:
    results = {name: total_return(ticker, start, end) for name, ticker in TICKERS_INDEX.items()}

    sox_proxy = results["SOXX"]["total_return"]
    sp_tr = results["SP500TR"]["total_return"]
    spread = sox_proxy - sp_tr
    results["analysis"] = {
        "sox_total_return": sox_proxy,
        "sp500_total_return": sp_tr,
        "spread_sox_minus_sp": round(spread, 6),
        "sc002_correct_if_h1_2026": bool(spread < 0),
    }
    return results


def fetch_combined_market_cap() -> dict:
    if yf is None:
        raise RuntimeError("yfinance is not installed.")
    caps = {}
    total = 0
    for name, ticker in TICKERS_MARKET_CAP.items():
        info = yf.Ticker(ticker).info
        cap = info.get("marketCap")
        caps[name] = cap
        if cap:
            total += cap
    caps["combined"] = total
    caps["as_of"] = date.today().isoformat()
    return caps


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", required=True, help="YYYY-MM-DD")
    parser.add_argument("--end", required=True, help="YYYY-MM-DD")
    parser.add_argument("--with-market-cap", action="store_true",
                        help="Also snapshot NVDA+AMD+ARM combined market cap (AV-005)")
    args = parser.parse_args()

    index_data = fetch_index_returns(args.start, args.end)
    path = write_snapshot("index-returns", index_data)
    print(f"Snapshot written: {path}")
    a = index_data["analysis"]
    print(f"  SOX TR:   {a['sox_total_return'] * 100:+.2f}%")
    print(f"  SP500 TR: {a['sp500_total_return'] * 100:+.2f}%")
    print(f"  Spread:   {a['spread_sox_minus_sp'] * 100:+.2f}pp")

    if args.with_market_cap:
        caps = fetch_combined_market_cap()
        cap_path = write_snapshot("combined-market-cap", caps)
        print(f"Snapshot written: {cap_path}")
        print(f"  Combined market cap: ${caps['combined'] / 1e12:.2f}T")

    return 0


if __name__ == "__main__":
    sys.exit(main())
