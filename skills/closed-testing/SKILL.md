---
name: closed-testing
description: Google Play closed testing requirements for new developer accounts (2024–2026)
trigger: when setting up a new app, preparing for open testing, or when user asks about testing tracks
---

## Closed testing requirement (new accounts)

### Who this applies to
Personal developer accounts created after **November 2023** must complete closed testing before they can:
- Publish to open testing
- Publish to production

Organization accounts and older personal accounts are not subject to this requirement (but closed testing is still recommended best practice).

### What is required
- **12 or more testers** who must opt in to the closed test
- **14 continuous days** of active closed testing
- All 12 testers must have opted in and be active during the 14-day window

### Step-by-step setup in Play Console

1. **Create a closed testing track**
   - App Dashboard → Testing → Internal testing OR Closed testing
   - Use **Closed testing** (not Internal) — Internal testing does not count toward the requirement

2. **Create a tester group**
   - Closed testing → Testers tab → Create email list
   - Add at least 12 email addresses
   - Emails must be Google accounts

3. **Generate the opt-in link**
   - After publishing to closed track, Play Console shows an opt-in URL
   - Share this link with your testers — they must click it and install the app

4. **Wait 14 days**
   - The 14-day clock starts when the 12th tester opts in
   - If a tester drops out below 12, the clock resets
   - Monitor tester count in Play Console → Testing → Closed testing → Testers

5. **Check eligibility**
   - App Dashboard → Production → Countries/regions
   - If the requirement is met, the option to publish to production becomes available

### Finding testers
- Friends, family, or colleagues with Android phones
- Developer communities: Reddit r/androiddev, XDA Developers forums
- Beta testing communities: betabound.com, testingtime.com
- Post in relevant subreddits or Discord servers for your app's niche

### Common mistakes
- Using Internal testing instead of Closed testing — does not count
- Testers click the link but do not install — they must install and remain active
- Starting the count before all 12 have opted in
- Removing testers mid-period — keep at least 12 opted in for the full 14 days
