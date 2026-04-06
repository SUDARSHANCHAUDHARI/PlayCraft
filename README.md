# PlayCraft — Claude Code Plugin

> Automate every Google Play Store publishing task — store listings, ASO, release notes, policy declarations, and screenshot copy — all from Claude Code.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Claude%20Code-blueviolet)
![Target](https://img.shields.io/badge/target-Android%20%2F%20Google%20Play-brightgreen)

---

## What It Does

1. Generates Play Store titles, short descriptions, and full descriptions — character limits enforced
2. Scores your ASO out of 30 and recommends keywords to add or remove
3. Writes release notes in plain user language, under 500 characters
4. Generates all required Play Console policy declarations — data safety, financial, AI content, families
5. Writes screenshot captions, alt text, and slot recommendations for up to 8 screenshots

---

## Install

```bash
/plugin install playcraft
```

When you install, Claude Code prompts you for your developer details once (name, company, email, GitHub username, country, default locale). These are stored globally and used automatically in every project.

---

## Commands

| Command | Description |
|---|---|
| `/playcraft:setup` | Show your current config and how to update it |
| `/playcraft:store-listing` | Generate title, short description, and full description |
| `/playcraft:release-notes` | Write what's new copy for an app update |
| `/playcraft:aso-audit` | Score and fix your ASO with keyword recommendations |
| `/playcraft:declarations` | Generate all required policy declarations checklist |
| `/playcraft:screenshots` | Write captions and alt text for Play Store screenshots |

---

## Quick Start

**1. Generate your store listing**
```
/playcraft:store-listing
```
Provide your app name, category, features, and target audience. Output includes title, short description, and full description with live character counts.

**2. Audit your ASO**
```
/playcraft:aso-audit
```
Paste your current listing. Get a score out of 30, keyword recommendations, and offers to rewrite any section that scores below 7.

**3. Write release notes**
```
/playcraft:release-notes
```
Paste your git log or describe your changes. Get polished, user-friendly release notes under 500 characters.

---

## How It Works

```
User input ──► store-listing ──► listing-writer ──► title / short desc / full desc
                                └──► policy-checker ──► policy review

User input ──► aso-audit ──► aso-agent ──► keyword report + scoring

User input ──► declarations ──► policy-checker ──► declarations checklist

User input ──► release-notes ──► locale-agent ──► localized versions (if requested)
```

---

## Plugin Structure

```
PlayCraft/
├── .claude-plugin/
│   ├── plugin.json              # Plugin manifest + userConfig
│   └── marketplace.json         # Marketplace manifest
├── commands/                    # /playcraft:setup|store-listing|release-notes|aso-audit|declarations|screenshots
├── agents/                      # aso-agent, listing-writer, policy-checker, locale-agent
├── skills/                      # play-policy-2026, closed-testing, financial-declarations,
│                                #   ai-content-declarations, developer-identity-th
├── hooks/
│   └── pre-release-check.md     # Pre-release checklist reminder
├── README.md
├── CHANGELOG.md
├── DOCUMENTATION.md
└── LICENSE
```

---

## Troubleshooting

**Commands say config is missing** — Go to Claude Code Settings → Plugins → PlayCraft → Configure and fill in your developer details.

**Character count exceeds limit** — The listing-writer agent will catch this. If it doesn't, ask: "Rewrite the title to be under 30 characters."

**Release notes over 500 characters** — Ask: "Trim the release notes to under 500 characters, keep the most user-visible changes."

**Localization not offered** — Set your target locales in Settings → Plugins → PlayCraft → Configure → Target Locales (comma-separated, e.g. `th-TH, fr-FR`).

---

## Requirements

- [Claude Code](https://claude.ai/code) installed and authenticated
- No MCP servers required
- No API keys required
- No external tools required

---

## Author

**SUDARSHANCHAUDHARI** — [github.com/SUDARSHANCHAUDHARI](https://github.com/SUDARSHANCHAUDHARI)
SudarshanTechLabs | sudarshantechlabs@gmail.com

---

## Documentation

For full details — all commands, agents, skills, compliance coverage, and architecture — see [DOCUMENTATION.md](DOCUMENTATION.md).

---

## License

MIT — see [LICENSE](LICENSE)
