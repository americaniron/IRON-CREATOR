# 🎬 AI Video Generator

A powerful Streamlit web application for generating AI videos using state-of-the-art models including Sora, Runway, Luma, Kling, Pika Labs, and more.

![AI Video Generator](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)

## ✨ Features

- **14 AI Video Models**: Choose from multiple cutting-edge AI video generation models
- **Intuitive Interface**: Easy-to-use UI with model selection, prompt input, and parameter controls
- **Flexible Settings**: 
  - Duration: 5-60 seconds (default: 10s)
  - Resolution: 720p or 1080p
- **Async Generation**: Handles API calls with automatic polling
- **Video Preview**: Watch generated videos directly in the app
- **Download Support**: Direct download links for all generated videos
- **Error Handling**: Clear error messages and status updates

## 🎨 Supported Models

1. **Sora (OpenAI)** - OpenAI's latest video generation model
2. **Runway Gen-3 Alpha Turbo** - Fast and high-quality video generation
3. **Luma Dream Machine (Ray-2)** - Cinematic video generation
4. **Kling AI** - ByteDance's video generation model
5. **Pika Labs** - Creative video transformations
6. **Vidu AI** - Advanced video synthesis
7. **Pony-like (Stable Video Diffusion)** - Open-source video generation
8. **Flux.1-schnell + SVD** - Fast image-to-video pipeline
9. **Flux.1-dev + SVD** - Development image-to-video pipeline
10. **Flux.1-pro + SVD** - Professional image-to-video pipeline
11. **Flux.1.1-pro + SVD** - Enhanced professional pipeline
12. **Flux.2 + SVD** - Latest Flux with video generation
13. **Flux.2-max + SVD** - Maximum quality Flux pipeline
14. **Flux Kontext + SVD** - Context-aware video generation

## 🚀 Quick Start

**New to the app?** Check out our guides:
- 📖 [Quick Start Guide](QUICKSTART.md) - Get your first video in 5 minutes
- 🔐 [API Configuration Guide](API_SETUP.md) - Detailed setup for all providers

### Prerequisites

- Python 3.9 or higher
- API keys for the models you want to use (see [API Keys](#-api-keys))

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/americaniron/IRON-CREATOR.git
   cd IRON-CREATOR
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys**
   
   Copy the secrets template:
   ```bash
   cp .streamlit/secrets.toml.template .streamlit/secrets.toml
   ```
   
   Edit `.streamlit/secrets.toml` and add your API keys:
   ```toml
   OPENAI_API_KEY = "your-openai-key"
   RUNWAY_API_KEY = "your-runway-key"
   LUMA_API_KEY = "your-luma-key"
   WAVESPEED_API_KEY = "your-wavespeed-key"
   REPLICATE_API_KEY = "your-replicate-key"
   VIDU_API_KEY = "your-vidu-key"
   ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser** to `http://localhost:8501`

## 🔑 API Keys

You'll need API keys for the models you want to use. Here's how to get them:

### OpenAI (Sora)
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Navigate to API Keys section
4. Create a new API key
5. Copy and save the key securely

### Runway ML
1. Visit [Runway ML](https://runwayml.com/)
2. Sign up for an account
3. Go to your account settings
4. Generate an API key
5. Copy the key

### Luma Labs (Dream Machine)
1. Visit [Luma Labs](https://lumalabs.ai/)
2. Create an account
3. Access your API settings
4. Generate an API key
5. Save the key

### Wavespeed (Kling AI & Pika Labs)
1. Visit [Wavespeed](https://wavespeed.ai/)
2. Sign up for an account
3. Navigate to API section
4. Create an API token
5. Copy the token

### Replicate (Flux & SVD models)
1. Visit [Replicate](https://replicate.com/account/api-tokens)
2. Sign in with GitHub
3. Create an API token
4. Copy the token
5. Note: This is used for Flux models and Stable Video Diffusion

### Vidu AI
1. Visit [Pollo AI](https://pollo.ai/)
2. Create an account
3. Access API settings
4. Generate your API key
5. Save the key securely

## ☁️ Deploy to Streamlit Cloud

Deploy your own instance of the AI Video Generator to Streamlit Cloud for free!

### Deployment Steps

1. **Fork this repository**
   - Click the "Fork" button at the top right of this page
   - This creates your own copy of the repository

2. **Sign in to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

3. **Deploy the app**
   - Click "New app"
   - Select your forked repository
   - Set the main file path: `app.py`
   - Click "Deploy"

4. **Configure secrets**
   - In your deployed app's settings, go to "Secrets"
   - Add your API keys in TOML format:
   ```toml
   OPENAI_API_KEY = "your-openai-key"
   RUNWAY_API_KEY = "your-runway-key"
   LUMA_API_KEY = "your-luma-key"
   WAVESPEED_API_KEY = "your-wavespeed-key"
   REPLICATE_API_KEY = "your-replicate-key"
   VIDU_API_KEY = "your-vidu-key"
   ```
   - Save the secrets

5. **Access your app**
   - Your app will be available at: `https://your-app-name.streamlit.app`
   - Share the URL with others!

### Important Notes

- **API Costs**: Each video generation uses your API credits. Monitor your usage on each platform.
- **Rate Limits**: Different APIs have different rate limits. The app handles polling automatically.
- **Secrets Security**: Never commit API keys to your repository. Always use Streamlit secrets.

## 📖 Usage Guide

1. **Select a Model**: Choose from the dropdown menu of 14 AI video models
2. **Enter a Prompt**: Describe the video you want to generate
3. **Set Duration**: Use the slider to choose video length (5-60 seconds)
4. **Choose Resolution**: Select 720p or 1080p
5. **Generate**: Click the "Generate Video" button
6. **Wait**: The app will poll the API until your video is ready
7. **Watch & Download**: View your video and download it

### Example Prompts

- "A serene sunset over a calm ocean with waves gently lapping the shore"
- "A futuristic city with flying cars and neon lights at night"
- "A timelapse of flowers blooming in a spring garden"
- "An astronaut floating in space with Earth in the background"
- "A cozy coffee shop with people reading and working on laptops"

## 🛠️ Technical Details

### Architecture

- **Frontend**: Streamlit web framework
- **Backend**: Python with async API calls
- **Video Generation**: Multiple AI model APIs
- **Polling**: Automatic status checking every 10 seconds
- **Caching**: Streamlit's caching for optimal performance

### Models Implementation

- **Direct API models**: Sora, Runway, Luma, Vidu
- **Wavespeed models**: Kling AI, Pika Labs
- **Replicate models**: Flux series, SVD
- **Hybrid approach**: Flux models generate image → SVD converts to video

### Error Handling

- Missing API key detection
- API error messages
- Failed generation alerts
- Network timeout handling

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🐛 Troubleshooting

**Need help?** See our comprehensive guides:
- 📖 [Quick Start Guide](QUICKSTART.md) - Common setup issues
- 🔐 [API Configuration Guide](API_SETUP.md) - API key problems

### Common Issues

**"API key not found" error**
- Make sure you've configured your secrets correctly
- Check that the API key is valid and active
- Verify the key name matches exactly (case-sensitive)

**Video generation fails**
- Check your API credits/balance
- Verify the API endpoint is accessible
- Try with a different model
- Check for rate limiting

**App won't start locally**
- Ensure Python 3.9+ is installed
- Verify all dependencies are installed (`pip install -r requirements.txt`)
- Check that port 8501 is not in use

**Slow generation times**
- This is normal - AI video generation takes time (typically 2-10 minutes)
- The app automatically polls every 10 seconds
- Don't refresh the page while generating

## 💡 Tips

- Start with shorter durations (5-10 seconds) for faster results
- Be specific and detailed in your prompts for better results
- Try different models for different styles and effects
- Monitor your API usage to avoid unexpected costs
- Use 720p for faster generation, 1080p for higher quality

## 🔗 Links

- [GitHub Repository](https://github.com/americaniron/IRON-CREATOR)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Report Issues](https://github.com/americaniron/IRON-CREATOR/issues)

## 📧 Support

If you have questions or need help:
- Open an issue on GitHub
- Check the troubleshooting section
- Review API provider documentation

---

**Built with ❤️ using Streamlit and cutting-edge AI models**

⭐ Star this repo if you find it useful!
