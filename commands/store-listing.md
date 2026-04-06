---
description: Generate a complete Play Store listing — title, short description, and full description with character limit checks and optional policy review.
argument-hint: (no arguments needed — you will be prompted)
---

Generate a complete Google Play Store listing for an Android app.

## Developer config

Use these values from plugin config throughout — never ask the user for them:
- Developer name: ${user_config.developer_name}
- Company: ${user_config.company}
- Default locale: ${user_config.default_locale}
- Target locales: ${user_config.target_locales}

## Steps

1. Ask the user for:
   - App name and package name
   - App category (utility, productivity, tools, finance, health, etc.)
   - Core features — list up to 5 bullet points
   - Target audience (who uses this app and why)
   - Any existing description to improve (optional — paste it in or skip)

2. Generate all required Play Store fields:

   **Title** (max 30 characters)
   - Include the primary keyword naturally
   - Do not pad with punctuation or symbols
   - Count characters and confirm ≤ 30 before outputting

   **Short description** (max 80 characters)
   - Lead with the main user benefit
   - Include one secondary keyword if it fits naturally
   - Count characters and confirm ≤ 80 before outputting

   **Full description** (max 4000 characters)
   Structure as:
   - Hook paragraph (2–3 sentences, benefit-first, primary keyword in first sentence)
   - Blank line
   - Features section using Unicode bullets (•), e.g. "WHY USERS LOVE [APP NAME]:"
   - Blank line
   - Use case / who it's for ("PERFECT FOR:")
   - Blank line
   - Permissions explanation if sensitive permissions are used (camera, location, contacts, microphone, storage) — explain why each is needed in plain language
   - Closing CTA line (soft — no imperative ALL CAPS)
   - Count characters and confirm ≤ 4000 before outputting

3. Check all character limits before outputting. If any field exceeds its limit, revise it before showing the user.

4. Output in this exact format:

```
TITLE: [title here]
SHORT DESC: [short description here]
FULL DESC:
[full description here]

CHARACTER COUNTS:
Title: X/30
Short desc: X/80
Full desc: X/4000
```

5. After outputting, ask: "Would you like me to run a policy check on this listing? (y/n)"
   - If yes: invoke the policy-checker agent on the generated listing.

## Rules
- No keyword stuffing — Google penalizes repetitive keyword use
- Do not mention competitor app names
- Do not make claims you cannot verify (e.g., "#1 app", "world's best")
- Avoid ALL CAPS except for acronyms and section headers
- Write in active voice
- Never use: "easy", "simple", "best", "amazing", "powerful" — show the value, don't label it
- Default to ${user_config.default_locale} for the listing language
- If ${user_config.target_locales} is set, offer to generate localized versions using locale-agent after the English listing is approved
