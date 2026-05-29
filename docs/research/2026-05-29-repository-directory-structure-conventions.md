---
title: Repository Directory Structure — Universal Principles, Conventions, and Patterns That Scale
type: research-input
captured: 2026-05-29
provenance: External research report supplied by conductor; ingested as the source justification for `docs/standards/26-internal-directory-layout--monorepo-feature-organization.md`. Restored to full fidelity 2026-05-29 (the initial ingest was a lossy condensation; this is the complete report).
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
  Treat as anecdotal; do **not** cite Octoverse 2024 as the source. It is flagged
  inline below where it appears (§7) and downgraded/cut in standard #26.

> **Fidelity note:** an earlier ingest stored a condensed synthesis at this path.
> This is the full report restored, so no detail (big-project breakdowns, FSD
> layers, worked examples, citations) is lost. The condensed key-findings remain
> available in git history.

---

# Repository Directory Structure: Universal Principles, Conventions, and Patterns That Scale

## TL;DR

- **Lead with a small, predictable root**: keep `src/` (or `apps/` + `packages/` for monorepos), `tests/`, `docs/`, `scripts/`, `.github/`, plus the canonical root files (`README.md`, `LICENSE`, `CHANGELOG.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`) — this single pattern is shared by React, Kubernetes, Rust, VS Code, and Turborepo and is what reviewers, recruiters, and new contributors expect to see.
- **Default to a monorepo with an `apps/` + `packages/` split for any project with more than one deployable, and use a `src/` layout for any library you intend others to install** — these two decisions prevent ~80% of the structural pain teams hit at the 6–18 month mark and align directly with the conventions enforced by Turborepo, Nx, pnpm/Yarn workspaces, and modern Python packaging.
- **Organize *inside* `src/` by feature/domain, not by technical type**, colocate tests and styles next to the code they belong to, and never nest deeper than ~3 levels — flat, feature-oriented trees scale from solo projects to Google-scale monorepos (≈2 billion lines of code in a single repo), whereas `components/`, `services/`, `utils/` grab-bags collapse before you hit 20 modules.

## Key Findings

1. **There is no single "official" standard, but there is strong cross-ecosystem convergence.** The same 6–10 top-level entries — `src/`, `tests/`, `docs/`, `scripts/` (or `tools/`), `examples/`, `build/`, `.github/`, `README.md`, `LICENSE`, `CHANGELOG.md` — appear in projects as different as jQuery, Node.js, three.js, Redis, Bitcoin, MongoDB, Facebook React, Rust, and ASP.NET. Treat this set as the de facto baseline.
2. **Two layout decisions matter more than any other**: (a) `src/` vs flat layout for importable code, and (b) `apps/` + `packages/` vs flat for repos with more than one deployable. Both decisions trade five minutes of upfront scaffolding for years of avoided refactors.
3. **Monorepos are the default for organizations operating at scale.** Google, Meta, Microsoft, Uber, Twitter, and Airbnb all use them; Google's monorepo holds approximately 2 billion lines of code across 9 million source files in 86 TB of storage. Per Potvin & Levenberg's July 2016 CACM paper, "Google's codebase is shared by more than 25,000 Google software developers from dozens of offices in countries around the world. On a typical workday, they commit 16,000 changes to the codebase, and another 24,000 changes are committed by automated systems" — 40,000 total daily changes across the single repository. *(Figures are a January 2015 snapshot — see editorial note.)*
4. **Open-source community-health files have a privileged, GitHub-aware location.** `README.md`, `LICENSE`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, `CODEOWNERS`, issue/PR templates, and `FUNDING.yml` are surfaced by GitHub when placed in the repo root or in `.github/` (or for some files, `docs/`). `LICENSE` must live in the root for GitHub's license detection to work; everything else can be safely consolidated under `.github/`.
5. **The "Standard Go Project Layout" (`cmd/`, `internal/`, `pkg/`) is a community convention, not a Go-team standard**, and is overkill for small projects. Use it only when its individual pieces map onto real problems you have (multiple binaries → `cmd/`; compiler-enforced privacy → `internal/`; explicit public API → `pkg/`).
6. **Co-location beats global folders.** Whether you're working in React, Nuxt, Next.js, Django, or a Go service, putting a component's test, styles, and types next to the component itself ages better than `components/`, `tests/`, `styles/` global directories.
7. **For docs, adopt Diátaxis** (Tutorials / How-To / Reference / Explanation). Gatsby (per a testimonial on diataxis.fr: "the Diátaxis framework was our go-to resource throughout the project"), Cloudflare ("Diátaxis became our north star for information architecture"), and Canonical (the employer of Diátaxis creator Daniele Procida) all use it, and the Python community is actively adopting it via the python.org "Adopting the Diátaxis framework for Python documentation" discussion. It works because it tells readers and writers where new content belongs. *(In the organvm corpus this is reconciled with the Logos tetrad — see standard #26 §5.)*

## Details

### 1. The Universal Baseline: What Belongs at the Root

After surveying conventions documented at the kriasoft/Folder-Structure-Conventions reference and the GitHub special-files guides, plus the actual roots of major OSS projects, a common minimum set emerges. Use short, lowercase names; the only ALL-CAPS files are the legacy community-health markers.

```
my-project/
├── .github/                # Issue/PR templates, workflows, CODEOWNERS, FUNDING.yml
├── .vscode/ or .idea/      # Optional: shared editor settings (commit only generic ones)
├── docs/                   # Long-form documentation (Diátaxis-organized)
├── src/  (or app/, lib/)   # All importable source code
├── tests/ (or test/)       # Tests not colocated with source
├── scripts/ (or tools/)    # Build, release, dev convenience scripts
├── examples/               # Runnable usage examples (libraries)
├── build/ or dist/         # Generated artifacts (usually .gitignored)
├── .editorconfig           # Cross-IDE formatting baseline
├── .gitignore
├── .gitattributes
├── README.md               # What/Why/How — the front door
├── LICENSE                 # MUST be at root for GitHub license detection
├── CHANGELOG.md            # Per Keep a Changelog convention
├── CONTRIBUTING.md         # Surfaced on New Issue / New PR pages
├── CODE_OF_CONDUCT.md
├── SECURITY.md             # Vulnerability disclosure policy
└── <language manifest>     # package.json, pyproject.toml, go.mod, Cargo.toml, etc.
```

**Why this layout works:** It puts every file a reviewer, recruiter, or new contributor looks for *exactly where they expect to find it*. GitHub Docs explicitly recognize this convention: "If you put your README file in your repository's hidden `.github`, root, or docs directory, GitHub will recognize and automatically surface your README." The same applies to community-health files.

**The `.github/` directory** is special. It holds:

- `workflows/*.yml` — GitHub Actions (this location is **mandatory**, not configurable)
- `ISSUE_TEMPLATE/` and `PULL_REQUEST_TEMPLATE.md`
- `CODEOWNERS` — automatic reviewer assignment (also valid at root or `docs/`, with `.github/` being the preferred location per GitHub Docs because it keeps repo-config files centralized and "takes precedence" when duplicated)
- `dependabot.yml`, `FUNDING.yml`, `release.yml`

### 2. Single-Application Layouts: `src/` vs Flat

**Flat layout** (importable code at the root):

```
my_app/
├── my_app/
│   └── __init__.py
├── tests/
└── pyproject.toml
```

**`src/` layout** (importable code inside `src/`):

```
my_app/
├── src/
│   └── my_app/
│       └── __init__.py
├── tests/
└── pyproject.toml
```

The Python Packaging Authority's authoritative guidance is unambiguous: "The src layout helps prevent accidental usage of the in-development copy of the code… [it] helps enforce that an editable installation is only able to import files that were meant to be importable." pyOpenSci, Real Python, and Poetry (as of Feb 2025) all recommend `src/` for any library you intend to publish or for any non-trivial application. uv currently defaults to flat layout but allows `uv init --package` to produce `src/`.

**Recommendation:**

- **Flat layout** for one-off scripts, demos, and prototypes.
- **`src/` layout** for any library, any application that will be packaged or containerized, anything older than a weekend, and anything a team will work on. The minor friction of `pip install -e .` is dwarfed by the time saved on import bugs.

The Go ecosystem has its own variant of this debate around `cmd/`, `internal/`, and `pkg/` from the community-driven `golang-standards/project-layout` repo (which the Go team explicitly does not endorse as official). The pragmatic consensus that has emerged in 2024–2025:

- **Start with `main.go` + `go.mod` at the root.** This is what `go install github.com/you/project@latest` works best against.
- **Add `cmd/<binary>/main.go` only when you have more than one binary** in the repo.
- **Use `internal/` when you genuinely want the Go compiler to block external imports** of your code — its semantics are language-enforced, which makes it valuable.  Many Go-experienced authors (Laurent Senta, Eli Bendersky, the Applied Go blog) argue most projects need only `cmd/` and `internal/`, never `pkg/`.
- **Add `pkg/` only when you're explicitly publishing a stable, externally consumed API**, since putting code there is a public-API commitment.

### 3. Monorepo Conventions

Companies including Google, Meta, Microsoft, Twitter, Uber, and Airbnb use monorepos. The reason isn't fashion — it's that monorepos eliminate cross-repo coordination overhead, enable atomic refactors across services, and give organizations a single source of truth for code, tooling, and dependencies. Google's monorepo is the largest documented example: Rachel Potvin and Josh Levenberg report in the July 2016 *Communications of the ACM* that "The Google codebase includes approximately one billion files and has a history of approximately 35 million commits spanning Google's entire 18-year existence. The repository contains 86TB of data, including approximately two billion lines of code in nine million unique source files." *(January 2015 snapshot — see editorial note.)*

The canonical modern monorepo layout — used by Turborepo, Nx (with `apps/` + `libs/`), pnpm/Yarn/npm workspaces, and most large JS/TS codebases — looks like this:

```
my-monorepo/
├── apps/                       # Deployable applications (sinks in the package graph)
│   ├── web/                    # Next.js / Vite / SvelteKit app
│   ├── api/                    # Express / Fastify / NestJS service
│   └── docs/                   # Docs site
├── packages/  (or libs/)       # Reusable libraries (consumed by apps)
│   ├── ui/                     # Shared component library
│   ├── config/                 # Shared ESLint/TS/Prettier configs
│   ├── utils/                  # Shared utilities
│   └── types/                  # Shared TypeScript types / schemas
├── tooling/  (optional)        # Custom dev tooling, codemods, generators
├── infrastructure/ or infra/   # Terraform/Pulumi/K8s manifests
├── docs/                       # Repo-level architecture docs
├── scripts/
├── .github/
├── turbo.json (or nx.json)     # Build orchestrator config
├── pnpm-workspace.yaml         # Workspace declaration
├── package.json                # Root: { "private": true, scripts: { build: "turbo run build" } }
└── tsconfig.base.json
```

**Key rules for monorepos** (synthesized from Turborepo's official "Structuring a repository" docs and Nx's folder-structure guidance):

1. **`apps/*` are package-graph sinks** — they import from `packages/*` but nothing imports from them. Per Turborepo's docs: "It's best practice that your Application Packages are the 'end' of your Package Graph, not being installed into other packages of your repository."
2. **Never reach across package boundaries with `../`.** If you find yourself doing it, install the package as a workspace dependency instead.
3. **Each package has its own `package.json`** (or `pyproject.toml`, `go.mod`, `Cargo.toml`). Each package owns its own scripts; the root only delegates: `"build": "turbo run build"`.
4. **No nested packages.** Turborepo will reject `apps/a/b` if `apps/a` is also a package — the ambiguity breaks tools.
5. **Group by domain, not by tech.** Nx's recommendation: group projects "usually updated together" — e.g., `libs/booking/`, `libs/check-in/`, `libs/shared/`. This minimizes navigation and surfaces team ownership.
6. **Use tags or directory boundaries to enforce dependency rules** (Nx tags, ESLint `no-restricted-imports`, Bazel `visibility`).
7. **One state-of-the-world per package.json `private: true`** at the root prevents accidental publishing of the meta-repo.

**Polyglot monorepos** (Bazel, Pants, Buck) follow the same shape but use `BUILD`/`BUILD.bazel` files at every directory that produces an artifact. Google's internal layout strictly enforces this — directory layout uniformity is the price of admission for monorepo tooling.

**When *not* to use a monorepo:** when teams need fully independent release cadences with strict source-access boundaries, when the tooling investment isn't justified, or when you're deploying highly autonomous services with different security postures. Polyrepos suit these cases better.

### 4. Inside `src/`: Organize by Feature, Not by Type

The single largest predictor of whether a codebase will age well is whether its internal structure is **feature/domain-based** or **type-based**. Type-based (`components/`, `services/`, `hooks/`, `utils/`) starts easy and rots fast — by the time you have 20 components, finding everything related to "checkout" means opening five directories.

Feature-based (colocation):

```
src/
├── features/
│   ├── billing/
│   │   ├── BillingForm.tsx
│   │   ├── BillingForm.test.tsx
│   │   ├── billing.api.ts
│   │   ├── billing.types.ts
│   │   └── billing.styles.css
│   ├── checkout/
│   └── auth/
├── shared/             # Generic, domain-free reusable building blocks
│   ├── ui/             # Buttons, modals, form primitives
│   └── lib/            # date, string, http helpers
└── app/                # Composition root, routing, providers
```

The same principle is the foundation of:

- **Feature-Sliced Design** (FSD) for frontends — layers `app/`, `processes/`, `pages/`, `widgets/`, `features/`, `entities/`, `shared/` with a strict dependency rule (lower layers don't import from higher ones).
- **Domain-Driven Design** package-by-feature for backends — `user/`, `order/`, `payment/` packages each containing their handler, service, and repository.
- **Next.js App Router colocation** — components, hooks, and helpers live next to the route that uses them, with `_components/` underscore-prefixed directories to opt out of routing.

**Co-location rules of thumb:**

- Unit tests sit next to the unit (`foo.ts` + `foo.test.ts`), giving short relative imports — Create React App, Jest, and Vitest all auto-discover this pattern.
- Integration/E2E tests get a top-level `tests/` or `e2e/` because they cross feature boundaries by definition.
- Move code to `shared/` only when it's used by ≥2 features and is genuinely generic.
- Cap directory nesting at ~3 levels. Deeply nested paths like `internal/services/user/handlers/http/v1/` are a code smell.

### 5. Documentation and Configuration Placement

**Documentation (`docs/`):** Adopt the Diátaxis framework. Per the diataxis.fr website, it "identifies four distinct needs, and four corresponding forms of documentation - tutorials, how-to guides, technical reference and explanation." Layout:

```
docs/
├── tutorials/         # Learning-oriented: get a beginner to first success
├── how-to/            # Task-oriented: solve a specific problem
├── reference/         # Information-oriented: API, config, CLI specs
└── explanation/       # Understanding-oriented: architecture, decisions, ADRs
```

For ADRs (Architecture Decision Records), `docs/adr/NNNN-title.md` is the convention popularized by Michael Nygard and the `adr-tools` project.

**Configuration files:** Modern best practice is to consolidate, not scatter. Two valid patterns:

1. **Root files (the dominant pattern)** — `.eslintrc`, `tsconfig.json`, `pyproject.toml`, `Makefile`, `Dockerfile` at the root. Pros: discoverable, tools find them by walking up the tree. Cons: root gets crowded.
2. **Dotfile consolidation** — `.config/` directory holding all per-tool configs (VS Code uses `.config/`). Modern tools increasingly support pointing at non-root config paths.

For monorepos: keep shared base configs (`tsconfig.base.json`, `eslint.config.base.js`) at the root, and let each package extend them via its own `tsconfig.json` / `.eslintrc`. Centralizing in a `configs/` or `tooling/` package is also common (Turborepo's `packages/eslint-config/`, `packages/typescript-config/` pattern).

**Environment-specific configs:** Use a directory-per-environment layout (`envs/dev/`, `envs/staging/`, `envs/prod/` or Kubernetes-style `overlays/dev`, `overlays/prod`). The OneUptime ArgoCD guide is blunt: "Do not use branch-per-environment. Using dev, staging, production branches sounds clean but creates merge hell and makes promotion difficult. Use directory-per-environment instead." The same applies to Terraform — prefer `envs/dev/`, `envs/prod/` directories over workspaces for any non-trivial layout.

### 6. How the Big Projects Actually Do It

These five layouts are worth studying as canonical examples because each represents a different scale and ecosystem; all are observable at the repo root on GitHub.

**React (`facebook/react`)** — JS monorepo built around `packages/`:

```
.github/  compiler/  fixtures/  flow-typed/  packages/  scripts/
+ package.json, babel.config.js, ReactVersions.js, CHANGELOG.md, CONTRIBUTING.md
```

`packages/` contains react, react-dom, scheduler, etc.; `fixtures/` holds standalone test apps used to validate React against real environments; `scripts/` holds Rollup, Jest, and release tooling. This is the textbook open-source JS monorepo shape.

**Kubernetes (`kubernetes/kubernetes`)** — large polyglot Go monorepo demonstrating `cmd/`/`pkg/`/`staging/`:

```
api/  build/  CHANGELOG/  cluster/  cmd/  docs/  hack/  pkg/  plugin/  staging/  test/  third_party/  vendor/
+ Makefile, OWNERS, OWNERS_ALIASES, go.mod, go.work, SECURITY_CONTACTS
```

`cmd/` contains main entry points for each binary (kubelet, kube-apiserver, etc.); `pkg/` holds the bulk of Go library code; `staging/src/k8s.io/...` is "the staging area for packages that have been split to their own repository… The code in the staging/ directory is authoritative, i.e. the only copy of the code" — it's then periodically published to standalone repos like `client-go`. `hack/` contains shell scripts for codegen, lint, and dev tasks. Kubernetes also uses `OWNERS` files (predecessor concept to GitHub's `CODEOWNERS`) at every directory level.

**Rust (`rust-lang/rust`)** — compiler + runtime monorepo:

```
.github/  LICENSES/  compiler/  library/  src/  tests/
+ Cargo.toml, Cargo.lock, x.py (bootstrap meta-driver), RELEASES.md, LICENSE-APACHE, LICENSE-MIT
```

`compiler/` contains the `rustc_*` crates that make up the compiler; `library/` contains the standard libraries (`core`, `alloc`, `std`, `proc_macro`, `test`); `src/` houses the bootstrap system (`src/bootstrap/`), tools (`src/tools/` — rustdoc, clippy, miri, tidy, compiletest), CI configs, docs, and the LLVM submodule; `tests/` holds the full compiler test suite. `x.py` is the meta build driver. Even this enormous codebase has fewer than ten top-level entries.

**VS Code (`microsoft/vscode`)** — TypeScript application with platform integration:

```
.config/  .devcontainer/  .github/  .vscode/  build/  cli/  extensions/  remote/  resources/  scripts/  src/  test/
+ package.json, product.json, gulpfile.mjs, eslint.config.js, ThirdPartyNotices.txt
```

`src/` is the TypeScript core editor source; `extensions/` is the bundled built-in extensions folder; `cli/` is the Rust-based command-line launcher; `remote/` supports remote/server scenarios; `build/` holds the gulp build pipeline; `product.json` differentiates the OSS build from the branded Microsoft build. Note the `.config/` directory consolidating per-tool configs.

**Turborepo (`vercel/turborepo`)** — the canonical `apps/` + `packages/` JS monorepo, plus a Rust binary:

```
.github/  apps/  cli/  crates/  docs/  examples/  packages/  scripts/  turborepo-tests/
+ turbo.json, pnpm-workspace.yaml, pnpm-lock.yaml, Cargo.toml, rust-toolchain.toml, package.json, tsconfig.json
```

`apps/` contains deployable applications; `packages/` contains shared internal packages; `crates/` contains the Rust crates implementing the `turbo` binary; `examples/` holds dozens of starter templates. The `apps/` + `packages/` split is echoed by every official Turborepo starter and by Yarn/pnpm/npm workspaces docs.

### 7. Why Structure Matters for Maintainability, Hiring, and Open Source

**Maintainability.** Predictable structure is the single highest-leverage decision a codebase makes. It dictates where new code goes (reducing bikeshedding), how easily code can be deleted (clean removal vs. orphaned files in five folders), and how confidently refactors can be performed (clear ownership boundaries). The Feature-Sliced Design team puts it precisely: a folder structure "becomes part of your team's shared language. It codifies conventions, reduces bikeshedding, and allows multiple teams to work in parallel on the same codebase architecture."

**Team collaboration.** `CODEOWNERS` plus a clean directory hierarchy means PRs auto-route to the right reviewers without coordination overhead. In monorepos, the directory tree often mirrors the team org chart, as Luca Pette argues: "you should organise a monorepo so that it loosely reflects the way teams are split" — making the repo itself a leadership communication tool.

**Hiring and portfolio.** When recruiters or hiring managers look at a candidate's GitHub (which they do mostly for tie-breaking between equally qualified candidates, per multiple hiring-manager reports), they're scanning for signals of professionalism: a real README, a license, consistent structure, and meaningful commits. A messy root with `app2-final-v3/`, no README, and committed `node_modules/` is actively disqualifying. ⚠️ **[Unverified — see editorial note]** A stat circulated as GitHub State of the Octoverse 2024 claims profiles "with optimized READMEs and consistent commit patterns receive 3x more profile visits and significantly more interview requests"; this figure could not be located in the primary Octoverse 2024 release — treat it as directional/anecdotal and do not cite Octoverse 2024 as the source.

**Open-source contribution.** A new contributor's first 60 seconds in a repo determine whether they file a PR or close the tab. They look for:

1. A README that says what the project is and how to run it.
2. A `CONTRIBUTING.md` that tells them the workflow.
3. A `src/` or `packages/` directory that matches what they'd expect for the language.
4. Tests they can run.
5. `LICENSE` (without it, GitHub doesn't even show the repo as properly licensed, and many contributors won't touch it).

Every one of these maps to a specific file or directory location convention.

## Recommendations

**For any new project, do these on day one:**

1. Initialize with a real `README.md`, `LICENSE` (at root), `.gitignore`, `.editorconfig`, and `CHANGELOG.md` keeping the Keep a Changelog format.
2. Pick **`src/` layout** unless you're certain this is a throwaway script. The 5 minutes it costs is the cheapest insurance you'll ever buy.
3. Create `.github/` with at least `ISSUE_TEMPLATE/bug_report.md`, `PULL_REQUEST_TEMPLATE.md`, and `workflows/ci.yml`. Add `CODEOWNERS` once you have ≥2 people.
4. Add `SECURITY.md` and `CODE_OF_CONDUCT.md` (Contributor Covenant) before going public.

**Add a monorepo (`apps/` + `packages/`) when:** you have more than one deployable, you start sharing code via `git submodule` or copy-paste, or you have ≥2 teams that need to refactor across services. Choose **Turborepo** for JS/TS-only (lower learning curve), **Nx** if you want generators, dependency-graph visualization, and stronger conventions, or **Bazel/Pants** for polyglot at >100 packages.

**Inside `src/`, switch from type-based to feature-based as soon as you have 3+ distinct functional areas.** Don't wait — every component you add to `components/` is a future migration cost.

**For docs, adopt Diátaxis from the start.** Create `docs/tutorials/`, `docs/how-to/`, `docs/reference/`, `docs/explanation/` even if three of them start empty. Having the slots forces correct categorization of new content.

**Benchmarks that should trigger a restructure:**

- `src/components/` (or equivalent) exceeds ~20 entries → switch to feature folders.
- More than one team owns code in the same `src/` subtree → introduce package boundaries (Nx tags, ESLint module-boundary rules, or split into a new workspace package).
- More than one runtime artifact builds from the same `package.json`/`go.mod`/`pyproject.toml` → split into `apps/<artifact>/` packages.
- Root-level file count > ~25 → consolidate configs into `.config/`, scripts into `scripts/`, and community files into `.github/`.
- Any directory >3 levels deep → flatten.
- Branch-per-environment in your config repo → switch to directory-per-environment.

**For a portfolio repo specifically:** pin 3–5 repos, each with a substantive README (problem, approach, screenshots/GIFs, tech stack, run instructions, "what I'd improve"), a real license, working tests, and a clean directory tree. Recruiters use GitHub as a tie-breaker, not a first filter — but a sloppy GitHub is worse than no GitHub.

## Caveats

- **None of this is enforced by language tooling for most ecosystems.** The exceptions are Go's `internal/` (compiler-enforced) and the existence-of-`BUILD`-files semantic in Bazel/Pants. Everything else is convention — easy to break, easy to lint, but no compiler will stop you.
- **The `golang-standards/project-layout` repo is *not* an official Go standard**, despite its name. The Go team has explicitly declined to bless it. Use it as a menu, not a checklist; for most Go projects, `main.go` + `go.mod` + maybe `internal/` is enough.
- **Many large scientific Python projects (NumPy, SciPy, Matplotlib) use flat layout, not `src/`.** Don't read this as a contradiction of the `src/` recommendation — they predate the convention and the migration cost would be enormous. For new projects, `src/` is the safer default.
- **Monorepos require tooling investment.** Without Turborepo/Nx/Bazel/Pants and a working CI cache, a monorepo will get slower than polyrepos by ~10× as it grows. Don't adopt a monorepo without committing to the tooling.
- **Trunk-based development and monorepos are coupled in practice.** If your branching model is GitFlow with long-lived release branches, you'll fight the monorepo. Google, Facebook, and Microsoft all run trunk-based on top of their monorepos.
- **Some patterns are framework-imposed and override generic advice.** Next.js's App Router dictates `app/`; Django dictates app-level structure; Rails has its own. Always follow framework conventions inside their footprint and apply the universal conventions outside it.
- **The Google statistics cited (≈2B LOC, 86 TB, 25,000+ developers, 16,000 human + 24,000 automated commits/day) are from January 2015** as reported in the July 2016 CACM paper by Potvin & Levenberg; the repository has continued to grow, but more recent canonical numbers are not publicly disclosed. The "3× profile visits" stat is attributed to GitHub's State of the Octoverse 2024 as cited by third parties; treat it as directional rather than precise — the underlying methodology was not located in the primary Octoverse 2024 release (see the ⚠️ editorial flag at the top of this file).
