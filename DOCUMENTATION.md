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
6. [ASO Guide](#aso-guide)
7. [Policy Declarations Guide](#policy-declarations-guide)
8. [Localization Guide](#localization-guide)
9. [Plugin Architecture](#plugin-architecture)

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
Take control of your finances without spreadsheets or complex apps...

CHARACTER COUNTS:
Title: 34/30 ← (would be revised before showing)
Short desc: 54/80
Full desc: 1842/4000
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

**Good release notes:**
```
• New dark mode — follows your system setting automatically
• Fixed crash when opening files larger than 50 MB
• Improved startup speed by 40%
• Added export to PDF option in settings
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

**Scoring criteria:**
- Title: keyword presence, character limit, readability
- Short desc: value proposition clarity, secondary keyword, character limit
- Full desc: keyword density (3–5x primary), benefit framing, CTA, formatting, length

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

**Slot strategy:**
- Slot 1: Hero shot — most compelling feature
- Slots 2–3: Core use case step by step
- Slots 4–6: Secondary features
- Slots 7–8: Social proof or onboarding moment

---

## Agents

### aso-agent

Keyword research and density analysis. Invoked automatically by `/playcraft:aso-audit`.

Produces: primary keyword recommendation, secondary keyword list with volume/competition estimates, long-tail phrases, keyword density check, stuffing risk flags.

### listing-writer

Play Store copywriter specialist. Invoked by `/playcraft:aso-audit` when user requests a rewrite.

Enforces all character limits strictly. Structures full descriptions with hook, benefits, use case, permissions explanation, and closing CTA.

### policy-checker

Pre-submission policy compliance review. Invoked by `/playcraft:store-listing` (optional) and `/playcraft:declarations`.

Checks: metadata policy (keyword stuffing, competitor mentions, unverifiable claims), content policy (rating alignment, deceptive patterns), developer policy (financial disclaimers, health disclaimers).

Output: PASSED / WARNINGS / BLOCKERS / VERDICT.

### locale-agent

Localizes listings for 14 supported locales. Invoked by `/playcraft:store-listing` and `/playcraft:release-notes` when target locales are configured.

Priority locales: en-US, th-TH, id-ID, ms-MY, zh-TW, zh-CN, ja-JP, ko-KR, de-DE, fr-FR, es-ES, pt-BR, ar.

Adapts idioms and cultural references — not word-for-word translation. Re-checks character limits after translation. Flags RTL considerations for Arabic.

---

## Skills

Skills are loaded automatically when relevant — you do not invoke them directly.

### play-policy-2026

2025–2026 Play Store rules: character limits, metadata policy, new requirements (AI declarations, financial declarations, closed testing, identity verification), data safety, rating system, payments policy.

Trigger: any Play Store submission or listing work.

### closed-testing

Requirements for new developer accounts: 12+ testers, 14 continuous days, step-by-step Play Console setup, finding testers, common mistakes.

Trigger: setting up a new app or preparing for open testing.

### financial-declarations

Financial features declaration walkthrough with Play Console navigation paths, IAP/subscription declaration requirements, common mistakes.

Trigger: app involving payments, financial data, banking, crypto, or subscriptions.

### ai-content-declarations

AI-generated content declaration guide (2025 requirement), Play Console navigation, moderation requirements, user disclosure requirements, Claude API / Gemini API specific guidance.

Trigger: app using AI to generate text, images, audio, or video.

### developer-identity-th

Developer identity verification for Thailand: individual account documents, organization/D-U-N-S requirements, Thai bank account setup, W-8BEN tax form, VAT registration, common issues.

Trigger: Play Console account setup or identity verification.

---

## Hooks

### pre-release-check

Fires before `Bash` or `Write` tool use when the command appears to be a release action (building release AAB/APK, signing, uploading).

Prints a non-blocking pre-flight checklist:
- Run `/playcraft:declarations`
- Run `/playcraft:aso-audit`
- Confirm release notes written
- Confirm version code incremented
- Confirm closed testing complete (if required)

---

## ASO Guide

### Character limit strategy

| Field | Limit | Goal |
|---|---|---|
| Title | 30 chars | Primary keyword + brand name |
| Short desc | 80 chars | Secondary keyword + core benefit |
| Full desc | 4000 chars | 3–5x primary keyword, benefits over features |

### Keyword placement

- **Title** — highest ranking weight. One primary keyword only.
- **Short description** — indexed by Google, shown in search results. One secondary keyword.
- **Full description** — primary keyword 3–5 times naturally. Secondary keywords woven in.

### Keyword density

- Primary keyword: 3–5 occurrences in full description = optimal
- Below 3: too few — Google may not associate your app with this term
- Above 5: keyword stuffing risk — policy violation

---

## Policy Declarations Guide

### Required for every app

- Data Safety section — must be complete before any update can be published
- Content rating — via IARC questionnaire

### Conditionally required

| Condition | Declaration required |
|---|---|
| App mentions money, banking, crypto, investments | Financial features declaration |
| App uses AI to generate content | AI-generated content declaration |
| App targets children under 13 | Families policy compliance |
| App requests background location | Prominent in-app disclosure |
| New developer account (post Nov 2023) | Closed testing (12 testers, 14 days) |

---

## Localization Guide

### Supported locales

| Locale | Language | Notes |
|---|---|---|
| en-US | English (US) | Default / source |
| th-TH | Thai | Priority for Southeast Asia |
| id-ID | Indonesian | 270M population, growing market |
| ms-MY | Malay | Malaysia + Brunei |
| zh-TW | Traditional Chinese | Taiwan, Hong Kong |
| zh-CN | Simplified Chinese | Mainland China |
| ja-JP | Japanese | Search in hiragana/katakana for foreign apps |
| ko-KR | Korean | |
| de-DE | German | EU tier 1 |
| fr-FR | French | EU tier 1 |
| es-ES | Spanish | EU + LatAm via es-419 |
| pt-BR | Brazilian Portuguese | Largest LatAm market |
| ar | Arabic | RTL — flag for layout mirroring |

---

## Plugin Architecture

```
User prompt
    │
    ▼
Command (.md)
    │
    ├── Reads ${user_config.*} from plugin userConfig (global)
    ├── Asks user for app-specific inputs
    │
    ▼
Agent(s) invoked as needed
    │
    ├── aso-agent ──── keyword research
    ├── listing-writer ─ copywriting
    ├── policy-checker ─ compliance review
    └── locale-agent ── localization
    │
    ▼
Skills loaded automatically by trigger
    │
    ├── play-policy-2026 ── character limits + rules
    ├── financial-declarations ── if financial app
    ├── ai-content-declarations ── if AI features
    ├── closed-testing ── if new account setup
    └── developer-identity-th ── if Thailand account
    │
    ▼
Output to user (formatted text in Claude Code session)
```
