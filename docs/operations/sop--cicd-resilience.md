> **Canonical location:** `praxis-perpetua/standards/SOP--cicd-resilience-and-recovery.md`. This file is a reference copy retained for local context.

# SOP: CI/CD Pipeline Resilience & Recovery

**Created:** 2026-03-06
**Author:** @4444j99 (AI-conductor model)
**Status:** ACTIVE
**Companions:** [`emergency-procedures.md`](./emergency-procedures.md), [`key-workflows.md`](./key-workflows.md), [`operational-cadence.md`](./operational-cadence.md)
**Precedent:** Portfolio pipeline blockage (Feb 17 – Mar 6, 2026) — 17 days, 10 commits, 4 push-watch-fix cycles, 5 failure categories
**Toolchain:** `gh` CLI, project-specific quality scripts

---

> Systematic protocol for diagnosing, unclogging, and structurally hardening CI/CD pipelines across the ORGANVM system.

---

## Table of Contents

1. [Part A: Thesis / Antithesis / Synthesis](#part-a-thesis--antithesis--synthesis)
2. [Part B: The Protocol](#part-b-the-protocol)
3. [Part C: Project Instantiation Template](#part-c-project-instantiation-template)

---

## Part A: Thesis / Antithesis / Synthesis

### Thesis — What mature quality systems do well

1. **Comprehensive gate coverage** catches real regressions, not theater
2. **Monotonic ratchets** (date-based, phase-based) create sustainable improvement trajectories
3. **Separating generation from validation** catches generator bugs before they poison downstream checks
4. **Build-first gating** prevents phantom passes — stale artifacts produce false greens
5. **"Plan all fixes, push once"** is orders of magnitude faster than serial fix-push-watch cycles

### Antithesis — Structural failure modes common to all quality-gated projects

1. **Drift magnets** — Any manually maintained list that mirrors filesystem structure will drift. Law: `P(drift) → 1` as `t → ∞`
2. **Sequential discovery tax** — N hidden failures cost `N × cycle_time` when found serially, but `~1 × cycle_time` if found in parallel locally. The multiplier is the CI round-trip time
3. **CI-only validation gap** — Checks that can only run in CI (browser-dependent, runner-dependent) create an irreducible feedback delay. Minimize the set of CI-only checks
4. **Invisible coupling** — When changing file A requires also changing file B, but no document or error message tells you about B until CI fails
5. **Environment-blind thresholds** — A threshold that works on a developer's M3 but flakes on a GitHub Actions runner is not a quality gate; it's a coin flip
6. **No local pre-flight** — If nothing runs before `git push`, every mistake costs a full CI cycle

### Synthesis — Universal structural principles

1. **Derive, don't duplicate.** Generate lists from filesystem/data at runtime. Never maintain a parallel copy
2. **Preflight locally.** Every project should have a single command that runs all locally-reproducible checks
3. **Document coupling.** Maintain a human-readable coupling map: "if you change X, also change Y, enforced by Z"
4. **Split thresholds by environment.** CI floors (tolerant, catches regressions) vs lab/local targets (aspirational, never blocks deploy)
5. **Diagnose fully before fixing.** Collect the entire failure surface before writing the first line of code

---

## Part B: The Protocol

### Phase 0 — Triage (5 min, any project)

```bash
gh run list --limit 1 --status failure --repo OWNER/REPO
gh run view RUN_ID --repo OWNER/REPO
gh run view RUN_ID --repo OWNER/REPO --log-failed | tail -100
```

**Output:** Complete list of all failing jobs + error messages. Do NOT fix anything yet.

### Phase 1 — Classify (10 min)

Categorize each failure:

| Category | Pattern | Fix archetype |
|----------|---------|---------------|
| Drift | Hardcoded list ≠ filesystem | Make dynamic |
| Threshold | Score too strict for CI | Relax to env-appropriate value |
| Formatter | Generated file fails lint | Exclude from formatter |
| Stale artifact | Old manifest/summary | Regenerate |
| Missing dep | Tool not installed in CI | Add install step |
| Code bug | Invalid HTML, broken link | Fix the code |

### Phase 2 — Reproduce locally (15 min)

```bash
# Project-specific preflight (if it exists):
npm run preflight        # or quality:local:no-lh, or pytest, etc.
# Generic fallback:
<lint> && <typecheck> && <build> && <test>
```

Fix all locally-reproducible failures in a single batch.

### Phase 3 — Fix CI-only failures (varies)

For browser-dependent / runner-dependent failures:

1. Extract exact values from CI logs (not just "failed")
2. Distinguish environmental flake from real regression
3. Fix regressions; adjust environmental thresholds with documented rationale

### Phase 4 — Single push, full watch

```bash
git add <specific files>
git commit -m "fix: unclog CI — [all fixes summarized]"
git push origin main
gh run watch $(gh run list --limit 1 --json databaseId -q '.[0].databaseId') --exit-status
```

If it fails: return to Phase 0 with fresh triage. Never push partial fixes.

### Phase 5 — Post-mortem audit

After green CI + successful deploy:

1. Review every change as if someone else made it — find flaws
2. For each fix, ask: "What structural change prevents this class of failure?"
3. Implement structural fixes as a separate commit

### Phase 6 — Feed back into this SOP

If this incident revealed a new failure category, coupling point, or principle, update this document. Version as `sop--cicd-resilience-v2.md` (never overwrite).

---

## Part C: Project Instantiation Template

Each project that adopts this SOP should create a `.quality/GOVERNANCE-COUPLING.md` with the following structure:

```markdown
## Coupling Map

| If you change... | Also update... | Enforced by |
|-----------------|----------------|-------------|
| (project-specific entries) | | |

## Preflight Command

`npm run preflight` / `make preflight` / etc.

## CI-Only Checks (cannot reproduce locally)

- (list checks that require CI environment)

## Environment-Split Thresholds

| Metric | CI floor (error) | Local target (warn) |
|--------|------------------|---------------------|
| (project-specific) | | |
```

---

## Appendix: Precedent Timeline (Portfolio, Feb–Mar 2026)

| Date | Commit | Failure category | Fix |
|------|--------|-----------------|-----|
| Feb 17 | Initial blockage | Multiple | — |
| Mar 5 | bd858c3 | Code bug | HTML validation errors |
| Mar 5 | f3209e6 | Drift | Missing routes in a11y manifest |
| Mar 5 | 50a0659 | Threshold | Lighthouse perf 0.98→0.90 for CI |
| Mar 5 | 73e4a2d | Formatter | Biome-formatted 0.9 vs 0.90 |
| Mar 6 | e0122bf | Mixed | Dynamic Lighthouse URLs, dead hover, logos guard |

Total: 10 commits, 4 push-watch-fix cycles, 8 files, 5 failure categories.

**Lesson:** A single `npm run preflight` would have caught 8 of 10 failures locally, reducing 17 days to ~2 hours.
