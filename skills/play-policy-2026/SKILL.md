---
name: play-policy-2026
description: Google Play Developer Policy key rules for 2025–2026 submissions
trigger: when working on Play Store submissions, store listings, or app publishing
---

## Critical Play Store rules (2025–2026)

### Metadata
- Title max 30 characters (enforced — submission rejected if exceeded)
- Short description max 80 characters
- Full description max 4000 characters
- No keyword stuffing — repeated keywords in title/description is a policy violation
- Icons and screenshots must accurately represent the app — no mockups of features that don't exist
- No "Download now" or CTAs in screenshot overlay text
- No emojis in the app title

### New requirements in 2025–2026
- AI-generated content must be declared in App Content → AI-generated content section
- Financial features declaration required for any app mentioning money, investments, banking, or crypto — even informational apps
- Closed testing with 12+ testers required for 14 days before open testing for new personal developer accounts (accounts registered after November 2023)
- Developer identity verification mandatory for all new accounts and prompted for many existing accounts
- Real-time location (background location) access requires prominent in-app disclosure and a separate permission
- Health Connect integration requires additional data safety declarations for each data type accessed

### Data Safety section (required for all apps)
Every app must complete the Data Safety form:
- Declare every data type collected — even analytics-only data (device identifiers, crash logs)
- Declare if data is shared with third parties (ad networks, analytics SDKs)
- Declare if data is encrypted in transit and at rest
- Declare if users can request data deletion
- Incomplete or inaccurate Data Safety = removal risk

### Rating system
- Use IARC rating questionnaire in Play Console — answer all questions honestly
- Wrong or missing rating = app removal
- Apps with violent, adult, or gambling content must be correctly rated
- Re-rate after adding new features that change content type

### Payments policy
- All in-app purchases for digital goods must use Google Play Billing
- No directing users to external payment for digital goods or subscriptions
- Physical goods and services are exempt (e.g., food delivery, ride-sharing, hotel booking)
- Free trials: terms must be shown before user subscribes; cancellation instructions must be accessible

### Sensitive permissions
- Camera: must state use clearly in listing and privacy policy
- Background location: requires prominent disclosure, cannot be bundled with foreground location request
- Contacts: cannot be collected without clear stated purpose
- READ_CALL_LOG / READ_SMS: restricted — only approved apps in specific categories may request these
