# DISPATCH-001: Replace Jupyter KeepAlive LaunchAgent with on-demand model

**Target agent:** Codex (mechanical — once Claude designs the replacement)
**Source repo:** `~/Workspace/4444J99/domus-semper-palingenesis` (chezmoi source — for the plist removal) + `~/Code/organvm/<repo-for-jupyter-mcp>` (for the on-demand wrapper)

**Work scope:**
Replace the current `~/Library/LaunchAgents/com.jupyter.server.plist` with an on-demand invocation model. Specifically:

1. Disable and remove the current LaunchAgent:
   ```bash
   launchctl unload ~/Library/LaunchAgents/com.jupyter.server.plist
   mv ~/Library/LaunchAgents/com.jupyter.server.plist \
      ~/Library/LaunchAgents/.disabled-com.jupyter.server.plist.bak
   ```

2. Create a CLI invocation (e.g., `~/.local/bin/jupyter-start` or `organvm jupyter start` subcommand) that:
   - Generates a fresh token: `JUPYTER_TOKEN=$(openssl rand -hex 32)`
   - Binds explicitly to `127.0.0.1` only
   - Re-enables XSRF check
   - Sets `--ServerApp.allow_origin=http://localhost:*` (narrowed CORS instead of wildcard)
   - Logs token to a file readable only by the user (chmod 600)
   - Provides a `jupyter-stop` command

3. Update the MCP server config in `~/.claude.json` to read the token at startup.

4. Cleanup: kill the ~50 accumulated ipykernel_launcher processes left behind by the old LaunchAgent (`pkill -f ipykernel_launcher`).

**Acceptance criteria:**
- `~/Library/LaunchAgents/com.jupyter.server.plist` not present
- `launchctl list | grep jupyter` returns nothing
- `netstat -an | grep 8888` returns no LISTEN line after `jupyter-stop`
- Jupyter MCP server still works when invoked via the new on-demand wrapper
- `~/.claude.json` reads the per-session token successfully

**Out of scope:**
- Removing the jupyter MCP server entirely (user may still want it).
- Changing how `vox--architectura-gubernatio` or other MCP servers interact with jupyter (those continue to work over the existing protocol, just gated by token now).

**Verification on return:**
Claude runs:
1. `git diff` against chezmoi source to see plist removal and the new wrapper script.
2. `launchctl list | grep jupyter` to confirm zero entries.
3. `netstat -an | grep 8888` to confirm no orphan listener.
4. `~/.local/bin/jupyter-start && curl http://127.0.0.1:8888/api/kernels` should fail without token and succeed with `-H "Authorization: token $JUPYTER_TOKEN"`.
5. `conductor_fleet_cross_verify` per Dispatch Protocol.
