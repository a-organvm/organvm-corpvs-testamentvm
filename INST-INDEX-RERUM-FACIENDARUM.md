# INST — Index Rerum Faciendarum

**Status:** ACTIVE
**Created:** 2026-03-20
**Authority:** META — System-wide governance instrument
**Purpose:** Universal hanging index of things to be done — the canonical gap between what the system IS and what it NEEDS TO BE.

> *Index Rerum Faciendarum* — after the classical scholarly apparatus: *Index Locorum* (places), *Index Nominum* (names), *Index Rerum* (things). The gerundive *faciendarum* transforms reference into obligation: not things that exist, but things that must be made to exist.

### The Four Indices

This document is the first of a four-part classical index apparatus for ORGANVM:

| Index | Latin | Purpose | Status |
|-------|-------|---------|--------|
| **Index Rerum Faciendarum** | *Things to be done* | Universal work registry — the gap between IS and NEEDS TO BE | **THIS DOCUMENT** |
| **Index Locorum** | *Index of places* | Canonical map of where everything lives — repos, directories, files, URLs, infrastructure endpoints, deployment targets | IRF-IDX-001 |
| **Index Nominum** | *Index of names* | Registry of all named entities — organs, repos, tools, agents, personas, regimes, orders, specifications, dissertations, people | IRF-IDX-002 |
| **Index Rerum** | *Index of things* | Ontological inventory of what exists — every artifact, its type, its state, its relationships, its provenance | IRF-IDX-003 |

Together, the four indices constitute a complete scholarly apparatus for the system: where things are (Locorum), what they're called (Nominum), what they are (Rerum), and what remains to be done (Rerum Faciendarum). The first three are reference instruments; this one is a governance instrument.

---

## How to Use This Document

This is a **living governance instrument**, not a snapshot. Every session that produces or discovers work items should update this index. The auditor (`vigiles_engine/auditor.py`) and the omega scorecard (`organvm omega status`) are the primary automated consumers.

**Update protocol:**
1. When a session closes, add completed items to `## Completed` with session ID and date.
2. When new work is discovered, add to the appropriate organ section with priority and source.
3. When work is blocked, move to `## Blocked` with blocking reason.
4. When work becomes irrelevant, move to `## Archived` with reason.

**Priority tiers:**
- **P0 — NOW**: Human-gated or zero-cost unblocking actions. Do today.
- **P1 — SOON**: Next-session work. Clear path, no blockers.
- **P2 — GROWTH**: Extends existing capability. No deadline pressure.
- **P3 — HORIZON**: Future work. Requires design or prerequisites.

---

## System-Wide

### Governance & Standards

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-SYS-001 | P1 | Consolidate universal standards into a single CONSTITUTION.md — naming conventions, required files, required processes, design standards | Agent | S14, Memory | None |
| IRF-SYS-002 | P2 | Deploy standard GitHub Actions workflow template across GRADUATED repos | Agent | Wants list | Need template designed first |
| IRF-SYS-003 | P2 | Seed.yaml coverage: 72/117 → 117/117 | Agent | CLAUDE.md | Incremental |
| IRF-SYS-004 | P1 | Descent Protocol remaining 22% — repos missing descriptions/topics on GitHub | Agent | S11 | None |
| IRF-SYS-005 | P2 | World Root Phase 2-4 — repo migration per `~/Workspace/Organizing-Local-Remote-Structure.md` | Human | Memory | Phase 1 audit complete, execution not started |

### Skills & Automation

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-SKL-001 | P2 | Map 142 skills to design-process phases for auto-triggering | Agent | Wants list | Needs phase taxonomy designed |
| IRF-SKL-002 | P2 | Implement hook-based triggering for "universal standards" tier skills | Agent | Wants list | Depends on IRF-SKL-001 |
| IRF-SKL-003 | P2 | Skills governance metadata enrichment — continue from S17 baseline | Agent | S17 | None |

### The Index Apparatus

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-IDX-001 | P1 | Build INST-INDEX-LOCORUM.md — canonical map of where everything lives: repos (117), directories, key files, URLs, infrastructure endpoints (Cloudflare, GitHub orgs, D1 databases), deployment targets, MCP servers | Agent | This session | Pattern: INST-INDEX-RERUM-FACIENDARUM.md |
| IRF-IDX-002 | P1 | Build INST-INDEX-NOMINUM.md — registry of all named entities: 8 organs, 117 repos, CLI tools (organvm, alchemia, ontologia), agent personas (Architect/QA Lead/Operator/Auditor), 22 regimes, 8 Watcher Orders, 18 SPECs, 64+ SOPs, 3 dissertations (D-001/D-002/D-003), 8 faculties, named protocols (Testament, Descent, Membrane, Styx), people (Chris, the Provost) | Agent | This session | Data exists across registry-v2.json, seed.yaml files, governance docs |
| IRF-IDX-003 | P1 | Build INST-INDEX-RERUM.md — ontological inventory of what exists: every artifact type (YAML spec, Python module, Markdown research, SVG visual, YAML regime, test file, dissertation chapter), its state (implemented/specified/planned), relationships (produces/consumes, depends-on, references), provenance (which session, which commit) | Agent | This session | Ontologia UID system exists for entity identity |

### Monitoring & Auditing

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-MON-001 | P2 | Deploy vigiles-aeternae watcher orders as scheduled monitoring agents (cron/Actions) | Agent | Wants list, S12 | Code exists, deployment config needed |
| IRF-MON-002 | P2 | Connect auditor findings to omega scorecard — watchers report on criteria health | Agent | Wants list | None |
| IRF-MON-003 | P3 | Continuous auditor mode — IRA running on schedule, not just on-demand | Agent | Wants list | Needs deployment infrastructure |

---

## META — Corpus (organvm-corpvs-testamentvm)

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-CRP-001 | P1 | Omega scorecard: advance from 4/17 toward next achievable criteria | Agent | S13 | None |
| IRF-CRP-002 | P2 | Registry-v2.json maintenance — keep in sync as repos evolve | Agent | S3-7 | Ongoing |
| IRF-CRP-003 | P2 | Testament Protocol — verify chain integrity after recent sessions | Agent | S7 | None |

---

## META — Praxis Perpetua (SGO)

### Research Corpus (COMPLETE)

All 7 research prompts from INQ-2026-004 are delivered:

| Prompt | Document | Lines | Session |
|--------|----------|-------|---------|
| 1 — Intellectual genealogy | `research/intellectual-genealogy/` | ~800 | S8 |
| 2 — Aesthetic movements | `research/aesthetic-movements/` | ~800 | S9 |
| 3 — Solo auteur to studio | `research/solo-auteur-to-studio/` | ~800 | S10 |
| 4 — Trash and church | `research/trash-and-church/` | ~800 | S16 |
| 5 — Radical authenticity | `research/radical-authenticity/` | 800 + 427 | S20 |
| 6 — Alchemy as structure | `research/alchemical-system-lifecycle/` | 801 | S21 |
| 7 — System as genre | `research/system-as-genre/` | 715 | S22 |

### Dissertations

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-SGO-001 | P1 | D-003 spec review: work through GitHub issues #17-#24 (8 issues) | Agent | S18 | None |
| IRF-SGO-002 | P2 | Write first dissertation chapter — convert research corpus into D-003 Ch 1 | Agent | S4, S8-22 | 170K+ words of research available |
| IRF-SGO-003 | P2 | D-001 needs: 3+ months v2 outcome data, retrospective comparison, MPI test | Human | inquiry-log.yaml | Time-gated (need outcome data) |
| IRF-SGO-004 | P2 | D-002 needs: second instantiation, human baseline, expanded panel, longitudinal data | Agent+Human | inquiry-log.yaml | Partially time-gated |
| IRF-SGO-005 | P2 | Add governance YAMLs to praxis-perpetua (Phase 1 roadmap next step) | Agent | Memory | None |
| IRF-SGO-006 | P3 | Build defense.py, publish.py, senate.py — SGO defense orchestration scripts | Agent | SGO spec | Depends on IRA code maturity |

### SGO Infrastructure (EXISTS)

Verified on disk 2026-03-20:
- `governance/charter.yaml` — constitutional document
- `governance/defense-protocol.yaml` — formal defense rules
- `governance/faculty-registry.yaml` — faculty definitions + rubrics
- `governance/senate-config.yaml` — panel composition rules
- `commissions/inquiry-log.yaml` — active research commissions
- `defenses/records/` + `defenses/transcripts/` — ready for use
- `publications/arxiv/` + `publications/journal/` + `publications/distilled/` — publication pipeline directories

---

## META — Vigiles Aeternae (IMPLEMENTED)

Verified on disk 2026-03-20 — full Python package:

**Source:** `src/vigiles_engine/` — 10 modules:
`auditor.py`, `orders.py`, `regime.py`, `consensus.py`, `divergence.py`, `chronicle.py`, `phaethon.py`, `reporter.py`, `cli.py`, `__init__.py`

**Data:** 22 regime YAMLs in `regimes/`, 8 Watcher Order YAMLs in `orders/`

**Tests:** 8 test files (test_auditor, test_orders, test_regime, test_consensus, test_divergence, test_chronicle, test_phaethon, test_reporter)

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-VIG-001 | P2 | Deploy as scheduled monitoring (cron or GitHub Actions) | Agent | S12 | Deployment config needed |
| IRF-VIG-002 | P2 | Integrate audit reports with system-dashboard | Agent | S12 | None |

---

## META — Trivium / Dialectica Universalis (IMPLEMENTED)

Verified on disk 2026-03-20:

**Spec:** `specs/SPEC-018.md`, `SPEC-018--dialect-taxonomy.md`, `SPEC-018--risk-register.md`

**Engine:** `organvm-engine/src/organvm_engine/trivium/` — 10 source files:
`dialects.py`, `taxonomy.py`, `detector.py`, `translator.py`, `synthesis.py`, `sources.py`, `content.py`, `edges.py`, `kinship.py`, `__init__.py`

**Tests:** 13 test files in `organvm-engine/tests/test_trivium_*.py`

**Plan:** `.claude/plans/2026-03-20-trivium-dialectica-universalis.md`

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-TRV-001 | P2 | Verify all tests pass, integrate into CI | Agent | Wants list | None |
| IRF-TRV-002 | P3 | Testament integration — add `trivium` to MODULE_SOURCES with PHILOSOPHICAL modality | Agent | Plan file | None |

---

## META — Testament Protocol (IMPLEMENTED)

Verified on disk 2026-03-20:

**Engine:** `organvm-engine/src/organvm_engine/testament/` — `pipeline.py`, `sources.py`, `manifest.py`, `network.py`, `aesthetic.py`, `catalog.py` + 6 renderers (sonic, statistical, social, html, prose, svg)

**Artifacts:** 30+ per-repo SVGs in `testament/artifacts/repos/`, sonic params, social pulse, self-portrait

**Network:** `network-map.yaml` with 3 lenses

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-TST-001 | P2 | Verify chain integrity post-22-session burst | Agent | S7 | None |

---

## ORGAN-II — Object Lessons

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-OBJ-001 | P0 | `npx wrangler pages secret put COLLABORATOR_PASSWORD` | Human | S19 | None |
| IRF-OBJ-002 | P0 | Share `https://object-lessons.pages.dev` with Chris | Human | S19 | None |
| IRF-OBJ-003 | P1 | Replace YouTube ID placeholders for 4 V1 episodes | Human | S19 | Need to look up IDs |
| IRF-OBJ-004 | P1 | Acquire `objectlessons.film` domain, point to Cloudflare Pages | Human | S19 | Domain availability |
| IRF-OBJ-005 | P1 | Add film stills/thumbnails to `public/images/` | Human | S19 | Need source images |
| IRF-OBJ-006 | P2 | Expand film database 253 → 302+ (omitted Tier 3 films) | Agent | S19 | None |
| IRF-OBJ-007 | P2 | Connect GitHub repo to Cloudflare Pages for auto-deploy on push | Agent | S19 | None |

---

## ORGAN-IV — Skills (a-i--skills)

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-SKL-001 | P2 | Map 142 skills to design-process phases | Agent | Wants list | Phase taxonomy needed |
| IRF-SKL-002 | P2 | Auto-trigger universal standards skills on push | Agent | Wants list | Depends on IRF-SKL-001 |

---

## ORGAN-VII — Kerygma (Distribution)

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-KER-001 | P3 | Build POSSE syndication pipeline — auto-post changes to socials | Agent | Wants list | ORGAN-VII repos exist but no automation |
| IRF-KER-002 | P3 | Connect Testament events to social distribution | Agent | Wants list | Depends on IRF-KER-001 |

---

## PERSONAL — Portfolio

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-PRT-001 | P2 | Performance job timeout (15min for 18 Lighthouse runs) — parallelize or subset | Agent | S15 | None |

---

## PERSONAL — Application Pipeline

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-APP-001 | P2 | Collect 3+ months v2 outcome data for D-001 | Human | inquiry-log.yaml | Time-gated |

---

## Generative Visuals

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-GEN-001 | P2 | Design generative art pipeline reading `organ-aesthetic.yaml` → per-organ visual identity | Agent | Wants list | Needs design spec |
| IRF-GEN-002 | P2 | Extend OG image generator pattern (S19) to system-wide use | Agent | S19 | Pattern exists in object-lessons |
| IRF-GEN-003 | P3 | Per-repo visual signatures derived from code characteristics | Agent | Wants list | Needs algorithm design |

---

## IRA / Evaluative Authority

Verified on disk 2026-03-20:

**Code:** `application-pipeline/scripts/diagnose_ira.py` — pure-stdlib ICC, Cohen's kappa, Fleiss kappa with Landis & Koch bands.
**Tests:** `tests/test_diagnose_ira.py`, `tests/test_math_proofs.py`, `tests/test_standards.py`
**Supporting:** `scripts/generate_ratings.py`, `scripts/standards.py`

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-IRA-001 | P2 | Second instantiation: deploy authority against ORGAN-IV (Taxis) | Agent | inquiry-log.yaml | None |
| IRF-IRA-002 | P2 | Human baseline: 3 expert engineers rate the pipeline; compare ICC | Human | inquiry-log.yaml | Need human raters |
| IRF-IRA-003 | P3 | Expand panel to 7 raters across 3 providers | Agent | inquiry-log.yaml | Depends on IRF-IRA-001 |

---

## Session Triage Findings (This Session — 2026-03-20)

Items discovered during the 22-session triage and filesystem verification that don't fit existing sections:

### Cross-Organ Architecture

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-ARC-001 | P1 | Persist this session's 22-session ledger as a canonical session archive (not just conversation memory) | Agent | This session | None |
| IRF-ARC-002 | P2 | Build session-to-IRF pipeline — every session close should check for new IRF items | Agent | This session | Needs hook or SOP |
| IRF-ARC-003 | P2 | Cross-session dependency map — which sessions' outputs feed into which other sessions | Agent | This session (S4→S8-10, S16, S18, S20-22 chain identified) | None |
| IRF-ARC-004 | P2 | Resolve old org alias remotes — local repos may still reference ivviiviivvi, omni-dromenon-machina, labores-profani-crux | Agent | Memory | Need per-repo audit |
| IRF-ARC-005 | P2 | Unarchive blocked repos on GitHub — 8 repos across 3 orgs can't push (see Memory: Archived repos) | Human | Memory | Need GitHub settings access |
| IRF-ARC-006 | P2 | Protected branch repos — 5 repos need PR + review approval, can't direct-push | Human | Memory | GitHub branch protection rules |

### Blockchain & Provenance

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-BLK-001 | P3 | Evaluate: publish Testament hash-chain attestations to external blockchain (Ethereum/Solana) for public verifiability | Agent | Wants list | Design decision needed: local chain sufficient vs. external attestation |
| IRF-BLK-002 | P2 | Connect Testament events to change tracking — every commit, promotion, governance change gets a chain entry | Agent | Wants list | Testament engine exists, needs event wiring |

### Documentation Gaps Identified

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-DOC-001 | P2 | Document the Vigiles Aeternae Python API — no public documentation beyond code | Agent | Filesystem verification | None |
| IRF-DOC-002 | P2 | Document the Trivium engine API — 10 modules, no usage guide | Agent | Filesystem verification | None |
| IRF-DOC-003 | P2 | Document IRA diagnostic tooling — diagnose_ira.py usage, rubric format, ratings format | Agent | Filesystem verification | None |
| IRF-DOC-004 | P1 | Verify all Vigiles tests pass: `pytest tests/` in vigiles-aeternae repo | Agent | Filesystem verification (.pytest_cache exists, tests may have drifted) | None |
| IRF-DOC-005 | P1 | Verify all Trivium tests pass: `pytest organvm-engine/tests/test_trivium_*.py` | Agent | Filesystem verification (13 test files exist) | None |

### Verification Debts (from this session's corrections)

| ID | Priority | Action | Owner | Source | Blocker |
|----|----------|--------|-------|--------|---------|
| IRF-VER-001 | P1 | Run full test suite across all META repos: engine, vigiles, trivium, alchemia, ontologia, mcp-server, dashboard | Agent | This session (claimed "complete" without running tests) | None |
| IRF-VER-002 | P1 | Verify praxis-perpetua research directory paths match the ledger (some paths in session transcripts may differ from actual disk) | Agent | This session | None |
| IRF-VER-003 | P2 | Audit all 22 session commits for unpushed branches or stale feature branches | Agent | This session | None |

---

## Completed (from 22-session cataloguing, 2026-03-20)

| ID | What | Session | Date |
|----|------|---------|------|
| DONE-001 | Application pipeline v2 with clearance gates | S1-2 | 2026-03-20 |
| DONE-002 | Testament Protocol — hash-linked event chain with flock | S3, S5-7 | 2026-03-20 |
| DONE-003 | 7/7 research prompts delivered (170K+ words) | S8-10, S16, S20-22 | 2026-03-20 |
| DONE-004 | Descent Protocol 22%→78% | S11 | 2026-03-20 |
| DONE-005 | Vigiles Aeternae — 22 regimes, 8 orders, full Python engine | S12 | 2026-03-20 |
| DONE-006 | Omega scorecard amendment | S13 | 2026-03-20 |
| DONE-007 | Dotfiles/chezmoi/PAT fix/permissions | S14 | 2026-03-20 |
| DONE-008 | Portfolio — 496 tests, 0 vulns, CI/CD | S15 | 2026-03-20 |
| DONE-009 | Skills 105→142 with governance metadata | S17 | 2026-03-20 |
| DONE-010 | D-003 dissertation design spec | S18 | 2026-03-20 |
| DONE-011 | Object Lessons website — deployed to Cloudflare | S19 | 2026-03-20 |
| DONE-012 | Trivium / Dialectica — SPEC-018 + engine module + 13 tests | Prior sessions | Pre-2026-03-20 |
| DONE-013 | IRA diagnostic code — ICC/kappa/consensus computation | Prior sessions | Pre-2026-03-20 |
| DONE-014 | 22-session triage, cataloguing, and filesystem verification | This session (S23) | 2026-03-20 |
| DONE-015 | Index Rerum Faciendarum — universal work registry created | This session (S23) | 2026-03-20 |
| DONE-016 | Wants-vs-sessions tracking with corrected completion states | This session (S23) | 2026-03-20 |

---

## Blocked

*None currently.*

---

## Archived

*None currently.*

---

## Statistics

- **Total active items:** 52
- **P0 (NOW):** 2 (both human-gated: collaborator password, share URL)
- **P1 (SOON):** 13 (includes 3 companion indices, 4 verification items, test runs)
- **P2 (GROWTH):** 28
- **P3 (HORIZON):** 9
- **Completed:** 16
- **Blocked:** 0

### By Domain

| Domain | Active | Completed | Total |
|--------|--------|-----------|-------|
| SYS (System-wide) | 5 | 0 | 5 |
| IDX (Index apparatus) | 3 | 1 | 4 |
| SKL (Skills) | 3 | 1 | 4 |
| MON (Monitoring) | 3 | 0 | 3 |
| CRP (Corpus) | 3 | 0 | 3 |
| SGO (Studium) | 6 | 3 | 9 |
| VIG (Vigiles) | 2 | 1 | 3 |
| TRV (Trivium) | 2 | 1 | 3 |
| TST (Testament) | 1 | 1 | 2 |
| OBJ (Object Lessons) | 7 | 1 | 8 |
| KER (Kerygma) | 2 | 0 | 2 |
| PRT (Portfolio) | 1 | 1 | 2 |
| APP (Application) | 1 | 1 | 2 |
| GEN (Generative) | 3 | 0 | 3 |
| IRA (Authority) | 3 | 1 | 4 |
| ARC (Architecture) | 6 | 0 | 6 |
| BLK (Blockchain) | 2 | 0 | 2 |
| DOC (Documentation) | 5 | 0 | 5 |
| VER (Verification) | 3 | 3 | 6 |
| **TOTAL** | **60** | **16** | **76** |

---

*Last updated: 2026-03-20 — Session: 22-session triage, filesystem verification, and index construction*
*Next update: After any session that produces or discovers work items*
