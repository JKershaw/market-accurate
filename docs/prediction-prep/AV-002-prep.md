# Prediction Resolution Prep: AV-002

## Prediction Details

| Field | Value |
|-------|-------|
| ID | AV-002 |
| Claim | At least one of Microsoft, Google, Amazon uses moderating language regarding AI capex in Q1 2026 earnings |
| Made | 2026-01-03 |
| Resolves | May 2026 (after Q1 2026 earnings cycle) |
| Status | Pending - Resolution Prep |

---

## Q1 2026 Earnings Calendar

| Company | Period | Expected Date | Notes |
|---------|--------|--------------|-------|
| Alphabet | Q1 2026 calendar | Late April 2026 | Full-year 2026 capex guidance update |
| Microsoft | Q3 FY2026 | Late April 2026 | FY26 capex framing, FY27 early signals |
| Meta | Q1 2026 calendar | Late April 2026 | Full-year 2026 range update |
| Amazon | Q1 2026 calendar | Early May 2026 | Full-year 2026 range update |

---

## Resolution Criteria

Prediction is **CORRECT** if any of MSFT/GOOG/AMZN uses at least one of these signals during Q1 2026 earnings:

| Signal Type | Example Language | Interpretation |
|-------------|------------------|----------------|
| Rate moderation | "slower pace of growth," "moderating," "tempering" | Growth rate reduction |
| Efficiency pivot | "optimizing," "efficiency-focused," "disciplined allocation" | ROI prioritization |
| Absolute reduction | "rationalizing," "reducing," "reprioritizing" | Absolute cuts |
| Guidance pullback | Any lowered full-year capex range | Hard numerical moderation |

Prediction is **INCORRECT** if:
- All three companies reiterate or raise 2026 capex guidance with no moderation language
- Language remains aggressive ("accelerating," "expanding," "significant increase")

Note: Meta is excluded from AV-002 (but captured in AV-007). Its commentary is informational only.

---

## Baseline: Language as of Q3/Q4 2025 Earnings

From the Hyperscaler Capex Tracker (published 2026-01-03):

| Company | Q3/Q4 2025 Tone | Signals Present |
|---------|----------------|-----------------|
| Microsoft | Measured | **Yes** — Amy Hood used "slower pace" for FY26 |
| Amazon | Aggressive | None |
| Google | Aggressive | Raised guidance 3x in 2025 |
| Meta | Aggressive | "Notably larger" 2026 |

**Key observation:** Microsoft has already used qualifying language as of publication. If "slower pace" recurs or Microsoft quantifies it in Q3 FY26 earnings (April 2026), the prediction resolves CORRECT.

Stricter reading: Because the prediction is "in Q1 2026 earnings," the moderation language must appear in Q1 2026 calendar-quarter earnings calls (April–May 2026), not in prior guidance. Microsoft must restate or reinforce for the prediction to resolve CORRECT on a strict reading.

**Recommended interpretation:** Count Q1 2026 calendar-quarter earnings calls only. Pre-existing language does not count; it must appear in the specific earnings window.

---

## Data Collection Protocol

### Step 1: Gather transcripts

- Pull prepared-remarks and Q&A transcripts from each company's IR site
- Cross-reference with Seeking Alpha or The Motley Fool transcript archives
- Pull press releases, 8-K filings, and CFO letters

### Step 2: Keyword scan

Search for these exact phrases and near-variants:

```
"slower pace"
"moderating" | "moderate" (in capex context)
"optimizing" | "optimization"
"disciplined" | "discipline"
"efficiency-focused" | "efficient deployment"
"rationalizing" | "right-sizing"
"more measured"
"prudent" (in capex context)
"returns-focused" | "ROI-focused"
"reducing" | "lowering" (applied to capex/guidance)
```

### Step 3: Numerical check

| Check | What to Record |
|-------|---------------|
| Guidance range change | New range vs. Q4 2025 stated range |
| Direction | Raised / Reiterated / Lowered |
| Magnitude | Dollar change if numerical |
| FY27 signal | Any forward commentary on 2027 capex trajectory |

### Step 4: Context weighting

Not all "moderating" language is meaningful. Require:
- Stated in prepared remarks OR analyst Q&A
- Referring to AI infrastructure or capex specifically (not general cost discipline)
- From CEO, CFO, or head of cloud/infrastructure

---

## Risk: False Positives

Words like "disciplined" are routinely used by CFOs as boilerplate. Required context:
- Must be applied specifically to AI or infrastructure capex
- Must represent a **change in tone** vs. Q4 2025 commentary
- A single use of "disciplined" without directional context does not qualify

---

## Resolution Checklist

When all Q1 2026 earnings released (~May 7, 2026):

- [ ] Collect transcripts (MSFT, GOOG, AMZN, META for context)
- [ ] Run keyword scan on each
- [ ] Record capex guidance changes vs. Q4 2025
- [ ] Classify each company: aggressive / neutral / moderating
- [ ] Determine: CORRECT (≥1 of MSFT/GOOG/AMZN moderating) or INCORRECT
- [ ] Update predictions/tracker.md
- [ ] Update analysis/hyperscaler-capex-2026-01.md
- [ ] Update analysis/ai-valuation-2026-01.md Track Record
- [ ] Commit: "Resolve: AV-002 - {outcome summary}"

---

## Sources

- [Microsoft IR](https://www.microsoft.com/en-us/investor)
- [Alphabet IR](https://abc.xyz/investor/)
- [Amazon IR](https://ir.aboutamazon.com/)
- [Meta IR](https://investor.atmeta.com/)
- [Hyperscaler Capex Tracker](/analysis/hyperscaler-capex-2026-01.md)

---

*Prepared: 2026-04-18*
