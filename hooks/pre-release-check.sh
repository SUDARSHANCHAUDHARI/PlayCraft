#!/usr/bin/env bash
# PlayCraft PreToolUse(Bash) hook: one-line listing/policy reminder before a release build or signing step.
# Build checks (versionCode, keystore) belong to DroidForge, not here. Never blocks: always exits 0.

input=$(cat)

if command -v jq >/dev/null 2>&1; then
  cmd=$(printf '%s' "$input" | jq -r '.tool_input.command // empty' 2>/dev/null)
elif command -v python3 >/dev/null 2>&1; then
  cmd=$(printf '%s' "$input" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null)
else
  # shortcut: sed pulls the last "command" string out of the JSON; escaped quotes stay escaped. Fine for matching.
  cmd=$(printf '%s' "$input" | sed -nE 's/.*"command"[[:space:]]*:[[:space:]]*"(([^"\\]|\\.)*)".*/\1/p')
fi

# Fire only when gradle(w) runs a *Release bundle/assemble task, or a signer runs as a command,
# so "grep bundleRelease docs/" or "echo apksigner" do not trigger it.
start='(^|[;&|(][[:space:]]*)([^[:space:];&|]*/)?'
printf '%s' "$cmd" | grep -Eq "${start}gradlew?[[:space:]][^;&|]*(bundle|assemble)[A-Za-z0-9]*Release|${start}(apksigner|jarsigner)([[:space:]]|\$)" || exit 0

msg="PlayCraft: before uploading, run /playcraft:declarations, /playcraft:aso-audit and /playcraft:release-notes, check versionCode was bumped, and finish closed testing if your account needs it."
printf '%s\n' "$msg" >&2
# systemMessage is how a PreToolUse hook shows text to the user at exit 0; stderr alone is only visible in verbose mode.
printf '{"systemMessage": "%s"}\n' "$msg"
exit 0
