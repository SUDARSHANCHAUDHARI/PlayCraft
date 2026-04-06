---
description: Show your current PlayCraft developer config and how to update it.
argument-hint: (no arguments needed)
---

Show the current PlayCraft developer configuration.

## Steps

1. Display the current config values from plugin userConfig:

```
PLAYCRAFT CONFIGURATION
────────────────────────
Developer:      ${user_config.developer_name}
Company:        ${user_config.company}
Email:          ${user_config.email}
GitHub:         ${user_config.github_username}
Country:        ${user_config.country}
Default locale: ${user_config.default_locale}
Other locales:  ${user_config.target_locales}
```

2. Explain how to update:
   - Claude Code → Settings → Plugins → PlayCraft → Configure
   - Update any field and save — changes apply immediately to all commands

## Note

Config is stored globally by Claude Code — not in a local file. You set it once at install time and it works across all your projects automatically.
