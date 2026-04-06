---
description: Write Play Store release notes (what's new) for an app update. Under 500 characters, user-friendly language, with optional localization.
argument-hint: (no arguments needed — you will be prompted)
---

Write Play Store release notes (what's new) for an app update.

## Developer config

Use these values from plugin config — never ask the user for them:
- Default locale: ${user_config.default_locale}
- Target locales: ${user_config.target_locales}

## Steps

1. Ask for:
   - List of changes in this version (paste git log output, a changelog, or describe in plain text)
   - Version number (e.g. 2.1.0)
   - Target locale(s) — defaults to ${user_config.default_locale}; ask if user wants additional locales

2. Write release notes that:
   - Are under 500 characters (Play Store limit — count and confirm before outputting)
   - Lead with the most user-visible change
   - Use plain language, not developer jargon (no "refactored", "migrated", "deprecated")
   - Start each item with an action verb: "Added", "Fixed", "Improved", "New:"
   - Never say "bug fixes and performance improvements" alone — be specific about what was fixed or improved
   - Use bullet format with • for multiple items

3. If the user requested multiple locales, spawn locale-agent for each additional locale after the English version is approved

4. Output in this exact format:

```
VERSION: x.x.x
LOCALE: [locale]
RELEASE NOTES:
[notes here]

CHARACTER COUNT: X/500
```

## Good example

```
• New dark mode — follows your system setting automatically
• Fixed crash when opening files larger than 50 MB
• Improved startup speed by 40%
• Added export to PDF option in settings
```

## Bad example — do not write like this

```
Bug fixes and performance improvements. Updated UI.
```

## Rules
- If the change list has more items than fit in 500 characters, prioritize user-facing features first, then bug fixes, then internal improvements
- Do not include version numbers or dates inside the notes — the Play Console already shows those
- Do not start with the app name — Play Console already displays it
