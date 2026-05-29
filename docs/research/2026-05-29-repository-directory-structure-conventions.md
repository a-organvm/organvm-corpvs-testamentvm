---
title: Repository Directory Structure — Universal Principles, Conventions, and Patterns That Scale
type: research-input
captured: 2026-05-29
provenance: External research report supplied by conductor; ingested as the source justification for `docs/standards/26-internal-directory-layout--monorepo-feature-organization.md`.
status: REFERENCE — informs standard #26; not itself normative.
---

# Editorial note (added on ingest, 2026-05-29)

This document is **source material**, not a normative standard. The normative
extraction lives in `docs/standards/26-internal-directory-layout--monorepo-feature-organization.md`,
which reconciles these generic conventions against the organvm corpus (defers to
`#22` essence-function naming and `#14` Logos documentation layer).

**Empirical-integrity flags (verified 2026-05-29):**

- ✅ **CONFIRMED** — Google monorepo figures (≈2B LOC, 86 TB, ~9M source files, 1B
  files, 25k+ devs, 16k human + 24k automated commits/day) trace to Potvin &
  Levenberg, *Communications of the ACM*, July 2016, reporting a **January 2015**
  snapshot. Retain the snapshot caveat when citing.
- ⚠️ **UNVERIFIABLE** — the "3× profile visits / more interview requests" figure
  attributed to GitHub Octoverse 2024 could not be located in primary sources.
  Treat as anecdotal; do **not** cite Octoverse 2024 as the source. Downgraded or
  cut in standard #26.

---

## TL;DR

- **Lead with a small, predictable root**: `src/` (or `apps/` + `packages/` for monorepos), `tests/`, `docs/`, `scripts/`, `.github/`, plus canonical root files (`README.md`, `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`). Shared by React, Kubernetes, Rust, VS Code, Turborepo.
- **Default to a monorepo with `apps/` + `packages/` for any project with more than one deployable, and use a `src/` layout for any library others install.** These two decisions prevent most structural pain at the 6–18 month mark.
- **Organize inside `src/` by feature/domain, not technical type**, colocate tests/styles next to code, never nest deeper than ~3 levels. Flat feature-oriented trees scale from solo to Google-scale; `components/`/`services/`/`utils/` grab-bags collapse before ~20 modules.

## Key Findings

1. **No single official standard, but strong cross-ecosystem convergence** on the same 6–10 top-level entries (`src/`, `tests/`, `docs/`, `scripts/`/`tools/`, `examples/`, `build/`, `.github/`, `README.md`, `LICENSE`, `CHANGELOG.md`). Baseline across jQuery, Node.js, three.js, Redis, Bitcoin, MongoDB, React, Rust, ASP.NET.
2. **Two layout decisions matter most** (and are orthogonal): (a) `src/` vs flat for importable code; (b) `apps/`+`packages/` vs flat for repos with >1 deployable.
3. **Monorepos are the default at scale** (Google, Meta, Microsoft, Uber, Twitter, Airbnb). Google: ~2B LOC / 9M files / 86 TB [Jan-2015 snapshot, CACM 2016].
4. **Community-health files have a GitHub-aware location** — root or `.github/` (LICENSE must be at root for license detection).
5. **"Standard Go Project Layout" (`cmd/`/`internal/`/`pkg/`) is a community convention, not a Go-team standard** — adopt piecewise only where the piece maps to a real problem.
6. **Co-location beats global folders** (React, Nuxt, Next.js, Django, Go).
7. **For docs, adopt Diátaxis** (Tutorials / How-To / Reference / Explanation). [In the organvm corpus this is reconciled with the Logos tetrad — see #26.]

## Details

### 1. Universal baseline at the root

```
my-project/
├── .github/        # Issue/PR templates, workflows, CODEOWNERS, FUNDING.yml
├── docs/           # Long-form docs (Diátaxis-organized)
├── src/            # All importable source code
├── tests/          # Tests not colocated with source
├── scripts/        # Build, release, dev scripts
├── examples/       # Runnable usage examples (libraries)
├── build/ or dist/ # Generated artifacts (.gitignored)
├── README.md       # The front door
├── LICENSE         # MUST be at root for GitHub license detection
├── CHANGELOG.md    # Keep a Changelog convention
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── <language manifest>
```

`.github/` holds `workflows/*.yml` (mandatory location), `ISSUE_TEMPLATE/`, `PULL_REQUEST_TEMPLATE.md`, `CODEOWNERS`, `dependabot.yml`, `FUNDING.yml`, `release.yml`.

### 2. Single-application layouts: `src/` vs flat

- **Flat** — importable code at root. For one-off scripts, demos, prototypes.
- **`src/`** — importable code inside `src/`. PyPA: "the src layout helps prevent accidental usage of the in-development copy of the code… [it] helps enforce that an editable installation is only able to import files that were meant to be importable." Recommended for any library, any packaged/containerized app, anything a team works on.
- **Go**: start `main.go` + `go.mod` at root; add `cmd/<binary>/main.go` only with >1 binary; use `internal/` for compiler-enforced privacy; add `pkg/` only when publishing a stable external API. `golang-standards/project-layout` is community, not official.

### 3. Monorepo conventions

```
my-monorepo/
├── apps/           # Deployable applications (package-graph sinks)
├── packages/       # Reusable libraries (consumed by apps)
├── tooling/        # Custom dev tooling
├── infra/          # Terraform/Pulumi/K8s
├── docs/
├── scripts/
├── .github/
├── turbo.json | nx.json
├── pnpm-workspace.yaml
├── package.json    # { "private": true }
└── tsconfig.base.json
```

Rules: `apps/*` are package-graph sinks (nothing imports them); never reach across packages with `../` (install as workspace dep); each package owns its manifest + scripts, root only delegates; no nested packages; group by domain not tech; enforce dependency rules via tags/boundaries; root `private: true`. Polyglot → Bazel/Pants/Buck with `BUILD` files. Avoid monorepo when teams need fully independent release cadence + strict source-access boundaries, or tooling investment isn't justified.

### 4. Inside `src/`: feature, not type

Feature/domain-based (colocation) ages far better than type-based (`components/`/`services/`/`hooks/`/`utils/`). Foundations: Feature-Sliced Design (frontend), DDD package-by-feature (backend), Next.js App Router colocation. Co-location rules: unit tests next to unit; integration/E2E in top-level `tests/`/`e2e/`; move to `shared/` only when used by ≥2 features; cap nesting ~3 levels.

### 5. Docs & configuration

- **Docs**: Diátaxis — `docs/{tutorials,how-to,reference,explanation}/`; ADRs at `docs/adr/NNNN-title.md`.
- **Config**: root files (discoverable) or `.config/` consolidation (VS Code pattern). Monorepo: shared base configs at root, packages extend.
- **Environments**: directory-per-environment (`envs/dev|staging|prod` or kustomize `overlays/`), NOT branch-per-environment.

### 6. How big projects do it

- **React** — JS monorepo around `packages/` + `fixtures/` + `scripts/`.
- **Kubernetes** — Go monorepo: `cmd/` (binaries), `pkg/` (libs), `staging/` (authoritative pre-split packages), `hack/` (scripts), `OWNERS` files.
- **Rust** — `compiler/`, `library/`, `src/` (bootstrap+tools), `tests/`, `x.py`. <10 top-level entries.
- **VS Code** — `src/` (TS core), `extensions/`, `cli/` (Rust), `remote/`, `build/`, `.config/`, `product.json`.
- **Turborepo** — `apps/` + `packages/` + `crates/` (Rust) + `examples/`.

### 7. Why structure matters

Maintainability (where new code goes, clean deletion, confident refactors); team collaboration (CODEOWNERS auto-routing; tree mirrors org chart); hiring/portfolio (README + LICENSE + consistent structure as professionalism signals); OSS contribution (first-60-seconds: README → CONTRIBUTING → expected `src/`/`packages/` → runnable tests → LICENSE).

## Recommendations (day one)

1. Real `README.md`, `LICENSE` (root), `.gitignore`, `.editorconfig`, `CHANGELOG.md`.
2. Pick `src/` unless certainly throwaway.
3. `.github/` with issue/PR templates + `workflows/ci.yml`; `CODEOWNERS` once ≥2 people.
4. `SECURITY.md` + `CODE_OF_CONDUCT.md` before going public.

**Restructure triggers:** `components/` >~20 entries → feature folders; >1 team in one subtree → package boundaries; >1 build artifact per manifest → split into `apps/<artifact>/`; root files >~25 → consolidate; any dir >3 levels → flatten; branch-per-env → directory-per-env.

## Caveats

- Mostly convention, not tooling-enforced (exceptions: Go `internal/`, Bazel/Pants `BUILD`).
- `golang-standards/project-layout` is NOT official Go.
- Many large scientific Python projects (NumPy, SciPy, Matplotlib) use flat layout (predate the convention); `src/` still safer for new projects.
- Monorepos require tooling investment (Turborepo/Nx/Bazel/Pants + CI cache).
- Trunk-based development and monorepos are coupled in practice.
- Framework-imposed structures (Next.js `app/`, Django, Rails) override generic advice within their footprint.
- Google statistics are Jan-2015 (CACM 2016); "3× profile visits" stat is unverified — see editorial note above.
