# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

This is a **planning and governance documentation corpus** — not a source code repository. It contains the complete planning, audit, and implementation record for an eight-organ creative-institutional system ("ORGAN I–VII + Meta") that coordinates 97 GitHub repositories across 8 GitHub organizations (7 organ orgs + 1 meta-org).

**Owner:** @4444j99 / @4444J99
**Status:** LAUNCHED (2026-02-11) — all 8 organs OPERATIONAL
**Repository:** `meta-organvm/organvm-corpvs-testamentvm`
**Documentation deployed:** ~404K+ words across 103 repos + 8 org profiles + 46 meta-system essays

There is no build system, test suite, or runtime code here. Executable artifacts include 5 validation scripts in `scripts/` and YAML/Python workflow specifications in `docs/implementation/github-actions-spec.md`.

## The Eight-Organ Model

| Organ | Domain | GitHub Org | Repos | Flagships |
|-------|--------|-----------|-------|-----------|
| I | Theory (epistemology, recursion, ontology) | `organvm-i-theoria` | 20 | recursive-engine--generative-entity |
| II | Art (generative, performance, experiential) | `organvm-ii-poiesis` | 30 | metasystem-master, a-mavs-olevm |
| III | Commerce (SaaS, B2B, B2C products) | `organvm-iii-ergon` | 27 | public-record-data-scrapper |
| IV | Orchestration (governance, routing) | `organvm-iv-taxis` | 7 | orchestration-start-here, agentic-titan |
| V | Public Process (essays, building in public) | `organvm-v-logos` | 2 | public-process |
| VI | Community (salons, reading groups) | `organvm-vi-koinonia` | 4 | — |
| VII | Marketing (POSSE distribution, announcements) | `organvm-vii-kerygma` | 4 | — |
| VIII | Meta (umbrella org) | `meta-organvm` | 3 | organvm-corpvs-testamentvm |

## Key Invariants (Enforced Across All Documents)

1. **`registry-v2.json` is the single source of truth** — all repo state lives there
2. **No back-edges in dependency graph** — flow is I→II→III only; ORGAN-III cannot depend on ORGAN-II
3. **All 8 organs are represented at launch** — each organ has at least one flagship repo fully documented; remaining repos may launch as stubs or in-progress (compatible with Bronze/Silver/Gold tiered approach)
4. **Documentation precedes deployment** — no Phase 2 until Phase 1 is complete
5. **Every README is a portfolio piece** — written for grant reviewers and hiring managers, not just developers
6. **Promotion is a state machine** — LOCAL → CANDIDATE → PUBLIC_PROCESS → GRADUATED → ARCHIVED (governs cross-organ promotion; repo documentation status uses a separate vocabulary: ACTIVE/DEPLOYED/SKELETON/EMPTY)

## Document Architecture

### Reading Order

1. `docs/genesis/00-c-master-summary.md` — Executive summary, start here (30 min)
2. `docs/strategy/parallel-launch-strategy.md` — Strategic rationale for simultaneous launch
3. `docs/genesis/00-d-organ-system-audit.md` — Current-state repo inventory per organ
4. `registry-v2.json` — Machine-readable source of truth (skim)
5. `docs/implementation/implementation-package-v2.md` — Master execution plan with subtask TE budgets
6. `docs/implementation/orchestration-system-v2.md` — Governance rules and dependency model
7. `docs/planning/01` through `05` — Phase 1 planning details (audit framework, templates, checklists, risk map)
8. `docs/implementation/public-process-map-v2.md` — ORGAN-V content strategy and essay outlines
9. `docs/implementation/github-actions-spec.md` — 5 CI/CD workflow specifications (YAML + Python)
10. `docs/standards/10-repository-standards.md` — Repository standards for all repos (naming, licensing, community health)
11. `docs/standards/11-specification-driven-development.md` — SDD methodology adapted for documentation deliverables
12. `docs/genesis/00-a` and `00-b` — Deep genesis transcripts (optional, 60+ min each)

### Document Layers

- **Layer 0 (Genesis):** `docs/genesis/00-a`, `00-b`, `00-c`, `00-d` — conversational source material and audit
- **Layer 1 (Phase 1 Planning):** `docs/planning/01` through `05`, `docs/standards/10-repository-standards.md`, `docs/standards/11-specification-driven-development.md` — sequential planning toolkit (scoring rubric, inventory, templates, checklists, risk map, repository standards, SDD methodology)
- **Layer 2 (Execution):** `docs/strategy/phase-1-execution-index.md`, `docs/strategy/parallel-launch-strategy.md`, `docs/strategy/sprint-catalog.md` (76 named sprints across 18 categories)
- **Layer 3 (v2 Active):** `docs/implementation/implementation-package-v2.md`, `docs/implementation/orchestration-system-v2.md`, `docs/implementation/public-process-map-v2.md`, `registry-v2.json`, `docs/implementation/github-actions-spec.md`
- **Operations:** `docs/operations/` — rolling-todo.md (work queue), operational-cadence.md (anti-patterns, review rhythm), concordance.md (invocation symbol table), stranger-test-protocol.md, key-workflows.md
- **Archive:** `docs/archive/` contains v1 predecessors (superseded by v2 documents)

### Cross-Document Dependency Map

```
docs/genesis/00-a (Genesis Q&A)
  ├─→ 00-b (Local/Remote Structure)
  ├─→ 00-d (System Audit)
  │     ├─→ registry-v2.json
  │     └─→ docs/implementation/orchestration-system-v2.md
  └─→ 00-c (Master Summary)
        ├─→ docs/planning/01–05 (Phase 1 Planning)
        └─→ docs/strategy/phase-1-execution-index

docs/strategy/parallel-launch-strategy
  ├─→ docs/implementation/implementation-package-v2
  ├─→ docs/implementation/orchestration-system-v2
  ├─→ docs/implementation/public-process-map-v2
  ├─→ docs/implementation/github-actions-spec
  └─→ registry-v2.json
```

## Implementation History (All Complete)

- **Phase -1 (2026-02-09):** Org architecture — 8 GitHub orgs created, env-var config, naming scheme
- **Phase 0 (2026-02-10):** Corpus refinement — repo transfers, cross-AI validation, task manifest
- **Phase 1 (2026-02-10):** Documentation audit — Bronze Sprint (7 flagships), Silver Sprint (58 READMEs, ~202K words), Gold Sprint (essays, health files, workflows)
- **Phase 2 (2026-02-10):** Micro-validation — all 8 organs locked, 1,267 links audited, 31 dependency edges validated
- **Phase 3 (2026-02-10):** Integration — 5 GitHub Actions workflows, POSSE distribution, branch protection
- **Launch (2026-02-11):** 9/9 criteria met, all 8 organs OPERATIONAL
- **Gap-Fill Sprint (2026-02-11):** 11 repos created, 14 READMEs deployed, 14 tier promotions, ~270K total words

## TE (Tokens-Expended) Budget Model

Effort is measured in LLM API tokens, not human-hours. The AI-conductor model means: AI generates volume, human reviews and refines.

### Token Arithmetic
- 1 token ≈ 4 characters ≈ 0.75 words
- 3,000-word README ≈ 4,500 output tokens
- One generation pass (system + template + context + output) ≈ 15,000–20,000 tokens
- With 2–3 revision iterations + validation ≈ 50,000–90,000 tokens per README

### Per-Task TE Estimates
| Task Type | TE Budget |
|-----------|-----------|
| README REWRITE | ~72K TE |
| README REVISE | ~50K TE |
| README POPULATE | ~88K TE |
| README EVALUATE | ~24K TE |
| README ARCHIVE | ~12K TE |
| Essay (4,000–5,000 words) | ~120K TE |
| Validation Pass (per repo) | ~15K TE |
| GitHub Actions Workflow | ~55K TE |

### Phase Budgets
| Phase | TE Budget | Calendar |
|-------|-----------|----------|
| Phase 1 (Documentation) | ~4.4M TE | Sprints 1–2 |
| Phase 2 (Validation) | ~1.0M TE | Sprint 3 |
| Phase 3 (Integration) | ~1.1M TE | Sprint 4 |
| **Total** | **~6.5M TE** | **Criteria-driven (D-08)** |

## Org Naming Architecture

Org names are **env-var-driven** for templating. The system uses a prefix + Greek ontological suffix scheme:

- **Template config:** `.config/organvm.env` (committed, provides defaults)
- **Instance config:** `.config/organvm.env.local` (gitignored, contains `ORGAN_PREFIX=organvm`)
- **Machine-readable:** `.config/organvm.config.json` (maps organ numbers to suffixes, env vars, domains)

All org references in docs, registry, and workflows use the resolved instance names (e.g., `organvm-i-theoria`). The template defaults use `${ORGAN_PREFIX}-i-theoria` etc.

## Working With This Corpus

- When editing `registry-v2.json`, maintain the existing JSON schema. Every repo entry has: `name`, `org`, `status`, `public`, `description`, `documentation_status`, `portfolio_relevance`.
- ORGAN-III repos additionally carry `type` (SaaS/B2B/B2C/internal) and `revenue` fields.
- The `docs/archive/` directory is frozen — do not modify v1 files; create v2+ variants in `docs/implementation/` instead.
- Documents `01`–`05` are sequentially numbered outputs of the master summary (`00-c`). They form a cohesive planning toolkit and cross-reference each other. They live in `docs/planning/`.
- The `docs/ANNOTATED-MANIFEST.md` provides an exhaustive per-file annotation of the entire directory and is the best starting point for understanding what each document contains.
- The execution plan is in `docs/strategy/roadmap-there-and-back-again.md` — the phased implementation roadmap from Phase -1 (org architecture) through Phase 3 (launch).
- The project constitution is at `docs/memory/constitution.md` — immutable principles (Articles I-VI) and post-cross-validation amendments (A-D) that govern all specifications and quality gates.
- Feature specifications live in `docs/specs/` — each deliverable (e.g., `docs/specs/bronze-sprint/`) contains a `spec.md` (requirements and success criteria) and `checklists/requirements.md` (validation checklist). The SDD methodology is defined in `docs/standards/11-specification-driven-development.md`.
- The **governance quadrilateral** is: roadmap (`docs/strategy/there+back-again.md`) + cadence (`docs/operations/operational-cadence.md`) + catalog (`docs/strategy/sprint-catalog.md`) + rolling TODO (`docs/operations/rolling-todo.md`). These four documents govern all planning and execution.
- **GitHub issue tracking:** 58 issues on `meta-organvm/organvm-corpvs-testamentvm` (omega criteria + sprint catalog) and 1 on `meta-organvm/organvm-engine` (scorecard fix). All omega criteria and unexecuted sprints have bidirectional links between issues and documentation.

## Invocation System

The governance corpus uses short IDs across 6 namespaces. When the user references an ID (e.g., "what's X1?", "show me AP-3", "which items advance #8"), look up context in `docs/operations/concordance.md`.

| Prefix | Namespace | Source | Example |
|--------|-----------|--------|---------|
| X1–X4 | TODO: P0 hermetic seal | rolling-todo.md / e2g-ii | X1 = Submit Creative Lab Five |
| E1–E5 | TODO: P1 engagement | rolling-todo.md / e2g-ii | E3 = Google Creative Fellowship |
| M1-II–M6-II | TODO: P2 quality | rolling-todo.md / e2g-ii | M2-II = Stripe integration |
| S1-II–S6-II | TODO: P3 strategic | rolling-todo.md / e2g-ii | S2-II = Host first salon |
| G1–G3 | TODO: setup guide | rolling-todo.md | G2 = Render hosting |
| #1–#17 | Omega criteria | there+back-again.md | #8 = Product live |
| H1–H5 | Horizons | there+back-again.md | H3 = Generate Revenue |
| AP-1–AP-7 | Anti-patterns | operational-cadence.md | AP-1 = Don't start another sprint |
| W/SP/BS/LC/BL/ET/LO-II | E2G-II findings | e2g-ii-action-items.md | W1-II = Zero external contact |
| 01–33 | Completed sprints | docs/specs/sprints/ | 33 = OPERATIO |

CLI: `python3 scripts/invoke.py <ID>` for terminal lookup. See `docs/operations/concordance.md` for the full symbol table.

## AI-Conductor Workflow Model

This corpus operates on an **AI-conductor model**: human directs, AI generates volume, human reviews and refines. Key implications for working with these documents:

- **Word count targets** (3,000+ words, 2,500+ words, etc.) are quality specifications, not labor estimates. AI generates the volume; human ensures accuracy and voice.
- **Time estimates** reflect human review time for AI-generated drafts, not writing time.
- **Quality assurance** is AI validation (template compliance, link checking, cross-references) + human strategic review (accuracy, positioning, portfolio language).
- **AI-specific risks** to watch for: hallucinated code examples, generic boilerplate phrasing, incorrect cross-references, missing project-specific context.

## Naming and Path Conventions

The workspace uses a flat 2-level structure that mirrors GitHub exactly:
```
~/Workspace/<github-org>/<repo>/
```
e.g. `~/Workspace/organvm-i-theoria/recursive-engine--generative-entity/`

Repo naming pattern: `[organ]-[type]--[specific-name]` (double-dash separates type from name).

## Artifact Routing

When completing tasks across the organ system, use this decision tree to determine where files should land:

**Q1: Working repo (code/application)?**
→ `~/Workspace/<github-org>/<repo>/`
  e.g. `~/Workspace/organvm-i-theoria/recursive-engine--generative-entity/`

**Q2: Governance/planning/architecture doc for the organ system?**
→ This corpus (`~/Workspace/meta-organvm/organvm-corpvs-testamentvm/`), routed by document layer:

| Artifact type | Destination |
|---|---|
| Raw transcript / session log | `docs/genesis/` |
| Planning toolkit / audit | `docs/planning/` |
| Strategy / roadmap | `docs/strategy/` |
| Implementation spec / workflow | `docs/implementation/` |
| Evaluation / review | `docs/evaluation/` |
| Standard / methodology | `docs/standards/` |
| ADR (short decision record) | `docs/adr/` |
| Sprint spec | `docs/specs/<sprint>/` |
| Application / submission (canonical source) | `docs/applications/` (covenant-ark, tracker, strategy — source of truth for identity/metrics) |
| Application / submission (pipeline ops) | `~/Workspace/4444J99/application-pipeline/` (pipeline YAML, blocks, variants, conversion tracking) |
| Essay draft | `docs/essays/` |

**Q2b: Application materials?**
→ Application work is split between two locations:
- **Canonical identity, metrics, evidence:** Stay in `docs/applications/` (covenant-ark is the source of truth)
- **Pipeline tracking, composable blocks, variants, conversion analytics:** Go to `~/Workspace/4444J99/application-pipeline/`
- When metrics change, update `docs/applications/00-covenant-ark.md` first, then propagate to `application-pipeline/blocks/`

**Q3: Unsorted / temporary / exploratory?**
→ `~/Workspace/intake/` (universal catch-all; triage later)

**NEVER** land files in: `~/` (home) or directly in `~/Workspace/` (only org directories and non-organ projects belong at the top level).

## Parent Directory Context

This corpus lives at `~/Workspace/meta-organvm/organvm-corpvs-testamentvm/`, alongside `~/Workspace/meta-organvm/alchemia-ingestvm/` in the meta-organvm org directory. The old path `~/Workspace/organvm-pactvm/ingesting-organ-document-structure/` is deprecated (restructured 2026-02-16).

<!-- ORGANVM:AUTO:START -->
## System Context (auto-generated — do not edit)

**Organ:** META-ORGANVM (Meta) | **Tier:** flagship | **Status:** PUBLIC_PROCESS
**Org:** `unknown` | **Repo:** `organvm-corpvs-testamentvm`

### Edges
- **Produces** → `unknown`: unknown
- **Consumes** ← `ORGAN-IV`: unknown

### Siblings in Meta
`.github`, `alchemia-ingestvm`, `schema-definitions`, `organvm-engine`, `system-dashboard`, `organvm-mcp-server`

### Governance
- *Standard ORGANVM governance applies*

*Last synced: 2026-02-24T12:41:28Z*
<!-- ORGANVM:AUTO:END -->
