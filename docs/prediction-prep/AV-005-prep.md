# Prediction Resolution Prep: AV-005

## Prediction Details

| Field | Value |
|-------|-------|
| ID | AV-005 |
| Claim | Combined market cap of NVIDIA + AMD + Arm will be **lower** on Dec 31, 2026 than on Jan 3, 2026 |
| Made | 2026-01-03 |
| Resolves | 2026-12-31 |
| Status | Pending |

---

## Baseline (Jan 3, 2026)

The original AI Valuation Analysis stated NVIDIA market cap "~$3.0T" — that figure was stale at publication. Reconciled against contemporaneous sources, the actual Jan 3, 2026 baseline is:

| Ticker | Market Cap (Jan 3, 2026) | Source |
|--------|-------------------------|--------|
| NVDA | ~$4.50T | [Intellectia / multiple aggregators](https://intellectia.ai/news/stock/nvidia-reaches-45-trillion-market-cap-data-center-business-could-double-by-2026); pullback from $5T peak in Oct 2025 |
| AMD | ~$0.25T (≈$155 share × 1.62B shares) | Macrotrends, public.com historical |
| ARM | ~$0.155T (≈$140 share × 1.05B shares) | Macrotrends, companiesmarketcap |
| **Combined** | **~$4.91T** | — |

**Data-discipline note:** The published analysis used ~$3.0T for NVIDIA, which would have implied a ~$3.4T baseline. Using the corrected ~$4.5T baseline gives ~$4.91T combined. The threshold for AV-005 resolution is **whichever baseline a reasonable third party can verify on Jan 3, 2026** — i.e. ~$4.91T. The published $3.0T figure is a known error in the source document and the resolution should not be evaluated against it. (Per the immutability protocol, the prediction text itself is unchanged; only the baseline-data clarification is updated here.)

---

## Interim Status (May 7–8, 2026)

| Ticker | Market Cap (May 7, 2026) | YTD Change | Source |
|--------|-------------------------|------------|--------|
| NVDA | ~$5.05T | +12% | [Capital.com](https://capital.com/en-int/markets/shares/nvidia-corp-share-price/market-cap), [CNBC: $5T close](https://www.cnbc.com/2026/04/24/nvidia-stock-closes-at-record-pushing-market-cap-past-5-trillion.html) |
| AMD | ~$0.687T | +175% | [public.com AMD market cap](https://public.com/stocks/amd/market-cap), all-time high $421.39 close on May 6, 2026 |
| ARM | ~$0.245T | +58% | [Capital.com ARM](https://capital.com/en-int/markets/shares/arm-holdings-plc-share-price-1/market-cap), [companiesmarketcap](https://companiesmarketcap.com/arm-holdings/marketcap/) |
| **Combined** | **~$5.98T** | **+22%** | — |

For AV-005 to resolve CORRECT, the combined market cap on Dec 31, 2026 must be **less than ~$4.91T** — i.e. the trio must give back the entire ~$2.5T of gains booked in the last 16 months and then some, in roughly 7.5 months.

**Probability assessment as of May 8, 2026:** The combined trio would need to fall ~18% from current levels just to revert to the Jan 3 baseline, and ~25%+ to clear the threshold meaningfully. This is not impossible (AI semis have shown 25%+ drawdowns multiple times in 24 months) but is now substantially harder than at January 2026.

Subjective probability of CORRECT resolution: **~15%** (down from an implicit ~40% at publication).

---

## Resolution Protocol

### Threshold

CORRECT iff: NVDA(Dec 31, 2026 close) + AMD(Dec 31, 2026 close) + ARM(Dec 31, 2026 close) all in market-cap terms, summed, is **strictly less than** ~$4.91T (the Jan 3, 2026 baseline).

### Tie-breaker

Per the pre-registration framework default for numerical thresholds: strict inequality. A combined market cap exactly equal to or above the baseline → INCORRECT.

### Source

Yahoo Finance closing market cap on Dec 31, 2026 (or last trading day of 2026 if Dec 31 is a weekend) for each ticker. Cross-check with companiesmarketcap.com and one of the listed exchange data feeds.

### Edge cases

- **Stock splits:** Use share counts as of Dec 31, 2026; market cap is the same regardless of split.
- **M&A:** If AMD or ARM is acquired and delisted, use the last reported market cap before delisting.
- **NVIDIA fiscal year offset:** Irrelevant — calendar Dec 31 closing prices apply.

---

## What would change this read

The probability of CORRECT resolution rises materially if any of these happen between now and December 2026:

1. **AI capex air-pocket:** A hyperscaler explicitly cuts 2026 H2 capex (HC-002 trigger) — direct read-through to NVDA/AMD orders.
2. **DeepSeek-style efficiency event:** A new open-source release that materially undermines API/training compute demand.
3. **HBM/memory price collapse:** Would compress NVDA gross margin and trigger valuation derate.
4. **Recession or rate shock:** Cyclical drawdown across high-beta semis.
5. **Antitrust action:** US, EU, or China regulatory move against NVIDIA's GPU dominance.
6. **Supply unblock:** If the supply-constraint story unwinds (transformers, power) faster than demand grows, NVDA's pricing power erodes.

Absent at least one of these, AV-005 resolves INCORRECT.

---

## Mechanism update vs. the original thesis

The January 2026 AI Valuation Analysis bet on **demand destruction via efficiency**. Q1 2026 earnings (resolved AV-002 INCORRECT on May 8, 2026) instead showed **demand exceeding supply**, with $700B combined Big-4 capex guidance. The mechanism that originally supported AV-005 — efficiency erodes the value of compute scarcity — is not currently visible in price action; if anything, the supply-constraint story has *increased* the value of installed GPU capacity.

For AV-005 to flip back to favorable, the *channel* by which efficiency would transmit into the trio's market cap needs to either (a) re-emerge in the form an efficiency event large enough to reset expectations, or (b) get blocked by a separate cyclical / regulatory shock.

---

## Sources

- [companiesmarketcap.com NVDA](https://companiesmarketcap.com/nvidia/marketcap/)
- [companiesmarketcap.com ARM](https://companiesmarketcap.com/arm-holdings/marketcap/)
- [Macrotrends AMD market cap](https://www.macrotrends.net/stocks/charts/AMD/amd/market-cap)
- [Macrotrends ARM market cap](https://www.macrotrends.net/stocks/charts/ARM/arm-holdings/market-cap)
- Original prediction: [analysis/ai-valuation-2026-01.md](../../analysis/ai-valuation-2026-01.md#prediction-5-ai-infrastructure-valuation-compression)

---

*Prepared: 2026-05-08*
