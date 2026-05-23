# FIND-006: Recurring shutdown stalls — two stalls in four days

**Severity:** warn
**Source:** `/Library/Logs/DiagnosticReports/shutdown_stall_*`
**First seen:** 2026-05-18 15:18:46 (1.5 MB shutdownStall report)
**Last seen:** 2026-05-22 00:59:59 (4.2 MB shutdownStall report — **today**, 75 min after the sysdiagnose capture)
**Occurrences:** 2 in 4 days
**Affected process/component:** system-wide (shutdown stalls are kernel/launchd-level)
**Affected ORGANVM organ:** N/A (host-level)

## Evidence
```
-rw-rw---- 1 root _analyticsusers 1487210 May 18 15:18 shutdown_stall_2026-05-18-151846_*.shutdownStall
-rw-rw---- 1 root _analyticsusers 4224736 May 22 00:59 shutdown_stall_2026-05-22-005959_*.shutdownStall
```

Both files are in macOS's binary spindump format (`Use spindump -i to generate textual report`). Rendering requires the macOS spindump tool against the source binary, which is outside this audit's read-only scope.

The 2026-05-22 stall is notable because (a) it's 4.2 MB — nearly triple the 2026-05-18 stall, suggesting more processes-stuck-on-exit, and (b) it happened 75 minutes after the sysdiagnose capture, meaning the user rebooted the machine sometime between capture and the audit's current execution (`uptime` reports ~2.5h up).

## Interpretation
Shutdown stalls are caused by one or more processes failing to exit cleanly when launchd issues SIGTERM during shutdown. Two stalls in four days is not yet a "crisis" but is a regression worth tracking — single stalls happen, recurrent stalls indicate one or more durably-misbehaving processes. The user did not file these in memory; they may not be aware. Most likely culprits given the rest of the audit:

- Ollama's `KeepAlive=true` LaunchAgent (FIND-002) — restart-loops can extend shutdown.
- Long-running Electron apps with file-backed write loops (Claude.app, FIND-003; Code Helper, Codex).
- The Jupyter LaunchAgent (FIND-001) and its accumulated ipykernel children — ipykernels can hold file descriptors past SIGTERM.

These are all hypotheses; the binary `.shutdownStall` files would name the actual offending processes. Audit cannot render them.

## Proposed action
- [ ] No-op
- [x] Draft IRF row (see below)
- [x] Dispatch envelope (Codex — mechanical: render the shutdown_stall binaries with `spindump -i`, return text report)
- [ ] Immediate fix needed

## Candidate IRF row
**Domain:** SYS
**Priority:** P2
**Title:** Render and triage two recurring shutdown_stall reports (2026-05-18, 2026-05-22)
**Body:** Two macOS shutdown_stall binary reports filed in the last 4 days, file sizes 1.5 MB and 4.2 MB. The 2026-05-22 stall happened 75 min after sysdiagnose capture. Rendering with `spindump -i` will name the processes that failed to terminate cleanly. Likely candidates per audit: ollama LaunchAgent (FIND-002), Electron file-backed write loops (FIND-003), accumulated ipykernels (FIND-001). One-shot Codex dispatch.

## Dispatch decision
**Work type:** mechanical (rendering binary diag to text + symptom enumeration)
**Recommended agent:** Codex
**Reasoning:** This is pure tool invocation (spindump CLI) and pattern-matching against the audit's existing finding inventory. No architecture decisions needed. Dispatch envelope DISPATCH-006 below.
