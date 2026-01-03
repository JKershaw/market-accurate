# Agent Infrastructure

How AI agents autonomously maintain and grow Market Accurate.

---

## Overview

Market Accurate is designed to be maintained by AI agents with minimal human intervention. This document describes the infrastructure that enables autonomous operation.

### Design Principles

1. **Accuracy over activity** — Do nothing rather than do something wrong
2. **Transparency** — All actions logged in git history
3. **Immutability** — Predictions never modified after publication
4. **Self-improvement** — System learns and improves over time

---

## Architecture

```
.claude/
├── orchestrator.md      # Full decision protocol
├── bootstrap.md         # Session initialization prompts
├── settings.json        # Configuration
└── commands/
    └── orchestrate.md   # Quick-start slash command
```

### Components

| Component | Purpose | Used By |
|-----------|---------|---------|
| `orchestrator.md` | Complete protocol for autonomous operation | AI agents |
| `bootstrap.md` | Starting prompts for new sessions | Human operators |
| `settings.json` | Project configuration and sub-agent definitions | AI agents |
| `orchestrate.md` | Slash command `/orchestrate` | Claude Code |

---

## Session Protocol

Every autonomous session follows this sequence:

```
┌─────────────────────────────────────────────────────────────┐
│  1. ORIENT                                                  │
│     • Parse current date                                    │
│     • Load predictions/tracker.md                           │
│     • Load CLAUDE.md (current focus)                        │
│     • Check gh issue list (if available)                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  2. ASSESS                                                  │
│     • Predictions past due? → IMMEDIATE                     │
│     • Predictions within 30 days? → HIGH                    │
│     • Data > 1 quarter stale? → MEDIUM                      │
│     • Expansion capacity? → LOW                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  3. DECIDE                                                  │
│     Select highest priority actionable item                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  4. EXECUTE                                                 │
│     Spawn appropriate sub-agent                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  5. REPORT                                                  │
│     • Summarize actions taken                               │
│     • Commit with proper message format                     │
│     • Push changes                                          │
└─────────────────────────────────────────────────────────────┘
```

---

## Priority Matrix

| Priority | Condition | Example | Action |
|----------|-----------|---------|--------|
| **IMMEDIATE** | Prediction past verification date | AV-001 due Feb 2026, now Mar 2026 | Resolve immediately |
| **HIGH** | Prediction within 30 days | AV-001 due Feb 2026, now Jan 15 2026 | Prepare resolution data |
| **MEDIUM** | Data older than 1 quarter | Q3 data in Q1 next year | Refresh metrics |
| **MEDIUM** | Roadmap item ready | Next expansion topic | Create new analysis |
| **LOW** | Methodology improvement | Better process identified | Propose improvement |
| **LOW** | No urgent tasks | All current | Quality review |

---

## Sub-Agents

The orchestrator delegates specific tasks to specialized sub-agents:

### prediction-resolver

**Purpose:** Resolve predictions when verification dates arrive.

**Inputs:**
- Prediction ID
- Original prediction text
- Verification criteria

**Process:**
1. Research outcome using primary sources
2. Gather evidence with links
3. Determine CORRECT or INCORRECT
4. Update `predictions/tracker.md`
5. Update original analysis Track Record section
6. Recalculate cumulative statistics

**Outputs:**
- Resolved prediction entry
- Updated statistics
- Commit: `Resolve: {ID} - {outcome summary}`

**Quality Gates:**
- Evidence must be from primary sources (SEC filings, earnings transcripts)
- Outcome must be unambiguous
- Original prediction wording never modified

---

### data-refresher

**Purpose:** Keep analysis metrics current.

**Inputs:**
- Analysis file path
- Stale metrics identified

**Process:**
1. Research current values from primary sources
2. Update metrics in document
3. Add changelog entry with old → new values
4. Cite source with link

**Outputs:**
- Updated analysis file
- Changelog entry
- Commit: `Update: Refresh {metric} in {analysis}`

**Quality Gates:**
- Source must be cited
- Date must be included
- Old value preserved in changelog

---

### analyst

**Purpose:** Create new analysis documents per expansion roadmap.

**Inputs:**
- Topic from roadmap
- Template from CONTRIBUTING.md

**Process:**
1. Research topic using primary sources
2. Form falsifiable thesis
3. Develop specific, time-bound predictions
4. Draft analysis following template
5. Pass quality checklist
6. Add predictions to tracker.md
7. Update CLAUDE.md

**Outputs:**
- New analysis file: `analysis/{topic}-{YYYY-MM}.md`
- Updated tracker.md
- Updated CLAUDE.md
- Commit: `Add: {Topic} Analysis - {description}`

**Quality Gates:**
- [ ] Thesis is falsifiable
- [ ] All data has sources and dates
- [ ] Predictions are specific, time-bound, verifiable
- [ ] Counterarguments steelmanned
- [ ] Confidence levels stated
- [ ] Limitations acknowledged

---

### researcher

**Purpose:** Gather external data for any task.

**Inputs:**
- Research query
- Required data type

**Process:**
1. Search using source hierarchy:
   1. SEC filings, official disclosures
   2. Earnings transcripts
   3. Academic papers
   4. Industry surveys
   5. Quality journalism
   6. Social media (corroborate only)
2. Return structured findings

**Outputs:**
- Data point
- Source URL
- Date
- Confidence level

**Quality Gates:**
- Always cite sources
- Always include dates
- Flag low-confidence findings

---

### quality-reviewer

**Purpose:** Ensure content meets project standards.

**Inputs:**
- Document to review
- Checklist criteria

**Process:**
1. Check against content standards
2. Verify prediction format
3. Validate data claims
4. Report issues or approve

**Outputs:**
- Quality report
- Issues list (if any)
- Approval status

---

## Guardrails

### Never Do

| Rule | Reason |
|------|--------|
| ❌ Modify predictions after publication | Destroys track record integrity |
| ❌ Fabricate data or sources | Undermines accuracy mission |
| ❌ Resolve predictions without evidence | Premature/incorrect resolution |
| ❌ Hide incorrect predictions | Dishonest track record |
| ❌ Use hedge words | Prevents falsification |
| ❌ Skip source citations | Unverifiable claims |

### Always Do

| Rule | Reason |
|------|--------|
| ✅ Cite primary sources | Verifiability |
| ✅ Include dates on all data | Context and freshness |
| ✅ Show reasoning explicitly | Transparency |
| ✅ Acknowledge uncertainty | Epistemic honesty |
| ✅ Update track record honestly | Core mission |
| ✅ Use proper commit format | Traceability |

---

## Error Handling

### Research Failures

```
IF primary sources unavailable:
  1. Try secondary sources
  2. Flag low confidence
  3. Document the gap
  4. NEVER fabricate data
```

### Ambiguous Outcomes

```
IF prediction outcome unclear:
  1. Document both interpretations
  2. Present evidence for each
  3. Flag for human decision
  4. NEVER resolve unilaterally
```

### Quality Failures

```
IF content fails quality check:
  1. Identify specific failure
  2. Attempt correction
  3. Re-check
  4. Flag for review if still failing
```

---

## Commit Protocol

| Prefix | Use Case | Example |
|--------|----------|---------|
| `Add:` | New analysis or feature | `Add: Semiconductor Cycle Analysis` |
| `Update:` | Data refresh | `Update: Refresh Q4 capex figures` |
| `Resolve:` | Prediction outcome | `Resolve: AV-001 - NVIDIA growth was 47%` |
| `Fix:` | Error correction | `Fix: Correct MSFT capex (was $80B, is $88.7B)` |
| `Meta:` | Documentation/process | `Meta: Update orchestrator protocol` |

---

## Usage

### Starting an Autonomous Session

**Option 1: Slash Command**
```
/orchestrate
```

**Option 2: Bootstrap Prompt**

Copy the prompt from `.claude/bootstrap.md` and provide to a new Claude Code session.

**Option 3: Manual Invocation**

```
Read .claude/orchestrator.md and execute the Session Start Protocol.
Report current state and recommended priority action.
```

### Monitoring

Check session outputs for:
- Actions taken
- Predictions resolved
- Data refreshed
- Analyses created
- Issues encountered

All actions are logged in git commit history.

---

## Self-Improvement

After each session, the system should:

1. **REFLECT** — What worked? What didn't?
2. **PROPOSE** — Identify one improvement
3. **IMPLEMENT** — If low-risk, make the change
4. **DOCUMENT** — Log in methodology.md

This creates a continuous improvement loop.

---

## Integration Points

### With CLAUDE.md

The orchestrator reads CLAUDE.md to understand:
- Current focus areas
- Upcoming prediction dates
- Priority actions

### With predictions/tracker.md

The orchestrator reads and updates the tracker to:
- Identify due predictions
- Record resolutions
- Update statistics

### With CONTRIBUTING.md

The orchestrator reads the expansion roadmap to:
- Identify next analysis topics
- Follow templates and standards

---

## Extending the System

### Adding a New Sub-Agent

1. Define in `.claude/settings.json`:
```json
"new-agent": {
  "description": "What it does",
  "triggers": ["when_to_run"],
  "required_tools": ["Tool1", "Tool2"]
}
```

2. Add specification in `.claude/orchestrator.md`

3. Add prompt template in `.claude/bootstrap.md`

### Modifying Priority Logic

Edit the decision logic in `.claude/orchestrator.md`:
- Add new priority levels
- Modify trigger conditions
- Adjust thresholds

---

## Metrics

Track orchestrator effectiveness:

| Metric | Target | Measurement |
|--------|--------|-------------|
| Predictions resolved on time | 100% | Resolved ≤ verification date |
| Data freshness | < 1 quarter | Last update date |
| Quality gate pass rate | > 95% | Reviews passed / total |
| Commit format compliance | 100% | Proper prefix usage |

---

## Troubleshooting

### "gh command not available"

Skip GitHub issue checking. Proceed with predictions/data/expansion priorities.

### "Can't find primary sources"

Use secondary sources with low-confidence flag. Document the gap for future resolution.

### "Prediction outcome ambiguous"

Do not resolve. Document both interpretations. Flag for human decision.

### "Quality check keeps failing"

Review the specific failure. If systemic, propose methodology improvement.

---

*Market Accurate: Autonomous accuracy through structured orchestration.*
