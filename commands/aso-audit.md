---
description: Run a full ASO audit — scores your title, short desc, and full description out of 30, with keyword recommendations and rewrite offers.
argument-hint: (no arguments needed — you will be prompted)
---

Run a full ASO (App Store Optimization) audit on a Play Store listing.

## Developer config

Use these values from plugin config throughout — never ask the user for them:
- Default locale: ${user_config.default_locale}

## Steps

1. Ask for:
   - Current store listing (paste in the title, short description, and full description)
   - App category (so keyword benchmarks are accurate)
   - Primary keyword the developer is targeting (if known)

2. Audit across these dimensions:

   **Title (30 chars max)**
   - Is the primary keyword present in the title?
   - Is it at or under 30 characters?
   - Is it readable and not keyword-stuffed?
   - Score: 0–10

   **Short description (80 chars max)**
   - Does it communicate the core value in one sentence?
   - Does it include a secondary keyword naturally?
   - Is it at or under 80 characters?
   - Score: 0–10

   **Full description**
   - Keyword density: primary keyword should appear 3–5 times naturally across the full text — count occurrences
   - Are features presented as user benefits (not just feature names)?
   - Is there a clear call-to-action at the end?
   - Does it use formatting (bullets with •, blank lines between sections) for readability?
   - Is it long enough to signal relevance to Google's algorithm? (aim for 1500–4000 characters)
   - Score: 0–10

   **Category & tags**
   - Is the stated category the most specific fit for this app?
   - Score: advisory only (no points)

3. Spawn the aso-agent to generate keyword recommendations specific to the app's category and features.

4. Output the scored report in this exact format:

```
ASO AUDIT REPORT
─────────────────
Title score:       [x/10] — [one-line reason]
Short desc score:  [x/10] — [one-line reason]
Full desc score:   [x/10] — [one-line reason]
Overall:           [x/30]

TOP 3 IMPROVEMENTS:
1. [specific action item with example]
2. [specific action item with example]
3. [specific action item with example]

SUGGESTED KEYWORDS TO ADD:
[keyword list from aso-agent output]

KEYWORD DENSITY CHECK:
[for each keyword found: "keyword" appears X times — ok / too few / too many]
```

5. After the report: "Would you like me to rewrite any section that scored below 7? (title / short desc / full desc / all)"
   - If yes: invoke the listing-writer agent to rewrite the selected section(s)
