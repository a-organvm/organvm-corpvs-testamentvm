# FIND-004: Antigravity (Google) 2 GB disk-write spike in 9 seconds — distinct from Claude pattern

**Severity:** warn
**Source:** `crashes_and_spins/Antigravity_2026-05-21-181739_*.diag`
**First seen:** 2026-05-21 18:17:28
**Last seen:** 2026-05-21 18:17:37
**Occurrences:** 1
**Affected process/component:** `/Applications/Antigravity.app/Contents/MacOS/Antigravity` — `com.google.antigravity` v2.0.1
**Affected ORGANVM organ:** N/A (third-party AI agent)

## Evidence
```
Event:        disk writes
Writes:       2147.48 MB of file backed memory dirtied over 9 seconds
              (239.66 MB per second average), exceeding limit of 24.86 KB/s
Limit:        2147.48 MB (tier-1)
Duration:     9 seconds
Action:       none
```

## Interpretation
This is **structurally different** from FIND-003. Claude.app accumulates ~100 KB/s over 23 hours (slow, sustained). Antigravity wrote 2 GB in **9 seconds** at 240 MB/s — that's a single short burst, almost certainly an initial workspace index or model-cache write on first invocation. The Phase 1 ecosystem inventory did not include Antigravity; it appears to have been installed/launched recently (no prior Antigravity diag in the rolling DiagnosticReports archive). This is benign on its own — fresh installs often write large caches — but it's a datum: Antigravity is on this machine and was used on 2026-05-21 at 18:17.

Note: presence is not a problem, but **two AI agents at once on a 16 GB host** (Claude.app + Antigravity, plus Claude Code CLI, plus Codex.app, plus the OpenCode/Gemini binaries on PATH) is a relevant input to FIND-007 memory pressure.

## Proposed action
- [x] No-op (informational)
- [ ] Draft IRF row
- [ ] Dispatch envelope
- [ ] Immediate fix needed

## Candidate IRF row
N/A (no action; included as a Phase 1 ecosystem-inventory delta).

## Dispatch decision
**Work type:** N/A
**Recommended agent:** N/A
**Reasoning:** Pure observational. The signal is "Antigravity exists" — already captured as an ecosystem-inventory delta in REPORT.md.
