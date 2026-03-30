# organvm Project Constitution

**Version:** 1.1.0 | **Ratified:** 2026-02-10 | **Last Amended:** 2026-03-04
**Source:** `CLAUDE.md` Key Invariants (lines 28-34) + `08-canonical-action-plan.md` §2 stable consensus

## Core Principles (Articles I-VI)

### I. Registry as Single Source of Truth
All repo state lives in `registry-v2.json`. The registry is never wrong; if reality and registry disagree, update the registry or fix reality. No document, workflow, or agent may claim authoritative repo state outside the registry.

### II. Unidirectional Dependencies
Flow is I->II->III only. No back-edges: ORGAN-III cannot depend on ORGAN-II; ORGAN-II cannot depend on ORGAN-III. ORGAN-IV orchestrates; ORGAN-V documents; ORGAN-VII amplifies. Dependency violations are structural failures, not style issues.

### III. All Eight Organs Visible at Launch
Each organ has at least one representative at launch — flagship (fully documented) or stub (purpose, status, and link to parent org). The eight-organ system must be visible in its entirety; individual organs may launch at different completeness tiers per Amendment A. "Visible" means a grant reviewer navigating all 8 orgs encounters evidence of each organ's existence and purpose, not that every repo is complete.

### IV. Documentation Precedes Deployment
No Phase N+1 until Phase N is complete. Documentation is the deliverable, not an afterthought. Every README is written before the feature it documents is promoted.

### V. Portfolio-Quality Documentation
Every README is a portfolio piece, written for grant reviewers and hiring managers, not just developers. The "Stranger Test" applies: a grant reviewer seeing this for the first time should be convinced.

### VI. Promotion State Machine
Repos follow: LOCAL -> CANDIDATE -> PUBLIC_PROCESS -> GRADUATED -> ARCHIVED. This governs cross-organ promotion. Repo documentation status uses a separate vocabulary: ACTIVE/DEPLOYED/SKELETON/EMPTY. No state may be skipped.

## Amendments (Post-Cross-Validation Consensus)

### Amendment A: Bronze Tier Launch Path
*Source: SC-2, D-08 in `08-canonical-action-plan.md`*

The Bronze Sprint produces the Minimum Viable Launch: 5 flagships (one per organ I-V) + stubs for VI-VII + hardened registry + process essay. Completion is criteria-driven (D-08 success criteria), not time-boxed. "5 Perfect Repos > 44 Mediocre Repos."

### Amendment B: Coordination Overhead Budget
*Source: SC-3, B7 in `06-evaluation-to-growth-analysis.md`*

Budget 10% of phase TE as explicit line item for reconciling parallel AI streams. Coordination overhead is real and must not be hidden inside task estimates.

### Amendment C: Registry Schema Completeness
*Source: SC-1 in `08-canonical-action-plan.md`*

`registry-v2.json` must include `dependencies[]`, `promotion_status`, `tier`, and `last_validated` fields before Phase 2. Schema evolves iteratively during Bronze (fields added as workflows need them, locked after majority of flagships are drafted).

### Amendment D: AI Non-Determinism Acknowledgment
*Source: Meta-finding in `THREE_CLI_COMPARISON_ANALYSIS.md`*

Same inputs produce different strategic outputs across AI models and across time. All AI-generated deliverables require human review. Budget estimates use scenario banding (ranges), not point estimates, to reflect this variance.

## Quality Gates

### Registry Gate
Does this deliverable update `registry-v2.json`? Is the schema satisfied? Are all required fields populated with verified (not aspirational) data?

### Portfolio Gate
Does this README or essay pass the "Stranger Test" (D-08, Copilot validation §7)? Would a grant reviewer seeing this for the first time be convinced? Score >=90/100 on the `01` rubric for flagships.

### Dependency Gate
Does this deliverable respect the I->II->III flow? No back-edges? Cross-references follow the dependency direction?

### Completeness Gate
Are all TBD markers resolved? 0 broken links? No placeholder content in shipped deliverables?

### Signal Closure Gate
Does this organ's active work have declared produces edges for all entailed outputs per the `entailment_flows` matrix in `governance-rules.json`? Are all downstream organs receiving the signals this activity logically entails? Validate with `organvm governance audit --signal-closure`.

### Triadic Self-Knowledge Gate
Does this formation's `seed.yaml` articulate all three dimensions: telos (the dream), pragma (the reality), and praxis (the plan to close the gap)? Are the fields genuine self-knowledge, not placeholder text? Does a stranger reading them understand why this formation exists, what it has achieved, and what remains? Validate with `organvm governance audit --self-knowledge`.

### Amendment E: Post-Construction Operational Shift
*Source: CONSTITUTIO sprint review (2026-03-04), REGULA governance update*

The system has transitioned from **construction** (building, documenting, deploying) to **operation** (sustaining, validating, evolving). Implications:
- Article III (all organs visible at launch) is **SATISFIED** — all 8 organs are operational (launched 2026-02-11). This article now governs any new organ additions, not existing ones.
- Article IV (documentation precedes deployment) applies to **new features and promotions**, not retroactive documentation of already-deployed repos.
- Amendment A (Bronze Tier Launch Path) is **COMPLETED** — Bronze, Silver, and Gold sprints are done. Amendment A remains as historical record of the launch methodology.
- Amendment C (Registry Schema Completeness) is **COMPLETED** — all required fields are present and validated. Schema formalized as v1.0.0.
- Quality gates remain active for all ongoing work. The Portfolio Gate and Stranger Test become increasingly important as external audiences grow.

### Amendment F: Signal Closure — Lex Necessitatis
*Source: First-principles derivation from Article II (unidirectional dependencies), Constitutional Map §8 (signal flows), AX-2 (epistemic membranes), and the operational principle "N/A is a vacuum." Ratified 2026-03-27.*

The organ system is logically closed under its own axioms. The definitions of organ functions, the canonical signal flows, and the epistemic membrane requirement together constitute a deductive system: given the axioms, certain inter-organ outputs are not optional but logically necessary. An activity in Ergon (III) that does not produce process documentation (→ Logos V), distribution material (→ Kerygma VII), community growth signals (→ Koinonia VI), or research feedback (→ Theoria I) violates the signal flow graph's own definitions.

This principle is deductive, not aspirational. Law is law; logic dictateth. If the axioms are what they are, the conclusions follow — regardless of whether the receiving formations have been built yet. Absence is not deferral; it is violation. Every entailed output that exists nowhere in the system is a vacuum that constitutional law mandates be filled. What is omitted here must, by law, exist elsewhere. What exists nowhere is a constitutional breach.

Implications:
- Every `seed.yaml` `produces` array must declare ALL entailed outputs, not only primary ones
- `organvm governance audit --signal-closure` validates organ-level signal completeness
- IRF-VAC entries are created for any entailed output lacking a receiving formation
- The `entailment_flows` section of `governance-rules.json` is the authoritative reference for which activities entail which outputs
- The Signal Closure Gate is now a mandatory quality gate for all deliverables

Encoded as: AX-6 (Signal Closure) + LIQ-008 (Signal Closure Across Functions) in `governance-rules.json`.

### Amendment G: Triadic Self-Knowledge — Lex Reflexionis
*Source: First-principles derivation from the observation that every directory is the concrete realization of an idealized form — an intersection of functionalities at work. Ratified 2026-03-30.*

Every non-archived formation in the system embodies an idealized form. That form has three constitutive dimensions:

1. **TELOS** (τέλος) — The theory, thesis, or dream that called the formation into existence. The intersectional functionalities it idealizes. Why it was conceived. What the world looks like if this formation achieves its purpose.

2. **PRAGMA** (πρᾶγμα) — The concrete thing realized. The honest account of what has been built, how far it is from the ideal, and where the delta lies. Not a description of features but a truthful reckoning of state.

3. **PRAXIS** (πρᾶξις) — The remediation plan. The attack vectors for sharpening and fortifying. The specific actions that close the gap between ideal and real. Not aspirational roadmap but concrete plans of attack addressing known failures and deficiencies.

Insights and theories are not ephemeral. They are structural obligations. Every directory in the system — since at its core it is an idealized form of some intersectional functionalities at work — has dreams for the dream that formed it, the concrete realized, and plans of attack for the difference between them. These three must be explicitly articulated, not left implicit in the developer's head or scattered across undiscoverable session logs.

**Implications:**
1. Every non-archived `seed.yaml` must include `telos`, `pragma`, and `praxis` fields (schema v1.2)
2. Empty or placeholder values are violations — the fields demand genuine self-knowledge
3. The triadic fields are consumed by: context generation (`organvm context sync`), signal routing (a formation that doesn't know its own purpose can't participate coherently in signal flows), audit (`organvm governance audit --self-knowledge`), and the Stranger Test (a reviewer encountering the formation should immediately understand its dream, its reality, and its plan)
4. The fields evolve as the formation evolves — they are living documents, not static declarations
5. AX-7 extends AX-6: signal closure requires that outputs exist elsewhere; triadic self-knowledge requires that the *reason for those outputs* is articulated within

Encoded as: AX-7 (Triadic Self-Knowledge) + RR-6 (Triadic Articulation) + LIQ-009 (Reflexive Knowledge Obligation) in `governance-rules.json`.

## Post-Launch Reviews

### Review 1 (2026-03-04) — CONSTITUTIO Sprint

**Reviewer:** @4444j99 (AI-conductor review)

**Findings:** All 6 core articles remain valid and enforced. No article requires modification. The constitution successfully governs post-launch operations as written.

| Article | Status | Notes |
|---------|--------|-------|
| I. Registry as SSOT | ACTIVE | registry-v2.json at schema v1.0.0, 103 repos tracked |
| II. Unidirectional Deps | ACTIVE | 0 back-edge violations. ORGAN-III→VI/VII edges are forward (higher→lower organ flow for community/distribution) |
| III. Eight Organs Visible | SATISFIED | All 8 organs operational since 2026-02-11 |
| IV. Doc Precedes Deploy | ACTIVE | Governs ongoing promotions and new features |
| V. Portfolio-Quality Docs | ACTIVE | Stranger Test not yet executed (omega #2) |
| VI. Promotion State Machine | ACTIVE | 68 CANDIDATE, 12 PUBLIC_PROCESS, 4 GRADUATED |

**Amendments status:** A (completed), B (active), C (completed), D (active), E (active), F (ratified 2026-03-27).

**Next review:** After stranger test execution (omega #2) or at 60-day post-launch mark, whichever comes first.

## Machine-Readable Constitution (Dictums)

The `dictums` section of `governance-rules.json` is the authoritative machine-readable encoding of this constitution's structural laws. It encodes three tiers:

- **Axioms (AX-*):** Universal invariants (AX-1 DAG, AX-2 Epistemic Membranes, AX-3 TTL Eviction, AX-4 Registry Coherence, AX-5 Organ Placement, AX-6 Signal Closure)
- **Organ Dictums (OD-*):** Per-organ constraints (OD-I through OD-VII + OD-META)
- **Repo Rules (RR-*):** Per-repository requirements (RR-1 Seed Contract, RR-2 SRP, RR-3 Event Handshake)

Each dictum declares enforcement mode (`automated`/`audit`/`manual`) and severity (`critical`/`warning`/`info`). Automated dictums are checked by validators in `organvm-engine/governance/dictums.py`.

**CLI commands:**
- `organvm governance dictums` — list all dictums
- `organvm governance dictums --check` — run compliance validators
- `organvm governance dictums --id AX-1` — show specific dictum
- `organvm governance audit` — includes dictum violations in full audit

**MCP tools:**
- `organvm_governance_dictums` — list dictums (optional `level` filter)
- `organvm_governance_check_dictums` — run compliance checks

## Governance

This constitution supersedes ad-hoc decision-making for the organvm project. All specifications (`docs/specs/`) and planning documents must be validated against these articles, amendments, and gates before execution.

Amendments require: (1) documented rationale with source citation, (2) human approval by @4444j99, (3) propagation to all affected documents per the E2G coherence review pattern established in `09-corpus-coherence-review.md`.
