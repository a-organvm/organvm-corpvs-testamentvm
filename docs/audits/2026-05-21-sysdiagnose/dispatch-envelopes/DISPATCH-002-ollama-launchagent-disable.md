# DISPATCH-002: Disable ollama brew-service

**Target agent:** Codex (single-command mechanical action)
**Source repo:** N/A (this is a brew-services state change, not a repo edit)

**Work scope:**
Disable the ollama brew-service that is currently in throttle-loop. Verify the change persists across reboot.

```bash
brew services stop ollama
brew services list | grep ollama  # confirm 'stopped' or absent
launchctl list | grep homebrew.mxcl.ollama  # confirm absent
```

Optionally (user authorization required separately): `brew uninstall ollama` if the user confirms they don't use it via the local-llm-fine-tuning skill.

**Acceptance criteria:**
- `brew services list` does not show ollama as `started` or `error`
- `~/Library/LaunchAgents/homebrew.mxcl.ollama.plist` either absent or marked disabled
- No `homebrew.mxcl.ollama` entries in `launchctl list`
- (Run after this) `spindump 1` does not show ollama in Launchd-throttled processes section

**Out of scope:**
- Uninstalling ollama unless user explicitly authorizes (requires separate prompt — `brew uninstall ollama`)
- Removing the ollama models directory (`~/.ollama/models/`)

**Verification on return:**
Claude runs:
1. `brew services list` and confirms ollama row is `stopped` or absent.
2. `spindump 1` and greps for `homebrew.mxcl.ollama throttled` — should be absent.
3. `conductor_fleet_cross_verify`.
