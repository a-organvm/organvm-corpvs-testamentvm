# Formation: AEGIS (Defensive Perimeter)

```
Formation ID:     FORM-INST-001
Name:             AEGIS
Status:           CRYSTALLIZED (pre-crystallized from architectural specification)
Trigger:          Immediate threats to housing, income, legal standing, or benefit eligibility
Layer:            Institutional substrate (protective)
Parent Specs:     SPEC-025 (Institutional Primitives), INST-COMPOSITION (Composition Grammar)
Date Crystallized: 2026-04-20
```

---

## 1. Composition Graph

```
guardian(threats) → [assessor(legal) || assessor(financial)] → counselor → mandator
                                                                    ↑
                                                                archivist (precedent lookup)
```

**Operators used**: CHAIN (→), PARALLEL (||), and implicit precedent feed to counselor.

## 2. Trigger Conditions

AEGIS activates when:
- Guardian detects a threshold crossing on any watched interest
- An external communication carries a legal/financial threat signal
- A deadline approaches within critical window (configurable, default: 7 days)
- Manual invocation by principal ("assess this threat")

## 3. Primitive Roles

| Primitive | Role in AEGIS | Frame |
|-----------|--------------|-------|
| guardian | Entry point — continuous monitoring of threat watchlist | threat_detection |
| assessor (legal) | Evaluates legal exposure, rights, obligations | legal |
| assessor (financial) | Evaluates financial impact, loss potential, recovery options | financial |
| counselor | Synthesizes parallel assessments + precedent into recommendation | integrated_defense |
| mandator | Formalizes recommendation into actionable directive | defense_directive |
| archivist | Provides precedent — what happened last time, what worked | precedent_retrieval |

## 4. Variation Points

| Point | Parameter | Options |
|-------|-----------|---------|
| assessor frames | frame | legal, financial, relational, reputational (add as needed) |
| counselor depth | synthesis_mode | quick (single-pass) or deep (feedback loop with strategist) |
| mandator scope | directive_authority | self-execute, human-review, professional-route |

## 5. Escalation Policy

| Primitive | Escalation Rule |
|-----------|----------------|
| guardian | Never escalates (detection is autonomous) |
| assessor | Escalates if confidence < 0.6 OR situation is novel (no precedent) |
| counselor | Escalates if recommendation involves irreversible action |
| mandator | ALWAYS escalates — principal approves all defense directives |

## 6. Exit Conditions

- Threat resolved: no guardian alerts for 7+ consecutive days on that threat
- Escalated to enforcer: if directive requires active enforcement, formation hands off to Praxis-variant or standalone enforcer invocation
- Superseded: new information renders the threat assessment obsolete; archivist records and AEGIS deactivates

## 7. Why AEGIS Crystallizes First

When the ground is unstable, the first institutional function that proves value is the one that catches what the principal missed — the notice not read, the deadline forgotten, the right not known. AEGIS is defensive awareness: the institutional immune system's first activation.

Without AEGIS, threats compound silently. With AEGIS, every threat is detected, assessed, and addressed within the system's clock speed.

## 8. INST-FORMATION Classification

**Formation type**: SYNTHESIZER (cross-configurational — combines sensing, analysis, synthesis, and directive issuance across domains).

**Interdependence profile**: Internal reciprocal (assessor↔counselor via archivist), external sequential (receives guardian signal, produces mandator directive).
