# Ignition Bootstrap Inspection Report

**Atom:** `231dfd0072c1`
**Date:** 2026-04-23
**Scope:** All repos with `.github/workflows/` across PERSONAL, META, ORGAN-I, ORGAN-III
**Exclusions:** contrib forks, materia-collider bench snapshots, google-takeout artifacts, upstream mirrors (fastmcp, agentkit, k6-contrib, openai-agents-contrib, python-sdk)
**Finding:** organvm-ii-poiesis workspace directory does not exist on disk; organvm-i-theoria and organvm-iii-ergon have no workflow files

---

## Summary Statistics

- **Total repos with workflows:** 77 (own repos, excluding forks/mirrors)
- **Unique secrets (non-GITHUB_TOKEN):** 82
- **Repos with non-GITHUB_TOKEN secrets:** 15
- **Repos with build commands:** 40

---

## Repo Inventory

### PERSONAL (4444J99)

| Repo | Workflows | Secrets | Build Commands |
|------|-----------|---------|----------------|
| 4444J99 (org profile) | validate-submodules.yml | NONE | NONE |
| 4444J99/4444J99 | blog-posts.yml, metrics.yml, snake.yml | METRICS_TOKEN | NONE |
| 4444J99/application-pipeline | quality.yml | NONE | `pip install -e ".[dev]"` |
| 4444J99/domus-semper-palingenesis | lint.yml | NONE | `brew install chezmoi`, `chezmoi init --apply`, `pip install ruff`, `pip install yamllint`, `shellcheck`, `bats` |
| 4444J99/portfolio | build-resume.yml, ci.yml, monitor.yml, refresh-data.yml | NONE | `npm ci`, `npm run build`, `npm run lint`, `npm run test:coverage`, `npm run typecheck:strict`, `pip install "rendercv[full]==2.6"` |

### META-ORGANVM (org-level repos)

| Repo | Workflows | Secrets | Build Commands |
|------|-----------|---------|----------------|
| meta-organvm (root) | ci-minimal.yml | NONE | NONE |
| .github (org defaults) | 143 workflow files (see detail below) | ADD_TO_PROJECT_PAT, APP_PRIVATE_KEY, AUTH_TOKEN, CLAUDE_CODE_OAUTH_TOKEN, CLOUDFLARE_ACCOUNT_ID, CLOUDFLARE_API_TOKEN, DIGEST_RECIPIENTS, DOCKER_PASSWORD, DOCKER_USERNAME, GEMINI_API_KEY, GH_PAT, GOOGLE_API_KEY, GOOGLE_CHAT_WEBHOOK_METRICS, GROK_API_KEY, NPM_TOKEN, OP_SERVICE_ACCOUNT_TOKEN, OPENAI_API_KEY, PAGERDUTY_INTEGRATION_KEY, PERPLEXITY_API_KEY, REGISTRY_PAT, RENDER_API_KEY, SEMGREP_APP_TOKEN, SENTRY_AUTH_TOKEN, SENTRY_ORG, SENTRY_PROJECT, SLACK_WEBHOOK, SLACK_WEBHOOK_ALERTS, SLACK_WEBHOOK_URL, SMTP_PASSWORD, SMTP_PORT, SMTP_SERVER, SMTP_USERNAME, VERCEL_ORG_ID, VERCEL_TOKEN | `npm ci`, `npm run build`, `npm test`, `npx semantic-release`, `npx stryker run`, `pip install pyyaml`, `npx playwright test` |
| .github-org | ci-minimal.yml, dependabot-auto-merge.yml, dispatch-receiver.yml | GITHUB_TOKEN | NONE |
| .github/docs | auto-enable-merge.yml | GITHUB_TOKEN | NONE |
| org-dotgithub | ci-minimal.yml, dispatch-receiver.yml | NONE | NONE |

### META-ORGANVM (application repos with secrets)

| Repo | Workflows | Secrets | Build Commands |
|------|-----------|---------|----------------|
| analytics-engine | ci.yml, weekly-metrics.yml | CROSS_ORG_DISPATCH_TOKEN, GOATCOUNTER_SITE, GOATCOUNTER_TOKEN | `pip install -e .`, `pytest tests/ -v`, `ruff check src/ tests/` |
| essay-pipeline | ci.yml, daily-log.yml, essay-generation.yml, weekly-intelligence.yml | ANTHROPIC_API_KEY, CROSS_ORG_DISPATCH_TOKEN, GEMINI_API_KEY, LLM_PROVIDER, OPENAI_API_KEY, ORCHESTRATION_PAT, PERPLEXITY_API_KEY | `pip install -e .`, `pytest tests/ -v`, `ruff check src/ tests/` |
| life-my--midst--in | auto-deploy.yml, ci-cd.yml, codeql.yml, deploy.yml, performance.yml, release.yml, secret-scan.yml, security.yml, stale.yml, test.yml | KUBE_CONFIG_PRODUCTION, KUBE_CONFIG_STAGING, KUBECONFIG, POSTGRES_DB, POSTGRES_USER, RENDER_DEPLOY_HOOK, SLACK_WEBHOOK, SONAR_TOKEN | `pnpm install --frozen-lockfile`, `pnpm build`, `pnpm lint`, `pnpm test`, `docker build`, `npx playwright install` |
| my-knowledge-base | ci.yml, codeql.yml, pages.yml, release.yml, runtime-probe-dispatch.yml, stale.yml | CODECOV_TOKEN, OP_SERVICE_ACCOUNT_TOKEN | `npm install`, `npm run build`, `npm run test:ci`, `npm run test:coverage`, `npm run generate-embeddings` |
| orchestration-start-here | 19 workflow files | BLUESKY_APP_PASSWORD, BLUESKY_HANDLE, CROSS_ORG_TOKEN, DISCORD_WEBHOOK, GHOST_ADMIN_KEY, LINKEDIN_TOKEN, MASTODON_TOKEN, ORCHESTRATION_PAT | `pip install requests`, `pip install requests pyyaml` |
| organvm-corpvs-testamentvm | ci.yml + 15 other workflow files | CROSS_ORG_TOKEN, DISCORD_WEBHOOK, MASTODON_TOKEN, ORCHESTRATION_PAT | `pip install pyyaml`, `pip install git+.../organvm-engine.git` |
| peer-audited--behavioral-blockchain | beta-promotion.yml, ci.yml, deploy.yml + 8 more | API_ENV_LABEL, API_URL, BETA_API_URL, BETA_DATABASE_URL, CI_BETA_API_URL, DATABASE_URL, RENDER_API_KEY, RENDER_*_SERVICE_ID (x6), STAGING_* (x4), WEB_URL | `npm ci`, `npx turbo run build`, `npx turbo run lint`, `npx turbo run test`, `terraform fmt -check` |
| public-record-data-scrapper | ci.yml + 15 more | AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, CROSS_ORG_DISPATCH_TOKEN, EAS_TOKEN, JF_ACCESS_TOKEN, JF_PASSWORD, JF_URL, JF_USER, TAURI_KEY_PASSWORD, TAURI_PRIVATE_KEY, TF_API_TOKEN | `npm install`, `npm run build`, `npm run lint`, `npm run test:server`, `npx eas build`, `npx tsc --noEmit`, `terraform apply` |
| stakeholder-portal | ci.yml, ingest-cron.yml, maintenance-cron.yml + 5 more | ALERT_EMAIL_FROM, ALERT_EMAIL_TO, ALERT_WEBHOOK_URL, CRON_SECRET, DATABASE_URL, RESEND_API_KEY, SLACK_WEBHOOK_URL | `npm ci`, `npm run build`, `npm run lint`, `npm run test`, `npm run typecheck` |
| sovereign-systems--elevate-align | ci.yml | CLOUDFLARE_API_TOKEN | NONE |
| system-governance-framework | ci.yml + 11 more | FOSSA_API_KEY, SEMGREP_APP_TOKEN | `npm install`, `pip install pre-commit`, `pytest`, `ruff check` |
| petasum-super-petasum | ci.yml + 7 more | ORG_PROJECT_TOKEN | `pytest --cov`, `ruff check` |

### META-ORGANVM (repos with GITHUB_TOKEN only)

| Repo | Workflows | Build Commands |
|------|-----------|----------------|
| a-i--skills | ci.yml, pr-comment.yml, stale.yml, validate-skills.yml | NONE |
| a-mavs-olevm | ci-cd.yml, codeql.yml, project-automation.yml, release-drafter.yml, secret-scan.yml, stale.yml | `npm ci`, `npm run build:exhibits`, `npm run lint`, `npm run test:unit`, `npx playwright install` |
| adaptive-personal-syllabus | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | `pytest --cov`, `ruff check .` |
| agent--claude-smith | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | `npm install -g pnpm` |
| agentic-titan | ci.yml, codeql.yml, governance-audit.yml, release-drafter.yml, secret-scan.yml, stale.yml | NONE |
| alchemia-ingestvm | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | `pytest tests/ -v` |
| announcement-templates | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | NONE |
| auto-revision-epistemic-engine | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | NONE |
| call-function--ontological | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml, validate.yml | `make registry`, `make validate`, `pytest tools/ -v` |
| classroom-rpg-aetheria | ci.yml, codeql.yml, dependency-review.yml, deploy-sandbox.yml, generate_videos.yml, release-drafter.yml, secret-scan.yml, stale.yml | `npm install`, `npm run build`, `npm test -- --run` |
| collective-persona-operations | ci.yml, codeql.yml, release-drafter.yml, stale.yml | NONE |
| community-hub | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | NONE |
| distribution-strategy | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | NONE |
| growth-auditor | ci.yml | `npm ci`, `npm run build`, `npm run lint`, `npm run test`, `npx playwright install` |
| ivi374ivi027-05 | ci.yml, codeql.yml, e2e.yml, release-drafter.yml, secret-scan.yml, stale.yml | NONE |
| kerygma-pipeline | ci.yml | ORCHESTRATION_PAT | NONE |
| koinonia-db | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | NONE |
| materia-collider | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | `pytest tests/ -v`, `ruff check src/ tests/` |
| metasystem-master | art-to-commerce.yml, cla.yml, codeql.yml, metasystem-ci.yml, release-drafter.yml, secret-scan.yml, stale.yml | ORCHESTRATION_PAT | `pnpm --filter @omni-dromenon/core-engine test`, `pnpm run typecheck` |
| narratological-algorithmic-lenses | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | `npm ci -w packages/web`, `uv run pytest`, `uv sync` |
| organvm-engine | ci.yml, cla.yml, dependabot-auto-merge.yml + 8 more | `pytest tests/ -v`, `ruff check src/ tests/` |
| organvm-mcp-server | ci.yml, codeql.yml, dependabot-auto-merge.yml, release-drafter.yml, secret-scan.yml, stale.yml | `pytest tests/ -v`, `ruff check src/ tests/` |
| organvm-ontologia | ci.yml, codeql.yml, stale.yml | `pytest tests/ -v`, `ruff check src/ tests/` |
| public-process | auto-merge.yml, ci.yml, data-refresh.yml, link-check.yml, notify-essay-published.yml, pages.yml, stale.yml | CROSS_ORG_DISPATCH_TOKEN | `pip install -e _pipeline/`, `pip install pyyaml httpx` |
| reading-group-curriculum | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | NONE |
| reading-observatory | ci.yml, weekly-feeds.yml | CROSS_ORG_DISPATCH_TOKEN | `pip install -e .`, `pytest tests/ -v`, `ruff check src/ tests/` |
| recursive-engine--generative-entity | ci.yml, cla.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | NONE |
| reverse-engine-recursive-run | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | `pytest tests/ -v`, `ruff check scripts/` |
| salon-archive | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | NONE |
| schema-definitions | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | `ruff check scripts/ tests/` |
| sema-metra--alchemica-mundi | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | `npm install -g pnpm` |
| social-automation | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | (installs from private repo via GITHUB_TOKEN) |
| system-dashboard | ci.yml, codeql.yml, dependabot-auto-merge.yml, release-drafter.yml, secret-scan.yml, stale.yml | `pytest tests/ -v`, `ruff check src/` |
| the-actual-news | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | `npm install -g pnpm` |
| tool-interaction-design | ci.yml, codeql.yml, release.yml, secret-scan.yml, stale.yml, test.yml | `pytest -q` |
| universal-node-network | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | NONE |
| vigiles-aeternae--agon-cosmogonicum | ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml | `pytest tests/ -v`, `ruff check src/` |
| vox--architectura-gubernatio | ci.yml | `pip install -e ".[dev]"`, `pytest tests/ -v`, `ruff check src/ tests/` |

### META-ORGANVM (repos with no secrets and no build commands)

| Repo | Workflows |
|------|-----------|
| alchemical-synthesizer | ci-minimal.yml, stale.yml |
| atomic-substrata | ci.yml |
| chthon-oneiros | catalog-validator.yml, ci.yml, stale.yml |
| cognitive-archaelogy-tribunal | ci.yml, stale.yml |
| commerce--meta | ci-minimal.yml, stale.yml |
| conversation-corpus-engine | ci.yml |
| editorial-standards | ci.yml |
| kerygma-profiles | ci.yml |
| krypto-velamen | ci-minimal.yml, stale.yml |
| linguistic-atomization-framework | ci.yml, stale.yml |
| nexus--babel-alexandria | ci-minimal.yml |
| praxis-perpetua | ci.yml, stale.yml |
| scale-threshold-emergence | ci.yml |
| styx-behavioral-art | ci.yml, stale.yml |
| styx-behavioral-economics-theory | ci.yml, stale.yml |
| vigiles-aeternae--corpus-mythicum | ci.yml, secret-scan.yml, stale.yml |
| vigiles-aeternae--theatrum-mundi | ci.yml, secret-scan.yml, stale.yml |

---

## Consolidated Secret Inventory

### Tier 1: Cross-Org Orchestration (needed by multiple repos)

| Secret | Used By |
|--------|---------|
| `ORCHESTRATION_PAT` | essay-pipeline, kerygma-pipeline, metasystem-master, organvm-corpvs-testamentvm, orchestration-start-here |
| `CROSS_ORG_DISPATCH_TOKEN` | analytics-engine, essay-pipeline, public-process, public-record-data-scrapper, reading-observatory |
| `CROSS_ORG_TOKEN` | orchestration-start-here, organvm-corpvs-testamentvm |
| `GH_PAT` / `ADD_TO_PROJECT_PAT` / `REGISTRY_PAT` | .github (org defaults) |
| `OP_SERVICE_ACCOUNT_TOKEN` | .github, my-knowledge-base |
| `ORG_PROJECT_TOKEN` | petasum-super-petasum |

### Tier 2: AI/LLM API Keys

| Secret | Used By |
|--------|---------|
| `ANTHROPIC_API_KEY` | essay-pipeline |
| `OPENAI_API_KEY` | .github, essay-pipeline |
| `GEMINI_API_KEY` | .github, essay-pipeline |
| `CLAUDE_CODE_OAUTH_TOKEN` | .github |
| `GROK_API_KEY` | .github |
| `PERPLEXITY_API_KEY` | .github, essay-pipeline |
| `GOOGLE_API_KEY` | .github |

### Tier 3: Infrastructure & Deploy

| Secret | Used By |
|--------|---------|
| `CLOUDFLARE_API_TOKEN` / `CLOUDFLARE_ACCOUNT_ID` | .github, sovereign-systems--elevate-align |
| `RENDER_API_KEY` / `RENDER_*_SERVICE_ID` | .github, life-my--midst--in, peer-audited--behavioral-blockchain |
| `VERCEL_TOKEN` / `VERCEL_ORG_ID` | .github |
| `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` | public-record-data-scrapper |
| `DATABASE_URL` | peer-audited--behavioral-blockchain, stakeholder-portal |
| `DOCKER_USERNAME` / `DOCKER_PASSWORD` | .github |
| `NPM_TOKEN` | .github |
| `TF_API_TOKEN` | public-record-data-scrapper |
| `KUBE_CONFIG_PRODUCTION` / `KUBE_CONFIG_STAGING` | life-my--midst--in |
| `EAS_TOKEN` | public-record-data-scrapper |
| `TAURI_PRIVATE_KEY` / `TAURI_KEY_PASSWORD` | public-record-data-scrapper |

### Tier 4: Notifications & Social

| Secret | Used By |
|--------|---------|
| `SLACK_WEBHOOK` / `SLACK_WEBHOOK_URL` / `SLACK_WEBHOOK_ALERTS` | .github, life-my--midst--in, stakeholder-portal |
| `DISCORD_WEBHOOK` | orchestration-start-here, organvm-corpvs-testamentvm |
| `BLUESKY_APP_PASSWORD` / `BLUESKY_HANDLE` | orchestration-start-here |
| `MASTODON_TOKEN` | orchestration-start-here, organvm-corpvs-testamentvm |
| `LINKEDIN_TOKEN` | orchestration-start-here |
| `GHOST_ADMIN_KEY` | orchestration-start-here |
| `PAGERDUTY_INTEGRATION_KEY` | .github |

### Tier 5: Observability & Security

| Secret | Used By |
|--------|---------|
| `SEMGREP_APP_TOKEN` | .github, system-governance-framework |
| `SENTRY_AUTH_TOKEN` / `SENTRY_ORG` / `SENTRY_PROJECT` | .github |
| `SONAR_TOKEN` | life-my--midst--in |
| `CODECOV_TOKEN` | my-knowledge-base |
| `FOSSA_API_KEY` | system-governance-framework |
| `GOATCOUNTER_SITE` / `GOATCOUNTER_TOKEN` | analytics-engine |

### Tier 6: Email & SMTP

| Secret | Used By |
|--------|---------|
| `SMTP_SERVER` / `SMTP_PORT` / `SMTP_USERNAME` / `SMTP_PASSWORD` | .github |
| `DIGEST_RECIPIENTS` | .github |
| `RESEND_API_KEY` | stakeholder-portal |
| `ALERT_EMAIL_FROM` / `ALERT_EMAIL_TO` | stakeholder-portal |

### Tier 7: App-Specific

| Secret | Used By |
|--------|---------|
| `METRICS_TOKEN` | 4444J99/4444J99 (profile) |
| `APP_PRIVATE_KEY` / `AUTH_TOKEN` | .github |
| `CRON_SECRET` | stakeholder-portal |
| `JF_*` (JFrog) | public-record-data-scrapper |
| `RENDER_DEPLOY_HOOK` | life-my--midst--in |
| `POSTGRES_DB` / `POSTGRES_USER` | life-my--midst--in |

---

## Build Command Taxonomy

### Python repos (pytest + ruff pattern)

```
pip install -e .
pip install -e ".[dev]"
pytest tests/ -v
ruff check src/ tests/
```

**Repos:** organvm-engine, organvm-mcp-server, organvm-ontologia, analytics-engine, essay-pipeline, reading-observatory, materia-collider, system-dashboard, vox--architectura-gubernatio, reverse-engine-recursive-run, vigiles-aeternae--agon-cosmogonicum, adaptive-personal-syllabus, alchemia-ingestvm, tool-interaction-design, nexus--babel-alexandria, petasum-super-petasum, schema-definitions, system-governance-framework

### Node.js repos (npm/pnpm pattern)

```
npm ci / npm install / pnpm install --frozen-lockfile
npm run build
npm run lint
npm run test
npx turbo run build (monorepos)
```

**Repos:** portfolio, .github, a-mavs-olevm, classroom-rpg-aetheria, growth-auditor, my-knowledge-base, peer-audited--behavioral-blockchain, public-record-data-scrapper, stakeholder-portal, metasystem-master, narratological-algorithmic-lenses

### Shell/config repos (linting only)

```
shellcheck / shfmt / yamllint / chezmoi
```

**Repos:** domus-semper-palingenesis

### Infrastructure

```
terraform fmt -check
terraform apply -auto-approve
docker build
```

**Repos:** peer-audited--behavioral-blockchain, public-record-data-scrapper, life-my--midst--in

---

## Gaps and Observations

1. **ORGAN-II workspace missing** -- `~/Workspace/organvm-ii-poiesis/` does not exist on disk. No workflows from Organ-II could be inspected.
2. **ORGAN-I and ORGAN-III** have workspace directories but zero workflow files locally.
3. **The `.github` repo** (org-level defaults) contains 143 workflow files and references 34 unique secrets -- this is the largest secret surface area and the primary target for ignition bootstrapping.
4. **CROSS_ORG_DISPATCH_TOKEN / ORCHESTRATION_PAT / CROSS_ORG_TOKEN** appear to serve overlapping roles across 8+ repos. The ignition script should clarify whether these are the same PAT or distinct tokens.
5. **Many repos use the standard 5-file pattern** (ci.yml, codeql.yml, release-drafter.yml, secret-scan.yml, stale.yml) -- candidates for a reusable workflow template.
6. **17 repos have no secrets and no build commands** -- pure content/docs repos that need only checkout + basic validation.
7. **No intake repos** use `cargo` or `go build` -- the build surface is strictly Python (pytest+ruff) and Node.js (npm/pnpm).
