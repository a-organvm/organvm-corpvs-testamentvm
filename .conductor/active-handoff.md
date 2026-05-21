# Agent Handoff: Knowledge Base Export + Epistemic Engine Architecture

**From:** Session S-2026-05-17-knowledge-base-epistemic-export | **Date:** 2026-05-17 | **Phase:** Complete (closeout executed)

## Current State

### Artifacts on Disk
| Artifact | Location | Size | Status |
|----------|----------|------|--------|
| Session archive | `~/session-archive-2026-05-17.tar.gz` | 786MB | Local only (too large for git) |
| Session manifest | `~/session-archive-MANIFEST.md` | — | Documents archive contents |
| Knowledge base export | `~/knowledge-base-export-2026-05-17.tar.gz` | 37MB | Local only (too large for git) |
| KB manifest | `~/knowledge-base-export-2026-05-17/MANIFEST.md` | — | Documents KB contents |
| Epistemic Engine arch | `~/knowledge-base-export-2026-05-17/conversation-context-llm-knowledge-bases.md` | — | Inside KB archive |
| Closeout summary | `data/closeout-S-2026-05-17-knowledge-base-epistemic-export.md` | 6.3K | Git-tracked, pushed |

### Git State (corpvs-testamentvm)
- Branch: `main`, clean, in sync with `origin/main`
- Latest commit: `3c73cd3` (chore autogen refresh)
- 5 commits pushed this session

### Cloned Repos (shallow, depth=1)
- `a-organvm/my-knowledge-base` → `/Users/4jp/Workspace/a-organvm/my-knowledge-base`
- `organvm-i-theoria/linguistic-atomization-framework` → `/Users/4jp/Code/organvm-i-theoria/`
- `organvm-i-theoria/nexus--babel-alexandria` → `/Users/4jp/Code/organvm-i-theoria/`

## Completed Work

- [x] Exported session archive (811 plans, 906 project memories, 21,908 files total)
- [x] Exported knowledge base (1,463 .md files across 7 repos)
- [x] Designed Epistemic Engine 5-node architecture (Intake → Compiler → Workbench → Oracle/Factory → Maintainer)
- [x] Designed plugin ecosystem (3-layer: 4 meta-plugins + ~160 existing skills + gap-fillers)
- [x] Defined gain staging rules for plugin chain
- [x] Updated IRF with 5 items (2 completions, 3 new)
- [x] Created 3 GitHub issues (#353, #354, #355)
- [x] Claimed DONE-533, DONE-534
- [x] Executed hall-monitor closeout (all violations found and fixed)
- [x] Committed and pushed all work

## Key Decisions

| Decision | Rationale |
|----------|-----------|
| 3-layer plugin architecture (meta-plugins + existing skills + gap-fillers) | ~160 skills already exist; build only the 4 orchestrators that don't exist yet |
| DIWS as Phase 0 substrate | Domain scaffolding must precede any session context or PDE work |
| Compressed tar.gz for exports | Disk at 52% (11GB free); exports too large for git, must be portable |
| Epistemic Engine = product, not scripts | User explicitly requested "incredible new product instead of a hacky collection of scripts" |
| Gain staging rules for plugin chain | Prevent context clipping and maintain truth fidelity across the chain |
| IRF canonical path = Code/organvm | `meta-organvm` path identified as vacuum (IRF-SYS-185 filed) |

## Critical Context

### Epistemic Engine Architecture (5 Nodes)
1. **Intake Node** — Web Clipper (browser extension normalizes web to Markdown) + Ingest Watcher (local daemon monitors raw/ directory)
2. **Compiler** — Incremental Indexing (LLM reads raw doc → summary → index card) + Ontology Mapping + Semantic Linking (autonomous backlinks)
3. **Workbench** — Obsidian as human-readable glass + Agentic CLI (commission research, not just search)
4. **Oracle & Factory** — Multi-Modal Output (Markdown essay, matplotlib chart, Marp slideshow) + Recursive Feedback Loop
5. **Maintainer** — Health Checks (contradictions, dead links, thin concepts) + Gap Imputation (web search to fill gaps)

### Plugin Ecosystem (4 Priority Meta-Plugins)
1. **session-orchestrator** — Master sequencer for Phase 0→3 chain
2. **vacuum-radar** — Real-time N/A detection during session
3. **triple-reference-tracker** — Enforce IRF+repo+GH issue during work
4. **atom-logger** — Log work units to prompt registry

### User Workflow (the product to build)
Raw data ingest → LLM-compiled wiki → Obsidian IDE → Q&A/output → recursive filing → autonomous linting. User rarely writes/edits manually; the LLM is the domain maintainer.

### Constraints
- macOS 26 ARM64, 16GB RAM — avoid parallel process spawning
- No LaunchAgents (HARD RULE) — on-demand CLI only
- Docker Desktop quit — native binary or Docker Compose only
- chezmoi governs dotfiles — fix bases, not outputs
- local:remote = 1:1 — nothing local only

## Next Actions

### P1 — Immediate (zero dependencies)
1. **IRF-THE-033:** Formalize Epistemic Engine product spec
   - Define MVP scope (which of 5 nodes first?)
   - Identify existing tools that map to each component
   - Write spec in `organvm-corpvs-testamentvm` or new repo

2. **IRF-SYS-184:** Implement 4 priority meta-plugins
   - Start with `session-orchestrator` (master sequencer)
   - Then `vacuum-radar` (real-time N/A detection)
   - Then `triple-reference-tracker` (enforce triple reference)
   - Then `atom-logger` (log to prompt registry)
   - Each should be an opencode skill or Claude Code skill

### P2 — Deferred (not blocked)
3. **IRF-SYS-185:** Fix IRF missing from meta-organvm
   - Decision needed: symlink vs copy vs document canonical location
   - Low effort, low urgency

### Ongoing — From Existing Active Handoff
4. **my-knowledge-base active-handoff.md** — Gemini theory work (T1–T10) still pending
   - T1: SOP Master Index
   - T2: UMFAS Monad Merge Decision
   - T3: Phase 5 Apple Notes Adapter
   - T4: Knowledge Graph Confidence Propagation
   - T5: Embedding Model Benchmark Expansion
   - T6: Theory-to-Concrete Handoff Governance
   - T7: Prompt Atomization Second-Pass Triage
   - T8–T10: Optional theory-substrate specs

## Risks & Warnings

- **Disk space:** 52% used (11GB free). Full 31GB report export blocked until external drive/cloud.
- **IRF vacuum:** IRF exists at `Code/organvm/organvm-corpvs-testamentvm/` but NOT at `meta-organvm/organvm-corpvs-testamentvm/`. Sessions operating from meta-organvm cannot access IRF.
- **Plugin design ≠ implementation:** The 4 meta-plugins are designed but not built. Next agent must not re-design; they must implement.
- **Epistemic Engine scope risk:** 5-node architecture is ambitious. MVP should be 1-2 nodes max.
- **16GB RAM constraint:** Max 4-6 concurrent agents. Do not spawn many parallel processes.
- **Shallow clones:** 3 repos cloned with depth=1. Full history not available locally.

## Conflict Zones

| Path | Rule |
|------|------|
| `INST-INDEX-RERUM-FACIENDARUM.md` | Read before write; never overwrite wholesale; append-only for new items |
| `data/done-id-counter.json` | Claim next ID atomically; increment after claim |
| `data/prompt-registry/prompt-atoms.json` | Targeted edits only; never replace wholesale |
| `.conductor/active-handoff.md` | Update, don't replace; preserve existing scope sections |

## Recovery Protocol

If next session finds state mismatch:
1. Check `git log` in corpvs-testamentvm for commits since `3c73cd3`
2. Verify archives still exist at `~/session-archive-2026-05-17.tar.gz` and `~/knowledge-base-export-2026-05-17.tar.gz`
3. Check GitHub issues #353, #354, #355 for any updates
4. Re-read IRF to confirm DONE-533, DONE-534 are logged

*— end envelope —*
---

## Addendum: 2026-05-21 — Four-Runtime Protocol Alignment (Claude session)

**Scope:** Orthogonal to the 2026-05-17 KB-export work above. Triggered by Codex SessionStart printout showing `NEON_API_KEY for MCP server 'Neon' is empty` and the user's reframe: "design ideal interactive ecosystem; not Claude only."

**Plans authored this session (both IN-PROGRESS, no DONE-NNN):**

| Plan | Path | Status |
|---|---|---|
| Four-runtime interactive ecosystem alignment | ~/.claude/plans/2026-05-21-four-runtime-interactive-ecosystem-alignment.md | IN-PROGRESS |
| Agent integration protocols past/present/potential | ~/.claude/plans/2026-05-21-agent-integration-protocols-past-present-potential.md | IN-PROGRESS |

**Key finding (the structural reframe):** Original three-layer plan (Secrets · MCP · Hooks) is incomplete. Honest decomposition is five layers: L1 Secrets, L2 Agent↔tool (MCP), L3 Hooks, L4 Editor↔agent (ACP — new), L5 Agent↔agent (A2A — new). Four runtimes participate in different subsets depending on driver/driven role.

**Files NOT modified:** INST-INDEX-RERUM-FACIENDARUM.md, prompt-atoms.json, registry-v2.json, this repo's working tree.

**Recovery for next session resuming this scope:**
1. Read four-runtime-interactive-ecosystem-alignment.md (the design).
2. Then agent-integration-protocols-past-present-potential.md (the research that reframed it).
3. User has NOT approved Phase 1 BUILD; do not implement until edge-priority decision is made.

*— end 2026-05-21 addendum —*

## Resolution received 2026-05-21 (supersedes prior "Phase 1 NOT approved" line above)

**Edge-priority answer (user, 2026-05-21):** All five layers — L1 Secrets · L2 MCP · L3 Hooks · L4 ACP · L5 A2A — are in scope, phased over multiple quarters. The three-of-four collapse from the closeout applies: Phase 0a (NEON_API_KEY injection trace), Phase 0e (per-runtime ACP audit), Phase 0f (conductor↔A2A reconciliation) are all UNFROZEN.

**Neon-fate answer (user, 2026-05-21, verbatim):** "notate, research all lanes, arrive at elevated plain" — do NOT collapse to vestigial (delete) or wanted (1Password wire) yet. Instead: document each runtime's current secret-handling, research per-lane mechanisms (Codex `bearer_token_env_var`, Claude's untraced injection, Gemini's settings.json, OpenCode's per-server env block), then synthesize at higher altitude. Phase 1a is gated on this research, not on a binary fix.

**What unfreezes for next session:** Phase 0 investigation (read-only; trace + audit + reconcile) plus the multi-lane Neon-handling notation. Phase 1 BUILD remains gated on the synthesis output, not on a fresh user decision.

*— end resolution block —*
