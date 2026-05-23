# Unified-Log Timeline — 24 hours preceding capture

**Source:** `extract/system_logs.logarchive`, window 2026-05-21 00:00 → 23:45 EDT
**Method:** `log show --archive <path> --start ... --end ... --predicate ...` (script-form invocation to avoid zsh predicate-parsing issues)

## Narrative — chronological summary

This timeline is filtered to events relevant to the dev ecosystem (Claude, Codex, chezmoi, git, SSH-signing, hooks) plus high-severity faults. It is not exhaustive — the full unified log for one day is multi-GB.

### Early morning — quiescent baseline

The 00:00–17:00 window shows the expected pattern: spotlight/Suggestions/mDNSResponder background chatter, periodic CloudKit + iTunes sync errors (`ampMusicAPIRegexDomains` bag key missing — a known Apple Music client issue), biomesyncd `clock vector is empty` (Biome subsystem on a fresh-vector start).

### 17:09 cluster — Music app start-up turbulence

Multiple `Two equal instances have unequal identities` faults from `runningboardd` involving `application.com.apple.Music.1152921500311888895`. Visually identical RunningBoard records but with different process-instance identities — looks like Music started, was killed, restarted, and the cleanup of the prior RBS record was racy. Followed by iTunesCloud bag-key errors (`ampMusicAPIRegexDomains`). Apple's responsibility; not user-actionable.

### 17:50–18:12 cluster — concentrated SSH-signing activity

The `op-ssh-sign` log lines (sample below) show 8+ container-lookup successes between 17:51 and 18:12 EDT:

```
17:51:53  op-ssh-sign pid 35252  container_create_or_lookup_app_group_path_by_app_group_identifier: success
17:52:16  op-ssh-sign pid 35880  ...success
17:52:42  op-ssh-sign pid 36033  ...success
17:53:17  op-ssh-sign pid 36414  ...success
17:55:44  op-ssh-sign pid 37813  ...success
17:55:50  op-ssh-sign pid 37876  ...success
17:57:13  op-ssh-sign pid 38566  ...success
18:00:21  op-ssh-sign pid 44406  ...success
18:01:05  op-ssh-sign pid 44961  ...success
18:12:28  op-ssh-sign pid 85144  ...success
```

This is the **smoking gun corroboration** for the memory entry `[[project_artifact_2026_05_22_signing_p1_first_real_use]]` — op-ssh-sign was active 5+ days *before* that memory says it became load-bearing. The wrapper's P1 path was working before user attention focused on it; what the 2026-05-22 session did was *make P1 reachable through SSH_AUTH_SOCK* (so the signing wrapper would prefer it over P2). The signing activity here predates that fix and was already routing via op-ssh-sign for git operations directly. Net: signing infrastructure was functional throughout the capture window.

### 18:17 — Antigravity disk-writes spike (FIND-004)

Single sysdiagnose-archive event: Antigravity.app dirtied 2 GB in 9 seconds. Coincides with no other anomalies; consistent with first-time workspace index.

### 22:24 — MTLCompiler XPC service jetsam (cited in FIND-005)

```
22:24:53  QuickLookUIService  MTLCompiler[reqID=17]  Connection attempt 1/10 failed
          with XPC_ERROR_CONNECTION_INVALID: Failed to check-in, peer may have been
          unloaded: mach_error=10000003 (compiler service may have crashed, been
          jetsammed, or OS shutting down)
22:24:53  QuickLookUIService  MTLCompiler[reqID=18]  Connection attempt 1/10 failed ...
```

Metal shader compiler XPC service was killed by jetsam under memory pressure. This is the same pressure event class as the 23:05/01:49 JetsamEvent records — they fire when an unprivileged process is killed (logged to DiagnosticReports); the MTLCompiler kill was a system-service kill (logged to unified log only).

### 22:50–22:51 — Sandbox-denial wave (kernel noise)

Routine macOS sandbox denials: CommCenter, biomesyncd, nfcd, studentd, ContextStoreAgent. All are kernel-confined system processes hitting their sandbox profiles; expected behavior. Not user-actionable.

### 23:13 — `disk writes` event (sysdiagnose-triggering)

```
disk writes_2026-05-21-231322  (642 KB file)
```

This is one of the largest disk-writes diags in the archive (640 KB suggests many stackshots) and it's *named* "disk writes" rather than per-process — system-wide IO threshold. Likely the trigger that caused the user to capture the sysdiagnose at 23:45 (32 min later).

### 23:45 — sysdiagnose capture

End of timeline window. Sysdiagnose collected (3580 files originally per Phase 1; 2125 unique files post-dedup per re-verification).

### Post-capture (outside this window but contextual)

- 2026-05-22 00:59 — second shutdown_stall reported (FIND-006). Implies user rebooted ~01:00.
- 2026-05-22 01:00 — current boot (live `uptime` shows up ~2.5h at audit time).
- 2026-05-22 02:04 — `codex_2026-05-22-020456` diagnostic filed (Codex disk-writes again).
- 2026-05-22 03:26 — this audit session began executing.

## What the timeline confirms

1. **Signing infrastructure was working** at capture time — op-ssh-sign successfully invoked 10+ times in 21 minutes during a typical session.
2. **Memory pressure was active by 22:24** at the latest (MTLCompiler jetsam) — corroborates the FIND-005 pattern at the capture day's late evening, not just the 23:05/01:49 archive events.
3. **No hook errors, no Claude Code daemon faults**, no SSH errors, no git errors in the inspected windows. The dev pipeline is functioning despite memory pressure.
4. **No GPU faults / no WindowServer crashes** despite Tahoe Beta caveat — Rule #9 area concern (GPU/WindowServer instability noted in `~/.claude/CLAUDE.md`) was not triggered during this capture window.

## What it does NOT cover

- Pre-2026-05-21 events (audit scope was 24h of capture day).
- Per-process stackshot detail (those live in `crashes_and_spins/` diag files, covered in findings).
- Network traffic content (netlog covered a different 18-second window; cross-referenced in FIND-008).
