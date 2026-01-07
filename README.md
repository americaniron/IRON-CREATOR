# 🎬 AI Video Generation Studio

A comprehensive Streamlit-based web application for generating videos using multiple state-of-the-art AI models. Create stunning videos from text prompts with an easy-to-use interface.

## ✨ Features

- **14 AI Models**: Support for Sora, Runway, Luma, Kling, Pika, Vidu, and multiple Flux variants
- **Easy-to-Use Interface**: Simple dropdown model selection, text prompt input, and customizable settings
- **Flexible Configuration**: 
  - Duration slider (5-60 seconds, default 10s)
  - Resolution selection (720p or 1080p)
- **Async Generation**: Automatic polling with status updates every 10 seconds
- **Video Preview**: Embedded video player for instant viewing
- **Download Support**: Direct download links for generated videos
- **Error Handling**: Clear error messages for failed generations

## 🤖 Supported Models

1. **Sora (OpenAI)** - State-of-the-art video generation
2. **Runway Gen-3 Alpha Turbo** - Fast, high-quality videos
3. **Luma Dream Machine (Ray-2)** - Dream-like, artistic videos
4. **Kling AI** - Advanced AI video synthesis
5. **Pika Labs** - Creative video generation
6. **Vidu AI** - High-quality text-to-video
7. **Pony-like (Stable Video Diffusion)** - Image-to-video using SVD
8. **Flux.1-schnell + SVD** - Fast Flux image → video pipeline
9. **Flux.1-dev + SVD** - Development Flux → video pipeline
10. **Flux.1-pro + SVD** - Professional Flux → video pipeline
11. **Flux.1.1-pro + SVD** - Enhanced pro Flux → video pipeline
12. **Flux.2 + SVD** - Latest Flux → video pipeline
13. **Flux.2-max + SVD** - Maximum quality Flux → video pipeline
14. **Flux Kontext + SVD** - Context-aware Flux → video pipeline

## 🚀 Quick Start - Run Locally

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/americaniron/IRON-CREATOR.git
   cd IRON-CREATOR
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys**
   
   Create a file `.streamlit/secrets.toml` with your API keys:
   ```toml
   OPENAI_API_KEY = "your-openai-api-key"
   RUNWAY_API_KEY = "your-runway-api-key"
   LUMA_API_KEY = "your-luma-api-key"
   REPLICATE_API_TOKEN = "your-replicate-api-token"
   VIDU_API_KEY = "your-vidu-api-key"
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   
   The app will automatically open at `http://localhost:8501`

## 🔑 Getting API Keys

### OpenAI (for Sora)
1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to API keys section
4. Create a new API key
5. **Note**: Sora access may be limited and require waitlist approval

### Runway ML
1. Visit https://runwayml.com/
2. Create an account
3. Go to your account settings
4. Generate an API key in the API section

### Luma Labs (Dream Machine)
1. Go to https://lumalabs.ai/
2. Sign up for an account
3. Access your API dashboard
4. Generate an API token

### Replicate (for Flux models, SVD, Kling, Pika)
1. Visit https://replicate.com/
2. Sign up or log in
3. Go to https://replicate.com/account/api-tokens
4. Create a new API token
5. **Note**: Most models use Replicate, so this is the most important key

### Vidu AI
1. Go to https://pollo.ai/
2. Create an account
3. Navigate to API settings
4. Generate your API key

## ☁️ Deploy to Streamlit Community Cloud

### Step 1: Fork the Repository
1. Click the "Fork" button at the top right of this repository
2. This creates a copy in your GitHub account

### Step 2: Deploy on Streamlit Cloud
1. Go to https://share.streamlit.io/
2. Sign in with your GitHub account
3. Click "New app"
4. Select:
   - Repository: `your-username/IRON-CREATOR`
   - Branch: `main` (or `copilot/build-streamlit-video-app`)
   - Main file path: `app.py`
5. Click "Deploy"

### Step 3: Configure Secrets
1. In the Streamlit Cloud dashboard, go to your app settings
2. Navigate to the "Secrets" section
3. Add your API keys in TOML format:
   ```toml
   OPENAI_API_KEY = "your-openai-api-key"
   RUNWAY_API_KEY = "your-runway-api-key"
   LUMA_API_KEY = "your-luma-api-key"
   REPLICATE_API_TOKEN = "your-replicate-api-token"
   VIDU_API_KEY = "your-vidu-api-key"
   ```
4. Save the secrets

### Step 4: Access Your App
- Your app will be available at: `https://share.streamlit.io/your-username/IRON-CREATOR/main/app.py`
- Share this URL with anyone to let them generate videos!

## 💡 Usage Tips

1. **Be Specific**: Provide detailed descriptions in your prompts for better results
2. **Start Small**: Begin with shorter durations (10-15 seconds) to test
3. **Model Selection**: Different models excel at different content types
   - Sora: Realistic, coherent videos
   - Runway: Fast generation, good for prototyping
   - Luma: Artistic, dream-like content
   - Flux + SVD: Great for stylized, consistent videos
4. **Resolution**: Start with 720p for faster generation, use 1080p for final output
5. **API Credits**: Be mindful that video generation consumes API credits

## 🔧 Technical Details

### Flux + SVD Pipeline
For Flux models, the app uses a two-step process:
1. **Image Generation**: Generate an image using the selected Flux model variant
2. **Video Synthesis**: Convert the image to video using Stable Video Diffusion

This approach provides:
- High-quality, consistent frames
- Better control over visual style
- Reliable video output

### Polling Mechanism
- The app polls APIs every 10 seconds during video generation
- Status updates are displayed in real-time
- Videos are automatically displayed when ready

## 📋 Project Structure

```
IRON-CREATOR/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                # This file
├── .streamlit/
│   └── secrets.toml         # API keys (create this locally)
└── .gitignore              # Git ignore rules
```

## 🐛 Troubleshooting

### "API key not found" error
- Ensure your secrets are properly configured in `.streamlit/secrets.toml` (local) or Streamlit Cloud secrets
- Check that key names match exactly (case-sensitive)

### Video generation fails
- Verify your API keys are valid and have sufficient credits
- Check your internet connection
- Some models may have rate limits or require special access

### Module not found error
- Run `pip install -r requirements.txt` to ensure all dependencies are installed
- Use a virtual environment to avoid conflicts

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Add support for more AI models
- Improve documentation

## 📄 License

This project is open source and available for educational and commercial use.

## ⚠️ Disclaimer

- This app requires valid API keys for each service
- Video generation consumes API credits from respective providers
- Some models may have usage restrictions or require approval
- Generated content should comply with each provider's terms of service

## 🔗 Links

- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API](https://platform.openai.com/docs/api-reference)
- [Replicate Documentation](https://replicate.com/docs)
- [Runway ML](https://runwayml.com/)
- [Luma Labs](https://lumalabs.ai/)

---

Made with ❤️ using Streamlit | Support for 14+ AI video models
