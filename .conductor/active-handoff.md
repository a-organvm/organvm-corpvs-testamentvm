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
