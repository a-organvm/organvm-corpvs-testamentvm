# FIND-005: Chronic memory pressure — three jetsam events in 36h, sustained swap thrash

**Severity:** error
**Source:** Multiple converging signals (see Evidence)
**First seen:** 2026-05-19 22:24:53 (MTLCompiler XPC service jetsammed per unified log)
**Last seen:** 2026-05-22 03:29 (live `vm_stat`: 4194 free pages = 67 MB in this very audit session)
**Occurrences:** 3+ jetsam events; ~35M swapins/42M swapouts over 78h uptime at capture
**Affected process/component:** System-wide; jetsam victims included bztransmit, DuckDuckGo, MTLCompiler XPC
**Affected ORGANVM organ:** infrastructure (host-level resource constraint affecting all organs)

## Evidence

**Jetsam events** (`/Library/Logs/DiagnosticReports/`):
1. `JetsamEvent-2026-05-19-230502.ips` — `"largestProcess": "bztransmit"` (Backblaze backup)
2. `JetsamEvent-2026-05-20-014934.ips` — `"largestProcess": "DuckDuckGo"`
3. Unified log 2026-05-21 22:24:53 — QuickLookUIService MTLCompiler XPC connection failed: *"compiler service may have crashed, been jetsammed, or OS shutting down"*

**Capture-time `top.txt`**:
```
PhysMem: 15G used (3176M wired, 3573M compressor), 445M unused
VM: 35,038,595 swapins, 42,295,336 swapouts
```

**Capture-time `spindump.txt`**:
```
Time Since Boot: 284,093s (~78 hours)
```

That works out to **~990 swap I/Os per second average** over the 78h uptime — sustained, not a spike.

**Live state during this audit** (post-reboot, ~2.5h uptime):
```
vm_stat: Pages free: 4194  (= 67 MB free of 16 GB)
Load avg: 2.24 2.86 3.38
```

**Contributing process inventory** (5 AI desktop apps on a 16 GB host):
- `/Applications/Claude.app` (Anthropic Claude Desktop, v1.8555.0)
- `/Applications/ChatGPT.app` (OpenAI, installed 2026-05-18)
- `/Applications/ChatGPT Atlas.app` (OpenAI browser, installed 2026-05-07)
- `/Applications/Codex.app` (OpenAI Codex Mac, running with helpers)
- `/Applications/Antigravity.app` (Google, v2.0.1, used 2026-05-21)

Plus Claude Code CLI (multiple concurrent sessions with spares + chrome session), Codex CLI helpers (`SkyComputerUseClient` ×3 alive), VS Code, kitty terminal, etc.

## Interpretation

This is the **load-bearing finding** for the audit. Everything else — Claude.app disk-write quota alerts (FIND-003), ollama LaunchAgent throttle (FIND-002), the spotlightknowledged CPU-resource diagnostics, the Code Helper / node / git disk-writes alerts — is downstream of one root condition: **a 16 GB machine running too many memory-hungry AI/dev surfaces simultaneously**.

The user's CLAUDE.md explicitly names "Memory-constrained (16GB RAM); avoid spawning too many parallel processes" as a System Constraint. The evidence shows this constraint is being violated in practice — sustained, not occasional. Three jetsam events in 36 hours is the kernel's last-resort defense; the system has been over capacity continuously, not bursting.

Rule #54 ("fix bases, not symptoms") points at the right level: don't add more disk-write quotas or per-app fixes. Reduce the resident set. Concrete levers, ranked by reversibility:

1. **Reversible (test first)**: Quit ChatGPT.app + ChatGPT Atlas.app + Antigravity.app when not in active use. These are user-facing apps with no MCP integration into the workflow — they don't add capability the Claude/Codex CLI flows don't already provide.
2. **Reversible**: Quit Claude.app desktop when working only through Claude Code CLI. Resident set of Claude.app is multi-hundred-MB Electron.
3. **Targeted**: Disable the Jupyter LaunchAgent (FIND-001) and the Ollama LaunchAgent (FIND-002). Recover ~2.8 GB of zombie ipykernel children plus the throttle-loop overhead.
4. **Strategic**: Treat the 16 GB ceiling as a forcing function for "one AI surface at a time." This is a values-laden choice (the user may want all five) but it's the underlying issue.

## Proposed action
- [ ] No-op
- [x] Draft IRF row (see below)
- [x] Dispatch envelope (research dispatch — Perplexity for "macOS jetsam tuning under chronic pressure" patterns)
- [x] **Immediate fix needed** — at minimum, run `osascript -e 'tell application "Antigravity" to quit'` style cleanup of unused AI apps when starting heavy work. Audit cannot execute this; it's a behavioral change.

## Candidate IRF row
**Domain:** SYS
**Priority:** P0
**Title:** 16 GB host runs 5+ AI desktop apps simultaneously — chronic jetsam-triggering pressure
**Body:** Three jetsam kills in 36 hours (bztransmit, DuckDuckGo, MTLCompiler XPC) plus 990 swap I/O/sec averaged over 78h uptime indicates sustained over-capacity. CLAUDE.md names this as a System Constraint; reality shows the constraint is regularly violated. Address by app-quit discipline (ChatGPT/ChatGPT-Atlas/Antigravity when idle), disabling Jupyter+Ollama LaunchAgents (see FIND-001/002), and treating "one AI surface at a time" as policy. Pairs with [[2026-05-22-sysdiagnose-forensic-audit]] artifact.

## Dispatch decision
**Work type:** debugging + research
**Recommended agent:** Claude (strategic — values-laden surface-reduction decisions) + Perplexity (research on jetsam tuning)
**Reasoning:** The remediation is partially behavioral (which apps to quit) and partially research (whether macOS 26.5 jetsam tuning has knobs the user can adjust). Dispatch envelope DISPATCH-005 below for the Perplexity research portion.
