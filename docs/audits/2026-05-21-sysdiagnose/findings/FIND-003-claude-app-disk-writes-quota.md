# FIND-003: Claude.app sustained 24-hour write quota breaches (×2 in 24h)

**Severity:** warn
**Source:** `crashes_and_spins/Claude_2026-05-21-115412_*.diag` + `crashes_and_spins/Claude_2026-05-21-164607_*.diag`
**First seen:** 2026-05-20 12:58:43 (start of 23-hour offending window)
**Last seen:** 2026-05-21 16:46:06
**Occurrences:** 2 in capture day; rolling DiagnosticReports archive shows a sustained pattern (see FIND-005 for the "disk writes" archive across May 16/18/19/20/21)
**Affected process/component:** `/Applications/Claude.app/Contents/MacOS/Claude` — `com.anthropic.claudefordesktop`
**Affected ORGANVM organ:** infrastructure (Claude.app is a dev tool, not an organ)

## Evidence
Diag #1 (1.8089.1 build, the older version that ran for 23 hours):
```
Event:           disk writes
Writes:          8589.95 MB of file backed memory dirtied over 82528 seconds
                 (104.09 KB per second average), exceeding limit of 99.42 KB
                 per second over 86400 seconds
Writes limit:    8589.93 MB  (this is the *tier-2* limit — Apple grants more
                              headroom only to persistent offenders)
Action taken:    none
Heaviest stack:  v8::ArrayBuffer::GetBackingStore() (Electron Framework)
```

Diag #2 (1.8555.0 build, post-upgrade, 2.3 hours):
```
Writes:          2147.49 MB over 8202 seconds (261.82 KB/s average,
                 exceeding limit of 24.86 KB/s)
Writes limit:    2147.48 MB  (tier-1 — fresh-PID limit)
Action taken:    none
Heaviest stack:  v8::ArrayBuffer::GetBackingStore() (Electron Framework)
```

Same V8 stack frame in both: `ArrayBuffer::GetBackingStore` → file-backed memory dirty. This is the same allocation pattern, both before and after the version upgrade.

## Interpretation
"Action taken: none" means macOS only logged this — it didn't throttle Claude.app. But the limit-tier escalation (Claude on PID 3599 hit tier-2 = 8.5 GB/24h, meaning macOS had already noticed it as a chronic offender) tells us this is *recurring*. Claude.app is producing ~100–260 KB/s of dirty file-backed pages over multi-hour windows — likely IndexedDB / SQLite / log writes from the Electron renderer. This directly contributes to the chronic memory-pressure pattern documented in FIND-007 (35M swapins, 42M swapouts over 78h uptime).

This is **expected behavior** for a long-running Electron app on a 16 GB machine, but it is **load-bearing context** for the swap-thrashing pattern. Not a bug; a known-cost we should track.

## Proposed action
- [x] No-op (informational only — Anthropic-side investigation, not user-actionable)
- [x] Draft IRF row (see below) — tracking for IRF awareness, not for fixing
- [ ] Dispatch envelope
- [ ] Immediate fix needed

## Candidate IRF row
**Domain:** MON
**Priority:** P3
**Title:** Track Claude.app disk-writes quota breaches against memory-pressure pattern
**Body:** Two `.diag` files in 24h confirm Claude.app is producing 100–260 KB/s of dirty file-backed pages from V8 ArrayBuffer backing stores — likely IndexedDB and renderer log writes. Limit-tier escalation indicates a recurring pattern. Not a bug per se, but a load-bearing input to chronic memory pressure on this 16GB host. Track in MON; correlate with reported user pain.

## Dispatch decision
**Work type:** N/A (no remediable code here from user's side)
**Recommended agent:** N/A
**Reasoning:** Informational. Anthropic is the only party who could change Claude.app's write pattern.
