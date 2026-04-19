# Prediction Resolution Prep: EA-001

## Prediction Details

| Field | Value |
|-------|-------|
| ID | EA-001 |
| Claim | Enterprise AI spending growth forecast falls below 25% YoY for 2027 in at least one major analyst forecast (IDC, Gartner, Forrester) by Q2 2026 |
| Made | 2026-01-03 |
| Resolves | June 30, 2026 |
| Status | Pending - Resolution Prep |

---

## Resolution Criteria

Prediction resolves **CORRECT** if, by June 30, 2026, any of:

- IDC Worldwide AI Spending Guide publishes a 2027 forecast showing <25% YoY growth
- Gartner IT Spending Forecast or Emerging Tech Impact Radar publishes 2027 AI growth forecast <25%
- Forrester Tech Budget or AI Predictions publishes 2027 forecast <25%

Any single forecast satisfies the claim.

Prediction resolves **INCORRECT** if all three publish 2027 forecasts ≥25% growth (or remain silent on 2027 specifically).

---

## Baseline

From Enterprise AI Adoption analysis (2026-01-03):

| Survey | 2026 Spending Intentions | Implicit Deceleration |
|--------|-------------------------|----------------------|
| Gartner CIO Survey | +28% | -4% vs 2025 |
| Forrester Tech Budget | +25% | -7% vs 2025 |
| IDC Spending Guide | +30% | -2% vs 2025 |
| **Average** | **+28%** | **-4% vs 2025** |

**Observation:** The 2026 forecasts straddle the 25% line. If deceleration continues at ~4pp/year, 2027 forecasts naturally fall below 25%. The prediction is effectively a directional continuation bet.

---

## Publication Timing

| Source | Typical Publication Window | Covers |
|--------|---------------------------|--------|
| IDC Worldwide AI Spending Guide | Semi-annual (March, September) | Rolling 5-year forecast |
| Gartner IT Spending Forecast | Quarterly updates | Current year + 2 forward years |
| Forrester Tech Budget | Annual (Q4), updated mid-year | 1-2 year forward |

**March 2026 publications are the most likely trigger.** Gartner's Q1 2026 update would first introduce 2027-specific AI figures. IDC's H1 2026 guide typically publishes in March–April.

---

## Data Collection Protocol

### Step 1: Monitor publication calendars

Watch for:
- IDC press releases tagged "AI Spending" or "AI Investment"
- Gartner "IT Spending Forecast" releases (check Gartner Newsroom)
- Forrester "Predictions" or "Tech Budget" publications

### Step 2: Extract 2027 figures

For each report, record:
- Specific 2027 YoY growth rate
- Whether "AI" is defined as GenAI only, all AI, or AI+infrastructure
- Sample size and methodology

### Step 3: Category normalization

Forecasts vary by definition. Accept any of:
- "GenAI spending growth"
- "AI software spending growth"
- "Enterprise AI investment growth"
- "AI-related IT spending growth"

Reject if only forecasting:
- "AI infrastructure" (too narrow, hyperscaler capex)
- "AI market size in dollars" (not a growth rate)

### Step 4: Cross-verification

If one source publishes <25% but the other two remain above:
- Prediction resolves CORRECT (claim requires only one)
- Document all three to demonstrate non-consensus nature

---

## Likelihood Assessment

### Structural factors favoring CORRECT resolution

- 2026 forecasts already trending down (28% → ~25% line)
- Base-year effect: 2026 AI spending is large, making 25%+ growth harder
- CFO ROI scrutiny rising (survey data shows 68% report higher scrutiny)
- Consulting firms reporting 70-85% project failure rates

### Factors favoring INCORRECT

- Catch-up effect: Laggard enterprises initiating AI programs
- Agentic AI narrative could re-accelerate spending
- IDC historically bullish on AI spending forecasts

**Subjective ex-ante probability of CORRECT: ~65%**

---

## Edge Cases

### What if an analyst publishes a range (e.g., 22-28%)?

Accept CORRECT if the midpoint is <25%. Reject if midpoint is ≥25%.

### What if only "GenAI" (not total AI) is <25%?

Accept. GenAI is the dominant current AI spending category and is a legitimate stand-in.

### What if the forecast is directional/qualitative ("deceleration expected") without a specific number?

Reject. Prediction requires a published quantitative forecast.

### What if a fourth analyst publishes <25% but IDC/Gartner/Forrester don't?

Reject on strict reading. Prediction names three specific sources.

---

## Resolution Checklist

By June 30, 2026:

- [ ] Monitor IDC, Gartner, Forrester publication channels
- [ ] Download any 2026 AI spending reports covering 2027
- [ ] Extract quantitative 2027 growth forecasts
- [ ] Verify definition matches enterprise AI spending
- [ ] Determine: CORRECT or INCORRECT
- [ ] Document source citation
- [ ] Update predictions/tracker.md
- [ ] Update analysis/enterprise-ai-adoption-2026-01.md
- [ ] Commit: "Resolve: EA-001 - {source, figure, outcome}"

---

## Sources

- [IDC AI Spending Guide](https://www.idc.com/getdoc.jsp?containerId=IDC_P39198)
- [Gartner IT Spending Forecast](https://www.gartner.com/en/information-technology/insights/it-spending)
- [Forrester Predictions](https://www.forrester.com/predictions/)
- [Enterprise AI Adoption Analysis](/analysis/enterprise-ai-adoption-2026-01.md)

---

*Prepared: 2026-04-18*
