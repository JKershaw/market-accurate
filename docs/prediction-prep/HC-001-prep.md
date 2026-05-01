# Prediction Resolution Prep: HC-001

## Prediction Details

| Field | Value |
|-------|-------|
| ID | HC-001 |
| Claim | Combined Big 4 (MSFT + GOOG + AMZN + META) quarterly capex will peak below $150 billion in any single quarter of 2026 |
| Made | 2026-01-03 |
| Resolves | December 31, 2026 |
| Status | Pending - Resolution Prep |

---

## Resolution Criteria

Prediction resolves **CORRECT** if:

- For every quarter Q1 2026, Q2 2026, Q3 2026, and Q4 2026, the combined capex of MSFT + GOOG + AMZN + META is < $150B in that quarter.

Prediction resolves **INCORRECT** if:

- Any single quarter in 2026 has combined Big 4 capex ≥ $150B.

---

## Measurement Conventions

| Detail | Specification |
|--------|---------------|
| Reporting basis | GAAP capex from cash flow statement (purchases of property and equipment) |
| Microsoft fiscal alignment | Microsoft's fiscal year ends June; for HC-001, use *calendar* quarter capex per 10-Q geographic disclosure or alternative reconciliation |
| Currency | USD |
| Source | 10-Q filings (Form 10-Q, cash flow statement) |
| Adjustments | Include finance leases for capacity (per company practice if disclosed); exclude pure office build-out where cleanly separable |
| Foreign exposure | All four are USD-reporters; no FX adjustment needed |

**Microsoft fiscal-quarter mapping:**

| Microsoft fiscal quarter | Calendar period |
|--------------------------|-----------------|
| Q3 FY26 | Jan–Mar 2026 (= Q1 cal 2026) |
| Q4 FY26 | Apr–Jun 2026 (= Q2 cal 2026) |
| Q1 FY27 | Jul–Sep 2026 (= Q3 cal 2026) |
| Q2 FY27 | Oct–Dec 2026 (= Q4 cal 2026) |

So Microsoft's calendar-2026 capex spans two fiscal years. Sum the four fiscal-quarter capex figures that fall within calendar 2026.

---

## Baseline Data

From the Hyperscaler Capex Tracker (Apr 2026 update):

| Company | Q3 2025 Capex | 2026 Full-Year Guidance | Implied Quarterly Avg |
|---------|--------------|------------------------|-----------------------|
| Amazon | $35.1B | ~$200B | ~$50B |
| Alphabet | ~$24B | $175–185B | ~$45B |
| Microsoft | ~$22B | ~$94B (FY26 framing); FY27 likely much higher | ~$23–35B |
| Meta | ~$20B | $115–135B | ~$29–34B |
| **Combined** | **~$101B** | **~$625B (midpoint)** | **~$155B** |

**The implied average quarterly figure is already above the $150B threshold.** This is a major shift from the Jan 2026 baseline of ~$100B/quarter.

---

## Interim Monitoring Points

| Quarter | Period | MSFT | GOOG | AMZN | META | Combined | vs $150B |
|---------|--------|------|------|------|------|----------|----------|
| Q1 2026 | Jan–Mar | | | | | | |
| Q2 2026 | Apr–Jun | | | | | | |
| Q3 2026 | Jul–Sep | | | | | | |
| Q4 2026 | Oct–Dec | | | | | | |

The first quarter (Q1 2026) reports in late April / early May 2026. Initial coverage suggests strong sequential acceleration consistent with stated FY26 guidance. **A single >$150B quarter resolves the prediction INCORRECT.**

---

## Rationale Snapshot

From January 2026:

- Q3 2025 combined Big 4 was ~$113B
- Trajectory implied ~$200B Q3 2026 if 75% YoY growth held
- Thesis: ROI gap forces deceleration → quarters cap below $150B
- This was a **bearish/contrarian** prediction; consensus already implied >$150B quarters

From April 2026:

- 2026 full-year guidance came in at ~$625B combined Big 4 (midpoint)
- Implied quarterly average: ~$155B
- Even with H1 < H2 cadence (typical), Q3/Q4 quarters easily clear $150B
- Supply-constraint story (delays/cancellations) reduces *delivered* capex but does not reduce *recognized* capex 1-for-1 because most spend is on already-ordered equipment

**Updated probability of CORRECT: dropped from ~50% (Jan) to ~20% (Apr).**

---

## Key Risks to Prediction

### Risks favoring CORRECT (no quarter exceeds $150B)

- All four companies materially miss their own 2026 guidance (>15% shortfall)
- Supply-constraint story binds harder than expected, capex slips into 2027
- One or more hyperscaler announces a strategic capex cut mid-2026
- Meta or AMZN delays a planned mega-project (1.5GW+) into 2027
- Currency or accounting reclassifications shift recognition

### Risks favoring INCORRECT (any quarter ≥ $150B)

- Big 4 deliver against $625B midpoint guidance — implies one or more quarters at $160B+
- Q3/Q4 typically heavier capex quarters (year-end installs); a $170B+ quarter is plausible
- Stargate-related accounting flowing through one of the Big 4
- M&A or AI-acquisition closing increases recognized capex
- Strong FX or repatriation effects

---

## Likelihood Assessment

| Scenario | Probability | Outcome |
|----------|-------------|---------|
| All four quarters $130–145B | 10% | CORRECT |
| All four quarters $145–149B (squeeze under threshold) | 5% | CORRECT |
| Q1 2026 < $150B but Q3/Q4 ≥ $150B | 50% | INCORRECT |
| Multiple quarters > $150B | 30% | INCORRECT |
| Hyperscaler capex *cut* mid-year, all quarters drop below | 5% | CORRECT |

**Subjective ex-ante probability of CORRECT (April 2026 update): ~20%**

The base rate strongly favors INCORRECT given current guidance. The prediction now requires either a major guidance cut or a substantial supply-constraint binding event.

---

## Data Sources

| Source | Usage |
|--------|-------|
| SEC EDGAR 10-Q filings | Primary capex data |
| Company IR earnings releases | First-look capex |
| Microsoft fiscal-to-calendar mapping | Calculator (build) |
| Bloomberg / FactSet | Cross-verification |

The `scripts/fetch_hyperscaler_capex.py` script supports per-company fetching; aggregation logic can be added.

---

## Sub-question to monitor: per-company quarterly breakdown

Watch for one company having an outsized quarter that pulls the combined figure above $150B even when the others are normal:

| Company | Likely peak quarter (2026) | Estimated quarterly peak |
|---------|----------------------------|--------------------------|
| Amazon | Q3 or Q4 | $55–60B |
| Alphabet | Q4 | $50–55B |
| Microsoft | Q4 (= Q2 FY27) | $30–40B |
| Meta | Q4 | $35–40B |
| **Combined Q4 2026** | — | **$170–195B** |

If these projections are even directionally correct, Q4 2026 alone resolves the prediction INCORRECT.

---

## Resolution Checklist

After Q4 2026 earnings (~early February 2027):

- [ ] Pull Q1, Q2, Q3, Q4 2026 capex from 10-Q/8-K for all four companies
- [ ] Reconcile Microsoft's fiscal-quarter capex to calendar 2026
- [ ] Sum quarterly figures
- [ ] Identify the highest single quarter
- [ ] Determine: CORRECT (max < $150B) or INCORRECT (max ≥ $150B)
- [ ] Document with linked filings
- [ ] Update predictions/tracker.md
- [ ] Update analysis/hyperscaler-capex-2026-01.md Track Record
- [ ] Commit: "Resolve: HC-001 — peak quarter ${X}B, outcome"

---

## Sources

- [Microsoft IR](https://www.microsoft.com/en-us/investor)
- [Alphabet IR](https://abc.xyz/investor/)
- [Amazon IR](https://ir.aboutamazon.com/)
- [Meta IR](https://investor.atmeta.com/)
- [Hyperscaler Capex Tracker](/analysis/hyperscaler-capex-2026-01.md)
- [SEC EDGAR](https://www.sec.gov/edgar)

---

*Prepared: 2026-05-01*
