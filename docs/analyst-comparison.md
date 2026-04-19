# Analyst Consensus Comparison Framework

This document tracks how Market Accurate predictions compare to Wall Street analyst consensus, enabling accuracy comparison against professional forecasters.

---

## Purpose

Comparing predictions to analyst consensus serves two goals:

1. **Calibration:** Are we making non-trivial predictions (different from consensus)?
2. **Relative Performance:** Do we outperform professional analysts over time?

---

## Methodology

### Data Sources for Consensus

| Source | Coverage | Update Frequency |
|--------|----------|------------------|
| FactSet | Earnings, revenue estimates | Daily |
| Bloomberg | Broad financial estimates | Real-time |
| LSEG (Refinitiv) | Global coverage | Daily |
| Yahoo Finance | Free consensus data | Daily |
| Visible Alpha | Detailed segment estimates | Weekly |

### Comparison Metrics

| Metric | Definition |
|--------|------------|
| **Contrarian Score** | % of predictions differing from consensus direction |
| **Accuracy vs. Consensus** | Our accuracy - Consensus accuracy |
| **Information Value** | Do our predictions provide signal beyond consensus? |

---

## Active Comparisons

### AV-001: NVIDIA Q4 FY26 Datacenter Growth

| Metric | Market Accurate | Wall Street Consensus |
|--------|----------------|----------------------|
| **Prediction** | <50% YoY growth | ~65% YoY growth |
| **Direction** | Bearish vs trend | Continuation |
| **Made** | 2026-01-03 | Current as of Jan 2026 |
| **Contrarian?** | Yes | — |

**Consensus Sources:**
- NVIDIA Q4 guidance: $65B total revenue (65% YoY growth)
- Sell-side estimates: $55-58B datacenter revenue
- Implied datacenter growth: 55-65% YoY

**Outcome:** Resolved 2026-04-19. Actual: $62.3B DC revenue, +75% YoY. **Both Market Accurate and consensus were wrong**, but consensus was directionally correct (predicted ~65% vs <50%) while we predicted <50% and missed by more. Scorecard: Market Accurate INCORRECT, Wall Street consensus technically INCORRECT (65% < 75%) but directionally closer. Lesson: contrarian calls need base-rate discipline; NVIDIA's growth had not shown deceleration in any of the four prior quarters, making <50% a high bar.

---

### AV-005: NVIDIA+AMD+Arm Market Cap

| Metric | Market Accurate | Wall Street Consensus |
|--------|----------------|----------------------|
| **Prediction** | Lower on Dec 31, 2026 | Generally bullish |
| **Direction** | Bearish | Bullish |
| **Made** | 2026-01-03 | — |
| **Contrarian?** | Yes | — |

**Consensus Sources:**
- Sell-side price targets generally above current prices
- Majority "Buy" or "Overweight" ratings

**Outcome:** Pending (December 31, 2026)

---

### SC-002: SOX Underperforms S&P H1 2026

| Metric | Market Accurate | Wall Street Consensus |
|--------|----------------|----------------------|
| **Prediction** | SOX underperforms | Mixed |
| **Direction** | Relatively bearish | — |
| **Made** | 2026-01-03 | — |
| **Contrarian?** | Moderately | — |

**Outcome:** Pending (July 1, 2026)

---

## Tracking Template

When adding new comparisons:

```markdown
### [Prediction ID]: [Title]

| Metric | Market Accurate | Wall Street Consensus |
|--------|----------------|----------------------|
| **Prediction** | [Our claim] | [Consensus view] |
| **Direction** | [Bull/Bear/Neutral] | [Bull/Bear/Neutral] |
| **Made** | [Date] | [As of date] |
| **Contrarian?** | [Yes/No/Moderately] | — |

**Consensus Sources:**
- [Source 1]
- [Source 2]

**Outcome:** Pending / [Result]
```

---

## Cumulative Statistics

| Metric | Value |
|--------|-------|
| Total Comparisons | 3 |
| Contrarian Predictions | 3 |
| Resolved | 1 |
| Our Correct, Consensus Wrong | 0 |
| Consensus Correct, We Wrong | 0 |
| Both Correct | 0 |
| Both Wrong | 1 (AV-001: actual 75% > both our <50% and consensus ~65%) |

---

## Interpretation Guidelines

### What Contrarian Means

- **Contrarian:** Our prediction differs from consensus direction
- **Non-contrarian:** Our prediction aligns with consensus
- **Value of contrarian:** Correct contrarian predictions are more valuable (information gain)

### Accuracy Comparison

| Scenario | Interpretation |
|----------|---------------|
| We correct, consensus wrong | Our thesis has predictive value |
| Consensus correct, we wrong | Re-evaluate thesis |
| Both correct | Prediction was not differentiated |
| Both wrong | Event was unpredictable |

### Long-Term Goals

1. **Positive accuracy differential:** Outperform consensus over 20+ predictions
2. **Calibrated contrarianism:** Be contrarian when we have genuine edge
3. **Transparent comparison:** No cherry-picking favorable comparisons

---

## Update Schedule

This document will be updated:
- When predictions resolve
- When consensus estimates change materially
- Quarterly for active predictions

---

*Updated: 2026-01-03*
