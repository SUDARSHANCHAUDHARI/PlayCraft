---
name: developer-identity-th
description: Developer identity verification for Thailand-based Google Play developers
trigger: when setting up Play Console account or verifying developer identity
---

## Developer identity verification — Thailand

### Individual developer account

**Required documents:**
- Thai national ID card (บัตรประชาชน) — front and back
- The name on the ID must match the name on your Google account
- Verification is done via Google's identity verification flow in Play Console

**Navigation:** Play Console → Settings → Developer account → Identity verification

**Process:**
1. Play Console will prompt you to start verification — or navigate there directly
2. Select "Individual" account type
3. Follow the document upload flow (photo of ID front + back, possibly a selfie)
4. Google reviews within 1–3 business days
5. You receive confirmation by email

### Organization / company account

**Required:**
- D-U-N-S number (Dun & Bradstreet) — apply free at dnb.com, takes 5–30 business days
  - Use the exact company name and registered address as it appears on your DBD documents
  - Expedite requests are available (fee may apply) if you need faster verification
- Business registration document from the Thai Department of Business Development (DBD)
  - DBD Online: dbdregis.dbd.go.th — download your company's certificate of incorporation (หนังสือรับรอง)
  - The document must be current (issued within 12 months) and show your company name in both Thai and English if possible

**Navigation:** Play Console → Settings → Developer account → Organization verification

### Payments setup (Thailand)

- Thai bank accounts are supported — set up in Play Console → Payments profile
- Currency: Google pays in USD, converted to THB by Google at market rate
- Minimum payout threshold: $1 USD equivalent

**Tax information:**
- Thai developers (individual or company) must complete the W-8BEN form (for individuals) or W-8BEN-E form (for organizations)
- Select: "I am not a US person"
- This reduces or eliminates US withholding tax on your Google Play earnings
- Navigate to: Play Console → Payments profile → Tax information → Manage tax info

**VAT:**
- Google collects VAT in Thailand on app purchases (7%)
- If your company is VAT-registered, enter your VAT registration number in Play Console → Payments profile → Business info
- If not VAT-registered, Google handles the VAT collection — no action required

### Common issues in Thailand

- **D-U-N-S application**: The address on the application must exactly match the registered address on your DBD certificate — any mismatch causes delays
- **Bank account name**: Must match the name of the Play Console account holder or company name exactly
- **W-8BEN not filed**: Without tax information, Google withholds 30% of earnings — file as soon as your account is created
- **DBD certificate language**: If your certificate is in Thai only, the English transliteration Google receives may differ from your English company name — consider registering an English company name with DBD if you haven't already
