# Cross-Organ Bottleneck Report

**Generated:** 2026-04-23  
**Source:** registry-v2.json (147 repos) + seed.yaml dependency edges (670 edges across 216 files)  
**Method:** Combined registry `dependencies` arrays with seed.yaml `produces`/`consumes` declarations. A repo qualifies as a bottleneck when it is depended upon by repos in 3 or more distinct organs.

---

## Summary

| Metric | Value |
|--------|-------|
| Total repos analyzed | 147 |
| Total dependency edges (registry) | 46 repos with declared dependencies |
| Total produces/consumes edges (seed.yaml) | 670 |
| Bottleneck repos (3+ organ dependents) | 6 |
| Critical bottleneck (5 organs) | 1 |
| Repos with failing CI | 3 |

---

## Bottleneck Repos

### Tier 1: Critical (5 organs)

| Repo | Organs (count) | CI Status | Tier | Risk |
|------|---------------|-----------|------|------|
| `recursive-engine--generative-entity` | ORGAN-I, ORGAN-II, ORGAN-IV, ORGAN-V, META-ORGANVM (5) | Python CI: PASSING, CodeQL: FAILING | flagship | **HIGH** |

**Detail:** The single most critical dependency in the entire system. RE:GE is the theoretical engine consumed by the art platform (metasystem-master via ORGAN-II), the orchestration layer (agentic-titan via ORGAN-IV), public discourse (public-process via ORGAN-V), and the governance engine (praxis-perpetua via META). Its CodeQL failure is a security-scan issue, not a functional break, but the breadth of dependents means any regression here cascades across 5 of 10 organs.

**Dependents:**
- ORGAN-I: `cognitive-archaelogy-tribunal`
- ORGAN-II: `metasystem-master` (which itself has 11 intra-organ dependents)
- ORGAN-IV: `agentic-titan`, `reverse-engine-recursive-run`, `contrib--langchain-langgraph`
- ORGAN-V: `public-process`
- META-ORGANVM: `praxis-perpetua`

---

### Tier 2: Significant (3 organs)

| Repo | Organs (count) | CI Status | Tier | Risk |
|------|---------------|-----------|------|------|
| `auto-revision-epistemic-engine` | ORGAN-I, ORGAN-II, META-ORGANVM (3) | Release Drafter: PASSING, Secret Scan: PASSING, CodeQL: PASSING | standard | LOW |
| `styx-behavioral-economics-theory` | ORGAN-I, ORGAN-II, ORGAN-III (3) | CodeQL: PASSING, CI: FAILING, Stale Issues: FAILING | standard | **MEDIUM** |
| `vigiles-aeternae--corpus-mythicum` | ORGAN-I, ORGAN-II, META-ORGANVM (3) | Stale Issues: FAILING (no functional CI) | standard | **HIGH** |
| `orchestration-start-here` | ORGAN-III, ORGAN-IV, META-ORGANVM (3) | Minimal CI: PASSING, Secret Scan: PASSING, CodeQL: PASSING | flagship | LOW |
| META-ORGANVM (org-level reference) | ORGAN-I, ORGAN-IV, META-ORGANVM (3) | N/A (org, not repo) | N/A | N/A |

---

### Tier 2 Details

#### `auto-revision-epistemic-engine`
Self-governing orchestration framework. Feeds the art derivative in ORGAN-II and the operational library in META. All CI green. Low risk.

**Dependents:**
- ORGAN-II: `art-from--auto-revision-epistemic-engine`
- META-ORGANVM: `praxis-perpetua`

#### `styx-behavioral-economics-theory`
Behavioral economics theory that feeds both the art layer (ORGAN-II) and the commercial product (ORGAN-III). The `CI` workflow is failing, which means the core test suite for the Styx theory foundation is broken. This matters because both downstream repos (`styx-behavioral-art`, `styx-behavioral-commerce`, `peer-audited--behavioral-blockchain`) depend on it for correctness.

**Dependents:**
- ORGAN-II: `styx-behavioral-art`
- ORGAN-III: `styx-behavioral-commerce`, `peer-audited--behavioral-blockchain`

#### `vigiles-aeternae--corpus-mythicum`
Mythic corpus repo bridging theory (ORGAN-I) to performance art (ORGAN-II) and system watchdog (META). Has 3 local workflow files but only the Stale Issues workflow runs on GitHub, and it is consistently failing. No functional CI (no build/test workflow). High risk given the absence of automated validation.

**Dependents:**
- ORGAN-II: `vigiles-aeternae--theatrum-mundi`
- META-ORGANVM: `vigiles-aeternae--agon-cosmogonicum`

#### `orchestration-start-here`
Central governance repo for ORGAN-IV. Consumed by META's MCP server and ORGAN-III's blockchain product. All CI green. Low risk.

**Dependents:**
- ORGAN-III: `peer-audited--behavioral-blockchain`
- META-ORGANVM: `organvm-mcp-server`

---

## High-Dependency Repos (2 organs, but many dependents)

These repos serve only 2 organs but have exceptionally high intra-organ fan-out, making them de facto bottlenecks:

| Repo | Organs | Intra-organ dependents | CI Status | Risk |
|------|--------|----------------------|-----------|------|
| `metasystem-master` | ORGAN-II, ORGAN-V | 12 (11 ORGAN-II + 1 ORGAN-V) | Monorepo CI: PASSING, CodeQL: PASSING | LOW |
| `organvm-corpvs-testamentvm` | META-ORGANVM (consumed by 6 META repos + ORGAN-III + ORGAN-IV via seed) | 6+ | CI: PASSING, CodeQL: PASSING | LOW |
| `organvm-engine` | META-ORGANVM (consumed by 4 META repos, produces context-files for ALL organs) | 4+ explicit, ALL organs implicit | CI: FAILING | **MEDIUM** |
| `agentic-titan` | ORGAN-IV, ORGAN-V | 3 | All PASSING | LOW |
| `koinonia-db` | ORGAN-VI only | 4 (all ORGAN-VI) | N/A | LOW |

---

## CI Health Summary for Bottleneck Repos

| Repo | Functional CI? | Last status | Last run |
|------|---------------|-------------|----------|
| `recursive-engine--generative-entity` | YES (Python CI) | PASSING (CodeQL failing) | 2026-04-23 |
| `auto-revision-epistemic-engine` | YES (Release Drafter + scans) | ALL PASSING | 2026-04-23 |
| `styx-behavioral-economics-theory` | YES (CI workflow) | **FAILING** | 2026-04-15 |
| `vigiles-aeternae--corpus-mythicum` | **NO** (only Stale Issues) | FAILING | 2026-04-23 |
| `orchestration-start-here` | YES (Minimal CI) | PASSING | 2026-04-23 |
| `organvm-engine` | YES (CI workflow) | **FAILING** | 2026-04-23 |

---

## Risk Assessment

### HIGH RISK (immediate attention)

1. **`recursive-engine--generative-entity`** -- 5-organ dependency, CodeQL failing. A breaking change here would cascade across the entire system. The Python CI passes, so functional risk is contained, but the security scan gap should be resolved.

2. **`vigiles-aeternae--corpus-mythicum`** -- 3-organ dependency, no functional CI at all. Any regression goes undetected. Needs a build/test workflow.

### MEDIUM RISK (scheduled attention)

3. **`styx-behavioral-economics-theory`** -- 3-organ dependency, CI failing since 2026-04-15. The Styx product chain (theory -> art -> commerce) has no automated validation on its foundation layer.

4. **`organvm-engine`** -- Not a 3-organ bottleneck by explicit dependency count, but it produces context-files consumed by ALL organs and its CI is failing. Functionally a system-wide dependency.

### LOW RISK (monitor)

5. **`auto-revision-epistemic-engine`** -- 3-organ dependency, all CI green.
6. **`orchestration-start-here`** -- 3-organ dependency, all CI green.
7. **`metasystem-master`** -- 2-organ but 12 dependents, all CI green.

---

## Recommended Actions

| Priority | Action | Target |
|----------|--------|--------|
| P0 | Fix CodeQL failure | `recursive-engine--generative-entity` |
| P0 | Add functional CI (build + test) | `vigiles-aeternae--corpus-mythicum` |
| P1 | Fix CI failure (broken since Apr 15) | `styx-behavioral-economics-theory` |
| P1 | Fix CI failure | `organvm-engine` |
| P2 | Add integration test: verify RE:GE API contract | Cross: RE:GE -> metasystem-master, agentic-titan |
| P2 | Add dependency-aware CI triggers | System-wide: changes to bottleneck repos trigger downstream CI |

---

## Methodology

1. Parsed `registry-v2.json` to extract all 147 repos with their organ assignments, dependency arrays, CI workflow declarations, and tier classifications.
2. Scanned 216 `seed.yaml` files across `~/Workspace/` (excluding archives and bench directories) to extract `produces`/`consumes` edge declarations.
3. Built a unified dependency graph mapping each target repo to the set of organs whose repos consume it.
4. Identified repos consumed by 3 or more distinct organs as bottlenecks.
5. Verified CI status for each bottleneck via `gh run list` against the correct GitHub organization for each repo.
6. Assessed risk as HIGH (no functional CI + 3+ organ dependents), MEDIUM (CI failing + 3+ organ dependents OR implicit system-wide dependency), or LOW (CI passing).
