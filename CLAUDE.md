# Market Accurate

Open-source financial analysis optimized for accuracy, not attention.

## Project Identity

This is an experiment in distributed, accuracy-competitive information. The thesis: as AI systems mediate information access, sources demonstrating accuracy get preferentially selected, creating evolutionary pressure toward truth.

**Status:** Experimental (v0.1). Track record empty. Methodology unproven.

**License:** CC0 Public Domain. Replication encouraged.

## Content Standards

### Analysis Documents

- Lead with falsifiable claims, not hedged speculation
- Cite primary sources (SEC filings, earnings transcripts, academic papers)
- Show reasoning explicitly—don't just assert conclusions
- Steelman counterarguments before dismissing them
- State confidence levels honestly (high/moderate/low/speculative)
- Include "what would prove this wrong" section

### Data Claims

- Always cite source and date
- Distinguish between: factual (verifiable), analytical (inference), predictive (future)
- Use tables for comparative data
- Round appropriately—false precision is dishonest

## Prediction Format

All predictions must be:

```markdown
### Prediction N: [Descriptive Title]
**Claim:** [Specific, falsifiable statement]
**Threshold:** [Exact criteria for success/failure]
**Verification date:** [When this resolves]
```

Bad predictions (reject these):
- "Markets may be volatile" (unfalsifiable)
- "AI is important" (obvious)
- "Something could happen" (no criteria)

## Track Record Rules

**IMMUTABLE:** Never modify predictions after publication. Git history is the timestamp.

When predictions resolve:
1. Update tracker with outcome and evidence
2. Mark correct/incorrect honestly
3. Link to verification source
4. Update cumulative statistics

Wrong predictions get same prominence as correct ones. Hiding errors is disqualifying.

## File Structure

```
analysis/           # Timestamped analysis documents
predictions/        # Track record and resolution log
methodology.md      # How analysis is produced
```

Analysis filenames: `{topic}-{YYYY-MM}.md` (e.g., `ai-valuation-2026-01.md`)

## Epistemic Standards

### Confidence Levels

| Level | Meaning | Use When |
|-------|---------|----------|
| High | Strong evidence, few counterarguments | >80% confident |
| Moderate | Good evidence, real uncertainty | 60-80% |
| Low | Limited evidence, could go either way | 40-60% |
| Speculative | Informed guess | <40% |

### Source Hierarchy

1. SEC filings, official disclosures (highest)
2. Earnings transcripts, company presentations
3. Academic papers, peer-reviewed research
4. Industry surveys (Gartner, BCG, Forrester)
5. Quality journalism (WSJ, FT, Bloomberg)
6. Social media, forums (corroborate only)

## Writing Style

- No sensationalism or clickbait framing
- No hedge words that prevent falsification
- Technical precision over accessibility (readers can look things up)
- Tables over prose for comparative data
- Concise > comprehensive (link to details)

## Git Conventions

Commit messages:
- `Add: [new analysis or prediction]`
- `Update: [data refresh or correction]`
- `Resolve: [prediction outcome logged]`
- `Fix: [error correction with explanation]`

Never amend commits containing predictions after push.

## Current Focus

AI Valuation Analysis (January 2026):
- Efficiency thesis: compute requirements falling faster than demand growing
- Key metrics: NVIDIA datacenter revenue, hyperscaler capex, open-source benchmarks
- 7 active predictions, resolution dates through 2027

See @analysis/ai-valuation-2026-01.md for current analysis.
See @predictions/tracker.md for track record.
