---
name: financial-declarations
description: How to complete financial features declarations on Google Play
trigger: when app involves payments, financial data, banking, crypto, or subscriptions
---

## Financial features declaration — step by step

### When required
Declare if your app:
- Offers financial products (loans, investments, insurance, banking features)
- Provides cryptocurrency features (wallets, trading, price tracking)
- Shows stock prices, exchange rates, or financial advice
- Mentions savings, credit, debt, or financial planning
- Has in-app purchases or subscriptions (separate declaration — see below)

Even informational apps (e.g., a currency converter or crypto price tracker) may require this declaration.

### Play Console navigation
App Dashboard → Policy → App content → Financial features

### Declaration fields

1. **Financial product type** — select all that apply:
   - Banking / payment
   - Investment / trading
   - Insurance
   - Cryptocurrency
   - Lending / credit / debt management

2. **License / registration** — if your app provides regulated financial services:
   - Upload a copy of the applicable financial license from your country's regulator
   - Thailand: Financial institution license from the Bank of Thailand (if offering regulated services)
   - Most utility apps that show financial data but do not offer services: select "No financial license required — app does not offer regulated financial services"

3. **Disclaimer** — if no license is required, add a disclaimer within the app:
   - Minimum required text: "This app does not provide financial advice. Consult a qualified financial advisor before making financial decisions."
   - This disclaimer should be visible in the app's settings or about screen, and referenced in the privacy policy

### IAP / Subscription declaration (separate from financial features)
Navigation: App Dashboard → Monetization setup → Products

Required for any app with:
- One-time in-app purchases (coins, features, content)
- Auto-renewing subscriptions

Requirements:
- Subscription terms (price, billing period, what is included) must be shown before the user subscribes
- Free trial terms must be visible before the user agrees — duration, what happens after trial ends
- Cancellation instructions must be accessible from within the app (e.g., in Settings → Subscription)
- Refund policy must be consistent with Google Play's refund policy

### Common mistakes
- Forgetting to declare when an app merely displays financial data (even read-only)
- Not updating the declaration after adding new financial features in an update
- Missing the subscription terms disclosure on the paywall screen
- Not including cancellation instructions in the app — this can trigger a policy strike
