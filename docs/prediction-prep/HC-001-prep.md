# Prediction Resolution Prep: HC-001

## Prediction Details

| Field | Value |
|-------|-------|
| ID | HC-001 |
| Claim | Combined Big 4 quarterly capex will peak below $150B in 2026 |
| Made | 2026-01-03 |
| Resolves | December 31, 2026 |
| Status | Pending — Resolution Prep |

---

## Threshold Interpretation

The prediction says "peaks below $150B." Resolution requires:
- **CORRECT:** No calendar quarter in 2026 has combined Big 4 (MSFT + GOOG + AMZN + META) capex ≥ $150B
- **INCORRECT:** Any calendar quarter in 2026 has combined capex ≥ $150B

**Tie-breaker:** Following the pre-registration default, strict inequality. A quarter at exactly $150.0B resolves as INCORRECT (not "below").

---

## Baseline

| Quarter | MSFT | GOOG | AMZN | META | Combined |
|---------|------|------|------|------|----------|
| Q1 2025 | $21.0B | $17.2B | $24.3B | $13.2B | ~$75.7B |
| Q2 2025 | $24.2B | $22.4B | $26.8B | $17.0B | ~$90.4B |
| Q3 2025 | $34.9B | $23.9B | $35.1B | $19.4B | ~$113.3B |
| Q4 2025 | $33.5B | $25.2B | $37.8B | $20.8B | ~$117.3B |

*Source: company 10-Q / 10-K filings. Microsoft reports on a fiscal calendar; Q3 2025 calendar = Q1 FY26. Data consolidated by calendar quarter for consistency.*

**Run rate entering 2026:** ~$117B/quarter on Q4 2025 actuals.

---

## 2026 Trajectory Required for INCORRECT

For HC-001 to resolve INCORRECT, one quarter in 2026 must reach $150B. Given the Q4 2025 baseline of $117B, this requires a ~28% QoQ increase at some point in 2026.

| Hyperscaler | 2026 annual guidance (midpoint) | Implied quarterly avg | Implied QoQ from Q4 2025 |
|-------------|-------------------------------|----------------------|--------------------------|
| MSFT (FY26) | ~$94B | $23.5B | -30% |
| GOOG | $180B | $45B | +79% |
| AMZN | ~$200B | $50B | +32% |
| META | $125B | $31.25B | +50% |
| **Combined** | **~$625B** | **~$156B** | **~+33%** |

**Implication:** 2026 annual guidance implies a quarterly average of ~$156B, which is already above the $150B threshold. If guidance is roughly delivered, HC-001 resolves INCORRECT early — likely Q2 or Q3 2026.

---

## Interim Check (April 24, 2026)

Q1 2026 earnings are reporting now. Data points available pre-HC-001-resolution:

- **Alphabet Q1 2026 (late April 2026):** Reported capex to be monitored
- **Microsoft Q3 FY26 (late April 2026):** Reported capex to be monitored
- **Meta Q1 2026 (late April 2026):** Reported capex to be monitored
- **Amazon Q1 2026 (early May 2026):** Reported capex to be monitored

**Expected Q1 2026 pattern:** First-quarter capex is typically ~22–25% of annual for hyperscalers. Applied to $625B annual, Q1 expected ~$140–155B. Even Q1 alone could push the prediction over the threshold.

---

## Data Collection Protocol

### Step 1: Collect quarterly capex by company

For each 2026 quarter:

| Company | Filing | Field | Notes |
|---------|--------|-------|-------|
| MSFT | 10-Q | "Additions to property and equipment" | FY boundaries — align MSFT calendar quarter |
| GOOG | 10-Q | "Purchases of property and equipment" | Straightforward |
| AMZN | 10-Q | "Purchases of property and equipment" | Includes AWS + retail |
| META | 10-Q | "Purchases of property and equipment" | Straightforward |

### Step 2: Compute combined quarterly

```
Q_i_combined = MSFT_Q_i + GOOG_Q_i + AMZN_Q_i + META_Q_i
```

For Microsoft, use the calendar-quarter mapping:
- Q1 CY = Q3 FY (Jan–Mar)
- Q2 CY = Q4 FY (Apr–Jun)
- Q3 CY = Q1 FY (Jul–Sep)
- Q4 CY = Q2 FY (Oct–Dec)

### Step 3: Test threshold

For each quarter: is combined capex ≥ $150B?

If any quarter is ≥ $150B → HC-001 INCORRECT (early resolution possible)
If all 4 quarters are < $150B → HC-001 CORRECT (confirm at Dec 31, 2026)

---

## Edge Cases

| Case | Handling |
|------|----------|
| Capex reported includes non-AI spend | The prediction says "capex" not "AI capex"; use total capex as reported |
| A hyperscaler changes reporting methodology | Use the new methodology as reported; note the change in resolution |
| Finance leases included or excluded | Use the same definition across baseline and resolution (prefer 10-Q line "purchases of property and equipment") |
| Alphabet includes Google Cloud's data-center spending with "Other Bets" | Use consolidated capex from the consolidated cash-flow statement |
| A quarter is restated | Use the restated figure from the most recent filing at resolution time |

---

## Thesis Context

The January prediction assumed deceleration dynamics. Since then:
1. Q4 2025 earnings (Feb 2026) revealed 2026 guidance of $625–690B combined — materially above the $600B assumed in the analysis
2. The supply-constraint story (40% of planned DCs delayed) suggests *deployment* may lag guidance, but *reported capex* would still show the spending
3. Microsoft's 1.5GW self-build freeze and AWS lease pause would reduce forward quarters' spending but likely not early 2026 quarters (capex commitments made 6–12 months prior are already in-flight)

**Updated subjective probability of CORRECT:** ~15% (down from ~40% at January prep).

The path to CORRECT now requires:
- Material cancellation of in-flight projects with spending reversals (unusual)
- Or, significant restated guidance downward (material capex cuts)
- Or, Q2 2026 earnings reveal a sharp slowdown that limits the annual total

---

## Resolution Checklist

- [ ] After each 2026 quarter's earnings cycle: collect quarterly capex for MSFT/GOOG/AMZN/META
- [ ] Compute combined quarterly
- [ ] Test against $150B threshold
- [ ] If a quarter breaches $150B: resolution can happen early
- [ ] At Dec 31, 2026: final confirmation using all 4 quarters
- [ ] Update predictions/tracker.md
- [ ] Update analysis/hyperscaler-capex-2026-01.md
- [ ] Commit: "Resolve: HC-001 — {outcome summary}"

---

## Sources

- [Microsoft IR](https://www.microsoft.com/en-us/investor) — 10-Q, cash flow
- [Alphabet IR](https://abc.xyz/investor/) — 10-Q, cash flow
- [Amazon IR](https://ir.aboutamazon.com/) — 10-Q, cash flow
- [Meta IR](https://investor.atmeta.com/) — 10-Q, cash flow
- [scripts/fetch_hyperscaler_capex.py](/scripts/fetch_hyperscaler_capex.py) — automated pull of quarterly capex

---

*Prepared: 2026-04-24*
