# Contributing to Market Accurate

How to grow and improve this project—for humans and AI agents.

---

## Quick Start for AI Agents

If you're an AI agent working on this project:

**Option 1: Use the Orchestrator**
```
/orchestrate
```
Or read `.claude/orchestrator.md` and follow the Session Start Protocol.

**Option 2: Manual Priority Check**
1. **Open issues** → `gh issue list` — prioritized work items
2. **Pending predictions** → `predictions/tracker.md` — check if any have resolved
3. **Data freshness** → analysis files have dates; refresh if stale
4. **Expansion opportunities** → see Roadmap section below

[Full agent infrastructure documentation →](docs/agent-infrastructure.md)

---

## Adding New Analysis

### 1. Create the file

```
analysis/{topic}-{YYYY-MM}.md
```

### 2. Use this template

```markdown
# MARKET ACCURATE
## {Topic} Analysis
### {Month} {Day}, {Year}

---

> **Disclaimer**
>
> This is **experimental analysis**, not financial advice. The author has **no positions**
> in securities discussed. Track record is **empty/X%**—see predictions/tracker.md.
> This represents one analytical perspective; it may be wrong. Do your own research.
>
> **Version:** 0.1

---

# Executive Summary

[2-3 paragraphs: core thesis, key findings, assessment]

---

# [Main Thesis Section]

## Definition

> [One-paragraph formal statement of the thesis]

## Evidence

### 1. [First Evidence Category]

[Data, sources, analysis]

### 2. [Second Evidence Category]

[Data, sources, analysis]

---

# Predictions

[Specific, time-bound, verifiable predictions following format in CLAUDE.md]

---

# Track Record

[Link to predictions/tracker.md]

---

# Methodology

[How this analysis was produced, sources used, limitations]

---

# Replication

[CC0 license notice, how to fork/improve]
```

### 3. Add predictions to tracker

Update `predictions/tracker.md` with new predictions.

### 4. Commit with clear message

```bash
git add analysis/{topic}-{YYYY-MM}.md predictions/tracker.md
git commit -m "Add: {Topic} Analysis - {brief description}"
```

---

## Resolving Predictions

When a prediction's verification date arrives:

### 1. Research the outcome

- Check primary sources (SEC filings, earnings reports, official data)
- Document evidence with links

### 2. Update tracker

In `predictions/tracker.md`, move from Active to Resolved:

```markdown
| ID | Prediction | Made | Resolved | Outcome | Correct? |
|----|-----------|------|----------|---------|----------|
| XX-001 | [prediction text] | 2026-01-03 | 2026-06-15 | [what happened] | Yes/No |
```

### 3. Update statistics

Recalculate accuracy percentage.

### 4. Update analysis document

Add outcome to the Track Record section of the original analysis.

### 5. Commit

```bash
git commit -m "Resolve: {Prediction ID} - {outcome summary}"
```

---

## Refreshing Data

Analysis documents contain dated metrics. To refresh:

### 1. Identify stale data

Look for metrics older than 1 quarter in active analyses.

### 2. Research current values

Use source hierarchy from CLAUDE.md (SEC filings > earnings > surveys > journalism).

### 3. Update with changelog entry

Add to document's changelog:

```markdown
| Date | Change |
|------|--------|
| {today} | Updated {metric} from {old} to {new} (source: {link}) |
```

### 4. Commit

```bash
git commit -m "Update: Refresh {metric} in {analysis}"
```

---

## Expansion Roadmap

### Near-term additions (same methodology, adjacent topics)

1. ⬜ **Semiconductor cycle analysis** — historical patterns, current position
2. ✅ **Hyperscaler capex tracking** — quarterly updates on MSFT/GOOG/AMZN/META spend *(completed 2026-01-03)*
3. ⬜ **Open-source model benchmark tracking** — systematic comparison updates
4. ⬜ **Enterprise AI adoption metrics** — survey aggregation

### Medium-term expansions (new domains)

1. **Energy/climate** — similar efficiency thesis may apply to renewables
2. **Biotech** — drug development cost curves, approval rates
3. **Real estate** — commercial real estate valuation vs. remote work trends

### Methodology improvements

1. **Automated data pipelines** — scripts to fetch and update key metrics
2. **Prediction scoring refinements** — Brier scores, calibration tracking
3. **Comparison benchmarks** — track accuracy vs. analyst consensus

---

## Quality Checklist

Before committing new analysis:

- [ ] Thesis is falsifiable (can be proven wrong)
- [ ] All data claims have sources and dates
- [ ] Predictions are specific, time-bound, verifiable
- [ ] Counterarguments are steelmanned
- [ ] Confidence levels are stated
- [ ] Limitations are acknowledged
- [ ] Disclaimer is present
- [ ] Added to predictions/tracker.md

---

## Using GitHub Issues

Create issues for:

- **New analysis ideas** — label: `analysis`
- **Data refresh needed** — label: `data`
- **Prediction resolution due** — label: `prediction`
- **Methodology improvements** — label: `meta`

AI agents should check `gh issue list` for prioritized work.

---

## Commit Message Convention

```
Add: [new analysis or feature]
Update: [data refresh or improvement]
Resolve: [prediction outcome]
Fix: [error correction]
Meta: [documentation, structure, process]
```

---

*The goal is accurate information. Better analysis should win.*
