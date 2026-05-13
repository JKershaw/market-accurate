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
- [Enterprise AI Adoption Analysis]({{ '/analysis/enterprise-ai-adoption-2026-01/' | relative_url }})

---

*Prepared: 2026-04-18*

---

## Addendum (May 8, 2026): Current state of 2027 forecasts (T-53 days)

### Gartner

**Headline 2026 forecast (Jan 15, 2026 release):** Total worldwide AI spending will reach $2.52T in 2026, +44% YoY ([Gartner press release Jan 15 2026](https://www.gartner.com/en/newsroom/press-releases/2026-1-15-gartner-says-worldwide-ai-spending-will-total-2-point-5-trillion-dollars-in-2026), [Next Platform analysis Jan 30 2026](https://www.nextplatform.com/2026/01/30/gartner-takes-another-stab-at-forecasting-ai-spending/)).

**2027 outlook (per Gartner sub-forecasts and analyst commentary):**

| Category | 2026 growth | 2027 growth | <25% threshold? |
|----------|-------------|-------------|-----------------|
| Total worldwide AI spending | +44% | reported "growth rate will slow in 2027 from 2026" — no specific number released | Indeterminate |
| AI software (specific) | 17.8% (forecast), grows to $297B by 2027 | **20.4%** (Gartner 2023-2027 forecast, 19.1% CAGR) | **Yes** |
| AI infrastructure | very high | slows but no number | Indeterminate |
| GenAI models | 80.8% (Gartner Feb 2026) | not specified | Indeterminate |

**Key Gartner data point that potentially resolves CORRECT:** The Gartner "Forecast Analysis: Artificial Intelligence Software, 2023-2027, Worldwide" report shows AI software market growth decelerating from 17.8% (2023-2026 average) to 20.4% in 2027, a 19.1% CAGR — both below 25%.

**Caveat:** This is the AI software sub-segment, not total enterprise AI spending. Per the prep doc (Section "Category normalization"), this is **acceptable** as "AI software spending growth" is one of the listed acceptable definitions. Reject only if "only forecasting AI infrastructure" — software is broader and acceptable.

### IDC

**2025–2029 CAGR:** 31.9% (driven by Agentic AI to $1.3T by 2029) ([IDC press release](https://my.idc.com/getdoc.jsp?containerId=prUS53765225)).

**2025 → 2028 trajectory:** $307B → $632B implies ~27% CAGR.

**Specific 2027 YoY:** Not yet published in a single-year breakout. IDC's Worldwide AI Spending Guide H1 2026 release expected before EA-001 resolution date.

**Read:** IDC remains above 25% on aggregate AI spending. Does NOT support CORRECT resolution from IDC alone.

### Forrester

**No 2027-specific public forecast yet found at time of writing.** Forrester typically publishes 2027 figures in Q4 2026 Predictions report (October–November 2026), which would be **after** the EA-001 resolution date.

If Forrester does not publish a 2027 figure by June 30, 2026, it cannot contribute to CORRECT or INCORRECT.

### Read at T-53 days

| Source | 2027 forecast status | Potentially resolves CORRECT? |
|--------|---------------------|-------------------------------|
| **Gartner (AI software sub-segment)** | 20.4% YoY for 2027 (in 2023-2027 forecast doc) | **Yes** — already below threshold |
| Gartner (total AI spending) | "Growth rate will slow" but no 2027 number released | Indeterminate |
| IDC (total AI spending) | ~27% implicit, ~32% CAGR through 2029 | No |
| Forrester | No 2027 figure expected pre-resolution | No |

### Probability update

The Gartner AI software 2027 figure of ~20.4% likely satisfies the EA-001 threshold under a fair reading of the prep doc's category-normalization rules. There is a reasonable INCORRECT-defense argument that the Gartner total (which is what most readers would think of as "enterprise AI spending") is still well above 25% and that the software sub-segment is too narrow.

**Strict-reading resolution:** Likely **CORRECT** (Gartner AI software 19.1% CAGR / 20.4% 2027).

**Conservative-reading resolution:** **INDETERMINATE** until Gartner or IDC publishes a top-line 2027 AI spending growth number specifically below 25%.

**Subjective probability of CORRECT resolution by June 30, 2026: ~70%** (up from 65% at April prep, given the Gartner AI software figures already in the public domain).

### Resolution actions in the next 4 weeks

1. **By May 22:** Pull the most recent Gartner "Forecast Analysis: Artificial Intelligence Software, 2023-2027" or successor document. Confirm 20.4% / 19.1% figures stand.
2. **By June 1:** Check whether IDC publishes its H1 2026 Worldwide AI Spending Guide update with explicit 2027 YoY rate.
3. **By June 15:** Check Forrester for any 2027 AI spending update tied to mid-year planning cycles.
4. **By June 30:** Final resolution. If Gartner AI software 20.4% figure is the strongest candidate, document the category-narrowness caveat in the resolution note.

---

*Addendum: 2026-05-08*
