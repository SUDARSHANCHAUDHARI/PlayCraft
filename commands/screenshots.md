---
description: Write captions (~30 chars), alt text, and slot recommendations for up to 8 Play Store screenshots. Optionally describes the feature graphic.
argument-hint: (no arguments needed — you will be prompted)
---

Write alt text, captions, and feature graphic descriptions for Play Store screenshots.

## Developer config

Use these values from plugin config throughout — never ask the user for them:
- Developer name: ${user_config.developer_name}
- Company: ${user_config.company}

## Steps

1. Ask the user to describe each screenshot or share screenshot filenames/descriptions.
   If they have multiple device form factors (phone, 7-inch tablet, 10-inch tablet), ask which they are describing.

2. Ask: How many screenshots total? (Play Store allows up to 8 per device type)

3. For each screenshot described, generate:
   - **Caption text** — overlay text for the screenshot graphic, max ~30 characters
     - Benefit-focused, not feature-focused ("Track in real time" not "Tracking feature")
     - Action-oriented phrasing
   - **Alt text** — accessibility metadata describing the screenshot content (1–2 sentences)
   - **Placement recommendation** — which slot (1–8) this screenshot best fits and why

4. Output each screenshot block in this format:

```
SCREENSHOT [N]
Caption:  [text — ~30 chars max]
Alt text: [1–2 sentence description]
Slot:     [slot number] — [reason, e.g. "First — hero shot showing core value"]
```

5. After all screenshots, print a summary sequence showing recommended slot order and what each communicates to users scanning the listing.

## Screenshot strategy rules

- **Slot 1** — Most compelling feature or "hero" moment. This is the only screenshot many users see before deciding to install.
- **Slots 2–3** — Core use case demonstrated step by step
- **Slots 4–6** — Secondary features and additional value
- **Slots 7–8** — Social proof (ratings, awards, press mentions), or onboarding moment if no social proof yet

## Caption writing rules
- Active verbs: "Track", "Organize", "Share", "Export", "Scan" — not "Tracking", "Organization"
- No "Download now" or CTAs in screenshot captions — Google policy violation
- No competitor names
- Captions should make sense without seeing the screenshot (accessibility)
- Prefer specific over vague: "Export to PDF in one tap" beats "Easy export"

## Feature graphic (optional)
If the user also needs a feature graphic description (the 1024×500 banner):
- Describe the visual layout: what should appear left / center / right
- Suggest a 5–7 word tagline for the graphic
- Note: no pricing, no time-limited offers in the feature graphic (policy)
