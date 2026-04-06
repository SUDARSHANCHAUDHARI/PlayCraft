# PlayCraft — Full Documentation

This document covers everything needed to use PlayCraft effectively. See [README.md](README.md) for a quick overview.

---

## Table of Contents

1. [Installation & Configuration](#installation--configuration)
2. [Commands](#commands)
   - [/playcraft:setup](#playcraftsetup)
   - [/playcraft:store-listing](#playcraftstore-listing)
   - [/playcraft:release-notes](#playcraftrelease-notes)
   - [/playcraft:aso-audit](#playcraftaso-audit)
   - [/playcraft:declarations](#playcraftdeclarations)
   - [/playcraft:screenshots](#playcraftscreenshots)
3. [Agents](#agents)
4. [Skills](#skills)
5. [Hooks](#hooks)
6. [Configuration Reference](#configuration-reference)
7. [ASO Guide](#aso-guide)
8. [Policy Declarations Guide](#policy-declarations-guide)
9. [Localization Guide](#localization-guide)
10. [Plugin Architecture](#plugin-architecture)

---

## Installation & Configuration

### Install the plugin

```bash
/plugin install playcraft
```

### First-time setup

After installing, Claude Code prompts you to enter your developer details. These are stored globally and reused across all your projects — you set them once.

| Field | Description | Example |
|---|---|---|
| Developer Name | Your full name or display name | `John Smith` |
| Company | Developer label shown on Play Store | `YourCompany` |
| Contact Email | Email for Play Console and privacy policy | `you@example.com` |
| GitHub Username | Your GitHub handle | `yourhandle` |
| Country | Country where you are based | `United States` |
| Default Locale | Primary locale for listings | `en-US` |
| Target Locales | Comma-separated additional locales | `fr-FR, de-DE` |

To update these values at any time: Claude Code → Settings → Plugins → PlayCraft → Configure.

---

## Commands

### /playcraft:setup

Shows your current PlayCraft configuration. Use this to verify your developer details are set correctly.

To update: Claude Code → Settings → Plugins → PlayCraft → Configure.

**Example output:**
```
PLAYCRAFT CONFIGURATION
────────────────────────
Developer:      John Smith
Company:        YourCompany
Email:          you@example.com
GitHub:         yourhandle
Country:        United States
Default locale: en-US
Other locales:  fr-FR, de-DE
```

---

### /playcraft:store-listing

Generates a complete Google Play Store listing with all three required fields.

**What it asks for:**
- App name and package name
- App category
- Core features (up to 5 bullet points)
- Target audience
- Existing description to improve (optional)

**What it produces:**
- Title (max 30 characters)
- Short description (max 80 characters)
- Full description (max 4000 characters) with structured sections
- Character counts for all three fields
- Optional policy check via policy-checker agent

**Example output:**
```
TITLE: Budget Tracker — Expense Log
SHORT DESC: Track spending and set budgets that actually stick.
FULL DESC:
Take control of your finances without spreadsheets or complex apps.
Budget Tracker helps you log every expense and stay on target — daily,
weekly, or monthly.

WHY USERS LOVE BUDGET TRACKER:
• Log expenses in under 3 seconds
• Set weekly and monthly budget limits per category
• Visual charts show exactly where your money goes
• Export to CSV for tax season
• Works offline — no account required

PERFECT FOR:
Anyone who wants to spend less time thinking about money and more time
keeping it. Ideal for students, freelancers, and families.

Download free and start tracking your spending today.

CHARACTER COUNTS:
Title: 28/30
Short desc: 55/80
Full desc: 683/4000
```

---

### /playcraft:release-notes

Writes user-friendly Play Store release notes (what's new) for an app update.

**What it asks for:**
- List of changes (git log, changelog, or free text)
- Version number
- Target locale(s) — defaults to your configured default locale

**What it produces:**
- Release notes under 500 characters
- Character count shown
- Optional localized versions via locale-agent

**Example output:**
```
VERSION: 2.4.0
LOCALE: en-US
RELEASE NOTES:
• New dark mode — follows your system setting automatically
• Fixed crash when opening files larger than 50 MB
• Improved startup speed by 40%
• Added export to PDF option in settings

CHARACTER COUNT: 187/500
```

**Bad example — PlayCraft will never write this:**
```
Bug fixes and performance improvements. Updated UI.
```

---

### /playcraft:aso-audit

Scores your current Play Store listing and provides keyword recommendations.

**What it asks for:**
- Current listing (title, short desc, full desc)
- App category
- Primary keyword you are targeting (if known)

**What it produces:**
- Score out of 30 (title/10, short desc/10, full desc/10)
- Top 3 improvement actions
- Keyword recommendations from aso-agent
- Keyword density analysis
- Offer to rewrite any section scoring below 7

**Example output:**
```
ASO AUDIT REPORT
─────────────────
Title score:       7/10 — Primary keyword present but title uses 18/30 chars, room to add secondary keyword
Short desc score:  5/10 — Leads with feature name, not user benefit; no secondary keyword
Full desc score:   6/10 — Primary keyword appears only 2x (aim for 3–5); no CTA at end
Overall:           18/30

TOP 3 IMPROVEMENTS:
1. Rewrite short desc to lead with benefit: "Track expenses and hit your budget goals — effortlessly."
2. Add primary keyword 2 more times naturally in the full description body
3. Add a closing CTA line: "Download free and start tracking today."

SUGGESTED KEYWORDS TO ADD:
expense tracker, monthly budget, spending log, money manager, finance app

KEYWORD DENSITY CHECK:
- "budget" appears 2 times — too few (add 1–2 more)
- "expense" appears 4 times — ok
- "track" appears 6 times — too many (reduce to avoid stuffing)
```

---

### /playcraft:declarations

Generates a complete Play Console policy declarations checklist tailored to your app.

**What it asks for:**
- Package name and category
- Financial features? (y/n)
- AI-generated content? (y/n)
- Targets children under 13? (y/n)
- Sensitive permissions used

**What it produces:**
- Data Safety section checklist (required for all apps)
- Financial features declaration (if applicable)
- AI-generated content declaration (if applicable)
- Families policy checklist (if applicable)
- Developer identity verification steps for your country
- All items include exact Play Console navigation paths

**Example output:**
```
DECLARATIONS CHECKLIST
─────────────────────────────────
App: com.example.budgettracker | Finance

☐ DATA SAFETY SECTION
  Path: App Dashboard → Policy → App content → Data safety
  - [ ] Declared data types: Financial info (user-entered budgets/expenses)
  - [ ] Encryption in transit: declare yes
  - [ ] Data deletion: declare whether user can request deletion

☐ FINANCIAL FEATURES DECLARATION
  Path: App Dashboard → Policy → App content → Financial features
  - [ ] Select type: "In-app purchases" (if IAP exists)
  - [ ] Add in-app disclaimer: "This app does not provide financial advice."

NEXT STEPS:
1. Complete each item above in Play Console
2. Run /playcraft:aso-audit before submitting
3. Confirm release notes are written (/playcraft:release-notes)
```

---

### /playcraft:screenshots

Writes captions, alt text, and placement recommendations for Play Store screenshots.

**What it asks for:**
- Description of each screenshot (or filename/content)
- Total screenshot count (up to 8 per device type)
- Device form factor (phone, 7-inch tablet, 10-inch tablet)

**What it produces per screenshot:**
- Caption text (~30 characters, benefit-focused)
- Alt text (1–2 sentences for accessibility)
- Slot recommendation (1–8) with reason
- Optional feature graphic description (1024×500 banner)

**Example output:**
```
SCREENSHOT 1
Caption:  Track every expense instantly
Alt text: Home screen showing daily expense log with categories and total spent today.
Slot:     1 — Hero shot showing core value immediately

SCREENSHOT 2
Caption:  Set budgets that stick
Alt text: Budget settings screen with weekly and monthly limits per spending category.
Slot:     2 — Core use case demonstrated

SCREENSHOT 3
Caption:  See where money goes
Alt text: Charts screen showing donut chart of spending by category for the current month.
Slot:     3 — Outcome/result of using the app
```

---

## Agents

### aso-agent

Keyword research and density analysis. Invoked automatically by `/playcraft:aso-audit`.

Produces: primary keyword recommendation, secondary keyword list with volume/competition estimates, long-tail phrases, keyword density check, stuffing risk flags.

### listing-writer

Play Store copywriter specialist. Invoked by `/playcraft:aso-audit` when user requests a rewrite, and by `/playcraft:store-listing` for full listing generation.

Enforces all character limits strictly. Structures full descriptions with hook, benefits (WHY USERS LOVE), use case (PERFECT FOR), permissions explanation, and closing CTA.

### policy-checker

Pre-submission policy compliance review. Invoked by `/playcraft:store-listing` (optional) and `/playcraft:declarations`.

**Checks:**
- Metadata policy: keyword stuffing, competitor mentions, unverifiable claims (#1, best)
- Content policy: rating alignment, deceptive patterns, misleading feature claims
- Developer policy: financial disclaimers, health disclaimers, VPN legitimacy

**Output format:** PASSED / WARNINGS (fix before submission) / BLOCKERS (will cause rejection) / VERDICT.

### locale-agent

Localizes listings for 14 supported locales. Invoked by `/playcraft:store-listing` and `/playcraft:release-notes` when target locales are configured.

Supported locales: en-US, th-TH, id-ID, ms-MY, zh-TW, zh-CN, ja-JP, ko-KR, de-DE, fr-FR, es-ES, pt-BR, ar.

Adapts idioms and cultural references — not word-for-word translation. Re-checks character limits after translation (CJK scripts are denser; Arabic can be longer). Flags RTL layout considerations for Arabic.

---

## Skills

Skills are loaded automatically when relevant — you do not invoke them directly.

### play-policy-2026

2025–2026 Play Store rules: character limits, metadata policy, new requirements (AI declarations, financial declarations, closed testing, identity verification), data safety, rating system, payments policy.

**Trigger:** any Play Store submission or listing work.

### closed-testing

Requirements for new developer accounts (post November 2023): 12+ testers, 14 continuous days, step-by-step Play Console setup, how to find testers, common mistakes.

**Trigger:** setting up a new app or preparing for open testing.

### financial-declarations

Financial features declaration walkthrough with Play Console navigation paths, IAP/subscription declaration requirements, common mistakes.

**Trigger:** app involving payments, financial data, banking, crypto, or subscriptions.

### ai-content-declarations

AI-generated content declaration guide (2025 requirement), Play Console navigation, moderation requirements, user disclosure requirements, Claude API and Gemini API specific guidance.

**Trigger:** app using AI to generate text, images, audio, or video.

### developer-identity-th

Developer identity verification for Thailand: individual account documents (Thai national ID), organization/D-U-N-S requirements, Thai bank account setup, W-8BEN tax form, VAT registration, common issues.

**Trigger:** Play Console account setup or identity verification for Thailand-based developers.

---

## Hooks

### pre-release-check

Fires before `Bash` or `Write` tool use when the command appears to be a release action (building release AAB/APK, running signing commands, uploading to Play Console).

Prints a non-blocking pre-flight checklist reminder:
- Run `/playcraft:declarations` — all declarations up to date?
- Run `/playcraft:aso-audit` — store listing reviewed?
- Confirm release notes written (`/playcraft:release-notes`)
- Version code incremented in `build.gradle`?
- Closed testing complete (if required for account type)?

Does not block the action — surfaces the reminder before proceeding.

---

## Configuration Reference

Configuration is stored globally via Claude Code's plugin `userConfig` system. Values are substituted automatically into every command and agent prompt using `${user_config.KEY}` tokens.

| Key | Title | Description | Used in |
|---|---|---|---|
| `developer_name` | Developer Name | Your full name or display name | `/playcraft:setup` display |
| `company` | Company | Developer label shown on Play Store | `/playcraft:store-listing`, `/playcraft:screenshots` |
| `email` | Contact Email | Email for Play Console and privacy policy | `/playcraft:declarations` |
| `github_username` | GitHub Username | Your GitHub handle | `/playcraft:setup` display |
| `country` | Country | Country of operation — used for identity verification guidance | `/playcraft:declarations` |
| `default_locale` | Default Locale | Primary locale for store listings | `/playcraft:store-listing`, `/playcraft:release-notes`, `/playcraft:aso-audit` |
| `target_locales` | Target Locales | Comma-separated additional locales | `/playcraft:store-listing`, `/playcraft:release-notes` |

All fields are plain strings. None are sensitive.

---

## ASO Guide

### Character limit strategy

| Field | Limit | Goal |
|---|---|---|
| Title | 30 chars | Primary keyword + brand name — highest ranking weight |
| Short desc | 80 chars | Secondary keyword + core benefit — shown in search results |
| Full desc | 4000 chars | 3–5x primary keyword, benefits over features |

### Keyword placement

- **Title** — highest ranking weight. One primary keyword only. Never keyword-stuff.
- **Short description** — indexed by Google, shown in search results. One secondary keyword.
- **Full description** — primary keyword 3–5 times naturally. Secondary keywords woven in throughout.

### Keyword density rules

| Occurrences | Status |
|---|---|
| 0–2 | Too few — Google may not associate your app with this term |
| 3–5 | Optimal |
| 6+ | Keyword stuffing — policy violation risk |

### Writing principles PlayCraft enforces

- Lead with user benefit, not feature name
- Active voice: "Track expenses" not "Expenses are tracked"
- No weak adjectives: "easy", "simple", "best", "amazing", "powerful"
- No unverifiable claims: "#1 app", "world's best", "most downloaded"
- No competitor names
- No ALL CAPS except acronyms and section headers

---

## Policy Declarations Guide

### Required for every app

| Declaration | Navigation | Notes |
|---|---|---|
| Data Safety | App Dashboard → Policy → App content → Data safety | Must be complete before any update can be published |
| Content rating | App Dashboard → Policy → App content → App content | Via IARC questionnaire — answer honestly |

### Conditionally required

| Condition | Declaration required | Navigation |
|---|---|---|
| App mentions money, banking, crypto, investments | Financial features declaration | App content → Financial features |
| App uses AI to generate text, images, audio, or video | AI-generated content declaration | App content → AI-generated content |
| App targets children under 13 | Families policy | App content → Target audience and content |
| App requests background location | Prominent in-app disclosure | Must be in app UI, not just policy |
| New developer account (post Nov 2023) | Closed testing: 12 testers, 14 days | Testing → Closed testing |
| All new and some existing accounts | Identity verification | Settings → Developer account → Identity verification |

---

## Localization Guide

### Supported locales

| Locale | Language | Notes |
|---|---|---|
| en-US | English (US) | Default / source language |
| th-TH | Thai | Priority — Southeast Asia |
| id-ID | Indonesian | 270M population, fast-growing Play Store market |
| ms-MY | Malay | Malaysia + Brunei |
| zh-TW | Traditional Chinese | Taiwan, Hong Kong |
| zh-CN | Simplified Chinese | Mainland China |
| ja-JP | Japanese | Foreign app names often searched in katakana |
| ko-KR | Korean | |
| de-DE | German | EU tier 1 |
| fr-FR | French | EU tier 1 |
| es-ES | Spanish | EU + LatAm (use es-419 for LatAm variant) |
| pt-BR | Brazilian Portuguese | Largest LatAm market |
| ar | Arabic | RTL — app screenshots may need mirroring |

### How localization works

locale-agent does not do word-for-word translation. For each locale it:
1. Translates accurately while adapting idioms for the target market
2. Re-checks all character limits after translation
3. Flags any content that may be culturally inappropriate
4. Notes market-specific search behavior (e.g. Japanese users often search in hiragana/katakana for foreign apps)

---

## Plugin Architecture

```
PlayCraft/
├── .claude-plugin/
│   ├── plugin.json              # Plugin manifest + userConfig schema
│   └── marketplace.json         # Marketplace listing metadata
├── commands/
│   ├── setup.md                 # /playcraft:setup
│   ├── store-listing.md         # /playcraft:store-listing
│   ├── release-notes.md         # /playcraft:release-notes
│   ├── aso-audit.md             # /playcraft:aso-audit
│   ├── declarations.md          # /playcraft:declarations
│   └── screenshots.md           # /playcraft:screenshots
├── agents/
│   ├── aso-agent.md             # Keyword research and density analysis
│   ├── listing-writer.md        # Play Store copywriter
│   ├── policy-checker.md        # Policy compliance review
│   └── locale-agent.md          # Localization for 14 locales
├── skills/
│   ├── play-policy-2026/        # 2025–2026 Play Store rules
│   ├── closed-testing/          # Closed testing requirements
│   ├── financial-declarations/  # Financial features declaration guide
│   ├── ai-content-declarations/ # AI content declaration guide
│   └── developer-identity-th/  # Thailand identity verification guide
├── hooks/
│   └── pre-release-check.md     # Pre-release checklist reminder
├── README.md                    # Quick overview
├── DOCUMENTATION.md             # This file — full reference
├── CHANGELOG.md                 # Version history
└── LICENSE                      # MIT
```

### How commands, agents, and skills interact

- **Commands** (`commands/*.md`) — define the user-facing workflow step by step. They read developer config from `${user_config.*}`, ask the user for app-specific inputs, and orchestrate which agents to spawn.
- **Agents** (`agents/*.md`) — specialized workers that handle a specific task (keyword research, copywriting, policy checking, localization). Spawned by commands via Claude's multi-agent system.
- **Skills** (`skills/*/SKILL.md`) — reference knowledge loaded automatically when their trigger condition matches. They provide rules, data tables, and compliance guides (e.g. the full Play Store policy rules, Thailand identity verification steps) without requiring agents to carry that knowledge themselves.

This separation means each agent stays focused, the workflow logic (commands) is clean, and the knowledge base (skills) can be updated independently.
