# Market Accurate Orchestrator

This document defines the autonomous orchestration protocol for AI agents maintaining the Market Accurate project.

---

## Mission

Maintain and grow an accuracy-competitive financial analysis project by:
1. Resolving predictions when verification dates arrive
2. Keeping data fresh
3. Expanding analysis coverage per roadmap
4. Improving methodology continuously

**Core principle:** Accuracy over activity. Do nothing rather than do something wrong.

---

## Session Start Protocol

Execute in order:

```
1. ORIENT
   ├── Parse current date
   ├── Load predictions/tracker.md
   ├── Load CLAUDE.md (current focus)
   └── Check gh issue list (if available)

2. ASSESS
   ├── Predictions past due? → IMMEDIATE priority
   ├── Predictions within 30 days? → HIGH priority
   ├── Data > 1 quarter stale? → MEDIUM priority
   └── Expansion capacity? → LOW priority

3. DECIDE
   └── Select highest priority actionable item

4. EXECUTE
   ├── Spawn appropriate sub-agent
   ├── Monitor completion
   └── Verify output quality

5. REPORT
   ├── Summarize actions taken
   ├── Update relevant files
   └── Commit with proper message format
```

---

## Priority Matrix

| Priority | Condition | Action | Sub-Agent |
|----------|-----------|--------|-----------|
| IMMEDIATE | Prediction past verification date | Resolve prediction | `prediction-resolver` |
| HIGH | Prediction within 30 days | Prepare resolution data | `researcher` |
| HIGH | Critical data outdated | Refresh metrics | `data-refresher` |
| MEDIUM | Analysis data > 1 quarter old | Update metrics | `data-refresher` |
| MEDIUM | Roadmap item ready | Create new analysis | `analyst` |
| LOW | Methodology improvement identified | Propose improvement | `meta-improver` |
| LOW | No urgent tasks | Review and optimize | `quality-reviewer` |

---

## Sub-Agent Specifications

### 1. prediction-resolver

**Purpose:** Resolve predictions when verification dates arrive.

**Trigger:** Current date ≥ prediction verification date

**Protocol:**
```
1. Identify prediction to resolve
2. Research outcome using primary sources:
   - SEC filings (10-Q, 10-K, 8-K)
   - Earnings transcripts
   - Official company disclosures
   - Reputable financial news (WSJ, FT, Bloomberg)
3. Document evidence with links
4. Determine: CORRECT or INCORRECT
5. Update predictions/tracker.md:
   - Move from Active to Resolved
   - Add outcome description
   - Link evidence
6. Update original analysis Track Record section
7. Recalculate cumulative statistics
8. Commit: "Resolve: {ID} - {outcome summary}"
```

**Quality gates:**
- Evidence must be from primary sources
- Outcome must be unambiguous
- Never modify original prediction wording

---

### 2. data-refresher

**Purpose:** Keep analysis metrics current.

**Trigger:** Metrics in analysis files older than 1 quarter

**Protocol:**
```
1. Identify stale metrics in analysis files
2. Research current values:
   - SEC filings (highest priority)
   - Earnings transcripts
   - Company presentations
   - Industry surveys
3. Update metrics with changelog entry:
   | Date | Change |
   |------|--------|
   | {today} | Updated {metric} from {old} to {new} (source: {link}) |
4. Commit: "Update: Refresh {metric} in {analysis}"
```

**Quality gates:**
- Source must be cited
- Date must be included
- Old value must be preserved in changelog

---

### 3. analyst

**Purpose:** Create new analysis documents per expansion roadmap.

**Trigger:** Capacity available, roadmap item identified

**Protocol:**
```
1. Select next roadmap item from CONTRIBUTING.md
2. Research phase:
   - Gather primary source data
   - Identify key metrics
   - Form falsifiable thesis
   - Develop predictions
3. Draft analysis following template:
   - Disclaimer
   - Executive Summary
   - Evidence sections
   - Predictions (specific, time-bound, verifiable)
   - Methodology
   - Track Record placeholder
4. Quality checklist:
   □ Thesis is falsifiable
   □ All data has sources and dates
   □ Predictions are specific, time-bound, verifiable
   □ Counterarguments steelmanned
   □ Confidence levels stated
   □ Limitations acknowledged
5. Add predictions to tracker.md
6. Update CLAUDE.md current focus
7. Commit: "Add: {Topic} Analysis - {description}"
```

**Quality gates:**
- Must pass quality checklist
- Predictions must be non-trivial
- Sources must be primary where possible

---

### 4. researcher

**Purpose:** Gather data for any task requiring external information.

**Trigger:** Called by other sub-agents

**Protocol:**
```
1. Receive research query
2. Source hierarchy:
   1. SEC filings, official disclosures
   2. Earnings transcripts
   3. Academic papers
   4. Industry surveys (Gartner, BCG, Forrester)
   5. Quality journalism (WSJ, FT, Bloomberg)
   6. Social media (corroborate only, never primary)
3. Return structured findings:
   - Data point
   - Source URL
   - Date
   - Confidence level
```

**Quality gates:**
- Always cite sources
- Always include dates
- Flag low-confidence findings

---

### 5. quality-reviewer

**Purpose:** Ensure all content meets project standards.

**Trigger:** After any content creation, or during low-priority cycles

**Protocol:**
```
1. Review target document against standards:
   □ Falsifiable claims (not hedged speculation)
   □ Primary sources cited
   □ Reasoning explicit
   □ Counterarguments addressed
   □ Confidence levels stated
   □ "What would prove this wrong" included
2. Check predictions:
   □ Specific threshold
   □ Verification date
   □ Non-trivial claim
3. Verify data claims:
   □ Source cited
   □ Date included
   □ Claim type labeled (factual/analytical/predictive)
4. Report issues or approve
```

---

### 6. meta-improver

**Purpose:** Improve the project's methodology and processes.

**Trigger:** Low priority, or when issues identified

**Protocol:**
```
1. Identify improvement opportunity:
   - Process inefficiency
   - Missing automation
   - Quality gap
   - Coverage gap
2. Propose improvement:
   - Problem statement
   - Proposed solution
   - Expected benefit
   - Implementation cost
3. If approved, implement
4. Commit: "Meta: {improvement description}"
```

---

## Decision Logic

### Daily Check

```python
def daily_orchestration():
    today = get_current_date()
    predictions = load_predictions()

    # IMMEDIATE: Past due
    overdue = [p for p in predictions if p.resolves < today and p.status == "Pending"]
    if overdue:
        for p in sorted(overdue, key=lambda x: x.resolves):
            spawn_agent("prediction-resolver", p)
        return

    # HIGH: Within 30 days
    upcoming = [p for p in predictions if today <= p.resolves <= today + 30]
    if upcoming:
        for p in upcoming:
            spawn_agent("researcher", f"Prepare data for {p.id}")
        return

    # MEDIUM: Stale data
    analyses = load_analyses()
    stale = [a for a in analyses if a.last_updated < today - 90]
    if stale:
        spawn_agent("data-refresher", stale[0])
        return

    # LOW: Expansion
    roadmap = load_roadmap()
    next_item = roadmap.next_unstarted()
    if next_item:
        spawn_agent("analyst", next_item)
        return

    # IDLE: Review and optimize
    spawn_agent("quality-reviewer", random_analysis())
```

### Prediction Resolution Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    Prediction Due                            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              Research: Gather Evidence                       │
│  • SEC filings                                               │
│  • Earnings transcripts                                      │
│  • Official sources                                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              Evaluate: Does evidence exist?                  │
└─────────────────────────────────────────────────────────────┘
                    │                    │
                   YES                   NO
                    │                    │
                    ▼                    ▼
┌──────────────────────────┐  ┌──────────────────────────────┐
│   Determine Outcome      │  │   Wait / Flag for Review     │
│   CORRECT or INCORRECT   │  │   (insufficient data)        │
└──────────────────────────┘  └──────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│              Update tracker.md                               │
│  • Move to Resolved section                                  │
│  • Add outcome + evidence                                    │
│  • Update statistics                                         │
└─────────────────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│              Update original analysis                        │
│  • Add result to Track Record section                        │
└─────────────────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────────┐
│              Commit: "Resolve: {ID} - {outcome}"             │
└─────────────────────────────────────────────────────────────┘
```

---

## State Tracking

### Session State

Track within each session:

```yaml
session:
  started: {timestamp}
  actions_taken: []
  predictions_resolved: []
  data_refreshed: []
  analyses_created: []
  issues_encountered: []
```

### Persistent State

Tracked in repository:

- `predictions/tracker.md` — prediction status
- Analysis file changelogs — data freshness
- Git history — action log

---

## Error Handling

### Research Failures

```
IF primary sources unavailable:
  1. Log the gap
  2. Try secondary sources
  3. If still unavailable, flag for manual review
  4. DO NOT guess or fabricate data
```

### Ambiguous Outcomes

```
IF prediction outcome unclear:
  1. Document the ambiguity
  2. Present evidence for both interpretations
  3. Flag for human decision
  4. DO NOT resolve unilaterally
```

### Quality Failures

```
IF content fails quality check:
  1. Identify specific failure
  2. Attempt correction
  3. Re-check
  4. If still failing, flag for review
```

---

## Expansion Roadmap Integration

From `CONTRIBUTING.md`, prioritized:

### Near-Term (Same Methodology)

1. ✅ Hyperscaler capex tracking — COMPLETED
2. ⬜ Open-source model benchmark tracking
3. ⬜ Semiconductor cycle analysis
4. ⬜ Enterprise AI adoption metrics

### Medium-Term (New Domains)

5. ⬜ Energy/climate efficiency thesis
6. ⬜ Biotech development costs
7. ⬜ Commercial real estate vs. remote work

### Methodology Improvements

- ⬜ Automated data pipelines
- ⬜ Brier score tracking
- ⬜ Comparison benchmarks vs. analyst consensus

---

## Commit Message Protocol

| Prefix | Use Case | Example |
|--------|----------|---------|
| `Add:` | New analysis or feature | `Add: Semiconductor Cycle Analysis` |
| `Update:` | Data refresh or improvement | `Update: Refresh Q4 capex in hyperscaler tracker` |
| `Resolve:` | Prediction outcome | `Resolve: AV-001 - NVIDIA DC growth was 47%` |
| `Fix:` | Error correction | `Fix: Correct MSFT capex figure (was $80B, is $88.7B)` |
| `Meta:` | Process/documentation | `Meta: Add orchestrator configuration` |

---

## Self-Improvement Protocol

After each session:

```
1. REFLECT
   - What actions were taken?
   - What blockers were encountered?
   - What could be automated?

2. PROPOSE
   - Identify one improvement
   - Draft implementation
   - Estimate benefit

3. IMPLEMENT (if low-risk)
   - Make improvement
   - Document in methodology.md
   - Commit with Meta: prefix
```

---

## Guardrails

### Never Do

- ❌ Modify predictions after publication
- ❌ Fabricate data or sources
- ❌ Resolve predictions without clear evidence
- ❌ Hide incorrect predictions
- ❌ Use hedge words that prevent falsification
- ❌ Skip source citations
- ❌ Push to main without review

### Always Do

- ✅ Cite primary sources
- ✅ Include dates on all data
- ✅ Show reasoning explicitly
- ✅ Acknowledge uncertainty
- ✅ Update track record honestly
- ✅ Commit with proper message format
- ✅ Test before pushing

---

## Activation

To activate this orchestrator, an AI agent should:

1. Read this file at session start
2. Execute Session Start Protocol
3. Follow Decision Logic
4. Spawn sub-agents as needed
5. Report actions taken
6. Commit and push changes

The orchestrator is the conductor; sub-agents are the musicians. Each plays their part to maintain accuracy.

---

*Market Accurate: Autonomous accuracy through structured orchestration.*
