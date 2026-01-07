# 🎬 AI Video Generator - Application Structure

## Visual Layout

```
┌─────────────────────────────────────────────────────────────┐
│                  🎬 AI Video Generator                      │
│         Generate stunning videos using AI models            │
└─────────────────────────────────────────────────────────────┘

┌──────────────────┐  ┌──────────────────────────────────────┐
│   ⚙️ Settings    │  │  🎨 Generation Settings              │
├──────────────────┤  ├──────────────────────────────────────┤
│ API Key Status:  │  │ Select AI Model: ▼                   │
│ OpenAI:    ❌    │  │ ┌────────────────────────────────┐   │
│ Runway:    ❌    │  │ │ • Sora (OpenAI)                │   │
│ Luma:      ❌    │  │ │ • Runway Gen-3 Alpha Turbo     │   │
│ Wavespeed: ❌    │  │ │ • Luma Dream Machine (Ray-2)   │   │
│ Replicate: ✅    │  │ │ • Kling AI                     │   │
│ Vidu:      ❌    │  │ │ • Pika Labs                    │   │
├──────────────────┤  │ │ • ... (14 models total)        │   │
│ About            │  │ └────────────────────────────────┘   │
│ This app gen...  │  │                                      │
│                  │  │ Video Prompt:                        │
│ 📚 Documentation │  │ ┌────────────────────────────────┐   │
│ • Quick Start    │  │ │ Describe the video you want    │   │
│ • API Setup      │  │ │ to generate...                 │   │
│ • Example Prompts│  │ │                                │   │
└──────────────────┘  │ └────────────────────────────────┘   │
                      │                                      │
                      │  ⚙️ Video Parameters                │
                      │  Duration: ◀─────●─────▶ 10 seconds │
                      │  Resolution: ○ 720p  ● 1080p        │
                      │                                      │
                      │  ┌────────────────────────────────┐  │
                      │  │    🎬 Generate Video           │  │
                      │  └────────────────────────────────┘  │
                      └──────────────────────────────────────┘

After clicking "Generate Video":

┌─────────────────────────────────────────────────────────────┐
│  ⏳ Creating video with Flux.1-schnell + SVD...             │
│  ⏳ Processing video... This may take a few minutes.        │
└─────────────────────────────────────────────────────────────┘

When complete:

┌─────────────────────────────────────────────────────────────┐
│  ✅ Video generated successfully!                           │
│                                                             │
│  📹 Generated Video                                         │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                                                       │  │
│  │              [Video Player]                          │  │
│  │                                                       │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                             │
│  ⬇️ Download Video                                          │
│  Direct link: https://replicate.delivery/...               │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow Architecture

```
┌─────────────┐
│    User     │
│   (Browser) │
└──────┬──────┘
       │
       │ 1. Selects model & enters prompt
       ▼
┌─────────────────────┐
│  Streamlit App      │
│     (app.py)        │
├─────────────────────┤
│ • UI Components     │
│ • API Key Manager   │
│ • Video Generator   │
│ • Polling Logic     │
└──────┬──────────────┘
       │
       │ 2. API calls with credentials
       ▼
┌─────────────────────────────────────┐
│        AI Model APIs                │
├─────────────────────────────────────┤
│ OpenAI → Sora                       │
│ Runway → Gen-3 Alpha Turbo          │
│ Luma → Dream Machine                │
│ Wavespeed → Kling AI, Pika Labs     │
│ Replicate → Flux models, SVD        │
│ Vidu → Vidu AI                      │
└──────┬──────────────────────────────┘
       │
       │ 3. Returns task ID
       ▼
┌─────────────────────┐
│   Polling Loop      │
│  (every 10 seconds) │
└──────┬──────────────┘
       │
       │ 4. Check status
       │    ↻ Repeat until complete
       ▼
┌─────────────────────┐
│  Video URL Ready    │
└──────┬──────────────┘
       │
       │ 5. Display video
       ▼
┌─────────────┐
│    User     │
│  (Watches & │
│  Downloads) │
└─────────────┘
```

## Component Breakdown

### 1. Main Application (app.py)

```python
# Key Components:

1. Configuration
   - Page setup
   - Model definitions
   - API key management

2. Helper Functions
   - get_api_key()           # Retrieve API keys from secrets
   - generate_sora_video()   # Sora implementation
   - generate_runway_video() # Runway implementation
   - generate_luma_video()   # Luma implementation
   - generate_kling_video()  # Kling implementation
   - generate_pika_video()   # Pika implementation
   - generate_vidu_video()   # Vidu implementation
   - generate_flux_image()   # Flux image generation
   - generate_svd_video()    # SVD video conversion
   - generate_pony_svd_video() # Pony+SVD
   - generate_flux_svd_video() # Flux+SVD pipeline
   - generate_video()        # Main dispatcher

3. User Interface
   - Sidebar (API status, docs)
   - Main area (inputs, controls)
   - Video display section

4. Generation Logic
   - Model selection
   - Parameter validation
   - API calls
   - Polling loop
   - Result display
```

### 2. Model Integration Patterns

#### Pattern A: Direct API (Sora, Runway, Luma, Vidu)
```
1. Submit generation request
2. Receive task ID
3. Poll for status (every 10s)
4. Retrieve video URL
5. Display to user
```

#### Pattern B: Wavespeed (Kling, Pika)
```
1. Call wavespeed.run()
2. Pass model ID and params
3. Receive video URL
4. Display to user
```

#### Pattern C: Flux + SVD Pipeline
```
1. Generate image with Flux
2. Display generated image
3. Convert image to video with SVD
4. Display final video
```

### 3. Security Model

```
┌──────────────────┐
│  User's Browser  │
└────────┬─────────┘
         │
         │ HTTPS
         ▼
┌──────────────────┐
│ Streamlit Cloud  │
│   (App Host)     │
└────────┬─────────┘
         │
         │ Secrets Manager
         ▼
┌──────────────────┐
│   API Keys       │
│  (st.secrets)    │
└────────┬─────────┘
         │
         │ Encrypted calls
         ▼
┌──────────────────┐
│  External APIs   │
│ (OpenAI, etc.)   │
└──────────────────┘
```

**Key Security Features:**
- ✅ No API keys in source code
- ✅ Secrets via Streamlit secrets manager
- ✅ HTTPS for all communications
- ✅ No client-side key exposure
- ✅ Proper exception handling

### 4. Error Handling Flow

```
┌─────────────────┐
│ User Input      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌──────────────┐
│ Validation      │────→│ Show Warning │
└────────┬────────┘     └──────────────┘
         │ ✓
         ▼
┌─────────────────┐     ┌──────────────┐
│ API Key Check   │────→│ Show Error   │
└────────┬────────┘     └──────────────┘
         │ ✓
         ▼
┌─────────────────┐     ┌──────────────┐
│ API Call        │────→│ Show Error   │
└────────┬────────┘     └──────────────┘
         │ ✓
         ▼
┌─────────────────┐     ┌──────────────┐
│ Polling         │────→│ Show Error   │
└────────┬────────┘     └──────────────┘
         │ ✓
         ▼
┌─────────────────┐
│ Success!        │
└─────────────────┘
```

## File Dependencies

```
app.py
├── streamlit            # Web framework
├── openai               # Sora integration
├── requests             # HTTP calls (Runway, Luma, Vidu)
├── wavespeed            # Kling & Pika
├── replicate            # Flux & SVD models
└── time, os, typing     # Standard library

requirements.txt
├── streamlit>=1.28.0
├── openai>=1.3.0
├── requests>=2.31.0
├── replicate>=0.22.0
└── wavespeed>=0.1.0

.streamlit/secrets.toml (runtime)
├── OPENAI_API_KEY
├── RUNWAY_API_KEY
├── LUMA_API_KEY
├── WAVESPEED_API_KEY
├── REPLICATE_API_KEY
└── VIDU_API_KEY
```

## Deployment Architecture

```
┌───────────────────────────────────────────┐
│           GitHub Repository               │
│  (americaniron/IRON-CREATOR)              │
│                                           │
│  • app.py                                 │
│  • requirements.txt                       │
│  • Documentation                          │
└───────────────┬───────────────────────────┘
                │
                │ Auto-deploy
                ▼
┌───────────────────────────────────────────┐
│         Streamlit Cloud                   │
│                                           │
│  • Runs app.py                            │
│  • Installs requirements                  │
│  • Loads secrets                          │
│  • Serves on public URL                   │
│                                           │
│  URL: https://your-app.streamlit.app      │
└───────────────┬───────────────────────────┘
                │
                │ Users access
                ▼
┌───────────────────────────────────────────┐
│           Public Internet                 │
│  Anyone with URL can:                     │
│  • Select AI models                       │
│  • Generate videos                        │
│  • Download results                       │
└───────────────────────────────────────────┘
```

## Model Processing Times

```
Fast (2-3 min)
├── Flux.1-schnell + SVD  ⚡⚡⚡

Medium (3-5 min)
├── Luma Dream Machine    ⚡⚡
├── Runway Gen-3          ⚡⚡
├── Flux.1-dev + SVD      ⚡⚡

Slower (5-10 min)
├── Sora                  ⚡
├── Kling AI              ⚡
├── Pika Labs             ⚡
└── Vidu AI               ⚡
```

## Cost Structure

```
Budget Tier ($0.10-0.30 per video)
└── All Flux + SVD models

Standard Tier ($0.40-1.00 per video)
├── Luma Dream Machine
├── Runway Gen-3
└── Vidu AI

Premium Tier ($2.00-5.00 per video)
└── Sora (OpenAI)
```

## User Journey

```
1. Discover App
   └─→ Visit Streamlit URL or GitHub repo

2. Fork Repository (optional)
   └─→ Create own copy on GitHub

3. Get API Keys
   └─→ Sign up for providers
   └─→ Generate API tokens

4. Deploy
   ├─→ Streamlit Cloud (5 min)
   └─→ Local setup (15 min)

5. Configure Secrets
   └─→ Add API keys to secrets

6. Generate First Video
   └─→ Select model
   └─→ Enter prompt
   └─→ Click generate
   └─→ Wait 2-10 minutes
   └─→ Watch & download

7. Explore & Experiment
   └─→ Try different models
   └─→ Test various prompts
   └─→ Adjust parameters
   └─→ Share creations
```

---

**This structure enables a complete, production-ready AI video generation platform! 🚀**
