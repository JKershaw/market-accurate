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

### AV-002: Hyperscaler Capex Language Moderation

| Metric | Market Accurate | Wall Street Consensus |
|--------|----------------|----------------------|
| **Prediction** | ≥1 of MSFT/GOOG/AMZN uses moderation language in Q1 2026 | Consensus does not explicitly forecast language; assumes continued expansion |
| **Direction** | Skeptical of continued acceleration | Continuation |
| **Made** | 2026-01-03 | — |
| **Contrarian?** | Moderately | — |

**Consensus Sources:**
- Sell-side 2026 capex forecasts consistent with aggressive expansion (pre-Q4 2025 earnings)
- Post Q4 2025 earnings: consensus embraced the $625–690B combined figure

**Outcome:** Pending (May 2026). Microsoft 1.5GW freeze and AWS lease pause are already visible as of April 2026.

---

### HC-001: Combined Big 4 Quarterly Capex <$150B in 2026

| Metric | Market Accurate | Wall Street Consensus |
|--------|----------------|----------------------|
| **Prediction** | Peaks below $150B | ~$156B quarterly average implied by 2026 guidance |
| **Direction** | Below consensus | Consensus embraces guidance |
| **Made** | 2026-01-03 | — |
| **Contrarian?** | Yes | — |

**Consensus Sources:**
- Hyperscaler 2026 guidance (Feb 2026): combined ~$625B implies $156B quarterly average
- Bloomberg/Futurum estimates of combined hyperscaler capex $650–690B

**Outcome:** Pending (December 31, 2026). Consensus strongly implies INCORRECT resolution unless physical constraints or guidance cuts materialize.

---

### OB-001: Open-Weights Maintains Parity

| Metric | Market Accurate | Wall Street Consensus |
|--------|----------------|----------------------|
| **Prediction** | Open-weights stays within 2 points of proprietary frontier | Mixed — many equity analysts assume proprietary moats persist |
| **Direction** | More bullish on open-weights than median sell-side | — |
| **Made** | 2026-01-03 | — |
| **Contrarian?** | Moderately | — |

**Consensus Sources:**
- Most equity research on MSFT, GOOG treats proprietary models as durable moats
- Venture analysts (Andreessen, Sequoia) more open-weights-bullish; public-market analysts more skeptical

**Outcome:** Pending (December 31, 2026). Q1 2026 releases show gap narrow-but-within-threshold (GPT-5 vs DeepSeek-V4 ~1.5 points on MMLU).

---

### CR-003: XLY Underperforms S&P 500 by 500bps in 2026

| Metric | Market Accurate | Wall Street Consensus |
|--------|----------------|----------------------|
| **Prediction** | XLY underperforms S&P by 500bps+ | Consensus: XLY modestly outperforms on mega-cap exposure (AMZN, TSLA) |
| **Direction** | Bearish discretionary | Neutral-to-bullish |
| **Made** | 2026-04-24 | — |
| **Contrarian?** | Moderately | — |

**Consensus Sources:**
- Sell-side consumer coverage generally positive on AMZN (cloud/AI halo) and TSLA (FSD narrative)
- Subsector views diverge from our end-demand-weakness thesis

**Outcome:** Pending (January 15, 2027).

---

### PC-001: BDC Non-Accrual Rate >3.0% in 2026

| Metric | Market Accurate | Wall Street Consensus |
|--------|----------------|----------------------|
| **Prediction** | Exceeds 3.0% in at least one quarter | Most sell-side expects modest rise to ~2.5–2.8% |
| **Direction** | More bearish on credit than consensus | — |
| **Made** | 2026-04-24 | — |
| **Contrarian?** | Moderately | — |

**Consensus Sources:**
- Wells Fargo BDC Monitor: expects stable-to-slightly-rising non-accruals
- Goldman Sachs BDC coverage: stress limited to specific vintages

**Outcome:** Pending (March 31, 2027).

---

### CR-005: No Technical Recession in 2026

| Metric | Market Accurate | Wall Street Consensus |
|--------|----------------|----------------------|
| **Prediction** | No recession | Mostly no recession (base case) |
| **Direction** | Consensus-aligned | — |
| **Made** | 2026-04-24 | — |
| **Contrarian?** | No | — |

**Consensus Sources:**
- Bloomberg recession probability tracker: ~35% for 2026 (as of April 2026)
- Fed Summary of Economic Projections: soft landing base case
- Blue Chip Economic Indicators consensus: ~2.0% real GDP 2026

**Outcome:** Pending (February 2027).

Note: Intentionally non-contrarian, to anchor calibration and guard against systematic pessimism bias. Low information value if resolved CORRECT — that's the point.

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
| Total Comparisons | 9 |
| Contrarian Predictions | 7 (2 consensus-aligned) |
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

*Updated: 2026-04-24 (added AV-002, HC-001, OB-001, CR-003, CR-005, PC-001 comparisons)*
