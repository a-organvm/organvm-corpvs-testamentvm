# SPEC-025: Institutional Primitive Vocabulary

```
Document ID:      SPEC-025
Title:            Institutional Primitive Vocabulary
Version:          1.0
Status:           DRAFT
Layer:            L1 — Metaphysical Identity
Authoritative:    Institutional primitive definitions, irreducibility criteria, execution mode taxonomy
Parent Specs:     SPEC-000 (System Manifesto), SPEC-002 (Primitive Register), SPEC-019 (Liquid Constitutional Order)
Extends:          SPEC-002 (adds institutional primitives to the conceptual primitive register)
Date Drafted:     2026-04-20
Principal Author: https://orcid.org/0009-0008-2007-3596
```

---

## 0. Preamble

SPEC-002 defines 7 irreducible conceptual primitives: Entity, Value, Relation, Event, State, Constraint, Capability. These govern what the system *is* and how it *reasons about itself*.

This specification extends the primitive vocabulary into the **institutional domain** — the operations required for a single principal to achieve institutional-grade agency. Where SPEC-002 defines ontological primitives (what things ARE), SPEC-025 defines operational primitives (what things DO in the service of institutional power).

### 0.1 The Gap

The ORGANVM system, as launched (2026-02-11), operates as a production-and-distribution engine. It lacks the institutional substrate that configures, protects, amplifies, and perpetuates the principal's position within larger power structures. SPEC-025 provides the primitive vocabulary from which institutional formations crystallize.

### 0.2 Design Axiom

**Ideal form logic takes precedence.** The primitive vocabulary is derived from irreducibility analysis of institutional operations, not from the convenience of implementation or the structure of existing organs. If an operation is irreducible (cannot be decomposed into two operations that make independent sense), it is primitive. If it is composite, it is a formation.

### 0.3 Relationship to SPEC-019

SPEC-019 (Liquid Constitutional Order) establishes that numbered organs yield to named physiological functions with signal signatures. The institutional primitives are the operational atoms from which these physiological functions compose. They inhabit the same shared pool as production primitives (reader, writer, publisher, etc.) — there is no separate "institutional layer."

---

## 1. Irreducibility Criterion

A candidate primitive is admitted to the register if and only if:

1. **Non-decomposability**: It cannot be split into two operations that execute independently and produce meaningful output separately.
2. **Non-redundancy**: No existing primitive (ontological or institutional) already covers its irreducible operation.
3. **Universality**: It appears as a component in at least three distinct institutional formations across different domains (legal, financial, relational, structural).
4. **Operationality**: It names an operation (verb-like), not a domain (noun-like). "Legal" is a domain. "Assessing liability" is an operation.

Primitives that fail any criterion are either decomposed (split into constituent primitives) or reclassified as formations (compositions of existing primitives).

---

## 2. The Primitive Interface Contract

Every institutional primitive conforms to a single interface shape:

```
PRIM-INST(context, frame, principal_position) → (output, confidence, escalation_flag, audit_trail)
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `context` | Signal | The situation, data, and environmental state under consideration |
| `frame` | Constraint | The normative/strategic frame to apply (legal, financial, relational, etc.) |
| `principal_position` | State | Current state, interests, and objectives of the principal |
| `output` | Value | The result of the primitive's operation |
| `confidence` | Scalar [0,1] | Self-assessed reliability — determines execution mode escalation |
| `escalation_flag` | Boolean | Whether human involvement is required before downstream consumption |
| `audit_trail` | Event | What was done, why, and on what basis (consumed by archivist, auditor) |

This contract maps to SPEC-002 primitives: context is an Entity carrying State; frame is a Constraint; principal_position is a State; output is a Value; audit_trail is an Event.

---

## 3. Execution Mode Taxonomy

Each primitive invocation selects an execution mode based on confidence and stakes:

| Mode | Trigger | Character |
|------|---------|-----------|
| **AI-performed** | confidence ≥ 0.8 AND stakes ≤ routine | Primitive executes autonomously via AI agent |
| **AI-prepared, human-reviewed** | 0.5 ≤ confidence < 0.8 OR stakes = significant | AI produces output; human reviews before downstream propagation |
| **Human-routed** | confidence < 0.5 OR stakes = critical OR novel situation | AI prepares context; routes to human professional for execution |
| **Protocol-structured** | Operation is deterministic given inputs | Executed by rule/automation without AI judgment (e.g., recurring transfers, scheduled filings) |

Execution mode is per-invocation, not per-primitive. The same primitive may execute differently depending on context. The confidence threshold and stakes assessment are themselves primitive operations (performed by the assessor primitive in meta-mode).

---

## 4. The Institutional Primitive Register

### 4.1 PROTECTIVE CLUSTER

Primitives governing the preservation of what exists.

---

#### PRIM-INST-001: ASSESSOR

**Irreducible operation**: Evaluates a situation, asset, relationship, or obligation against a normative frame and returns a structured risk/opportunity profile.

**Distinction from production primitives**: `analyzer` (production) extracts patterns from data. `assessor` applies a normative frame to determine exposure, liability, or advantage. Analyzer answers "what is happening." Assessor answers "what does this mean for you."

**Default execution modes**: AI-primary (routine), human-routed (novel/high-stakes).

**Signal output type**: Risk/opportunity profile (structured assessment with quantified exposure and identified action vectors).

**Universality evidence**: Appears in Aegis (threat assessment), Oikonomia (entitlement assessment), Praxis (market assessment), Tessera (standing assessment). Domain-independent — frame parameter determines whether assessment is legal, financial, relational, or strategic.

---

#### PRIM-INST-002: GUARDIAN

**Irreducible operation**: Maintains a watchlist of interests, rights, deadlines, and obligations; triggers alerts and defensive responses when thresholds are crossed.

**Distinction from other primitives**: Guardian does not decide what to protect (that comes from assessor output) and does not act on violations (that is enforcer). Guardian watches and triggers. It is the sensing membrane.

**Default execution modes**: Protocol-structured (monitoring), AI-performed (alerting), human-routed (response decisions).

**Signal output type**: Alert signal (threshold crossed, with context payload for downstream assessment).

**Universality evidence**: Aegis (threat monitoring), Oikonomia (cash flow thresholds), Tessera (registration/license expiry), any formation requiring continuous awareness.

---

#### PRIM-INST-003: ADVOCATE

**Irreducible operation**: Constructs and presents arguments optimized for a specific audience and decision-maker on behalf of the principal's interests.

**Key property**: Advocate always argues FROM a position. It does not weigh both sides (that is assessor's job). It takes an assessed position and makes the strongest possible case for it.

**Default execution modes**: AI-primary (drafting), human-performed (delivery in adversarial/legal contexts), hybrid (negotiation prep).

**Signal output type**: Argument structure (claim, evidence, warrant, tailored to audience).

**Universality evidence**: Aegis (legal defense), Praxis (pitch/proposal), Tessera (formal applications), any context requiring persuasion toward the principal's interest.

---

#### PRIM-INST-004: INSULATOR

**Irreducible operation**: Creates structural separation between domains to limit liability propagation, information leakage, or risk contagion.

**Institutional analogue**: The corporate veil. LLCs, NDAs, separate accounts, compartmented information — all are insulator instantiations.

**Default execution modes**: Protocol-structured (entity structures, information barriers), AI-performed (document/communication separation analysis).

**Signal output type**: Separation schema (what is compartmented from what, via what mechanism).

**Universality evidence**: Praxis (entity separation for contracts), Tessera (compartmentalized identity presentation), Oikonomia (account separation), any formation interfacing with adversarial entities.

---

### 4.2 ECONOMIC CLUSTER

Primitives governing the generation and management of value flows.

---

#### PRIM-INST-005: APPRAISER

**Irreducible operation**: Determines the exchange value of an asset, service, obligation, or opportunity in a specific market context.

**Distinction from assessor**: Assessor evaluates risk/opportunity profiles. Appraiser determines what something is worth in exchange. Assessor says "this lease exposes you to X risk." Appraiser says "this lease is worth $Y to exit."

**Default execution modes**: AI-primary (market comparables, standard assets), human-routed (novel/illiquid assets).

**Signal output type**: Valuation (with comparables, methodology, confidence band).

**Universality evidence**: Oikonomia (asset/entitlement valuation), Praxis (service pricing), Aegis (damage quantification), any context requiring a price.

---

#### PRIM-INST-006: LEDGER

**Irreducible operation**: Records, categorizes, and maintains the authoritative state of all value flows (monetary, equity, obligation, receivable).

**Key property**: Ledger is the irreducible act of maintaining an authoritative record of economic state. Everything from a bank balance to an equity cap table to an IOU is a ledger entry. It is not "accounting software" — it is the ontological ground of economic awareness.

**Default execution modes**: Protocol-structured (double-entry, immutable logs), AI-performed (categorization, reconciliation).

**Signal output type**: Economic state snapshot (current position across all value domains).

**Universality evidence**: Oikonomia (central economic state), Praxis (project economics), Aegis (exposure quantification), any formation requiring knowledge of what the principal has, owes, or is owed.

---

#### PRIM-INST-007: OPTIMIZER

**Irreducible operation**: Given a set of constraints and an objective function, determines the allocation of resources (time, money, attention, entity structure) that maximizes the objective.

**Key property**: Optimizer determines the IDEAL allocation. It does not execute (allocator does that). Optimizer is strategy; allocator is treasury.

**Default execution modes**: AI-primary (computation), human-routed (objective-setting and constraint validation).

**Signal output type**: Allocation plan (resource → destination mapping with rationale).

**Universality evidence**: Oikonomia (survival allocation), Praxis (effort allocation across income streams), Aegis (defense resource allocation), any context with competing resource demands.

---

#### PRIM-INST-008: COLLECTOR

**Irreducible operation**: Identifies, tracks, and executes the conversion of receivables, entitlements, and owed obligations into realized value.

**Scope**: Not just invoices. Tax credits, benefit eligibility, contractual entitlements, refunds, equity distributions, insurance claims — anything owed to the principal that has not yet been realized.

**Default execution modes**: Protocol-structured (invoicing, payment schedules), AI-performed (tracking, reminders, eligibility identification), human-routed (enforcement, dispute escalation).

**Signal output type**: Collection action (what is owed, by whom, via what mechanism to realize).

**Universality evidence**: Oikonomia (receivables + entitlements), Praxis (invoice management), Aegis (damage collection), any context where value is owed but not yet in hand.

---

#### PRIM-INST-009: ALLOCATOR

**Irreducible operation**: Distributes available resources across competing demands according to a priority schema.

**Distinction from optimizer**: Optimizer determines the ideal allocation (strategic). Allocator executes the distribution (operational). Optimizer asks "what should the allocation be?" Allocator moves the resources.

**Default execution modes**: AI-primary (routine distribution), human-routed (priority-setting), protocol-structured (automatic transfers, scheduled payments).

**Signal output type**: Distribution record (what went where, when, per what authority).

**Universality evidence**: Oikonomia (resource distribution), Praxis (effort/time allocation), any formation with a budget or resource pool.

---

### 4.3 RELATIONAL CLUSTER

Primitives governing the interface between principal and world.

---

#### PRIM-INST-010: NEGOTIATOR

**Irreducible operation**: Conducts structured exchange of positions, concessions, and commitments between the principal and counterparties to reach an agreement.

**Key property**: Negotiator synthesizes advocate output (best case for position), assessor output (actual exposure), and appraiser output (what this is worth) into a dynamic interaction strategy. It manages the real-time give-and-take.

**Default execution modes**: Hybrid (AI-prepared, human-delivered in high-stakes; AI-performed in routine/automated contexts).

**Signal output type**: Agreement terms (or negotiation state if incomplete).

**Universality evidence**: Praxis (compensation, contracts), Oikonomia (debt negotiation), Tessera (relationship terms), any adversarial exchange toward mutual agreement.

---

#### PRIM-INST-011: REPRESENTATIVE

**Irreducible operation**: Presents a consistent, strategically calibrated identity and position to external parties on behalf of the principal.

**Key property**: Representative manages not just what is said but the coherence of the presented identity. It is the PR/spokesman/registered-agent function reduced to its primitive.

**Default execution modes**: AI-performed (routine communications, form responses), human-performed (high-context appearances), protocol-structured (standard disclosures).

**Signal output type**: Identity presentation (calibrated for specific audience and context).

**Universality evidence**: Tessera (central function), Praxis (professional presentation), any external-facing communication where identity coherence matters.

---

#### PRIM-INST-012: REGISTRAR

**Irreducible operation**: Maintains authoritative records of the principal's formal relationships, memberships, registrations, licenses, and standing with external entities.

**Distinction from credential (production primitive)**: Credential authenticates access. Registrar maintains the formal standing itself — business registrations, professional licenses, tax IDs, memberships, account relationships.

**Default execution modes**: Protocol-structured (databases, renewal schedules), AI-performed (filing, updating), human-routed (complex applications).

**Signal output type**: Standing record (entity relationship state with expiry/renewal metadata).

**Universality evidence**: Tessera (central function), Praxis (professional credentials), Aegis (insurance/benefit standing), any context where formal standing gates access.

---

#### PRIM-INST-013: LIAISON

**Irreducible operation**: Maintains an ongoing bidirectional relationship channel with a specific external entity, accumulating context and managing the relationship state over time.

**Distinction from representative**: Representative presents the principal's face (one-to-many, identity-focused). Liaison maintains the ongoing relationship with a SPECIFIC counterparty (one-to-one, relationship-focused). One representative function; many liaison instances.

**Default execution modes**: AI-performed (routine contact maintenance), human-performed (high-trust relationships), hybrid (AI-drafted, human-sent).

**Signal output type**: Relationship state (contact history, accumulated context, relationship health, next action).

**Universality evidence**: Tessera (relationship management), Praxis (client relationships), any sustained external engagement requiring accumulated context.

---

### 4.4 EPISTEMIC CLUSTER

Primitives governing institutional knowledge and judgment.

---

#### PRIM-INST-014: COUNSELOR

**Irreducible operation**: Synthesizes assessments, appraisals, and contextual knowledge into an integrated recommendation for action, explicitly surfacing trade-offs and second-order effects.

**Key property**: Counselor does not just analyze (assessor) or argue (advocate). It integrates across domains and recommends. This is the "trusted advisor" function — the boardroom-in-a-primitive.

**Default execution modes**: AI-primary (synthesis), human-routed (novel situations requiring judgment beyond training data).

**Signal output type**: Recommendation (action + trade-offs + second-order effects + confidence).

**Universality evidence**: Aegis (defense strategy recommendation), Oikonomia (financial strategy), Praxis (career/business strategy), any decision point requiring cross-domain synthesis.

---

#### PRIM-INST-015: AUDITOR

**Irreducible operation**: Independently verifies the accuracy, consistency, and integrity of records, claims, processes, and outputs against their authoritative standards.

**Key property**: Auditor checks the system's own outputs. Did ledger categorize correctly? Did insulator achieve separation? Did collector pursue all receivables? This is the immune system of the institutional substrate.

**Default execution modes**: AI-primary (systematic verification), protocol-structured (scheduled audits), human-routed (interpretive disputes).

**Signal output type**: Audit finding (conformance assessment with evidence and remediation).

**Universality evidence**: Oikonomia (financial audit), Aegis (compliance audit), any formation requiring integrity verification. Also self-referential: auditor audits other primitives' outputs.

---

#### PRIM-INST-016: ARCHIVIST

**Irreducible operation**: Captures, preserves, indexes, and makes retrievable the institutional memory — precedents, decisions, rationales, outcomes, and learned patterns.

**Distinction from indexer (production primitive)**: Indexer makes content findable. Archivist preserves institutional knowledge — why a decision was made, what happened last time, what the precedent is. Indexer is a library catalog. Archivist is institutional memory.

**Default execution modes**: AI-performed (automatic capture and indexing), protocol-structured (retention policies, access controls).

**Signal output type**: Memory retrieval (precedent, decision rationale, outcome record) or confirmation of capture.

**Universality evidence**: Every formation benefits from institutional memory. Aegis (precedent lookup), Oikonomia (past decision outcomes), Praxis (what worked before), Tessera (relationship history). Archivist is the universal substrate primitive.

---

### 4.5 STRUCTURAL CLUSTER

Primitives governing the architecture of power itself.

---

#### PRIM-INST-017: INCORPORATOR

**Irreducible operation**: Creates, configures, and maintains formal organizational structures (entities, trusts, accounts, contracts) that give legal and economic form to the principal's activities.

**Key property**: This is the function that gives the one-person institution its formal skeleton. Every LLC, trust, DBA, contract, bank account, and investment vehicle is an incorporator output.

**Default execution modes**: Human-routed (legal formation), AI-performed (structure selection, document preparation), protocol-structured (maintenance/compliance).

**Signal output type**: Structural artifact (entity definition, formation document, account configuration).

**Universality evidence**: Praxis (entity for contracts), Oikonomia (account structures), Tessera (formal standing structures), any context requiring legal/economic form.

---

#### PRIM-INST-018: ENFORCER

**Irreducible operation**: Detects violations of the principal's rights, agreements, and boundaries, and initiates and manages the escalation/resolution process.

**Distinction from guardian**: Guardian watches and alerts. Enforcer ACTS on violations. Guardian says "your contractor missed the deadline." Enforcer initiates the contractual remedy (notice, penalty, termination).

**Default execution modes**: AI-performed (detection, documentation), protocol-structured (escalation ladders), human-routed (legal action, adversarial engagement).

**Signal output type**: Enforcement action (violation documented, remedy initiated, escalation stage).

**Universality evidence**: Aegis (rights enforcement), Praxis (contract enforcement), Tessera (boundary enforcement), any context where agreed terms are violated.

---

#### PRIM-INST-019: STRATEGIST

**Irreducible operation**: Models the principal's position within larger systems (markets, legal environments, political landscapes, social fields) and identifies moves that improve positional advantage.

**Distinction from counselor**: Counselor synthesizes available information into a recommendation for the current situation. Strategist models the field itself and identifies moves that reshape it. Counselor is reactive (given this situation, what should you do?). Strategist is proactive (what moves change the situation in your favor?).

**Default execution modes**: AI-primary (modeling, scenario generation), human-routed (strategic judgment on novel configurations).

**Signal output type**: Positional analysis (current position, available moves, projected outcomes, recommended sequence).

**Universality evidence**: Praxis (market positioning), Aegis (defensive positioning), Tessera (institutional positioning), any context requiring long-game thinking about power configurations.

---

#### PRIM-INST-020: MANDATOR

**Irreducible operation**: Formalizes decisions into executable directives — translating intent into binding instructions with clear authority chains, scope limits, and completion criteria.

**Key property**: This is the missing link between "decide" and "do." When counselor recommends and the principal decides, mandator converts that decision into a structured directive that other primitives can execute against. It is the warrant function — the formal authority to act.

**Default execution modes**: Protocol-structured (directive templates, authority delegation), AI-performed (directive generation from decisions).

**Signal output type**: Directive (action, authority, scope, completion criteria, expiry).

**Universality evidence**: Every formation requires mandator to convert decisions into actions. Aegis (defense directives), Oikonomia (allocation directives), Praxis (engagement directives). Mandator is the universal execution primitive — nothing happens without a directive.

---

## 5. Cluster Independence

The five clusters (Protective, Economic, Relational, Epistemic, Structural) are descriptive groupings for cognitive navigation. They carry NO architectural weight. Primitives compose across clusters freely — a formation may draw from all five clusters simultaneously. No coupling rules, signal restrictions, or governance constraints are derived from cluster membership.

---

## 6. Relationship to Production Primitives

The 13 production primitives (reader, classifier, labeler, scheduler, credential, writer, renderer, publisher, distributor, broadcaster, analyzer, indexer, orchestrator) and the 19 institutional primitives (PRIM-INST-001 through PRIM-INST-020) inhabit a **single shared pool**.

The orchestrator remains the composition authority — it composes any primitive with any other primitive regardless of origin. Formations may be:
- Purely production (the current organ pipelines)
- Purely institutional (Aegis monitoring)
- Hybrid (publishing with liability assessment woven in)

There is no hierarchy between production and institutional primitives. They are peers in the pool.

---

## 7. Evolution Constraints

SPEC-025 may be amended through the governed process defined in SPEC-008 (Evolution & Migration Law):

| Amendment Type | Definition | Requirements |
|---------------|-----------|--------------|
| **Conservative Refinement** | Refines existing PRIM-INST definitions, adjusts execution mode defaults, adds detail to distinctions | Adversarial review + principal sign-off |
| **Constrained Extension** | Adds new PRIM-INST identifiers (must pass irreducibility criterion in Section 1) | Adversarial review + impact assessment on INST-COMPOSITION and all formations + principal sign-off |
| **Breaking Revision** | Changes the interface contract, modifies execution mode taxonomy, removes primitives | New grounding + adversarial review + formation migration plan + principal sign-off |

PRIM-INST identifiers are permanent. Removed primitives have their identifiers retired, not reassigned.

---

## 8. Traceability

### 8.1 Upward Traceability (to SPEC-000)

| SPEC-000 Element | SPEC-025 Grounding |
|------------------|-------------------|
| AX-000-003 (Individual Primacy) | Every primitive optimizes for the principal — no competing interests, no principal-agent misalignment |
| AX-000-004 (Constitutional Governance) | Primitives operate within governed bounds; mandator is the constitutional authority for action |
| AX-000-005 (Evolutionary Recursivity) | Primitive vocabulary evolves through Section 7; new primitives may be admitted or retired |
| AX-000-006 (Topological Plasticity) | Institutional primitives compose into formations that crystallize into organs per INST-FORMATION |
| AX-000-009 (Modular Alchemical Synthesis) | Primitives are the atoms; composition grammar (INST-COMPOSITION) is the synthesis; formations are the compounds |

### 8.2 Lateral Traceability

| Peer Spec | Connection |
|-----------|-----------|
| SPEC-002 (Primitive Register) | SPEC-025 extends the primitive vocabulary into the institutional domain; interface contract maps to SPEC-002 primitive types |
| SPEC-019 (Liquid Constitutional Order) | Institutional primitives are the operational atoms of the physiological functions SPEC-019 anticipates |
| INST-FORMATION (Formation Protocol) | Institutional formations crystallize per INST-FORMATION lifecycle; formations are compositions of SPEC-025 primitives |
| INST-COMPOSITION (Composition Grammar) | Defines how SPEC-025 primitives combine — companion governance instrument |

### 8.3 Downward Traceability (to implementation)

| SPEC-025 Element | Current Code Location | Alignment |
|-----------------|----------------------|-----------|
| Primitive definitions (Section 4) | Not implemented | MISSING — no primitive classes or interfaces |
| Interface contract (Section 2) | Not implemented | MISSING — no standard input/output contract |
| Execution mode taxonomy (Section 3) | Not implemented | MISSING — no confidence/escalation routing |
| Formation compositions | Not implemented | MISSING — see INST-COMPOSITION |

---

## 9. The Singularity Property

When all 32 primitives (13 production + 19 institutional) are operational and compose freely through the composition grammar (INST-COMPOSITION), the system achieves **Coherent Institutional Agency**:

1. **No principal-agent misalignment** — every primitive optimizes for the principal
2. **No compartment boundaries** — unified memory via archivist; every primitive's output available to every other
3. **No reconfiguration inertia** — institutional posture reconfigures in minutes, not months
4. **Institutional clock speed** — cycle time in minutes/hours vs. traditional weeks/months

The threshold for this property is compositional coverage, not capability depth. All primitives at 60% capability with free composition exceeds five primitives at 95% without composition. The power is in the grammar, not the vocabulary alone.
