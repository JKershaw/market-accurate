# Prediction Resolution Prep: HC-002

## Prediction Details

| Field | Value |
|-------|-------|
| ID | HC-002 |
| Claim | At least one hyperscaler will reduce full-year 2026 capex guidance mid-year |
| Made | 2026-01-03 |
| Resolves | October 31, 2026 |
| Status | Pending — Resolution Prep |

---

## Threshold Interpretation

Resolution requires:
- **CORRECT:** During 2026, at least one of MSFT/GOOG/AMZN/META provides revised 2026 capex guidance that is lower (in midpoint or range) than previously stated guidance for that year
- **INCORRECT:** No hyperscaler lowers 2026 capex guidance during 2026

**Key distinction:** "Lower than previously stated guidance for 2026." Raising 2026 guidance in Q1 then lowering it in Q3 still counts as CORRECT — the comparison is between two 2026 guidance figures, not between 2026 and 2025.

**Stricter reading (also acceptable):** Lowered midpoint from most recent prior guidance.

**Recommended reading (less strict):** Any reduction from any prior 2026 guidance figure during 2026 counts. This avoids penalizing a hyperscaler for raising then slightly cutting back.

---

## Baseline: 2026 Guidance as of April 2026

| Company | 2026 Guidance (midpoint) | When Stated | Notes |
|---------|--------------------------|-------------|-------|
| MSFT | ~$94B (FY26); implied CY26 ~$120B | Jan 2026 (Q2 FY26 call) | "Slower pace" language |
| GOOG | $180B (range $175–185B) | Feb 4, 2026 (Q4 2025 call) | Roughly doubled vs 2025 |
| AMZN | ~$200B | Feb 2026 (Q4 2025 call) | +60% YoY |
| META | $125B (range $115–135B) | Jan 29, 2026 (Q4 2025 call) | +70% YoY midpoint |

For HC-002 to resolve CORRECT, one of these figures must be lowered during 2026.

---

## Interim Check (April 24, 2026)

Q1 2026 earnings cycle begins this week. Key signals to monitor:

### Alphabet (late April)
- Maintains $175–185B? Raises? Narrows?
- Commentary on data center delivery constraints
- Any mention of "reprioritizing," "adjusting," "reassessing"

### Microsoft (late April, Q3 FY26)
- FY26 capex has been stable at ~$94B
- More relevant: any FY27 (July 2026 onward) signal
- Separate question: does Microsoft provide CY26 capex framing?

### Meta (late April)
- Maintains $115–135B? Tightens range? Lowers?
- Reality Labs vs. AI infrastructure breakout

### Amazon (early May)
- Maintains ~$200B?
- AWS capex commentary
- "Routine capacity management" framing (Kevin Miller quote from April)

---

## Resolution Criteria by Signal Type

| Signal | Qualifies as CORRECT? |
|--------|----------------------|
| Explicit lowered range ("was $175–185B, now $170–180B") | YES |
| Narrowed to lower end ("now expect to be at low end of range") | YES |
| Qualitative lowering without specific figure ("spending will be lower than previously indicated") | YES if specifically about 2026 |
| Reduced investment in a subsidiary or segment | NO (aggregate capex is the measure) |
| Slowed pace with unchanged annual guidance | NO |
| Deferred capacity to 2027 but maintains 2026 total | NO — total is unchanged |
| Cancelled specific projects without updating total | Ambiguous — see below |

### Ambiguous case: Project cancellations without guidance update

If a hyperscaler cancels specific projects (e.g., Microsoft's 1.5GW freeze) but does not formally update annual 2026 guidance, this does not automatically resolve HC-002. The prediction is about *stated guidance* changes.

However: if analysts' consensus moves ≥5% lower based on disclosed cancellations, and the company confirms in an earnings call that "our 2026 capex expectations are below what we previously indicated," that qualitative statement would count.

---

## Data Collection Protocol

### Step 1: Collect guidance history

For each hyperscaler, maintain a table:

| Company | Event | Date | 2026 Guidance | Change vs. prior |
|---------|-------|------|---------------|------------------|
| MSFT | Q2 FY26 call | Jan 2026 | FY26 ~$94B | — |
| MSFT | Q3 FY26 call | Apr 2026 | TBD | TBD |
| MSFT | Q4 FY26 call | Jul 2026 | TBD | TBD |
| MSFT | Q1 FY27 call | Oct 2026 | TBD | TBD |
| GOOG | Q4 2025 call | Feb 4, 2026 | $175–185B | — |
| GOOG | Q1 2026 call | Apr 2026 | TBD | TBD |
| GOOG | Q2 2026 call | Jul 2026 | TBD | TBD |
| ... | ... | ... | ... | ... |

### Step 2: Detect lowering events

For each post-initial guidance update, compare midpoint and range to prior.

### Step 3: Classify

A lowering event is:
- **Hard:** Midpoint lowered by ≥5%
- **Soft:** Midpoint lowered by 0.1–5%
- **Qualitative:** Range unchanged but language explicitly indicates downward revision

Either type triggers CORRECT resolution.

---

## Edge Cases

| Case | Handling |
|------|----------|
| Company provides no explicit range, only "similar to 2025" → then updates to "lower than 2025" | CORRECT |
| Capital efficiency offsets maintain guidance despite physical cancellations | INCORRECT — guidance is unchanged |
| Merger / acquisition changes reporting perimeter | Compare like-for-like; document adjustment |
| Company withdraws guidance entirely | Not a reduction, but not an increase either — INCONCLUSIVE for this signal |

---

## Thesis Context

The January prep noted that the pattern of *raising* guidance may reverse. As of April 2026:
- Alphabet, Meta, and Amazon all *raised* 2026 guidance materially at Q4 2025 earnings
- Microsoft has been consistent at ~$94B FY26 with "slower pace" language
- Microsoft's 1.5GW project freeze is a physical action, not a guidance update

The probability of HC-002 resolving CORRECT now depends on:

1. Whether physical supply constraints (power, transformers) force guidance down later in 2026
2. Whether demand concerns emerge (unlikely given current trajectory)
3. Whether a hyperscaler consolidates or reprioritizes in response to competitive pressure

**Updated subjective probability of CORRECT:** ~40% (unchanged from January, but mechanism is different — supply-side rather than demand-side).

Leading candidates to lower guidance:
1. Microsoft (already showing pullback signals)
2. Amazon (lease pause signals)
3. Meta (balance-sheet sensitive, stock already punished for capex)
4. Google (least likely — most aggressive posture)

---

## Resolution Checklist

- [ ] After each Q1/Q2/Q3 2026 earnings cycle: update guidance table
- [ ] Identify any lowering events
- [ ] Classify (hard/soft/qualitative)
- [ ] If any qualifies: resolution can happen prior to Oct 31, 2026
- [ ] At Oct 31, 2026: final determination using full guidance history
- [ ] Update predictions/tracker.md
- [ ] Update analysis/hyperscaler-capex-2026-01.md
- [ ] Commit: "Resolve: HC-002 — {outcome summary}"

---

## Sources

- Company earnings calls and 10-Q filings (MSFT / GOOG / AMZN / META)
- [Seeking Alpha earnings transcripts](https://seekingalpha.com/earnings)
- TD Cowen, SemiAnalysis, UBS analyst reports for triangulation on physical buildout

---

*Prepared: 2026-04-24*
