# Prediction Resolution Prep: SC-002

## Prediction Details

| Field | Value |
|-------|-------|
| ID | SC-002 |
| Claim | The PHLX Semiconductor Index (SOX) total return will be less than the S&P 500 total return for H1 2026 (Jan 1 – Jun 30, 2026) |
| Made | 2026-01-03 |
| Resolves | July 1, 2026 |
| Status | Pending - Resolution Prep |

---

## Resolution Criteria

Prediction resolves **CORRECT** if:

- SOX total return (price return + dividends reinvested) for Jan 1 – Jun 30, 2026 < S&P 500 total return for the same period

Prediction resolves **INCORRECT** if:

- SOX total return ≥ S&P 500 total return
- Ties (within 10 bps) resolve INCORRECT (strict underperformance required)

---

## Measurement Conventions

| Detail | Specification |
|--------|---------------|
| Start price | Closing price December 31, 2025 |
| End price | Closing price June 30, 2026 |
| Return type | Total return including reinvested dividends |
| Currency | USD |
| Index for SOX | PHLX Semiconductor Index (^SOX) |
| Proxy ETF (if needed) | SOXX or SMH for total-return calculation |
| Index for S&P 500 | S&P 500 Total Return Index (^SP500TR) |

**Note:** The price SOX index does not reinvest dividends. For total return, use an ETF proxy (SOXX) with dividends reinvested, or compute ourselves from index dividend yield (~1%).

---

## Baseline Data (Dec 31, 2025)

To be populated from market close on Dec 31, 2025 (already past):

| Index | Dec 31, 2025 Close | Source |
|-------|-------------------|--------|
| SOX (^SOX) | _to be recorded_ | Yahoo Finance |
| SP500TR (^SP500TR) | _to be recorded_ | S&P Global |
| SOXX ETF | _to be recorded_ | iShares |
| SPY ETF | _to be recorded_ | State Street |

**Action item:** On first data pipeline run, record these baselines.

---

## Interim Monitoring Points

Track monthly through H1 2026:

| Date | SOX Level | S&P 500 Level | YTD Spread |
|------|-----------|---------------|------------|
| Jan 31, 2026 | | | |
| Feb 28, 2026 | | | |
| Mar 31, 2026 | | | |
| Apr 30, 2026 | | | |
| May 31, 2026 | | | |
| Jun 30, 2026 | | | |

Spread = SOX YTD return − S&P 500 YTD return. Negative spread means prediction tracking CORRECT.

---

## Rationale Snapshot

From the Semiconductor Cycle Analysis (2026-01-03):

- SOX returned +41% in 2025 vs S&P 500's ~25%
- SOX P/E at 41x (TTM), 85%+ historical percentile
- NVIDIA datacenter growth decelerating (100%+ → 66% in latest quarter)
- Memory prices at late-cycle levels (HBM contracts +20%)
- DeepSeek event (January 2025) validated efficiency thesis

**Thesis:** Extreme outperformance in 2025 plus late-cycle indicators make mean reversion likely in H1 2026. Prediction is a bet on cycle timing, not secular direction.

---

## Key Risks to Prediction

### Risks of underperformance (favor CORRECT)

- NVIDIA Q4 FY26 deceleration below consensus
- Hyperscaler capex guidance moderation in Q1 2026 earnings
- Continued AI efficiency news flow
- DRAM price softening as HBM supply catches up
- Rate/inflation surprise hitting growth multiples disproportionately

### Risks of outperformance (favor INCORRECT)

- NVIDIA Blackwell/Rubin beat-and-raise cycle
- New AI use cases (agents, robotics) driving compute demand
- Hyperscaler capex raise in Q1 2026
- Broader market weakness (relative outperformance via lower losses)
- China tensions lift reshoring/fab-stock valuations

---

## Likelihood Assessment

| Scenario | Probability | Outcome |
|----------|-------------|---------|
| SOX down, SPX up | 25% | CORRECT |
| SOX up less than SPX | 30% | CORRECT |
| SOX up roughly equal to SPX | 10% | INCORRECT |
| SOX beats SPX | 30% | INCORRECT |
| Both down, SOX down more | 5% | CORRECT |

**Subjective ex-ante probability of CORRECT: ~60%**

---

## Data Sources

| Source | Usage |
|--------|-------|
| Yahoo Finance (^SOX, ^SP500TR) | Price and total return data |
| iShares SOXX fund page | Total return verification |
| S&P Dow Jones Indices | Official S&P 500 TR calculation |
| NASDAQ Index Services | Official SOX data |

---

## Resolution Checklist

On July 1, 2026 (or first trading day after June 30):

- [ ] Pull SOX close (Jun 30, 2026)
- [ ] Pull S&P 500 TR close (Jun 30, 2026)
- [ ] Pull SOXX ETF NAV total return (dividend-inclusive)
- [ ] Calculate both YTD returns
- [ ] Compute spread
- [ ] Determine: CORRECT or INCORRECT
- [ ] Document with signed, dated screenshot or data-API response
- [ ] Update predictions/tracker.md
- [ ] Update analysis/semiconductor-cycle-2026-01.md Track Record
- [ ] Commit: "Resolve: SC-002 - {SOX XX.X% vs SPX YY.Y%, outcome}"

---

## Sources

- [S&P Dow Jones Indices S&P 500 TR](https://www.spglobal.com/spdji/en/indices/equity/sp-500/)
- [NASDAQ Semiconductor Index](https://www.nasdaq.com/market-activity/index/sox)
- [Semiconductor Cycle Analysis](/analysis/semiconductor-cycle-2026-01.md)

---

*Prepared: 2026-04-18*
