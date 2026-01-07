# 🔐 API Configuration Guide

Complete guide for setting up API keys for all supported video generation models.

## 📋 Overview

The AI Video Generator supports 14 different models from 6 providers. You don't need all API keys - just get keys for the models you want to use.

### Minimum Setup (Recommended for Testing)
- **Replicate API Key** - Enables 8 models (all Flux + SVD models + Pony SVD)
- Cost: Free tier available, then pay-as-you-go
- Setup time: 2 minutes

### Full Setup (All 14 Models)
- All 6 API keys configured
- Maximum flexibility and options

## 🚀 Quick Setup: Replicate Only

Perfect for getting started quickly!

### 1. Create Replicate Account
1. Visit: https://replicate.com
2. Click "Sign up"
3. Use GitHub or email to create account
4. Verify your email

### 2. Get API Token
1. Go to: https://replicate.com/account/api-tokens
2. Click "Create token"
3. Copy the token (starts with `r8_`)
4. Save it securely

### 3. Add to Streamlit Cloud
1. In your Streamlit Cloud app settings
2. Click "Secrets"
3. Add:
   ```toml
   REPLICATE_API_KEY = "r8_your_token_here"
   ```
4. Save

### 4. Add for Local Development
1. Copy `.streamlit/secrets.toml.template` to `.streamlit/secrets.toml`
2. Edit and add:
   ```toml
   REPLICATE_API_KEY = "r8_your_token_here"
   ```
3. Save

### 5. Models You Can Use
With just Replicate, you can use:
- Flux.1-schnell + SVD ✓
- Flux.1-dev + SVD ✓
- Flux.1-pro + SVD ✓
- Flux.1.1-pro + SVD ✓
- Flux.2 + SVD ✓
- Flux.2-max + SVD ✓
- Flux Kontext + SVD ✓
- Pony-like (Stable Video Diffusion) ✓

## 🎬 Full Setup: All Providers

### Provider 1: OpenAI (Sora)

**What it enables:** Sora model - Highest quality, most realistic videos

#### Steps:
1. **Create Account**
   - Visit: https://platform.openai.com
   - Sign up with email or Google
   - Verify email

2. **Add Credits**
   - Go to: https://platform.openai.com/account/billing
   - Add payment method
   - Add credits ($10+ recommended)

3. **Get API Key**
   - Visit: https://platform.openai.com/api-keys
   - Click "Create new secret key"
   - Name it (e.g., "video-generator")
   - Copy the key (starts with `sk-`)
   - **Important:** Save immediately, you can't see it again!

4. **Add to App**
   ```toml
   OPENAI_API_KEY = "sk-your-key-here"
   ```

**Cost:** ~$2-5 per video (varies by duration and resolution)

---

### Provider 2: Runway ML (Gen-3 Alpha Turbo)

**What it enables:** Runway Gen-3 Alpha Turbo - Fast professional video generation

#### Steps:
1. **Create Account**
   - Visit: https://runwayml.com
   - Click "Sign up"
   - Use email or Google

2. **Subscribe to Plan**
   - Go to: https://runwayml.com/pricing
   - Choose a plan (Standard or Pro)
   - Enter payment details

3. **Get API Key**
   - Go to: https://app.runwayml.com/settings
   - Click "API Keys" tab
   - Generate new key
   - Copy and save

4. **Add to App**
   ```toml
   RUNWAY_API_KEY = "your-runway-key-here"
   ```

**Cost:** ~$0.75-1.50 per video

---

### Provider 3: Luma Labs (Dream Machine)

**What it enables:** Luma Dream Machine (Ray-2) - Cinematic video generation

#### Steps:
1. **Create Account**
   - Visit: https://lumalabs.ai
   - Click "Get started"
   - Sign up with email

2. **Verify and Setup**
   - Verify email
   - Complete profile
   - Go to account settings

3. **Get API Key**
   - Navigate to: https://lumalabs.ai/account/api
   - Click "Create API key"
   - Copy the key

4. **Add Credits**
   - Go to billing section
   - Add payment method
   - Purchase credits

5. **Add to App**
   ```toml
   LUMA_API_KEY = "luma-your-key-here"
   ```

**Cost:** ~$0.50-1.00 per video

---

### Provider 4: Wavespeed (Kling & Pika)

**What it enables:** 
- Kling AI (ByteDance's model)
- Pika Labs (Creative transformations)

#### Steps:
1. **Create Account**
   - Visit: https://wavespeed.ai
   - Sign up for account
   - Verify email

2. **Choose Plan**
   - Select subscription tier
   - Add payment method

3. **Get API Key**
   - Go to API section
   - Generate new token
   - Copy and save

4. **Add to App**
   ```toml
   WAVESPEED_API_KEY = "ws-your-key-here"
   ```

**Cost:** Varies by plan (~$0.30-0.80 per video)

**Note:** Wavespeed is a unified API for multiple models. One key gives you access to both Kling and Pika.

---

### Provider 5: Replicate

**What it enables:**
- All 7 Flux + SVD model combinations
- Pony-like Stable Video Diffusion
- Total: 8 models

#### Steps:
See "Quick Setup: Replicate Only" section above.

---

### Provider 6: Vidu AI (Pollo.ai)

**What it enables:** Vidu AI - Advanced video synthesis

#### Steps:
1. **Create Account**
   - Visit: https://pollo.ai
   - Sign up with email
   - Verify account

2. **Get API Access**
   - Go to: https://pollo.ai/account/api
   - Generate API key
   - Copy the key

3. **Add Credits**
   - Navigate to billing
   - Add payment method
   - Purchase credits

4. **Add to App**
   ```toml
   VIDU_API_KEY = "vidu-your-key-here"
   ```

**Cost:** ~$0.40-0.90 per video

---

## 📝 Complete Configuration Files

### For Streamlit Cloud

In your app's Secrets section:

```toml
# Required for Flux models (8 models total)
REPLICATE_API_KEY = "r8_your_replicate_token"

# Optional: Add only the ones you need
OPENAI_API_KEY = "sk-your_openai_key"
RUNWAY_API_KEY = "your_runway_key"
LUMA_API_KEY = "your_luma_key"
WAVESPEED_API_KEY = "your_wavespeed_key"
VIDU_API_KEY = "your_vidu_key"
```

### For Local Development

File: `.streamlit/secrets.toml`

```toml
# Replicate (Required for Flux models)
REPLICATE_API_KEY = "r8_your_replicate_token"

# OpenAI (Optional - for Sora)
OPENAI_API_KEY = "sk-your_openai_key"

# Runway ML (Optional - for Gen-3)
RUNWAY_API_KEY = "your_runway_key"

# Luma Labs (Optional - for Dream Machine)
LUMA_API_KEY = "your_luma_key"

# Wavespeed (Optional - for Kling & Pika)
WAVESPEED_API_KEY = "your_wavespeed_key"

# Vidu AI (Optional - for Vidu)
VIDU_API_KEY = "your_vidu_key"
```

## 🔒 Security Best Practices

### Do's ✅
- Store keys in `.streamlit/secrets.toml` (local)
- Use Streamlit Cloud secrets (production)
- Keep keys confidential
- Rotate keys periodically
- Use different keys for dev/prod
- Monitor usage and costs
- Set spending limits where available

### Don'ts ❌
- Never commit secrets to Git
- Don't share keys publicly
- Don't hardcode in source files
- Don't store in plain text files in repo
- Don't use production keys for testing
- Don't share screenshots with keys visible

## 💡 Tips

### Testing on a Budget
1. Start with Replicate only (free tier)
2. Use Flux.1-schnell (fastest, cheapest)
3. Test with short durations (5-10 seconds)
4. Use 720p resolution
5. Monitor costs closely

### Cost Optimization
- Use Flux.1-schnell for testing
- Generate at 720p when possible
- Start with shorter durations
- Only add API keys for models you'll actually use
- Set up billing alerts on provider platforms

### Multi-Environment Setup

**Development:**
```toml
# .streamlit/secrets.toml
REPLICATE_API_KEY = "r8_dev_token"
```

**Production (Streamlit Cloud):**
```toml
# App secrets
REPLICATE_API_KEY = "r8_prod_token"
OPENAI_API_KEY = "sk-prod-key"
RUNWAY_API_KEY = "prod_runway_key"
# ... etc
```

## 🆘 Troubleshooting

### Key Not Working
1. Check for typos (copy-paste recommended)
2. Verify key is active on provider's website
3. Check if key has expired
4. Ensure you have credits/active subscription
5. Check for proper TOML syntax

### Key Not Found
1. Verify file location (`.streamlit/secrets.toml`)
2. Check key name matches exactly (case-sensitive)
3. Restart Streamlit app after adding keys
4. For cloud: check secrets in app settings

### Invalid Key Error
1. Regenerate key on provider's site
2. Copy entire key including prefix
3. Check for extra spaces or line breaks
4. Verify account is in good standing

## 📞 Provider Support

If you have issues getting API keys:

- **OpenAI:** https://help.openai.com
- **Runway:** https://support.runwayml.com
- **Luma:** https://lumalabs.ai/support
- **Wavespeed:** Contact via website
- **Replicate:** https://replicate.com/docs/get-started
- **Vidu/Pollo:** https://pollo.ai/support

## ✅ Verification Checklist

Before generating videos:

- [ ] At least one API key configured
- [ ] Keys added to correct location (secrets.toml or Cloud secrets)
- [ ] No syntax errors in TOML file
- [ ] App restarted after adding keys
- [ ] Credits/subscription active on provider
- [ ] Status shows "✅ Configured" in app sidebar

---

**Ready to generate! 🎬**

Once your keys are configured, head to the app and start creating amazing AI videos!
