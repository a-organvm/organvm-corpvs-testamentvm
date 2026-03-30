# Formation Chemistry — The Bonding Rules of ORGANVM

**Date:** 2026-03-30
**Authority:** LEX-II (Universal Composition), LIQ-003 (Signal Signatures), AX-6 (Signal Closure)
**Genesis:** ChatGPT-Scientific Principles Across Disciplines.md, ChatGPT-Scientific Systems Frameworks.md
**Status:** SPEC — ready for implementation in organvm-engine

---

## The Problem

The seed graph maps which formations connect. It does not explain:
- WHY those connections form (bonding force)
- What HAPPENS when signals flow through them (reaction dynamics)
- What occurs if you MOVE a wire (predictive chemistry)
- Which connections SHOULD exist but don't (Mendeleev gaps)
- Which connections are TOXIC (harmful byproducts)
- What the LIMITING REAGENT is (system bottleneck)

AX-6 says signals MUST flow. Chemistry says HOW they flow, at what RATE, with what ENERGY, producing what PRODUCTS.

---

## I. The Periodic Table of Formations

### Organizing Principle

The periodic table's power is that POSITION predicts BEHAVIOR. Mendeleev left gaps and predicted undiscovered elements. The ORGANVM periodic table must do the same.

### Axes

**Rows (Periods) = Phase bands:**
- α-Foundation (Energy 0-20)
- β-Hardening (Energy 21-40)
- γ-Automation (Energy 41-60)
- δ-Intelligence (Energy 61-80)
- ω-Sovereignty (Energy 81-100)

**Columns (Groups) = Functional roles:**
- GROUP 1: GENERATOR — produces primary signal (high output valence)
- GROUP 2: ENGINE — transforms signal between types (high throughput)
- GROUP 3: RESERVOIR — stores and serves accumulated signal (high input valence, low output)
- GROUP 4: CATALYST — enables reactions without being consumed (ORGAN-IV pattern)
- GROUP 5: INTERFACE — transfers signal between the organism and external systems
- GROUP 6: SUBSTRATE — provides foundational material other formations build on (schemas, databases)

### Atomic Properties (per formation)

```yaml
# Computed from seed.yaml + registry + git activity
atomic_properties:
  # Identity
  symbol: "SS-EA"  # abbreviated formation name
  atomic_number: 87  # registry position (unique, sequential)

  # Bonding
  signal_signature:
    inputs: [Σ, Θ]          # what it consumes (electron shells seeking)
    outputs: [Σ, Ω, Δ]      # what it produces (electrons to share)
  valence: 5                  # total bond capacity (len(inputs) + len(outputs))
  unsatisfied_bonds: 4        # declared produces with no receiving formation

  # Reactivity
  reactivity: 0.8             # unsatisfied_bonds / valence — how "desperate" to bond
  electronegativity: 0.3      # ratio of inbound signal to outbound signal

  # Phase
  phase: "β-Hardening"
  energy: 35
  promotion_status: LOCAL

  # Activity
  half_life_days: null         # days since last commit (LEX-III / AX-3)
  metabolic_rate: 0.0          # signals_produced_30d / signals_consumed_30d
```

### Predictive Power

With this table, the engine can compute:

1. **Mendeleev gaps** — "GROUP 2 (ENGINE) has no formation in δ-Intelligence phase for ORGAN-V. The system needs an intelligent essay generation engine. This formation doesn't exist but the table demands it."

2. **Isotopes** — "These 3 formations have identical signal signatures. They're isotopes — functionally redundant. Candidates for LEX-V apoptosis (consolidate or archive 2 of 3)."

3. **Noble gases** — "This formation has valence 0 (no produces, no consumes). It's inert — not participating in any reaction. Either it's misplaced or it's dead."

4. **Reactive species** — "sovereign-systems has reactivity 0.8 (4 of 5 bonds unsatisfied). It's a free radical — highly reactive, seeking bonds. Priority: fulfill its produces edges."

---

## II. Bonding Rules

### Bond Types

| Bond Type | Chemical Analog | ORGANVM Expression | Strength |
|-----------|----------------|-------------------|----------|
| **Covalent** | Shared electrons | Bidirectional produces/consumes between two formations (A produces for B AND B produces for A) | Strong — hard to break, requires energy |
| **Ionic** | Electron transfer | Unidirectional produces → consumes (A gives, B takes, no return) | Medium — asymmetric, can dissolve in the right solvent |
| **Hydrogen** | Weak electrostatic | Event subscriptions (formation listens to events from another without direct edge) | Weak — easy to form and break, but essential in bulk |
| **Metallic** | Shared electron cloud | Shared infrastructure (koinonia-db consumed by 4 sibling formations) | Delocalized — affects all formations in the cluster |

### Bond Formation Rules

```
RULE 1: Complementarity
  A formation bonds with another iff output_set(A) ∩ input_set(B) ≠ ∅
  (Already in LIQ-003)

RULE 2: Valence Satisfaction
  A formation seeks bonds until all declared edges have receiving partners.
  Unsatisfied bonds = constitutional violations (AX-6).
  Formations with high unsatisfied bond count are "free radicals" — unstable.

RULE 3: Electronegativity Gradient
  Signal flows from low-electronegativity formations (producers) to
  high-electronegativity formations (consumers/flagships).
  Flagships attract signal. Infrastructure radiates it.

RULE 4: Activation Energy
  Every new bond requires work to form (writing code, creating content,
  deploying infrastructure). LEX-VIII (Latent Heat) applies.
  Catalysts (GROUP 4 formations) lower this barrier.

RULE 5: Stoichiometric Ratios
  Reactions consume inputs in predictable ratios.
  1 consulting engagement → 1 case study → 1 POSSE dispatch → N platform posts.
  The LIMITING REAGENT determines system throughput.
```

---

## III. Reaction Dynamics

### Reaction Template

Every signal flow is a reaction:

```
REACTANTS + ACTIVATION_ENERGY → PRODUCTS + BYPRODUCTS

Example:
  sovereign-systems(III) + case-study-writing(energy) →
    essay(V) + distribution-signal(VII) + community-material(VI) + research-insight(I)
    + BYPRODUCT: client-IP-boundary-awareness(governance learning)
```

### Reaction Types

| Type | Pattern | Example |
|------|---------|---------|
| **Synthesis** | A + B → AB | Theory(I) + Creative(II) → Art-with-theoretical-grounding |
| **Decomposition** | AB → A + B | Monolith → microservices (RR-2 Single Responsibility) |
| **Single displacement** | A + BC → AC + B | New formation replaces old in a signal chain |
| **Double displacement** | AB + CD → AD + CB | Two formations swap signal partners |
| **Combustion** | Formation + O₂ → CO₂ + H₂O + Energy | Formation meets selection pressure → useful energy (learning) + waste (archived code) |
| **Redox** | Coupled oxidation-reduction | Every produces/consumes pair — one loses signal, one gains it |

### Equilibrium

Le Chatelier's Principle applied to ORGANVM:

```
If you increase consulting work (ORGAN-III inputs):
  → Demand for documentation (ORGAN-V) increases
  → Demand for distribution (ORGAN-VII) increases
  → System shifts until new balance is found

If you remove the human reviewer (reduce quality gate throughput):
  → Quality drops
  → Selection pressure (LEX-VI) increases
  → Weakest formations archived (LEX-V apoptosis)
  → System re-equilibrates at lower quality, fewer formations
```

### Limiting Reagent Analysis

The system's throughput is constrained by whichever input is scarcest:

```
Current limiting reagents (2026-03-30):

  1. ORGAN-V essays = 0 new from ORGAN-III
     (42 essays exist but none from consulting/client work)
     BOTTLENECK: No III→V signal has ever been produced

  2. ORGAN-VII dispatches from ORGAN-I = 0
     (SGO has 13 works, 500K words, none distributed)
     BOTTLENECK: Research exists but distribution signal never emitted

  3. Human review bandwidth = 1 person
     (LEX-IX gravity means flagships consume disproportionate attention)
     BOTTLENECK: Carrying capacity of the system
```

### Toxic Reactions

Some combinations produce harmful byproducts:

```
TOXIC:
  governance + governance → meta-governance (PROHIB-I inversion)
  documentation + documentation → documentation-of-documentation
  planning + planning → planning-to-plan (never executing)

DETECTION: If a reaction's primary product is MORE of the same
input type (governance producing governance), it's autocatalytic
in the toxic sense — runaway positive feedback producing nothing
the organism needs.
```

---

## IV. Implementation Plan

### Phase 1: Compute Atomic Properties
**Where:** `organvm-engine/src/organvm_engine/chemistry/`
**What:** New module that reads registry + seed graph + git activity and computes atomic properties for every formation.
**CLI:** `organvm chemistry properties [--repo X] [--organ X]`

### Phase 2: Build the Periodic Table
**Where:** Same module
**What:** Organize formations into the Group × Phase matrix. Identify Mendeleev gaps, isotopes, noble gases, free radicals.
**CLI:** `organvm chemistry table [--format ascii|json|svg]`

### Phase 3: Reaction Prediction
**Where:** Same module
**What:** Given a proposed new edge (A produces for B), predict: activation energy, products, byproducts, equilibrium shift, toxicity check.
**CLI:** `organvm chemistry predict --from <repo> --to <repo> --signal <type>`

### Phase 4: Limiting Reagent Analysis
**Where:** Same module
**What:** Across the full system, identify which missing signal is the bottleneck. Report as "the system's throughput is limited by X."
**CLI:** `organvm chemistry bottleneck`

### Phase 5: Dashboard Integration
**Where:** `system-dashboard/`
**What:** Periodic table visualization. Click a formation → see its atomic properties, bonds, reactivity. Click a gap → see what formation the table predicts should exist.

---

## V. Relationship to Existing Infrastructure

| Existing Tool | Chemistry Extension |
|--------------|-------------------|
| `organvm seed graph` | Computes the wiring diagram → chemistry adds FORCE, RATE, and PREDICTION to the wires |
| `organvm governance audit --signal-closure` | Checks if edges exist → chemistry checks if the REACTIONS those edges enable are productive |
| `organvm context sync` | Propagates CLAUDE.md → chemistry could propagate atomic properties into formation context |
| `organvm omega status` | Binary scorecard → chemistry adds continuous metrics (system reactivity, limiting reagent, equilibrium state) |
| IRF-LIQ-004 (swarm topology) | Computes signal affinity from existing graph → chemistry PREDICTS affinity before bonds form |

---

## VI. The Baseline of Expectations

This is the key insight: chemistry gives the system a **baseline of expectations.**

Before chemistry: "A produces for B" is a declaration with no predictive power. Moving the wire is an arbitrary choice with unknown consequences.

After chemistry: "A produces for B because A has output Σ and B needs input Σ, the bond is ionic (unidirectional), the reaction produces essay + distribution-signal at a rate limited by human review bandwidth, and moving this wire to C instead would require activation energy of X and produce byproduct Y."

Every wire has a reason. Every reason has a force. Every force has a prediction. Move the wire and the chemistry tells you what happens next.
