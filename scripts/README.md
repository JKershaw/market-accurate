# Market Accurate Data Pipelines

Lightweight scripts to fetch and snapshot the metrics that underpin active predictions. The goal is to make data refreshes reproducible and reduce the manual effort of checking prediction thresholds.

These scripts favor **stable public sources** (SEC EDGAR, Yahoo Finance, HuggingFace) and avoid proprietary APIs. They are intentionally small—this is documentation-via-code, not a production ETL stack.

---

## Layout

```
scripts/
  README.md                  # this file
  requirements.txt           # pinned dependencies
  common.py                  # shared HTTP + snapshot helpers
  fetch_nvidia_earnings.py   # NVIDIA datacenter revenue (supports AV-001)
  fetch_hyperscaler_capex.py # MSFT/GOOG/AMZN/META capex (supports HC-001, AV-002, AV-007)
  fetch_index_returns.py     # SOX vs SPX total returns (supports SC-002, AV-005)
  fetch_stablecoin_supply.py # USDT/USDC/PYUSD supply + peg check (supports DA-003, DA-004)
  snapshot/                  # append-only JSON snapshots, gitignored by default
```

---

## Principles

1. **Append-only snapshots.** Every successful fetch writes a timestamped JSON file. Do not overwrite prior snapshots; they are the evidence trail.
2. **Fail loudly.** If a source shape changes, scripts should raise a clear error, not silently fall back to stale data.
3. **No credentials in repo.** Any API key comes from environment variables. Currently all sources are public; nothing required.
4. **Manual review before resolution.** Scripts produce data, not verdicts. Human verification is still required to resolve a prediction.

---

## Running

```bash
pip install -r scripts/requirements.txt

python scripts/fetch_index_returns.py --start 2025-12-31 --end 2026-06-30
python scripts/fetch_nvidia_earnings.py
python scripts/fetch_hyperscaler_capex.py --company MSFT
```

Each script prints a short summary and writes a JSON snapshot to `scripts/snapshot/<source>-<YYYY-MM-DD>.json`.

---

## Adding a new source

1. Copy an existing fetcher as a template.
2. Implement `fetch()` returning a plain dict.
3. Call `common.write_snapshot(name, data)` to persist.
4. Add a row to the **Supported predictions** table below.

---

## Supported predictions

| Script | Metric | Supports |
|--------|--------|----------|
| `fetch_nvidia_earnings.py` | Datacenter revenue, YoY growth | AV-001 |
| `fetch_hyperscaler_capex.py` | Quarterly capex per company | HC-001, HC-002, AV-002, AV-007 |
| `fetch_index_returns.py` | SOX, S&P 500 TR, combined market cap | SC-002, SC-005, AV-005 |
| `fetch_stablecoin_supply.py` | USDT/USDC/PYUSD circulating, peg check | DA-003, DA-004 |

---

## Roadmap

- `fetch_benchmark_leaderboard.py` — Open LLM leaderboard scrape for AV-003, OB-001
- `fetch_bnef_battery_prices.py` — Annual battery pack prices for EC-002
- `fetch_office_vacancy.py` — Yardi/CBRE office vacancy for CRE-001, CRE-004
- `fetch_ny_fed_household_debt.py` — CC delinquency data for CR-002
- `fetch_bdc_filings.py` — BDC non-accrual and PIK disclosure for PC-001
