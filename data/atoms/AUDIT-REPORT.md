# Prompt & Pipeline Data Audit
**Generated**: 2026-03-07

## Executive Summary

- **Prompts analyzed**: 4039
- **Signal prompts**: 4039 (100%)
- **Noise prompts**: 0 (0.0%)
- **Tasks**: 3257 (completion: 8.0%)
- **Links**: 1601 (empty-FP contamination: 0.0%)
- **Sessions**: 921
- **Recommendations**: 1 (1 P0)

**Overall Health Grade: B**

## Data Quality

| Noise Type | Count |
|------------|-------|

## Completion Funnel

| Stage | Count |
|-------|-------|
| Plans parsed | 1 |
| Tasks extracted | 3257 |
| Tasks with links | 302 |
| Tasks with HQ links (J>=0.30) | 302 |
| Completed tasks | 261 |

**Completion rate**: 8.0%
**Linkage rate (J>=0.30)**: 9.3%

### By Organ

| Organ | Tasks | Completed | HQ Linked | Plans |
|-------|-------|-----------|-----------|-------|
| I | 3 | 0 | 0 | 1 |
| II | 145 | 21 | 15 | 1 |
| III | 554 | 89 | 31 | 1 |
| IV | 644 | 24 | 61 | 1 |
| LIMINAL | 708 | 88 | 80 | 1 |
| META | 1062 | 39 | 96 | 1 |
| V | 134 | 0 | 19 | 1 |
| VII | 7 | 0 | 0 | 1 |

## Prompt Effectiveness

### By Prompt Type

| Type | Prompts | Linked Tasks | Completed |
|------|---------|-------------|-----------|
| command | 1357 | 539 | 47 |
| git_ops | 766 | 109 | 12 |
| plan_invocation | 717 | 555 | 105 |
| question | 467 | 62 | 2 |
| context_setting | 323 | 314 | 31 |
| continuation | 252 | 0 | 0 |
| exploration | 140 | 22 | 7 |
| correction | 17 | 0 | 0 |

### By Size Class

| Size | Prompts | Linked Tasks | Completed |
|------|---------|-------------|-----------|
| long | 1262 | 836 | 140 |
| medium | 424 | 273 | 36 |
| short | 985 | 289 | 15 |
| terse | 1368 | 203 | 13 |

### Specificity Analysis

| Specificity | Linked Tasks | Completed |
|-------------|-------------|-----------|
| high | 281 | 77 |
| low | 1320 | 127 |

**Correction rate**: 0.0% of threads (0/108)

## Session Patterns

### Session Length

| Prompts per Session | Count |
|---------------------|-------|
| 1 | 160 |
| 2-5 | 546 |
| 6-10 | 140 |
| 11-20 | 65 |
| 21-50 | 10 |
| 51+ | 0 |

### Session Duration

| Duration | Count |
|----------|-------|
| <5m | 73 |
| 5-15m | 143 |
| 15-30m | 173 |
| 30-60m | 167 |
| 1-2h | 90 |
| 2h+ | 115 |

**Productive sessions** (ending with git_ops): 156 (16.9%)

**Avg projects/day**: 3.9 | **Max**: 14

**Session churn**: 17.4% single-prompt (160/921)

### Hourly Distribution

| Hour | Prompts |
|------|---------|
| 00:00 | 262 |
| 01:00 | 233 |
| 02:00 | 88 |
| 03:00 | 53 |
| 04:00 | 35 |
| 05:00 | 68 |
| 06:00 | 25 |
| 07:00 | 32 |
| 08:00 | 29 |
| 09:00 | 84 |
| 10:00 | 170 |
| 11:00 | 245 |
| 12:00 | 253 |
| 13:00 | 245 |
| 14:00 | 192 |
| 15:00 | 222 |
| 16:00 | 269 |
| 17:00 | 184 |
| 18:00 | 168 |
| 19:00 | 165 |
| 20:00 | 296 |
| 21:00 | 263 |
| 22:00 | 234 |
| 23:00 | 224 |

## Linking Quality

**Total links**: 1601
**Empty-fingerprint contamination**: 0 (0.0%)
**Generic-tag-only links**: 52 (3.2%)
**High fan-out tasks (>100 links)**: 0

### Threshold Analysis

| Jaccard >= | Links | Tasks w/ Links | % of Total |
|-----------|-------|----------------|------------|
| 0.15 | 1601 | 302 | 100.0% |
| 0.20 | 1601 | 302 | 100.0% |
| 0.30 | 1601 | 302 | 100.0% |
| 0.40 | 617 | 158 | 38.5% |
| 0.50 | 536 | 117 | 33.5% |

## Recommendations

| Priority | Category | Finding | Recommendation |
|----------|----------|---------|----------------|
| P0 | completion | Only 8.0% task completion rate | Run `organvm atoms reconcile --write` to update completion from git history |
