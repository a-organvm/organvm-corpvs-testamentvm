# SPEC-018 Dialect Taxonomy: Eight Voices of Universal Logic

## The Dialect Mapping

| Organ | Dialect | Classical Parallel | Translation Role | Formal Basis |
|-------|---------|--------------------|-----------------|--------------|
| I (Theoria) | Formal Logic & Type Theory | Logic (Trivium) | The Grammar — well-formedness | Martin-Löf 1984, dependent types |
| II (Poiesis) | Aesthetic Form & Generative Expression | Music (Quadrivium) | The Poetry — formal→sensory | Generative grammar, algorithmic composition |
| III (Ergon) | Executable Algorithm & Engineering | Arithmetic (Quadrivium) | The Engineering — proof→computation | Curry-Howard (programs are proofs) |
| IV (Taxis) | Governance Logic & Orchestration | Rhetoric (Trivium) | The Meta-Logic — rules as propositions | ADICO institutional grammar |
| V (Logos) | Natural Language Rhetoric & Discourse | Grammar (Trivium) | The Hermeneutics — formal↔natural translation | Speech act theory (Austin 1962) |
| VI (Koinonia) | Pedagogical Dialectic & Communal Understanding | Geometry (Quadrivium) | The Dialectic — teaching IS translation | Socratic method, constructivism |
| VII (Kerygma) | Signal Propagation & Syndication | Astronomy (Quadrivium) | The Broadcast — structure-preserving projection | Information theory (Shannon 1948) |
| META | Self-Witnessing & Constitutional Proof | The Eighth Art | The Witness — all translations compose | Gödel 1931, fixed-point theorems |

## Translation Pairs (The 28 Edges of K₈)

Every pair of 8 organs forms a potential translation surface. C(8,2) = 28 pairs.

### Tier 1: Formally Grounded (3 pairs)

Mathematical proof of structure-preservation exists.

| Pair | Evidence | Preservation |
|------|----------|--------------|
| **I↔III** (Logic↔Algorithm) | Curry-Howard correspondence (Howard 1969) | Isomorphism |
| **I↔IV** (Logic↔Governance) | SPEC-002 propositions-as-types (Martin-Löf 1984) | Isomorphism |
| **I↔META** (Logic↔Self-Witnessing) | Gödel numbering, fixed-point theorems (Gödel 1931) | Homomorphism |

### Tier 2: Structurally Grounded (5 pairs)

Empirical structural isomorphism demonstrated.

| Pair | Evidence | Preservation |
|------|----------|--------------|
| **II↔III** (Art↔Engineering) | Generative art = algorithm + aesthetic constraint | Homomorphism |
| **III↔VII** (Engineering↔Broadcast) | Serialization as structure-preserving projection | Projection |
| **IV↔V** (Governance↔Discourse) | Governance rules as speech acts (Austin 1962) | Homomorphism |
| **IV↔META** (Governance↔Witness) | Constitutional self-observation (SPEC-011) | Homomorphism |
| **V↔VI** (Discourse↔Community) | Teaching as bidirectional translation (Vygotsky 1978) | Homomorphism |

### Tier 3: Analogically Grounded (4 pairs)

Strong structural parallel without formal proof.

| Pair | Evidence | Preservation |
|------|----------|--------------|
| **II↔V** (Art↔Discourse) | Both externalize internal structure | Projection |
| **II↔VI** (Art↔Community) | Performance IS communal experience | Resonance |
| **III↔VI** (Engineering↔Community) | Open source IS community engineering | Resonance |
| **VI↔VII** (Community↔Broadcast) | Communities generate their own broadcasts | Projection |

### Tier 4: Emergent (16 pairs)

Translation surface exists but not yet characterized. The system should discover these through ongoing detection, not presuppose them.

All remaining pairs from the K₈ graph. Each is initialized at PreservationDegree.RESONANCE and will be reclassified as evidence accumulates.

## Composition Rules

Translations compose transitively. If T(A→B) and T(B→C) exist, then T(A→C) = T(B→C) ∘ T(A→B).

**Composition constraints:**
- The composed preservation degree is the *minimum* of the two legs
- The composed tier is the *weakest* of the two legs
- Compositions can be computed by `trivium/taxonomy.py::compose_translation()`

**Example:** I→III (isomorphism, formal) composed with III→VII (projection, structural) yields I→VII (projection, structural) — the formal tier of the first leg is overridden by the structural tier of the second, and the isomorphism degree is reduced to projection.

## Preservation Degree Lattice

```
Isomorphism (4)     — bijective, invertible, all structure preserved
    ↓
Homomorphism (3)    — structure-preserving, not necessarily invertible
    ↓
Projection (2)      — information-reducing but content-preserving
    ↓
Resonance (1)       — structural similarity without formal mapping
```

This lattice is a total order. Composition takes the meet (minimum) of two degrees.
