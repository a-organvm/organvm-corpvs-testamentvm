# DISPATCH-006: Render shutdown_stall binaries to text

**Target agent:** Codex (single-shell-command mechanical task)
**Source repo:** N/A

**Work scope:**
The shutdown_stall reports filed on 2026-05-18 and 2026-05-22 are in macOS's binary spindump format. Render them to text:

```bash
mkdir -p ~/Workspace/_diagnostics/sysdiagnose-2026-05-21/findings/rendered/
spindump -i /Library/Logs/DiagnosticReports/shutdown_stall_2026-05-18-151846_*.shutdownStall \
  > ~/Workspace/_diagnostics/sysdiagnose-2026-05-21/findings/rendered/shutdown_stall_2026-05-18.txt
spindump -i /Library/Logs/DiagnosticReports/shutdown_stall_2026-05-22-005959_*.shutdownStall \
  > ~/Workspace/_diagnostics/sysdiagnose-2026-05-21/findings/rendered/shutdown_stall_2026-05-22.txt
```

Then identify, by reading both text outputs:
- Which processes were holding launchd hostage at SIGTERM time
- Whether the same process(es) appear in both reports
- Whether any of them are user-installed (vs Apple system processes)

Produce a 1-page summary at `findings/rendered/shutdown_stall_summary.md` with the process names and a hypothesis on why they didn't exit cleanly.

**Acceptance criteria:**
- Two .txt files in `findings/rendered/` (one per shutdown_stall)
- One summary .md with named processes and overlap analysis
- No additional files written (e.g., don't try to fix anything found)

**Out of scope:**
- Modifying any process or LaunchAgent based on findings
- Cross-referencing against findings/FIND-* (that's Claude's synthesis job)

**Verification on return:**
Claude reads `shutdown_stall_summary.md` and updates FIND-006 with the named processes, then re-files if any new IRF rows are warranted.
