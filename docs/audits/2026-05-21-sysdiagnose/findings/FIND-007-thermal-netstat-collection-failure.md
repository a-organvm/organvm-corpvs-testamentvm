# FIND-007: Sysdiagnose collection partial failure — thermal.txt empty, netstat.txt absent

**Severity:** info
**Source:** `extract/thermal.txt` (0 bytes) + missing `extract/netstat.txt`
**First seen:** 2026-05-21 23:45 (sysdiagnose capture itself)
**Last seen:** same
**Occurrences:** 1 (this capture)
**Affected process/component:** sysdiagnose collection tool
**Affected ORGANVM organ:** N/A

## Evidence
```
$ cat extract/thermal.txt   # 0 bytes

$ ls extract/netstat.txt
ls: ... netstat.txt: No such file or directory

$ cat extract/errors/utilities-logGen_task_failures.txt
/usr/bin/thermal config exited with status 1 in 0.1 seconds.

$ cat extract/errors/securebootVariables_task_failures.txt
... nvram ApChipID exited with status 1 ...
... nvram ApBoardID exited with status 1 ...
(× 8 secure-boot variable lookups failed)
```

The netstat substitute is `network-info/get-network-info.txt` which is a *manifest of commands invoked*, not the output. Many of the listed commands also failed (e.g., `/usr/local/bin/nsputil doesn't exist`, several `pmap` operations not permitted on system disks).

## Interpretation
This is **about the sysdiagnose tool itself**, not the system. macOS 26.5 Tahoe Beta's sysdiagnose tool has a partial-collection contract failure: `thermal config` returns 1, `nvram` returns 1 for 8 secure-boot variables, and the netstat raw output isn't present where users expect it. The data is *available* (live `netstat -an` works fine, live `thermal` works fine — these were per-execution failures), it just wasn't captured into the bundle.

This affects audit fidelity: any future forensic audit using this sysdiagnose cannot answer "what was the listening-socket state at capture time?" except by inference from the unified log archive. Worth filing upstream with Apple as a Tahoe Beta bug, and worth noting on this audit's findings as a limitation.

## Proposed action
- [x] No-op (documented limitation; no fix from user side except waiting for Tahoe non-beta)
- [x] Draft IRF row (see below) — tracks the limitation so future audits know to compensate
- [ ] Dispatch envelope
- [ ] Immediate fix needed

## Candidate IRF row
**Domain:** MON
**Priority:** P3
**Title:** Tahoe Beta sysdiagnose tool drops thermal.txt + netstat.txt collection
**Body:** macOS 26.5 (25F71) sysdiagnose produces empty thermal.txt and no netstat.txt (per errors/utilities-logGen_task_failures.txt — `thermal config` exited with status 1). secureBootVariables also produces 8 nvram-lookup failures. Affects forensic audits of this host until non-beta Tahoe ships. Workaround: for future audits, complement sysdiagnose with `netstat -an > capture-netstat.txt; thermal > capture-thermal.txt` shell snapshot at the same moment.

## Dispatch decision
**Work type:** N/A
**Recommended agent:** N/A
**Reasoning:** Tracked for audit-fidelity awareness; no remediation.
