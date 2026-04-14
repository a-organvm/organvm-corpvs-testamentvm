# SPEC-000-RECONCILIATION: Axiom Reconciliation

```
Document ID:      SPEC-000-RECONCILIATION
Title:            Axiom Reconciliation -- SPEC Canonical, SEED Corollaries
Version:          1.0
Status:           RATIFIED
Layer:            L1 -- Metaphysical Identity
Parent:           SPEC-000 (System Manifesto)
Date Ratified:    2026-04-14
IRF:              IRF-SYS-088
GitHub Issue:     meta-organvm/organvm-corpvs-testamentvm#311
Principal Author: https://orcid.org/0009-0008-2007-3596
```

---

## 1. Problem Statement

Two incompatible 9-axiom formulations exist in the system. Neither had been
declared canonical. The genome carried two conflicting readings:

**SEED.md** (`post-flood/SEED.md`, A1--A9) defines a generative grammar for
computational organisms -- a DNA-like document that prescribes how an organism
grows from an empty directory. Its axioms are operational: they govern what
the organism does and how it maintains itself.

**SPEC-000** (`specs/SPEC-000.md`, AX-000-001 through AX-000-009) defines the
constitutional manifesto of the ORGANVM system. Its axioms are constitutional:
they govern what the system is, how it governs itself, and what constraints
bind all downstream specifications.

The two formulations share only 3 direct mappings out of 9 axioms each. The
remaining 6 on each side carry different structural commitments.

---

## 2. Decision

**SPEC AX-000-001 through AX-000-009 are the canonical axiom set.**

The SPEC axioms are canonical because they:

1. Carry formal academic grounding with traceable citations
   (Maturana & Varela 1980, Luhmann 1995, Ostrom 1990, Ashby 1956, etc.)
2. Have formalization status declarations (FORMAL, FORMALIZABLE, JUDGMENT)
3. Are referenced by the entire downstream SPEC ladder (SPEC-001 through SPEC-017)
4. Underwent adversarial review (G3 review incorporated, per SPEC-000 header)
5. Define the constitutional topology, invariants, and failure modes that
   govern the living system

The SEED axioms are not discarded. They are reclassified: the 3 shared axioms
are confirmed as identical commitments expressed in different registers, and
the 3 SEED-only concepts (Purpose, Persistence, Minimality) are formally
derived as corollaries of the SPEC set.

The A1--A9 numbering scheme is deprecated. All future axiom references must
use the AX-000-NNN identifiers.

---

## 3. Direct Mappings (SEED to SPEC)

Three SEED axioms map 1:1 to SPEC axioms. In each case, the SPEC formulation
is a constitutional elaboration of the same commitment expressed operationally
in the SEED.

### 3.1 Organizational Closure

| | |
|---|---|
| **SEED A6** | "The organism's governance governs itself. The rules that constrain growth are subject to the same constraints." |
| **SPEC AX-000-002** | "Every constitutive process of the system is specified by processes within the system." |
| **Relationship** | Identical commitment. SEED states it as a recursive constraint on governance. SPEC elaborates the mechanism: registry validates engine, engine governs registry, governance rules constrain how the registry may change, constitutional specs constrain the governance rules. Both derive from Maturana & Varela's autopoiesis via Luhmann's communicative route. |

### 3.2 Individual Primacy

| | |
|---|---|
| **SEED A7** | "The organism exists to serve the individual who operates it. No structural optimization may override this purpose." |
| **SPEC AX-000-003** | "The system exists to amplify individual creative capacity, not to replace it." |
| **Relationship** | Identical commitment. SEED frames it as a constraint on optimization. SPEC frames it as a constitutional principle requiring individual-impact assessment. Both are novel ethical architectural decisions with no direct academic precedent. |

### 3.3 Topological Plasticity + Alchemical Inheritance

| | |
|---|---|
| **SEED A8** | "The organism's structural organization is a governed variable, not a frozen constant. Mechanisms may fuse, split, or dissolve through governed evolution." |
| **SPEC AX-000-006** | "The system's functional differentiation into distinct organs is designed to be a governed variable, not a frozen constant." |
| **Relationship** | Identical commitment, near-identical language. SPEC adds the specific mechanism of era transition and constitutional revision. |

| | |
|---|---|
| **SEED A9** | "When any structural element is dissolved, its lineage must be preserved. Dissolution does not erase history." |
| **SPEC AX-000-007** | "The system's prior structural failures are not waste but prima materia." |
| **Relationship** | Identical commitment. SPEC elaborates the required lineage fields (predecessor UIDs, successor UIDs, dissolution reason, dissolution date, lineage type) and grounds in alchemical tradition + North 1990 path dependence. |

---

## 4. SEED-Only Concepts as SPEC Corollaries

Three SEED axioms have no direct SPEC counterpart. Each is formally derivable
from the SPEC axiom set. They are not axioms (irreducible commitments) but
corollaries (consequences of deeper commitments).

### 4.1 Purpose (SEED A1)

> "The organism exists to do work. Work is the transformation of inputs into
> outputs."

**Derivation.** Purpose is a consequence of three SPEC axioms acting together:

- **AX-000-001 (Ontological Primacy)** requires every entity to be
  ontologically declared before behavioral rules apply. An entity with no
  declared purpose has no ground for behavioral rules, hence no reason to
  exist in the ontology.
- **AX-000-003 (Individual Primacy)** subordinates the system to the
  amplification of individual creative capacity. This supplies the telos:
  the system's purpose is derived from the individual's purpose.
- **AX-000-004 (Constitutional Governance)** requires every component to
  have constitutional authorization via seed.yaml, which declares
  produces/consumes edges -- i.e., what work the component does.

Therefore: every entity has declared purpose (from AX-001), that purpose
serves the individual (from AX-003), and that purpose is constitutionally
registered (from AX-004). Purpose is not an independent axiom but a
necessary consequence of ontological primacy + individual primacy +
constitutional governance.

**Corollary COR-000-001 (Purpose):** Every constitutionally authorized entity
performs declared work -- transformations with typed inputs and outputs --
in service of individual creative capacity.

### 4.2 Persistence (SEED A3)

> "The organism must maintain itself over time. It must not decay into
> disorder without external intervention."

**Derivation.** Persistence is a consequence of two SPEC axioms:

- **AX-000-002 (Organizational Closure)** requires the system's constitutive
  processes to be self-produced. A system whose organization is self-produced
  is by definition self-maintaining: if it were not, its constitutive
  processes would cease, violating closure.
- **AX-000-007 (Alchemical Inheritance)** requires that no era may discard
  the memory of prior eras. This is temporal persistence: the system's
  identity persists through structural transformation because lineage is
  never destroyed.

Together: organizational closure guarantees structural self-maintenance, and
alchemical inheritance guarantees identity persistence through change. The
SEED's "must maintain itself over time" is the union of these two guarantees.

**Corollary COR-000-002 (Persistence):** The system is self-maintaining by
organizational closure and identity-preserving by alchemical inheritance.
It does not decay into disorder because its constitutive processes
recursively produce the conditions for their own continuation.

### 4.3 Minimality (SEED A5)

> "No structural element exists without a derivable reason. If a structure
> can be removed without violating any axiom, it must be removed."

**Derivation.** Minimality is a consequence of three SPEC axioms:

- **AX-000-004 (Constitutional Governance)** requires every component to
  have constitutional authorization. A component without derivable reason
  has no constitutional authorization, hence violates AX-004.
- **AX-000-001 (Ontological Primacy)** requires ontological declaration
  before behavioral rules. A structure without ontological ground cannot
  receive behavioral rules, hence has no function.
- **AX-000-005 (Evolutionary Recursivity)** provides the governed process
  for removing unauthorized components: the rules themselves evolve
  through governed revision, and components that no longer serve the
  system can be dissolved through governed processes.

Therefore: constitutional governance forbids unauthorized structure,
ontological primacy forbids ungrounded structure, and evolutionary
recursivity provides the mechanism for pruning. Minimality is not an
independent constraint but the logical consequence of a system that
requires authorization for existence and provides governed dissolution.

The SEED's own caveat -- "A7 overrides A5 when they conflict: the operator's
needs are the terminal authority" -- further demonstrates that Minimality
is subordinate, not axiomatic. In the SPEC framework, this override is
already encoded: AX-000-003 (Individual Primacy) is a JUDGMENT-class axiom
that constitutionally outranks any structural optimization, including
minimality.

**Corollary COR-000-003 (Minimality):** No structural element exists
without constitutional authorization (AX-004) and ontological ground
(AX-001). Structure that loses both may be dissolved through governed
evolution (AX-005), subject to the supremacy of individual creative
needs (AX-003).

---

## 5. Remaining SEED Concepts

Two SEED axioms (A2 Composition, A4 Adaptation) are not SEED-only concepts
but are already subsumed by SPEC axioms without requiring separate corollary
status:

- **A2 (Composition)** -- "The output of one transformation can serve as the
  input of another." This is the definition of signal flow, which is
  constitutionally governed by AX-000-008 (Multiplex Flow Governance) and
  AX-000-009 (Modular Alchemical Synthesis). The patch matrix, signal
  classes, and typed routing substrate formalize composition at a level
  far beyond A2's simple assertion.

- **A4 (Adaptation)** -- "The organism must modify its own structure and
  behavior in response to change." This is precisely AX-000-005
  (Evolutionary Recursivity), which provides three orders of change
  (state, rules, meta-rules) where A4 provides only one undifferentiated
  assertion. AX-000-006 (Topological Plasticity) adds the specific
  mechanism of governed topological mutation.

---

## 6. Full Mapping Table

| SEED | Name | SPEC Equivalent | Status |
|------|------|----------------|--------|
| A1 | Purpose | COR-000-001 (derived from AX-001 + AX-003 + AX-004) | **Corollary** |
| A2 | Composition | Subsumed by AX-000-008 + AX-000-009 | **Subsumed** |
| A3 | Persistence | COR-000-002 (derived from AX-002 + AX-007) | **Corollary** |
| A4 | Adaptation | Subsumed by AX-000-005 + AX-000-006 | **Subsumed** |
| A5 | Minimality | COR-000-003 (derived from AX-001 + AX-004 + AX-005) | **Corollary** |
| A6 | Organizational Closure | AX-000-002 | **Direct mapping** |
| A7 | Individual Primacy | AX-000-003 | **Direct mapping** |
| A8 | Topological Plasticity | AX-000-006 | **Direct mapping** |
| A9 | Alchemical Inheritance | AX-000-007 | **Direct mapping** |

---

## 7. Deprecation of A1--A9 Numbering

The SEED A1--A9 numbering scheme is hereby deprecated. All axiom references
in governance documents, specifications, engine code, seed.yaml schemas,
and diagnostic tooling must use the canonical AX-000-NNN identifiers.

The SEED.md file (`post-flood/SEED.md`) retains its A1--A9 numbering as a
historical artifact. It is a constitutional source document (per
`post-flood/CLAUDE.md`: "This is not an archive. It is the active definition
of the system's identity"). However, its axiom numbering is no longer
authoritative. When SEED.md axioms are referenced in any downstream context,
the AX-000-NNN identifier must be used, with the SEED designation noted
parenthetically if needed for traceability.

---

## 8. Implications

### 8.1 SEED.md Remains Valid

SEED.md is not invalidated by this reconciliation. Its generative grammar
(Sections I through VII: depth theorem, growth procedures, signal graph,
mechanism classification, naming conventions, governance, evolution) remains
operative for the a-organvm organism and any future organism instances.
The reconciliation affects only Section 0 (Axioms): the A1--A9 numbering
is deprecated in favor of AX-000-NNN, and the three SEED-only concepts
are reclassified from axioms to corollaries.

### 8.2 Corollary Register

The three corollaries (COR-000-001 through COR-000-003) are registered
as derived commitments of SPEC-000. They may be referenced by downstream
specifications and implementations. They do not require the amendment
process defined in SPEC-000 Section 9 to modify, since they are derivations,
not axioms. However, modifying them requires demonstrating that the
derivation chain from the source axioms has changed.

### 8.3 IRF-SYS-088 Resolution

This document resolves IRF-SYS-088. The genome no longer has two conflicting
readings. SPEC-000 is canonical. SEED.md axioms are either direct mappings,
corollaries, or subsumed.

---

## 9. Traceability

```
SPEC-000-RECONCILIATION (this document)
├── Resolves: IRF-SYS-088, GH#311
├── Source A: specs/SPEC-000.md (AX-000-001 through AX-000-009)
├── Source B: post-flood/SEED.md (A1 through A9)
├── Declares: COR-000-001 (Purpose), COR-000-002 (Persistence), COR-000-003 (Minimality)
├── Deprecates: A1--A9 numbering scheme
└── Downstream: IRF-SYS-089 (primitive set reconciliation) may reference this pattern
```
