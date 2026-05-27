# 24: Routine Canonical Form — Naming, Structure, SemVer, Witnessing

**Date:** 2026-05-27
**Status:** ACTIVE — applies to every Class-(I) routine (scheduled-tasks-MCP entries; future Class-(III) reusable workflows that invoke Claude)
**Derived from:** 2026-05-26 defect inventory (7 of 8 routines missing audit-log writes) + the user's framing "naming protocols & standards & structure & semver for both the routines but also as routines"
**Complements:** `17-branch-governance.md` (write contract), `18-scheduled-process-contract.md` (Rule #55a + §9 audit-log universal applicability), `19-two-org-consolidation-architecture.md`, `20-reusable-workflow-architecture.md`, `21-apps-surface-policy.md`, `22-essence-function-naming-convention.md` (general naming), `23-no-deletion-principle--alchemical-evolution.md`

---

## 1. Purpose & Scope

The system runs ~8 Class-(I) routines today. Without canonical form, the routines drift — different SKILL.md shapes, inconsistent audit-log discipline, no clear "what counts as a breaking change," no way to detect a routine that has stopped being conformant.

This document codifies four interlocking requirements:

1. **Naming** — task IDs + descriptions + label conventions
2. **Structure** — what every SKILL.md MUST contain (sections, ordering, frontmatter)
3. **SemVer** — versioning convention (when to bump major/minor/patch, what counts as breaking)
4. **Witnessing** — the routines that audit other routines for conformance (self-enforcement layer)

Together these make the routine surface **self-correcting**: a routine that drifts from canonical form gets flagged by the witness on its next run.

## 2. Naming protocol (extending doc 22)

### 2.1 Three coexisting name forms

Per the scheduled-tasks-MCP architecture, every routine carries THREE name forms:

| Form | Where | Pattern | Example |
|---|---|---|---|
| **taskId** | `{taskId}/SKILL.md` directory; MCP `list_scheduled_tasks` key | `<cadence>-<short-essence>` | `daily-pr-management` |
| **Description** | Frontmatter `description:` + sidebar label | `<essence>--<function>[-<cadence>] (<class>, v<semver>) — Class-(I) per docs/standards/22 …` | `pr-cascade--tier-merge-report (daily, v1.0.0) — Class-(I) per docs/standards/22 essence-function naming` |
| **LaunchAgent label** (Class-(II) only) | `~/Library/LaunchAgents/<label>.plist` | `com.${CONDUCTOR_LABEL_PREFIX}.<essence>--<function>-<cadence>` | `com.conductor.archive-summon--daily-md-scrub` |

The taskId is the audit-log key (preserves lookup history); the description is the canonical essence-function name (per doc 22); the LaunchAgent label encodes the conductor-author class.

### 2.2 Cadence-prefix vs cadence-suffix

Per doc 22 §4: **cadence is metadata, not identity** — so cadence appears as suffix in the canonical essence-function name (`pr-cascade--tier-merge-report-daily`). However, the taskId form keeps cadence as prefix for sidebar grouping (`daily-pr-management`). Both coexist; the description carries the canonical form.

### 2.3 Essence-suffix lexicon

Per the existing system, certain noun-phrases recur as essence suffixes:

| Essence noun | Use |
|---|---|
| `warden` | Bounded enforcement (`worktree-warden`, `repo-warden`, `stale-warden`) |
| `probe` | Read-only sensor that flags drift (`hook-drift-probe`) |
| `monitor` | Continuous-state observer (`irf-decay-monitor`) |
| `witness` | Self-audit routine that audits other routines (`scope-pattern-witness`, `apps-dormancy-witness`, `topology-witness`) |
| `auditor` | Periodic compliance check producing a 3-bucket report (`launchagent-auditor`) |
| `cascade` | Multi-phase write workflow with internal gating (`pr-cascade`) |
| `summarizer` | Reduces a time-window into a report (`commit-summarizer`) |
| `triage` | Sort-and-classify task (rarely standalone; usually compound) |

New essence nouns are allowed but require IRF-row justification (doc 24's own enforcement applies: an unrecognized essence noun is a `weekly-routine-conformance-witness` finding).

## 3. Structural standard (SKILL.md canonical shape)

Every Class-(I) routine SKILL.md MUST contain these sections in this order:

```markdown
---
name: <taskId>
description: <essence>--<function>[-<cadence>] (<class>, v<semver>) — Class-(I) per docs/standards/22 essence-function naming
---

## Version: v<semver>
## Status format: <status-pattern-spec>

## Audit log (start — invoke FIRST)
Run: `~/.local/bin/scheduled-task-audit-bookend <taskId> start`
Per docs/standards/18 §9, every Class-(I) fire must emit start + end entries regardless of writes.

## [Operate under clause — cite governing standards docs]

## Pre-flight
[List of required preconditions]

## Procedure

### Phase A: [enumerate / read]
### Phase B: [classify / analyze]
### Phase C: [report / safe writes]
### Phase D: [higher-authority writes] (if applicable)
### Phase E: [unified report] (if Phase D exists)

## What this task NEVER does
[Hard constraints per docs/standards/17 §10 hard-NEVERs]

## Audit log (end — invoke LAST, after the report)
Run: `~/.local/bin/scheduled-task-audit-bookend <taskId> end <status>`
where `<status>` follows the format declared above. Use hyphens; no whitespace.
```

### 3.1 Mandatory sections (the conformance witness checks)

| Section | Required? | Rationale |
|---|---|---|
| Frontmatter with `name:` + `description:` | YES | MCP needs name; description carries canonical essence-function form per doc 22 |
| `## Version: v<semver>` header | YES | Per §4 below |
| `## Status format:` header | YES | Declares the contract for the bookend-end `<status>` parameter |
| `## Audit log (start)` invocation | YES | Per doc 18 §9 invariant |
| Operate-under clause citing standards docs | YES | Routes durable authorization through docs 17 + 18 + 24 |
| Pre-flight section | YES | Surfaces required preconditions |
| Procedure section with phases | YES | Structures the work |
| What-this-task-NEVER-does | YES | Codifies hard constraints (mirrors doc 17 §10 pattern) |
| `## Audit log (end)` invocation | YES | Per doc 18 §9 invariant |

### 3.2 Optional sections

- `## Context` — why the task exists (often a memory-file reference)
- `## Failure semantics` — how partial failures cascade
- `## Higher-authority writes` — for Phase D Tier-3 work per doc 17 §10
- `## Cross-references` — other docs/routines this task relates to

## 4. SemVer convention

Versions encode: `MAJOR.MINOR.PATCH`

### MAJOR bump (vN → v(N+1).0.0)

A breaking change to behavior, interface, or downstream-readable contract. Examples:
- Changing the status format (breaks dashboards that grep `<status>`)
- Changing the taskId (breaks audit-log lookup history)
- Removing a write action (e.g., Tier-2 enablement removed from `daily-pr-management`)
- Removing a phase
- Tightening a write-class hard constraint (e.g., per-run cap reduced from 5 to 3)

### MINOR bump (v1.N → v1.(N+1).0)

Additive feature, no breaking change. Examples:
- New bucket added to classification (e.g., adding `STALE-PRUNABLE` to `daily-worktree-triage` Phase B)
- New optional flag or environment variable
- New canonical-replies template added
- Loosening a constraint (e.g., per-run cap raised)
- New phase added (additive only)

### PATCH bump (v1.0.N → v1.0.(N+1))

Bug fix, prompt clarification, no behavior change. Examples:
- Fixing a regex typo in the procedure
- Clarifying wording in the pre-flight section
- Updating a doc cross-reference path
- Adding missing audit-log entries to existing phases (the recent doc 18 §9 fix was a v0.1.0 → v1.0.0 MAJOR bump for the existing routines because the bookend-end status format is a new downstream contract)

### Version persistence

Version lives in the SKILL.md prompt header (`## Version: v1.0.0`) AND in the description (`(<class>, v1.0.0)`). Both must match. The conformance witness verifies match.

### Version-zero

New routines start at `v0.1.0` until shipped through their first scheduled fire successfully. After first successful fire, the conductor bumps to `v1.0.0` to signal "operational." Versions below `v1.0.0` indicate pre-flight; downstream consumers (the witnesses) should report-only-not-flag-defects on `v0.X.Y` routines.

## 5. Witnessing — the self-enforcement layer

Two Class-(I) witness routines audit Class-(I) routines (eating their own dog food):

### 5.1 `weekly-routine-conformance-witness`

**Cadence:** Weekly (Sunday 10:07 EDT — chosen to fall AFTER all daily-Sunday runs but BEFORE the new week starts)

**Purpose:** Read every active scheduled-task SKILL.md; verify each follows doc 24 §3 structural standard. Report violations.

**Status format:** `<R>-routines-<C>-conformant-<V>-violations`

**Checks (per routine):**
- Frontmatter has `name:` + `description:` ✓
- Description carries `(<class>, v<semver>)` marker ✓
- Prompt has `## Version: v<semver>` header matching description ✓
- Prompt has `## Status format:` header ✓
- Prompt has `## Audit log (start)` invocation ✓
- Prompt has `## Audit log (end)` invocation ✓
- Prompt has Pre-flight section ✓
- Prompt has Procedure with at least one Phase ✓
- Prompt has What-this-task-NEVER-does section ✓
- Essence noun matches doc 24 §2.3 lexicon OR has IRF-row justification ✓

**Violations report:** per-routine listing of which checks failed, with severity (missing-bookend = P0; missing-version = P1; unknown-essence = P2).

### 5.2 `weekly-audit-log-coverage-witness`

**Cadence:** Weekly (Sunday 10:09 EDT — staggered after conformance witness)

**Purpose:** Grep the last 7 days of audit logs; verify every active routine fired the expected number of times AND every fire produced a matching start+end pair.

**Status format:** `<R>-routines-<F>-fires-<P>-paired-<U>-unpaired-<M>-missing`

**Checks (per routine × per expected-day):**
- For each active routine + each day in the last 7 where the cron would fire: expect exactly one `start` entry + one `end` entry
- Missing pair → defect (routine didn't fire OR didn't bookend)
- `start` without `end` → mid-fire failure (routine crashed)
- `end` without `start` → corrupted log OR routine skipped its bookend-start (defect)

**Violations report:** per-routine + per-day listing of missing/unpaired entries with classification.

### 5.3 Recursion — the witnesses witness themselves

Both witnesses are themselves Class-(I) routines following doc 24. They:
- Are named per §2 lexicon (`witness` is a canonical essence noun)
- Carry `v1.0.0` versions per §4
- Bookend per doc 18 §9
- Will appear in each other's reports

Self-witnessing closure: if a witness stops firing or stops conforming, the OTHER witness will surface it next Sunday. The system catches its own audit-instrumentation defects.

## 6. Migration of existing routines

Per doc 23 §3 (no deletion; only alchemical evolution):
- Existing taskIds stay (preserves audit-log history)
- Descriptions get the `(<class>, v<semver>)` marker added in the next prompt update
- Prompt headers get the `## Version:` + `## Status format:` declarations added in the next prompt update

The 8 active routines as of doc 24's landing are at implicit `v0.1.0` until updated; the `weekly-routine-conformance-witness` will report all 8 as "version-zero, please bump after next successful fire" on first run.

A future session updates the 8 prompts to add the version + status format headers (low-effort batch — 8 update_scheduled_task calls). After that, the routines are at `v1.0.0` and the witnesses report `8-routines-8-conformant-0-violations`.

## 7. Status format conventions (canonical examples)

Per routine, the `<status>` parameter to `scheduled-task-audit-bookend end` follows a declared format. The conformance witness verifies the format declaration exists; doesn't verify (yet) that emitted statuses match the format.

| Routine | Status format |
|---|---|
| `daily-hook-drift` | `no-drift` \| `drift-detected-<event-types>` \| `error-<reason>` |
| `daily-repo-hygiene` | `<N>-repos-<U>-unpushed-<O>-orphan-<S>-stale-<P>-pushes` |
| `daily-pr-management` | `<N>-prs-tier1=<X>-tier2=<Y>-tier3=<Z>-writes=<W>` |
| `daily-worktree-triage-and-cleanup` | `<R>-repos-<W>-worktrees-<C>-removals-<D>-dirty-<L>-locked` |
| `daily-code-review` | `<N>-commits-summarized-<R>-repos` \| `no-commits-since-yesterday` |
| `weekly-irf-aging` | `<R>-rows-<A>-aging-<S>-shipped-<O>-overdue` |
| `weekly-sibling-scope-drift` | `<S>-scopes-<C>-cross-3plus-<P>-promotion-candidates` |
| `monthly-launchagent-audit` | `compliant=<C>-exempt=<E>-violation=<V>` |
| `weekly-routine-conformance-witness` | `<R>-routines-<C>-conformant-<V>-violations` |
| `weekly-audit-log-coverage-witness` | `<R>-routines-<F>-fires-<P>-paired-<U>-unpaired-<M>-missing` |

Future format extension: when a routine's status needs richer structure, bump MAJOR (per §4) and declare the new format.

## 8. Cross-references

- `${DOC_NAMING_CONVENTION}` (doc 22) — general essence-function naming; doc 24 §2 specializes for routines
- `${DOC_SCHEDULED_PROCESS_CONTRACT}` (doc 18) §9 — audit-log universal applicability that doc 24 §3 codifies as mandatory section
- `${DOC_BRANCH_GOVERNANCE}` (doc 17) §10 — write-action hard-NEVERs that doc 24 §3 codifies as mandatory section
- `${DOC_NO_DELETION}` (doc 23) — lifecycle vocabulary; doc 24 §6 (migration) uses "evolution" not "rewrite"
- `${CORPVS_ROOT}/.config/organvm.env` — `ROUTINE_*` env vars; doc 24 §2 names map to env values

## 9. The closure

After doc 24 + the 2 witnesses + the 8 SKILL.md prompt updates (to add `## Version:` + `## Status format:` headers) land:

- Every routine has a canonical form (§3)
- Every routine is versioned (§4)
- Every routine writes audit log (§5 + doc 18 §9)
- Every routine is audited by other routines (§5)
- Routines that drift get reported within 7 days
- Routines that fail to fire get reported within 7 days
- The system catches its own routine-defects

This is the self-correcting layer. The standards aren't *enforced by hooks at write-time* (too brittle); they're *audited by routines at fire-time* (catch-up rather than block). The witness pattern matches the alchemical evolution principle: nothing prevented at write; everything surfaced for amendment.
