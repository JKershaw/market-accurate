# Prediction Resolution Prep: AV-001

## Prediction Details

| Field | Value |
|-------|-------|
| ID | AV-001 |
| Claim | NVIDIA Q4 FY2026 datacenter revenue YoY growth will be below 50% |
| Made | 2026-01-03 |
| Resolves | February 2026 |
| Status | Pending - Resolution Prep |

---

## Current Data (as of 2026-01-03)

### Q3 FY2026 Results (Reported November 2025)

| Metric | Value | Source |
|--------|-------|--------|
| Datacenter Revenue | $51.2B | NVIDIA Q3 FY26 Earnings |
| Datacenter YoY Growth | 66% | NVIDIA Q3 FY26 Earnings |
| Total Revenue | $57.0B | NVIDIA Q3 FY26 Earnings |
| Total YoY Growth | 62% | NVIDIA Q3 FY26 Earnings |

### Q4 FY2026 Guidance

| Metric | Value | Source |
|--------|-------|--------|
| Total Revenue Guidance | $65B ± $1.3B | NVIDIA Q3 Earnings Call |
| Implied Total YoY Growth | ~65% | Calculation |
| Wall Street Datacenter Estimate | $55.78B | Analyst consensus |
| Gross Margin Guidance | 75.0% ± 50bps | NVIDIA Q3 Earnings Call |

### Historical Datacenter Growth (for context)

| Quarter | Datacenter Revenue | YoY Growth |
|---------|-------------------|------------|
| Q4 FY2025 | ~$39.2B | +100%+ |
| Q1 FY2026 | ~$42.6B | ~79% |
| Q2 FY2026 | ~$47.4B | ~69% |
| Q3 FY2026 | $51.2B | 66% |

**Trend:** Growth is decelerating but still above 50% threshold.

---

## Preliminary Assessment

### For Prediction (growth <50%)

- Deceleration trend is clear: 100%+ → 79% → 69% → 66%
- Each quarter shows ~5-10 point deceleration
- If trend continues, Q4 could approach 55-60% range
- Base effects getting larger (Q4 FY25 was massive)

### Against Prediction (growth ≥50%)

- Q4 guidance implies strong 65% YoY total growth
- Blackwell demand remains robust
- Major contracts: OpenAI (10GW), Anthropic (1GW), xAI Colossus
- Wall Street expects $55.78B datacenter (would be ~42% sequential growth)
- No signs of demand weakness in guidance

### Current Probability Assessment

| Outcome | Probability | Reasoning |
|---------|-------------|-----------|
| Growth <50% (prediction correct) | 25% | Would require major miss vs guidance |
| Growth 50-60% | 50% | Continued deceleration within trend |
| Growth >60% | 25% | Guidance beat on strong Blackwell ramp |

---

## Resolution Requirements

### Data Source

- **Primary:** NVIDIA Q4 FY2026 earnings release
- **Expected Date:** Late February 2026 (typically third week)
- **Where to Find:** [NVIDIA Investor Relations](https://investor.nvidia.com/)

### Calculation

```
Datacenter YoY Growth = (Q4 FY26 DC Revenue - Q4 FY25 DC Revenue) / Q4 FY25 DC Revenue × 100
```

### Q4 FY2025 Baseline

| Metric | Value | Source |
|--------|-------|--------|
| Q4 FY2025 Datacenter Revenue | ~$39.2B | NVIDIA Q4 FY25 Earnings |

### Threshold Calculation

For prediction to be **CORRECT** (growth <50%):
- Q4 FY26 Datacenter Revenue must be < $58.8B ($39.2B × 1.50)

For prediction to be **INCORRECT** (growth ≥50%):
- Q4 FY26 Datacenter Revenue must be ≥ $58.8B

---

## Resolution Checklist

When Q4 FY2026 earnings are released:

- [ ] Download earnings release from NVIDIA IR
- [ ] Extract datacenter segment revenue
- [ ] Calculate YoY growth rate
- [ ] Compare to 50% threshold
- [ ] Determine: CORRECT or INCORRECT
- [ ] Update predictions/tracker.md
- [ ] Update analysis/ai-valuation-2026-01.md Track Record
- [ ] Commit: "Resolve: AV-001 - {outcome summary}"

---

## Sources

- [NVIDIA Q3 FY2026 Earnings](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-third-quarter-fiscal-2026)
- [NVIDIA Investor Relations](https://investor.nvidia.com/)
- [Futurum Group Analysis](https://futurumgroup.com/insights/nvidia-q3-fy-2026-record-data-center-revenue-higher-q4-guide/)

---

*Prepared: 2026-01-03*
