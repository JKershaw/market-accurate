# Pre-Registration Framework

How Market Accurate commits to predictions before outcomes are known, to prevent after-the-fact rationalization.

---

## Why Pre-Registration Matters

A prediction track record only has epistemic value if predictions are:

1. **Public before resolution** — timestamped by git history, not an internal note
2. **Interpretable before resolution** — thresholds stated unambiguously
3. **Unmodifiable after publication** — original wording preserved
4. **Resolvable** — evidence sources identified before the fact

Without these, a track record becomes a post-hoc narrative where "correct" predictions are emphasized and "incorrect" ones are reinterpreted.

---

## The Five Commitments

Every Market Accurate prediction must satisfy these before merge:

### 1. Falsifiability

A prediction must specify a condition under which it would be judged wrong. "AI will be important" is not falsifiable. "NVIDIA datacenter revenue YoY growth <50% in Q4 FY26" is.

| Test | Acceptable | Unacceptable |
|------|-----------|--------------|
| Is there a clear threshold? | Yes | No |
| Is the metric publicly measurable? | Yes | No |
| Could a third party verify? | Yes | No |

### 2. Time-Boundedness

A resolution date. Not "by the end of the cycle" — a specific date or event window.

### 3. Source Specification

Where will the evidence come from? Named sources reduce cherry-picking at resolution time. If the source is "any published report," specify which publications qualify.

### 4. Threshold Unambiguity

If a prediction says "<50%", does 50.0% count as correct? State it. If it says "by Q3," does a July 1 outcome count? State it.

### 5. Prior Belief Disclosure

Each prediction should be accompanied by an ex-ante probability estimate. This enables Brier-score calibration assessment and makes the prediction's information value measurable.

---

## Pre-Registration Template

When adding a new prediction:

```markdown
### Prediction {ID}: {Descriptive Title}

**Claim:** {single-sentence falsifiable statement}

**Threshold:** {exact boundary condition, with tie-breaking}

**Verification date:** {specific calendar date, or "after X event"}

**Source(s):** {named publications, filings, or data providers}

**Ex-ante probability:** {percentage, as of publication}

**Edge cases considered:**
- {edge case 1 and how it resolves}
- {edge case 2 and how it resolves}

**What would prove this wrong:** {specific disconfirming evidence}
```

---

## The Resolution Prep Document

For each prediction, a resolution-prep document lives in `docs/prediction-prep/{ID}-prep.md`. This document is written **between prediction publication and resolution**, and contains:

- Baseline data as of publication
- Interim monitoring points
- Specific data-collection protocol
- Tie-breaker rules for edge cases
- Resolution checklist

The prep document can be updated. The prediction itself cannot.

### Why separate them?

If we allowed editing the prediction, we could drift the threshold in our favor. If we allowed no editing of the protocol, we could be blocked by a technicality (e.g., a data provider renames a series). Separating the two lets us make the protocol precise without moving the target.

**Rule:** The prep document can clarify ambiguity in the original prediction in ways consistent with the prediction's plain text and intent. If a clarification would change the outcome, escalate to a new prediction rather than modifying the old one.

---

## Immutability Protocol

### What Cannot Change After Publication

- Prediction claim text
- Stated threshold
- Stated verification date
- Stated ex-ante probability
- Stated source specification

### What Can Change

- Prep documents (with changelog)
- Verification tooling / scripts
- Cross-references to other analyses
- Clarifications that do not affect outcome interpretation

### Enforcement

Git history is the timestamp. Any commit that modifies a prediction's text in a published file must be reverted. Reviewers should check:

```bash
git log --follow predictions/tracker.md
git log --follow analysis/{topic}-{YYYY-MM}.md
```

Any diff that edits prediction rows (not status) is a violation.

---

## Resolution Protocol

When verification date arrives:

1. **Gather evidence** per the prep document's specified sources
2. **Apply threshold** as written — do not renegotiate
3. **Document verdict** in predictions/tracker.md with link to evidence
4. **Update analysis document** Track Record section
5. **Recalculate statistics** (accuracy, Brier score, calibration)
6. **Preserve original prediction text** unchanged
7. **Commit** with message `Resolve: {ID} — {outcome summary}`

### Tie-breaking defaults

If a prep document failed to specify a tie-breaker and the outcome lands on a boundary:

| Default | Rule |
|---------|------|
| Numerical thresholds | Strict inequality ("<" does not include equality) |
| "By {date}" | Outcome on that date counts |
| "In Q{N}" | First or last day of that calendar quarter counts |
| Qualitative judgement | Default to INCORRECT (avoid favorable defaults) |

The default-to-INCORRECT rule reflects that an ambiguous prediction is a bad prediction, and the cost should fall on the predictor.

---

## Calibration Expectations

Over a sufficient sample of predictions (target: n ≥ 30 resolved):

| Stated Confidence | Target Accuracy | Well-Calibrated Range |
|-------------------|-----------------|----------------------|
| 35–45% | 35–45% correct | Within 5pp |
| 50–60% | 50–60% correct | Within 5pp |
| 65–75% | 65–75% correct | Within 5pp |
| >75% | >75% correct | Within 5pp |

Systematic deviations indicate:

- **Accuracy > confidence:** Under-confident. Could make stronger claims.
- **Accuracy < confidence:** Over-confident. Common failure mode for thesis-driven analysts.

---

## Known Failure Modes to Resist

### 1. The "I was basically right" move

A prediction of "X by Y" resolves on date Z where X is 90% of the way there. This is INCORRECT, not "directionally correct." Directional-correctness claims are narrative. The threshold is the threshold.

### 2. Goalpost-shifting via source switching

If the prep document says "per IDC," and IDC doesn't publish in time, Gartner does not substitute. The prediction resolves INCONCLUSIVE or INCORRECT depending on the prep document.

### 3. Survivorship narrative

Highlighting correct predictions and de-emphasizing incorrect ones. The tracker's cumulative statistics counter this; analyses should cite track record honestly.

### 4. Ex-post probability updating

If a prediction stated 60% confidence and was wrong, do not rewrite history to say "of course it was more like 40%." The published probability stands.

### 5. Condition stacking

Long conditional chains ("if X and Y and Z then A") have low prior probability by construction. Single-claim predictions are preferable.

---

## When to Retire a Prediction

A prediction may be declared **INCONCLUSIVE** (not CORRECT or INCORRECT) only if:

- The specified data source no longer exists and no equivalent substitute is available
- A force majeure event makes the prediction impossible to evaluate
- The prediction was malformed (ambiguous) and reasonable interpretations yield opposite outcomes

INCONCLUSIVE resolutions do not count toward accuracy but DO count toward Brier score at 0.25 (midpoint), to discipline against writing vague predictions.

---

## Workflow Summary

```
┌─────────────────────┐
│ Draft prediction    │
│ (pre-merge)         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Review against 5    │  ← falsifiable, time-bound,
│ commitments         │    source-specified, threshold-clear,
└──────────┬──────────┘    prior-probability-stated
           │
           ▼
┌─────────────────────┐
│ Commit + push       │  ← git timestamp locks the prediction
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Write prep doc      │  ← baseline, protocol, edge cases
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Monitor (optional)  │  ← data pipeline runs, interim notes
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Resolution at date  │  ← apply threshold, document verdict
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Update tracker +    │  ← tracker.md, analysis track record,
│ statistics          │    cumulative stats, commit
└─────────────────────┘
```

---

*The goal is accurate information. Discipline in how we make and resolve predictions is how we demonstrate accuracy.*

---

*Last updated: 2026-04-18*
