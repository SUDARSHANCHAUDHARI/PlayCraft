---
description: Generate all required Play Console policy declarations — data safety, financial features, AI content, families, and identity verification checklist.
argument-hint: (no arguments needed — you will be prompted)
---

Generate all required Google Play policy declarations for an app submission.

## Developer config

Use these values from plugin config — never ask the user for them:
- Country: ${user_config.country}
- Email: ${user_config.email}

## Steps

1. Ask for:
   - App package name and category
   - Does the app handle payments, subscriptions, or financial data? (y/n)
   - Does the app use any AI-generated content (text, images, audio, or video)? (y/n)
   - Does the app target children under 13? (y/n)
   - Sensitive permissions used — list any that apply: camera, location (background or foreground), contacts, microphone, phone state, external storage

2. Invoke the policy-checker agent to scan inputs for any additional policy flags before generating the checklist.

3. Generate a declarations checklist tailored to the answers above:

   **Data Safety section** (required for all apps)
   - Navigation: App Dashboard → Policy → App content → Data safety
   - For each permission listed:
     - Camera → declares image/video capture; specify if data is shared or stored
     - Location → declares precise or approximate location; required: prominent disclosure in app
     - Contacts → declares contacts data; required: explain use in privacy policy
     - Microphone → declares audio capture; specify if recordings are stored or processed
     - Storage → declares files/docs; specify types read or written
   - Required fields for every app: Is data encrypted in transit? Can users request deletion?

   **Financial features declaration** (only if answered yes above)
   - Navigation: App Dashboard → Policy → App content → Financial features
   - Select all applicable types: banking/payment, investment, insurance, cryptocurrency, lending/credit
   - Upload license if required in ${user_config.country}, or select "No financial license required"
   - Add in-app disclaimer if no license: "This app does not provide financial advice. Consult a qualified financial advisor."
   - For IAP/subscriptions: App Dashboard → Monetization setup → Products
     - Subscription terms must be visible before user subscribes
     - Cancellation instructions must be accessible from app settings

   **AI-generated content declaration** (only if answered yes above)
   - Navigation: App Dashboard → Policy → App content → AI-generated content
   - Check content types: Text / Images / Audio / Video (select all that apply)
   - Describe moderation approach: automated filtering, human review, user reporting, output guardrails
   - Confirm in-app disclosure: label or note on AI-generated content visible to users

   **Families / children policy** (only if answered yes above)
   - Navigation: App Dashboard → Policy → App content → Target audience and content
   - Select "Designed for children" or "Mixed audience"
   - Additional requirements: no interest-based advertising, compliant third-party SDKs only

   **Developer identity verification** (applies to ${user_config.country} accounts)
   - Navigation: Play Console → Settings → Developer account → Identity verification
   - Individual: government-issued ID matching Google account name
   - Organization: D-U-N-S number + business registration document

4. Output as a ready-to-copy checklist with Play Console navigation paths for each item, formatted as:

```
DECLARATIONS CHECKLIST
─────────────────────────────────
App: [package name] | [category]

☐ DATA SAFETY SECTION
  Path: App Dashboard → Policy → App content → Data safety
  - [ ] Declared data types: [list based on permissions]
  - [ ] Encryption in transit: yes/no declared
  - [ ] Data deletion: user can request yes/no declared

[additional sections only if applicable — financial, AI, families, identity]

NEXT STEPS:
1. Complete each item above in Play Console
2. Run /playcraft:aso-audit before submitting
3. Confirm release notes are written (/playcraft:release-notes)
```
