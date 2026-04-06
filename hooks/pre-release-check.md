---
event: PreToolUse
tools: ["Bash", "Write"]
description: Warn before any file operation that looks like a Play Store release action
---

When the user runs a command that appears to be preparing a Play Store release — for example:
- Building a release AAB or APK (`./gradlew bundleRelease`, `./gradlew assembleRelease`)
- Running signing commands (`jarsigner`, `apksigner`)
- Uploading to Play Console or running a deployment script

Print this pre-flight checklist reminder **before the action runs**. Do not block the action — just surface the reminder.

```
PLAYCRAFT PRE-RELEASE CHECK
────────────────────────────
Before submitting to Play Store:

☐ /playcraft:declarations — all policy declarations up to date?
☐ /playcraft:aso-audit — store listing reviewed and scored?
☐ /playcraft:release-notes — what's new copy written for this version?
☐ Version code incremented in build.gradle / build.gradle.kts?
☐ Closed testing complete (if required for your account type)?

Proceeding with your command...
```

If the command does not appear to be release-related, do nothing — do not print the checklist for regular builds or unrelated file operations.
