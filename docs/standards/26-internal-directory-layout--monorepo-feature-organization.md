# 26: Internal Directory Layout — Monorepo & Feature Organization

**Date:** 2026-05-29
**Status:** ACTIVE — applies to all ~148 repos across the organ system
**Derived from:** External research synthesis (`docs/research/2026-05-29-repository-directory-structure-conventions.md`) reconciled against the existing standards corpus.
**Complements:** `10-repository-standards.md` (root hygiene — this doc adds *internal* layout), `14-logos-documentation-layer.md` (governance docs), `16-data-mesh-medallion-architecture.md` (data layout), `22-essence-function-naming-convention.md` (naming).
**Disambiguation:** "apps/" in this document means the **monorepo directory of deployable applications**. It is unrelated to `21-apps-surface-policy.md`, which governs installed **GitHub Apps (bots)**. Do not conflate.

---

## 1. Purpose & Scope

`10-repository-standards.md` governs the **root** (which files belong in the lobby) and the **README/community-health/badge** surface. This document governs what lives **inside** a repo: source layout, monorepo structure, internal organization, documentation taxonomy, and nesting discipline.

Two layout decisions dominate all others. They are **orthogonal** — decide each independently:

1. **`src/` vs flat** — an *import-isolation* decision (does importable code live under `src/`?).
2. **Monorepo (`apps/` + `packages/`) vs single-project** — a *deployable-count* decision (more than one thing ships from this repo?).

## 2. Decision 1 — `src/` vs flat layout

| Use | When |
|---|---|
| **`src/` layout** (importable code under `src/<pkg>/`) | Any library others install; any app that is packaged/containerized; anything a team works on; anything older than a weekend. **Default for organ repos.** |
| **Flat layout** (code at root) | One-off scripts, demos, throwaway prototypes only. |

**Rationale (PyPA):** the `src/` layout prevents accidental import of the in-development copy and enforces that an editable install imports only what was meant to be importable.

**Per-language `src/` equivalent** (defers to ecosystem norm; never fight the framework):

| Language | Importable-code home |
|---|---|
| Python | `src/<package>/` (PyPA src layout; `uv init --package`) |
| TypeScript/JS | `src/` |
| Rust | `src/` (Cargo default) or `crates/<crate>/src/` in a workspace |
| Go | root `main.go` + `go.mod`; `cmd/<binary>/` only with >1 binary; `internal/` for compiler-enforced privacy; `pkg/` **only** when publishing a stable external API |

> **Go caution:** `golang-standards/project-layout` is a community convention, **not** a Go-team standard. Adopt `cmd/`/`internal/`/`pkg/` piecewise, only where each maps to a real problem.

## 3. Decision 2 — Monorepo `apps/` + `packages/`

Adopt a monorepo when a repo has **more than one deployable**, or when code is being shared by copy-paste / submodule across repos.

```
<repo>/
├── apps/        # Deployable applications — package-graph SINKS (nothing imports them)
├── packages/    # Reusable libraries — consumed by apps
├── tooling/     # Custom dev tooling, codemods (optional)
├── infra/       # IaC: Terraform / Pulumi / K8s (optional)
├── docs/
├── scripts/
├── .github/
├── turbo.json | nx.json
├── pnpm-workspace.yaml
├── package.json          # { "private": true } — root delegates only
└── tsconfig.base.json
```

**Invariants:**
1. `apps/*` are package-graph **sinks** — they import from `packages/*`; nothing imports an app.
2. **Never** reach across package boundaries with `../` — install the package as a workspace dependency.
3. Each package owns its own manifest + scripts; the root only delegates (`"build": "turbo run build"`).
4. **No nested packages** (`apps/a/b` where `apps/a` is also a package breaks tooling).
5. **Group by domain, not by tech** — `packages/booking/`, not `packages/components/`.
6. Enforce dependency rules via tags / module boundaries / `BUILD` visibility.
7. Root manifest is `private: true`.

**Do NOT adopt a monorepo** when teams need fully independent release cadences with strict source-access boundaries, or when the build-tooling + CI-cache investment isn't justified. Monorepos are coupled to trunk-based development in practice.

> **Organ-system note:** the workspace is *already* a 2-level monorepo-of-repos (`~/Workspace/<org>/<repo>/`, doc `#22`). This section governs the **intra-repo** monorepo decision, not the org topology.

## 4. Inside `src/` — organize by feature, not by type

The single largest predictor of whether a codebase ages well. **Feature/domain folders** (colocation) scale; **type folders** (`components/`/`services/`/`hooks/`/`utils/`) collapse before ~20 modules.

```
src/
├── features/
│   ├── billing/        # component + test + api + types + styles, colocated
│   └── checkout/
├── shared/             # generic, domain-free building blocks (used by ≥2 features)
└── app/                # composition root, routing, providers
```

- **Co-locate** unit tests, styles, and types next to the code (`foo.ts` + `foo.test.ts`).
- **Integration/E2E** tests get a top-level `tests/` or `e2e/` (they cross feature boundaries).
- Promote to `shared/` **only** when used by ≥2 features and genuinely generic.
- **Cap nesting at ~3 levels.** `internal/services/user/handlers/http/v1/` is a smell.

Lineages: Feature-Sliced Design (frontend), DDD package-by-feature (backend), Next.js App Router colocation (`_components/` to opt out of routing).

## 5. Documentation taxonomy — Diátaxis, reconciled with Logos

The corpus runs **two documentation layers at different altitudes**. They coexist; neither replaces the other.

| Layer | Framework | Lives in | Answers |
|---|---|---|---|
| **Technical / user docs** | **Diátaxis** | `docs/{tutorials,how-to,reference,explanation}/` | "How do I use this software?" |
| **Governance narrative** | **Logos tetrad** (doc `#14`) | `docs/logos/{telos,pragma,praxis,receptio}.md` | "What is this formation, honestly, and where is it going?" |

- ADRs: `docs/adr/NNNN-title.md`.
- A repo MAY have both trees. Diátaxis governs **how-to-use**; Logos governs **what-it-is/why** per the Tetradic Counterpart. **Do not force Diátaxis onto governance corpora**, and do not force Logos onto a plain library's user docs.

## 6. Configuration & environments

- **Tool configs:** prefer `.config/` consolidation where tooling supports it (per `#10` §2); otherwise root.
- **Monorepo configs:** shared base at root (`tsconfig.base.json`, `eslint.config.base.js`); packages extend.
- **Environments:** **directory-per-environment** (`envs/{dev,staging,prod}/` or kustomize `overlays/`). **Never branch-per-environment** — it creates merge-hell and breaks promotion.
- **Data layout** (medallion/bronze-silver-gold) defers to `16-data-mesh-medallion-architecture.md`.

## 7. Naming — defer to essence-function (#22)

Generic advice says "short lowercase names." **Inside the organ system, `22-essence-function-naming-convention.md` is authoritative** — repos follow `[organ]-[type]--[specific-name]` (double-dash). Internal directories use short lowercase kebab/snake per language norm. Where generic advice and `#22` conflict, `#22` wins.

## 8. Restructure triggers (when to act)

| Signal | Action |
|---|---|
| `components/` (or any type-folder) exceeds ~20 entries | Switch to feature folders (§4) |
| >1 team owns code in one `src/` subtree | Introduce package boundaries (§3) |
| >1 build artifact from one manifest | Split into `apps/<artifact>/` (§3) |
| Root file count >~25 (code repos; cf. `#10` <20 target) | Consolidate configs/scripts/community files |
| Any directory >3 levels deep | Flatten (§4) |
| Branch-per-environment in a config repo | Switch to directory-per-environment (§6) |

## 9. Compliance checklist (append to `#10` §7 usage)

### Internal layout
- [ ] Importable code under `src/` (or language equivalent) unless a justified flat/throwaway repo
- [ ] Monorepo decision matches deployable count; `apps/` are sinks; no `../` cross-package imports
- [ ] `src/` organized by feature/domain, not technical type
- [ ] Unit tests colocated; integration/E2E in top-level `tests/`/`e2e/`
- [ ] No directory deeper than ~3 levels
- [ ] Docs use Diátaxis (technical) and/or Logos `#14` (governance) appropriately
- [ ] Environments use directory-per-environment, not branch-per-environment
- [ ] Naming defers to `#22` (repo) and language norm (internal dirs)

## Appendix: Precedence & relationship

This document is **additive** (per no-deletion principle `#23`) and introduces **no contradictions** with existing standards:

- For **root** files/dirs, README, community-health, badges, curation → defer to `10-repository-standards.md`.
- For **repo naming** → defer to `22-essence-function-naming-convention.md`.
- For **governance documentation** → defer to `14-logos-documentation-layer.md`.
- For **data/lakehouse layout** → defer to `16-data-mesh-medallion-architecture.md`.
- For **GitHub Apps/bots** (NOT `apps/` dirs) → see `21-apps-surface-policy.md`.
- For **internal source layout, monorepo structure, feature organization, doc taxonomy, nesting, environments**, **this document is authoritative.**
