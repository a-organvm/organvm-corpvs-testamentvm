# April 2026 — The Ultima Evolution

> *Single canonical artifact distilled from 287 sessions, 4 base tables, 9 predicate gates.*
> Generated: 2026-04-27T15:02:29

---

## I. Provenance

- **Sessions:** 287
- **Date range:** 2026-04-01 → 2026-04-27
- **Scopes:** 18 unique
- **Events captured:** 38,190 (2066 user prompts, 10868 assistant turns, 21194 tool calls)
- **Atoms:** 48,633 (2,063 parent + 46,570 child)
- **Entities:** 1115 unique (people / projects / paths)
- **Verdicts:** 2583 (287 × 9 predicates)

**Pipeline stages:** enumerate → decompose → predicate → synthesize. Base tables under `data/corpus/april-2026/`.

---

## II. Standardization Baseline (Extracted, Not Imposed)

These rates **define** April. Future months get measured against these as the baseline.

| Predicate | PASS | FAIL | N_A | PASS-rate (excl. N_A) |
|---|---:|---:|---:|---:|
| sisyphus | 243 | 42 | 2 | 85.3% |
| hall_monitor | 205 | 82 | 0 | 71.4% |
| irf | 110 | 0 | 177 | 100.0% |
| vacuum | 238 | 0 | 49 | 100.0% |
| parity | 4 | 16 | 267 | 20.0% |
| additive | 0 | 0 | 287 | — |
| recover | 245 | 42 | 0 | 85.4% |
| commit_push | 4 | 16 | 267 | 20.0% |
| universal_context | 0 | 0 | 287 | — |

- **Mean prompts/session:** 7.2
- **Median events/session:** (107)

---

## III. Recovery List (Stage 7 — Warp-Killed & Truncated)

**37 sessions** ended with user prompting last (no assistant reply).
**5 sessions** ended mid-assistant-response in known kill-windows.
**Total unsafe close: 42**

### Today's Warp-restart (2026-04-27 ~07:50 local) — recover these now:

```bash
claude --resume 116a45d8-38f0-4289-9b58-f1b6cb6dbf72    # -Users-4jp — 169 events
claude --resume ac066cac-7d54-4aa0-b62b-3f91100376a9    # -Users-4jp — 53 events
claude --resume 5ebeebd3-d8e4-4726-80b4-855995af538e    # -Users-4jp — 51 events
claude --resume f6adcad7-911d-441e-99db-78f80ae9ff35    # -Users-4jp — 27 events
claude --resume 8bac99ae-b8b6-4d19-a0ee-2bb934bdeffe    # -Users-4jp — 28 events
```

### Earlier-April unanswered prompts (case-1, top 15 by event count):

| Session | Events | Date | Scope |
|---|---:|---|---|
| `2f07b96a` | 344 | 2026-04-20 | -Users-4jp-Workspace-meta-organvm-post-flood-archive-original |
| `be87233a` | 207 | 2026-04-01 | -Users-4jp-Workspace-organvm-iv-taxis-orchestration-start-here |
| `9041b50e` | 184 | 2026-04-02 | -Users-4jp-Workspace-organvm-iv-taxis-orchestration-start-here |
| `c10b0a34` | 129 | 2026-04-04 | -Users-4jp-Workspace |
| `16aa6e75` | 123 | 2026-04-01 | -Users-4jp-Workspace |
| `16bf7dff` | 91 | 2026-04-16 | -Users-4jp-Workspace-organvm-iii-ergon-sovereign-systems--elevate-align |
| `7574b6b7` | 74 | 2026-04-04 | -Users-4jp-Workspace-organvm-iv-taxis |
| `0d4fd2e1` | 58 | 2026-04-25 | -Users-4jp |
| `ef0f6117` | 22 | 2026-04-22 | -Users-4jp |
| `aace623d` | 6 | 2026-04-04 | -Users-4jp-systems |
| `9016ce4a` | 5 | 2026-04-19 | -Users-4jp-system-system--system |
| `022eeab8` | 3 | 2026-04-04 | -Users-4jp-Workspace-organvm-iii-ergon-sovereign-systems--elevate-align |
| `cc44a561` | 2 | 2026-04-22 | -Users-4jp |
| `1d19c860` | 1 | 2026-04-22 | -Users-4jp |
| `442f335d` | 1 | 2026-04-16 | -Users-4jp-Workspace |

---

## IV. Hall-Monitor — Top Rule Violations

**82 sessions** flagged. Top offenders:

| Session | Date | Scope | Violations |
|---|---|---|---|
| `7f671579` | 2026-04-23 | -Users-4jp | rambling ratio 69/5 |
| `bffe3bb7` | 2026-04-18 | -Users-4jp | rambling ratio 56/6 |
| `6cb6e33e` | 2026-04-21 | -Users-4jp | rambling ratio 48/5 |
| `af8465e2` | 2026-04-21 | -Users-4jp | rambling ratio 67/3 |
| `78e28596` | 2026-04-21 | -Users-4jp | rambling ratio 17/2 |
| `5e6b1b1c` | 2026-04-25 | -Users-4jp | rambling ratio 24/2 |
| `e87291f8` | 2026-04-23 | -Users-4jp | rambling ratio 110/8 |
| `e4d7bfeb` | 2026-04-26 | -Users-4jp | rambling ratio 34/3 |
| `ce4999dd` | 2026-04-21 | -Users-4jp | rambling ratio 55/4 |
| `967521eb` | 2026-04-15 | -Users-4jp | rambling ratio 142/11 |

---

## V. Parity & Commit-Push Failures

**16 sessions** left dirty/unpushed git state.

| Session | Date | Cwd | Issue |
|---|---|---|---|
| `9a022a0b` | 2026-04-16 | `/Users/4jp/Workspace/4444J99` | dirty |
| `9d9ed4ba` | 2026-04-06 | `/Users/4jp/Workspace/4444J99/application-pipeline` | dirty |
| `e964dc14` | 2026-04-01 | `/Users/4jp/Workspace/4444J99/application-pipeline` | dirty |
| `46fbd866` | 2026-04-03 | `/Users/4jp/Workspace/4444J99/application-pipeline` | dirty |
| `8442f1dc` | 2026-04-03 | `/Users/4jp/Workspace/4444J99/application-pipeline` | dirty |
| `6ac7c33e` | 2026-04-15 | `/Users/4jp/Workspace/meta-organvm/post-flood/archive_original` | dirty |
| `b23e3aca` | 2026-04-11 | `/Users/4jp/Workspace/meta-organvm/post-flood/archive_original` | dirty |
| `1b0958d0` | 2026-04-14 | `/Users/4jp/Workspace/meta-organvm/post-flood/archive_original` | dirty |
| `c1759668` | 2026-04-09 | `/Users/4jp/Workspace/meta-organvm/post-flood/archive_original` | dirty |
| `2f07b96a` | 2026-04-20 | `/Users/4jp/Workspace/meta-organvm/post-flood/archive_original` | dirty |

---

## VI. Scope Distribution

| Scope | Sessions |
|---|---:|
| `-Users-4jp` | 108 |
| `-Users-4jp-system-system--system` | 47 |
| `-Users-4jp-Workspace` | 32 |
| `-Users-4jp-Workspace-organvm-iv-taxis` | 23 |
| `-Users-4jp-Workspace-meta-organvm` | 22 |
| `-Users-4jp-Workspace-meta-organvm-post-flood-archive-original` | 15 |
| `-Users-4jp-Workspace-organvm-iii-ergon-sovereign-systems--elevate-align` | 11 |
| `-Users-4jp-Workspace-organvm-iv-taxis-orchestration-start-here` | 11 |
| `-Users-4jp-Workspace-4444J99-application-pipeline` | 4 |
| `-Users-4jp-Workspace-a-organvm` | 4 |
| `-Users-4jp-Workspace-4444J99` | 2 |
| `-Users-4jp-substance-subtrate-organvm--major-instance-organvm-origin-organvm-iii-ergon-sovereign-systems--elevate-align` | 2 |
| `-Users-4jp-Workspace-meta-organvm-post-flood` | 1 |
| `-Users-4jp-Workspace-meta-organvm-praxis-perpetua-prompt-corpus` | 1 |
| `-Users-4jp-Workspace-void--edge-object--plane-organvm--major-instance-organvm-origin-organvm-iii-ergon-sovereign-systems--elevate-align` | 1 |
| `-Users-4jp-sovereign--ground` | 1 |
| `-Users-4jp-substance-subtrate-organvm--major-instance-organvm-origin-meta-organvm` | 1 |
| `-Users-4jp-systems` | 1 |

---

## VII. The Atom Graph — Top Entities

### Top named entities (people / projects / concepts)

| Name | Kind | Sessions | First seen |
|---|---|---:|---|
| `GitHub` | named | 124 | 2026-04-01 |
| `Provide` | named | 120 | 2026-04-01 |
| `Sisyphus?` | named | 118 | 2026-04-01 |
| `What` | named | 39 | 2026-04-01 |
| `Base` | named | 38 | 2026-04-02 |
| `Code` | named | 33 | 2026-03-31 |
| `I'm` | named | 32 | 2026-03-31 |
| `You` | named | 29 | 2026-03-31 |
| `Claude` | named | 27 | 2026-03-31 |
| `Start` | named | 24 | 2026-04-02 |
| `Session` | named | 23 | 2026-04-01 |
| `CLI` | named | 20 | 2026-04-01 |
| `Plan` | named | 20 | 2026-04-01 |
| `Brainstorming` | named | 20 | 2026-04-02 |
| `Ideas` | named | 20 | 2026-04-02 |

### Top paths referenced

| Path | Sessions |
|---|---:|
| `/Users/4jp/.claude/plugins/cache/claude-plugins-official/superpowers/5.0.7/skill` | 20 |
| `/Users/4jp/Desktop/Screenshot` | 17 |
| `/Users/4jp` | 7 |
| `/Users/4jp/.claude/plugins/cache/claude-plugins-official/superpowers/5.0.7/skill` | 5 |
| `/Users/4jp/Workspace/meta-organvm` | 5 |
| `~/Workspace` | 4 |
| `/Users/4jp/.claude/plugins/cache/claude-plugins-official/superpowers/5.0.7/skill` | 4 |
| `/Users/4jp/sovereign--ground/holds--same/a-organvm` | 4 |
| `/Users/4jp/Workspace/meta-organvm/post-flood/archive_original` | 3 |
| `/Users/4jp/Desktop/Screenshot\` | 3 |
| `/Users/4jp/.claude/plugins/cache/claude-plugins-official/superpowers/5.0.7/skill` | 3 |
| `/Users/4jp/system-system--system--monad` | 3 |
| `/Users/4jp/system-system--system` | 3 |
| `/Users/4jp/.claude/skills/knowledge-architecture` | 3 |
| `/Users/4jp/Workspace/organvm-iv-taxis` | 3 |

---

## VIII. Tool Usage — Aggregate

| Tool | Calls |
|---|---:|
| `Bash` | 11,770 |
| `Read` | 4,159 |
| `Edit` | 2,727 |
| `Write` | 1,335 |
| `TaskUpdate` | 1,098 |
| `Agent` | 960 |
| `Grep` | 908 |
| `TaskCreate` | 578 |
| `ToolSearch` | 496 |
| `ExitPlanMode` | 293 |
| `Glob` | 247 |
| `AskUserQuestion` | 121 |
| `Skill` | 57 |
| `WebSearch` | 44 |
| `mcp__claude-in-chrome__computer` | 44 |

---

## IX. Sisyphus's Verdict

**April 2026 closes** with the following permanent record:

- **243/287** sessions closed substantively (84.7%).
- **42** sessions need recovery (case-1 case-2 unsafe close).
- **82** sessions flagged for hall-monitor review (rambling / all-talk-no-shipping).
- **16** sessions left dirty git state.
- **16** sessions left unpushed commits.

**Is April safe to close?** Not without addressing the recovery list (§ III) and parity failures (§ V). The 5 today-killed sessions in particular contain in-flight work that did not return to prompt.

**What rolls into May:**
- Recovery of 42 unsafe-close sessions (manual review per resume command in § III)
- Resolution of 16 parity/commit-push failures
- Universal-context cross-reference (predicate #9 deferred — implement as Stage 4 follow-up)
- Additive-rule diff verification (predicate #6 deferred — needs git diff history)

---

## Appendix — Base Tables (canonical, frozen)

All under `~/Workspace/organvm/organvm-corpvs-testamentvm/data/corpus/april-2026/`:

- `events.jsonl` — 38,190 records
- `atoms.jsonl` — 48,633 records
- `entities.jsonl` — 1115 records
- `verdicts.jsonl` — 2,583 records
- `session-index.jsonl` — 287 records

**Projections** (queryable views over the base):
- This document = view F (aggregate)
- views A–E (by-session, timeline, by-domain, by-scope, by-predicate) deferred to follow-up scripts

---

*Plan-as-sculpture. Sources eternal, derivations versioned, projections free.*  
*Generated by `apply-sequence` Stages 1–4 on 2026-04-27.*
