# Formation: OIKONOMIA (Survival Economics)

```
Formation ID:     FORM-INST-002
Name:             OIKONOMIA
Status:           CRYSTALLIZED (pre-crystallized from architectural specification)
Trigger:          Cash flow below sustainability threshold OR economic position opaque
Layer:            Institutional substrate (economic)
Parent Specs:     SPEC-025 (Institutional Primitives), INST-COMPOSITION (Composition Grammar)
Date Crystallized: 2026-04-20
```

---

## 1. Composition Graph

```
ledger(current_state) → appraiser(assets + entitlements) → optimizer(survival_constraints) → allocator → collector(receivables)
                                                                                                   ↑
                                                                                               auditor (verify completeness)
```

**Operators used**: CHAIN (→), with auditor providing verification feedback to allocator.

## 2. Trigger Conditions

OIKONOMIA activates when:
- Cash flow falls below defined sustainability threshold
- Economic position has not been assessed in > 14 days (staleness trigger)
- A new income/expense/obligation event occurs that materially changes position
- Manual invocation by principal ("what's my financial situation?")
- Guardian (from AEGIS) flags a financial threshold crossing

## 3. Primitive Roles

| Primitive | Role in OIKONOMIA | Frame |
|-----------|------------------|-------|
| ledger | Entry point — establishes current authoritative economic state | economic_state |
| appraiser | Values all assets, entitlements, receivables (including non-obvious: tax credits, benefits, refunds, equity) | market_value |
| optimizer | Determines optimal allocation given survival constraints (rent, food, critical services, debt obligations) | survival_optimization |
| allocator | Executes the distribution per optimizer's plan | resource_distribution |
| collector | Pursues all identified receivables and entitlements | collection |
| auditor | Verifies nothing was missed — no uncounted asset, unclaimed benefit, or untracked obligation | completeness_audit |

## 4. Variation Points

| Point | Parameter | Options |
|-------|-----------|---------|
| optimizer constraints | constraint_set | survival (bare minimum), stability (3-month runway), growth (investment capacity) |
| appraiser scope | asset_classes | monetary, equity, intellectual_property, entitlements, receivables, tangible_assets |
| collector aggressiveness | collection_mode | passive (reminders), active (formal demand), escalated (legal) |

## 5. Escalation Policy

| Primitive | Escalation Rule |
|-----------|----------------|
| ledger | Never escalates (state recording is autonomous) |
| appraiser | Escalates if asset valuation is uncertain (illiquid, novel) |
| optimizer | Escalates if no allocation satisfies all survival constraints (impossible problem) |
| allocator | Escalates if distribution requires closing an account or liquidating an asset |
| collector | Escalates if collection requires adversarial engagement |
| auditor | Escalates if discovered gap is material (> 10% of total position) |

## 6. Exit Conditions

- Economic position is clear and sustainable: no survival constraint violations for 30+ days
- Upgraded to growth mode: when survival constraints are satisfied with margin, OIKONOMIA shifts constraint_set from "survival" to "stability" or "growth"
- Merged with PRAXIS: when income generation becomes the bottleneck, OIKONOMIA feeds into PRAXIS as the economic ground

## 7. Why OIKONOMIA Crystallizes Second

After defense (AEGIS), resource mobilization. Most people in financial crisis are not broke — they are disorganized. They have uncollected receivables, unclaimed benefits, misallocated spend, and unappraised assets. OIKONOMIA makes the actual position visible and actionable.

The insight: the difference between "I have no money" and "I have resources I haven't mobilized" is the difference OIKONOMIA reveals.

## 8. INST-FORMATION Classification

**Formation type**: TRANSFORMER (applies specialized economic analysis process to the principal's raw financial data, producing actionable allocation plans).

**Interdependence profile**: Internal sequential (ledger → appraiser → optimizer → allocator → collector), with auditor providing feedback. External: feeds AEGIS (financial assessment) and receives from PRAXIS (income data).
