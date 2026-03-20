---
uid: SOP-META-IRA-001
title: "IRA Grade-Norming: Multi-Rater System Quality Assessment"
version: "1.0"
status: active
effective_date: "2026-03-13"
owner: "@4444J99"
approver: "@4444J99"
review_cycle: quarterly
category: quality-assurance
tags: [ira, grade-norming, diagnostics, inter-rater-agreement, quality]
---

# SOP: IRA Grade-Norming

## 1. Purpose

Establish reliable system quality scores through multi-rater agreement for any ORGANVM organ or project. This SOP enables convergence on ground truth about system quality by comparing independent assessments from multiple perspectives (AI models and/or humans).

## 2. Scope

Any project that:
- Has a `system-grading-rubric.yaml` (or equivalent) defining weighted dimensions with scoring guides
- Has a diagnostic script that produces objective measurements as JSON
- Wants to assess quality through multi-rater comparison rather than single-perspective evaluation

**Out of scope:** Rater training, LLM fine-tuning, applicant-facing scoring rubrics.

## 3. Responsibilities

| Role | Responsibility |
|------|---------------|
| **Session lead** | Coordinates the IRA round, distributes prompts, collects ratings |
| **Raters** (3+ required) | Independently score each dimension using evidence and rubric guides |
| **Rubric owner** | Refines rubric when divergence persists; version-bumps after changes |

## 4. Prerequisites

- Python 3.11+ with PyYAML
- A grading rubric YAML with:
  - Weighted dimensions (must sum to 1.0)
  - Scoring guides with anchored descriptors (minimum at levels 1, 5, 10)
  - Evidence sources per dimension
  - IRA config (agreement method, consensus method, outlier threshold)
- A diagnostic script producing JSON: `{"rater_id": "...", "dimensions": {"dim_name": {"score": N, ...}}}`
- 3+ independent raters (AI models, human experts, or mix)
- A `ratings/` directory in the project root

## 5. Procedure

### Step 1 — Define Rubric

Create or verify `strategy/system-grading-rubric.yaml`:

```yaml
version: "1.0"
effective_date: "YYYY-MM-DD"
composite_method: weighted_sum
scale:
  min: 1.0
  max: 10.0
  precision: 1

dimensions:
  dimension_name:
    label: Human-Readable Label
    type: objective | subjective | mixed
    weight: 0.XX  # All weights must sum to 1.0
    description: >-
      What this dimension measures.
    scoring_guide:
      1: "Description of lowest quality"
      5: "Description of mid-range quality"
      10: "Description of highest quality"
    evidence_sources:
      - command: "script that measures this"
        measures: metric_name
    ira_config:
      agreement_method: icc
      consensus_method: median
      outlier_threshold: 1.5

ira:
  min_raters: 3
  max_raters: 7
  consensus:
    method: median
    outlier_iqr_factor: 1.5
    re_rate_threshold: 0.61
```

### Step 2 — Generate Objective Baseline

Run the diagnostic tool to produce automated measurements:

```bash
python scripts/diagnose.py --json --rater-id objective > ratings/objective.json
```

This scores all `type: objective` dimensions automatically.

### Step 3 — Generate Subjective Prompts

```bash
python scripts/diagnose.py --subjective-only
```

Distribute the generated prompts to each rater. Each prompt includes:
- Dimension name, description, and scoring guide
- Evidence excerpts from the codebase
- The scale (1.0-10.0) and what each anchor means

### Step 4 — Collect Independent Ratings

Each rater independently:
1. Reviews the rubric and evidence sources
2. Scores each subjective dimension (1.0-10.0, one decimal)
3. Provides: score, confidence level, strengths, weaknesses, evidence cited
4. Saves to `ratings/<rater-id>.json`

**Critical rules:**
- No discussion between raters before completing individual ratings
- Each rater session must be independent (fresh context for AI raters)
- All raters use the same rubric version

Rating JSON schema:
```json
{
  "rater_id": "rater-name",
  "timestamp": "ISO-8601",
  "rubric_version": "1.0",
  "dimensions": {
    "dimension_name": {
      "score": 7.5,
      "confidence": "high|medium|low",
      "evidence": "What evidence was considered",
      "strengths": ["..."],
      "weaknesses": ["..."]
    }
  }
}
```

### Step 5 — Compute IRA

```bash
# Basic report
python scripts/diagnose_ira.py ratings/*.json

# With consensus scores
python scripts/diagnose_ira.py ratings/*.json --consensus

# Machine-readable
python scripts/diagnose_ira.py ratings/*.json --consensus --json
```

### Step 6 — Evaluate Agreement

| ICC/Kappa Range | Interpretation | Action |
|----------------|----------------|--------|
| < 0.00 | Poor | Rubric needs fundamental revision |
| 0.00 - 0.20 | Slight | Sharpen scoring guides significantly |
| 0.21 - 0.40 | Fair | Add concrete evidence examples to anchors |
| 0.41 - 0.60 | Moderate | Minor rubric refinements, then re-rate |
| **0.61 - 0.80** | **Substantial** | **Acceptable — adopt consensus** |
| 0.81 - 1.00 | Almost Perfect | Excellent agreement |

**Target:** ICC >= 0.61 (substantial) for all dimensions.

If any dimension falls below 0.61:
1. Identify divergent raters (IQR outlier flags)
2. Compare which evidence raters weighted differently
3. Sharpen scoring guide anchors at levels 3, 5, 7
4. Re-rate that dimension only

### Step 7 — Apply Consensus

Median scores become the official system grade:

```bash
# Save consensus
python scripts/diagnose_ira.py ratings/*.json --consensus --json > ratings/consensus-YYYY-MM-DD.json

# Archive to history
mkdir -p signals/diagnostic-history
cp ratings/consensus-YYYY-MM-DD.json signals/diagnostic-history/
```

### Step 8 — Archive

After consensus is recorded:

```bash
mkdir -p ratings/archive/YYYY-QN
mv ratings/*.json ratings/archive/YYYY-QN/
# Keep consensus copy in signals/diagnostic-history/
```

## 6. Quality Checks

- [ ] All rater files parse as valid JSON
- [ ] All rater files cover the same dimension set
- [ ] ICC computed for every dimension
- [ ] No dimension below 0.61 ICC without documented reason
- [ ] Consensus scores saved to diagnostic history
- [ ] Rubric version matches across all rating files

## 7. Troubleshooting

| Issue | Resolution |
|-------|-----------|
| Rater file won't parse | Validate JSON: `python -m json.tool ratings/rater.json` |
| ICC returns NaN | Need 3+ raters with variance; 2 identical scores produce NaN |
| All raters score identically | Variance is zero — ICC undefined; this is actually perfect agreement |
| Dimension consistently divergent | Rubric anchor is ambiguous; add examples from the codebase |
| AI rater scores suspiciously high | Check if prompt included leading context; use fresh sessions |

## 8. Review Frequency

| Event | Frequency |
|-------|-----------|
| Full IRA round | Quarterly |
| Objective-only snapshot | Monthly |
| Post-major-change assessment | As needed |
| Rubric revision | After any round with ICC < 0.61 |

## Appendix A — Reference Implementation

The application-pipeline (`~/Workspace/4444J99/application-pipeline/`) is the reference implementation:

| Component | Path |
|-----------|------|
| Rubric | `strategy/system-grading-rubric.yaml` |
| Diagnostic tool | `scripts/diagnose.py` |
| IRA engine | `scripts/diagnose_ira.py` |
| System audit | `scripts/audit_system.py` |
| Rating files | `ratings/*.json` |
| Pipeline-specific SOP | `docs/sop--diagnostic-inter-rater-agreement.md` |

## Appendix B — Rating JSON Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["rater_id", "dimensions"],
  "properties": {
    "rater_id": {"type": "string"},
    "timestamp": {"type": "string", "format": "date-time"},
    "rubric_version": {"type": "string"},
    "dimensions": {
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "required": ["score"],
        "properties": {
          "score": {"type": "number", "minimum": 1.0, "maximum": 10.0},
          "confidence": {"enum": ["high", "medium", "low"]},
          "evidence": {"type": "string"},
          "strengths": {"type": "array", "items": {"type": "string"}},
          "weaknesses": {"type": "array", "items": {"type": "string"}}
        }
      }
    }
  }
}
```
