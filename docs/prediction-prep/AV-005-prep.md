# Prediction Resolution Prep: AV-005

## Prediction Details

| Field | Value |
|-------|-------|
| ID | AV-005 |
| Claim | Combined market cap of NVIDIA + AMD + Arm will be lower on Dec 31, 2026 than on Jan 3, 2026 |
| Made | 2026-01-03 |
| Resolves | December 31, 2026 |
| Status | Pending — Resolution Prep |

---

## Baseline as of Publication (Jan 3, 2026)

| Ticker | Close price (Jan 2, 2026) | Shares outstanding (approx) | Market cap |
|--------|---------------------------|------------------------------|------------|
| NVDA | ~$129.50 | 24.54B | ~$3.18T |
| AMD | ~$122.60 | 1.62B | ~$198B |
| ARM | ~$128.70 | 1.04B | ~$134B |
| **Combined** | — | — | **~$3.51T** |

*Prices sourced from Yahoo Finance close on 2026-01-02 (last trading day before Jan 3). Share-count figures approximate; resolution should use end-of-day Dec 31, 2026 data from the same source to maintain consistency.*

**Key point for resolution:** Because this prediction was made on a holiday (Jan 3, 2026 was a Saturday), use the Jan 2, 2026 close as the baseline and the Dec 31, 2026 close as the resolution value. Document the exact data provider and timestamp in the resolution note.

---

## Interim Check (Apr 24, 2026)

| Ticker | Close Apr 23, 2026 (approx) | YTD change |
|--------|------------------------------|------------|
| NVDA | ~$138 | +6.5% |
| AMD | ~$115 | -6.2% |
| ARM | ~$122 | -5.2% |
| **Combined market cap** | ~$3.55T | +1.1% |

*Directional read only — resolution will use final Dec 31, 2026 data.*

**Interim interpretation:** Combined market cap is up ~1% YTD. NVIDIA Q4 FY26 earnings (Feb 25, 2026) produced a +75% YoY Data Center growth print that strengthened the bull case (see AV-001 resolution). AMD and Arm have been weaker due to competitive concerns (AMD) and mobile cycle softness (Arm). Probability that the combined figure is lower on Dec 31 is presently below 50%.

---

## Resolution Criteria

Prediction is **CORRECT** if:
- Combined market cap (NVDA + AMD + ARM) on Dec 31, 2026 close < Combined market cap on Jan 2, 2026 close
- Use the same data provider for both baseline and resolution (Yahoo Finance default)
- Use "shares outstanding" figures from the most recent 10-Q filed before each date

Prediction is **INCORRECT** if the combined figure is equal to or greater than the baseline.

---

## Edge Cases

| Case | Handling |
|------|----------|
| NVDA stock split | Use market cap, not price, for comparison |
| AMD secondary offering | New share count is baked into market cap at resolution date |
| ARM tender offer / buyback | Same — use market cap at each date |
| Merger: any of the three acquires another | Combined market cap is still the sum of whatever entities survive from the set |
| Merger: one of the three is acquired by outside party | Use the last public trading day's market cap for the acquired entity, plus the acquirer-implied value at close date if stock consideration; prefer last-trading-day market cap if cash-only |
| Trading halt on Dec 31 | Use last trading day of 2026 |

---

## Data Collection Protocol

### Step 1: Pull closing data on Jan 2, 2027 (first trading day of 2027)

| Data point | Source |
|-----------|--------|
| NVDA Dec 31, 2026 close | Yahoo Finance historical |
| AMD Dec 31, 2026 close | Yahoo Finance historical |
| ARM Dec 31, 2026 close | Yahoo Finance historical |
| NVDA shares outstanding | Latest 10-Q available Dec 31 |
| AMD shares outstanding | Latest 10-Q available Dec 31 |
| ARM shares outstanding | Latest 10-Q / 20-F available Dec 31 |

### Step 2: Compute

```
Combined_Dec31_2026 = (NVDA_close × NVDA_shares) + (AMD_close × AMD_shares) + (ARM_close × ARM_shares)
Combined_Jan2_2026  = $3.51T (baseline established at publication)

Result = Combined_Dec31_2026 < Combined_Jan2_2026 ? CORRECT : INCORRECT
```

### Step 3: Cross-check

- Compare against Bloomberg Terminal or Refinitiv to confirm Yahoo figures
- If discrepancy >1% between providers, use the higher-quality source and document

---

## Context: Thesis Evolution

The January prep noted two scenarios that would resolve CORRECT:
1. **Demand destruction** via AI efficiency gains (efficiency thesis binds)
2. **Macro risk-off** that compresses high-multiple tech

The April 2026 interim update to [ai-valuation-2026-01.md](/analysis/ai-valuation-2026-01.md) introduced a third scenario that makes INCORRECT *more* likely:
3. **Supply-constraint scarcity premium** — physical infrastructure bottlenecks make existing NVIDIA/AMD capacity *more* valuable, not less

The original prediction logic relied on scenarios 1 or 2. Scenario 3 has strengthened materially since January:
- 30–50% of planned 2026 US AI DCs delayed/cancelled on power/transformer constraints
- Hyperscaler 2026 capex guidance raised, not lowered
- NVIDIA Q4 FY26 +75% YoY (AV-001 resolution)

**Updated subjective probability of CORRECT:** ~25% (down from ~45% at January prep).

---

## Resolution Checklist

When Jan 2, 2027 market opens:

- [ ] Pull Dec 31, 2026 close for NVDA, AMD, ARM
- [ ] Pull latest shares-outstanding data for each
- [ ] Compute combined market cap
- [ ] Compare to $3.51T baseline
- [ ] Cross-check against secondary data source
- [ ] Update predictions/tracker.md with outcome
- [ ] Update analyst-comparison.md
- [ ] Update ai-valuation-2026-01.md Track Record
- [ ] Update cumulative statistics (accuracy, Brier score)
- [ ] Commit: "Resolve: AV-005 — {outcome summary}"

---

## Interim Monitoring

Record quarterly snapshots to detect drift:

| Date | NVDA market cap | AMD market cap | ARM market cap | Combined | Delta vs. baseline |
|------|-----------------|---------------|----------------|----------|-------------------|
| Jan 2, 2026 (baseline) | ~$3.18T | ~$198B | ~$134B | ~$3.51T | — |
| Apr 24, 2026 | ~$3.39T | ~$186B | ~$127B | ~$3.55T | +1.1% |
| Jul 31, 2026 | TBD | TBD | TBD | TBD | TBD |
| Oct 31, 2026 | TBD | TBD | TBD | TBD | TBD |
| Dec 31, 2026 | (resolve) | (resolve) | (resolve) | (resolve) | (resolve) |

Use scripts/fetch_index_returns.py as a template for automating these snapshots.

---

## Sources

- [Yahoo Finance NVDA](https://finance.yahoo.com/quote/NVDA/)
- [Yahoo Finance AMD](https://finance.yahoo.com/quote/AMD/)
- [Yahoo Finance ARM](https://finance.yahoo.com/quote/ARM/)
- [NVIDIA 10-K / 10-Q filings](https://investor.nvidia.com/financial-info/sec-filings/)
- [AMD Investor Relations](https://ir.amd.com/)
- [Arm Holdings Investor Relations](https://investors.arm.com/)

---

*Prepared: 2026-04-24*
