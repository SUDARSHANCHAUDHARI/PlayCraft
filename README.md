# PlayCraft

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](.claude-plugin/plugin.json)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
![Platform](https://img.shields.io/badge/platform-Claude%20Code-blueviolet)
![Target](https://img.shields.io/badge/target-Android%20%2F%20Google%20Play-brightgreen)

> Automate every Google Play Store publishing task — store listings, ASO, release notes, policy declarations, and screenshot copy — all from Claude Code.

**PlayCraft** is a Claude Code plugin that encodes the full Play Store submission workflow into
structured commands, agents, and skills — built from publishing 22+ apps at fleet scale under
SudarshanTechLabs.

## Table of Contents

- [Overview](#overview)
- [What It Does](#what-it-does)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Commands](#commands)
- [How It Works](#how-it-works)
- [Plugin Structure](#plugin-structure)
- [Troubleshooting](#troubleshooting)
- [Requirements](#requirements)
- [Documentation](#documentation)
- [License](#license)
- [About](#about)

## Overview

Play Store compliance had no repeatable structure. Each submission was manually reconstructed —
listing copy format, release notes character limits, Data Safety section declarations. At fleet
scale across 22+ apps, this was producing compliance gaps and inconsistent listing quality.

PlayCraft encodes the full Play Store submission workflow into structured commands. Every listing
goes through the same format, the same character limit enforcement, the same ASO scoring pass.
The compliance declarations checklist runs before every release. No manual reconstruction, no
missed fields.

## What It Does

1. Generates Play Store titles, short descriptions, and full descriptions — character limits enforced
2. Scores your ASO out of 30 and recommends keywords to add or remove
3. Writes release notes in plain user language, under 500 characters
4. Generates all required Play Console policy declarations — data safety, financial, AI content, families
5. Writes screenshot captions, alt text, and slot recommendations for up to 8 screenshots

## Installation

**Step 1 — Add the marketplace**
```bash
/plugin marketplace add SUDARSHANCHAUDHARI/PlayCraft
```

**Step 2 — Install the plugin**
```bash
/plugin install playcraft
```

When you install, Claude Code prompts you for your developer details once (name, company, email, GitHub username, country, default locale). These are stored globally and used automatically in every project.

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

## Commands

| Command | Description |
|---|---|
| `/playcraft:setup` | Show your current config and how to update it |
| `/playcraft:store-listing` | Generate title, short description, and full description |
| `/playcraft:release-notes` | Write what's new copy for an app update |
| `/playcraft:aso-audit` | Score and fix your ASO with keyword recommendations |
| `/playcraft:declarations` | Generate all required policy declarations checklist |
| `/playcraft:screenshots` | Write captions and alt text for Play Store screenshots |

## How It Works

```
/playcraft:store-listing ──► listing-writer ──► title / short desc / full desc
                          └──► policy-checker ──► compliance review

/playcraft:aso-audit ─────► aso-agent ────────► keyword report + scored listing

/playcraft:declarations ──► policy-checker ───► declarations checklist

/playcraft:release-notes ─► locale-agent ─────► localized versions (if requested)
```

- **listing-writer** — specialist copywriter enforcing all Play Store character limits
- **aso-agent** — keyword research, density analysis, and stuffing detection
- **policy-checker** — pre-submission compliance review against 2025–2026 Play Store policies
- **locale-agent** — localization for 14 locales, adapts idioms not just translates

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

## Troubleshooting

**Commands say config is missing** — Go to Claude Code Settings → Plugins → PlayCraft → Configure and fill in your developer details.

**Character count exceeds limit** — The listing-writer agent will catch this. If it doesn't, ask: "Rewrite the title to be under 30 characters."

**Release notes over 500 characters** — Ask: "Trim the release notes to under 500 characters, keep the most user-visible changes."

**Localization not offered** — Set your target locales in Settings → Plugins → PlayCraft → Configure → Target Locales (comma-separated, e.g. `th-TH, fr-FR`).

## Requirements

- [Claude Code](https://claude.ai/code) installed and authenticated
- No MCP servers required
- No API keys required
- No external tools required

## Documentation

For full details — all commands, agents, skills, compliance coverage, and architecture — see [DOCUMENTATION.md](DOCUMENTATION.md).

## License

MIT — see [LICENSE](LICENSE).

---

## About

I'm Sudarshan Chaudhari, a Senior Quality Engineer, Test Automation specialist, and AI systems builder based in Bangkok, Thailand.

I have 13+ years of experience in software quality engineering, working across SaaS, fintech, gaming, web, mobile, cloud, and digital signage platforms. My background combines hands-on test automation with QA leadership, test strategy, CI/CD, release quality, production investigation, and cross-platform validation.

Alongside my professional QA career, I run [SudarshanTechLabs](https://sudarshantechlabs.com/), my independent engineering and product lab where I design, build, test, and ship software across Android, web, AI, cybersecurity, developer tooling, and cross-platform applications.

### What I work on

- ⚙️ **Quality Engineering & Test Automation** — Playwright, Selenium, Cypress, Appium, API testing, automation frameworks, end-to-end testing, CI/CD, release gates, GitHub Actions, risk-based testing, and production validation
- 🤖 **AI Systems & Automation** — AI agents, multi-agent orchestration, MCP servers, AI-assisted QA, prompt tooling, developer workflows, automation systems, and Claude Code plugins
- 📱 **Mobile & Cross-Platform Applications** — Android applications built with Kotlin and Jetpack Compose, Google Play releases, automated build and publishing pipelines, and cross-platform development spanning iOS, web, Windows, and macOS
- 🌐 **Web Applications & Platforms** — Full-stack applications using Next.js, TypeScript, Firebase, Cloudflare, REST APIs, and modern web infrastructure
- 🛠️ **Developer Tooling & CLI Engineering** — Rust, Python, TypeScript, CLI utilities, multi-repository tooling, build automation, release tooling, and engineering productivity systems
- 🛡️ **Cybersecurity & Observability** — Threat detection, log analysis, security auditing, vulnerability assessment, monitoring, and security-focused developer tools
- 📺 **Digital Signage & Device Platforms** — Content validation, playback testing, device compatibility, production investigation, monitoring, and QA across diverse hardware and operating-system environments

My work sits at the intersection of quality engineering, automation, AI, and software development. I approach products with a QA mindset from the beginning: understanding failure modes, designing for testability, automating repetitive work, and building release confidence into the engineering process.

Through SudarshanTechLabs, I also build products and tools from idea to production, covering architecture, development, testing, CI/CD, release automation, monitoring, and ongoing maintenance.

🌐 [sudarshantechlabs.com](https://sudarshantechlabs.com/) · 💼 [LinkedIn](https://linkedin.com/in/sudarshan-chaudhari) · 🐙 [GitHub](https://github.com/SUDARSHANCHAUDHARI) · ✉️ [sunny.sudarshan@gmail.com](mailto:sunny.sudarshan@gmail.com)
