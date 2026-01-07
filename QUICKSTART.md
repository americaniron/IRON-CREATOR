# 🎯 Quick Start Guide for AI Video Generator

This guide will help you get started with the AI Video Generator app quickly.

## 📋 Prerequisites

Before you begin, make sure you have:
- Python 3.9 or higher installed
- A GitHub account
- API keys for at least one video generation service

## 🚀 Option 1: Deploy to Streamlit Cloud (Recommended)

The fastest way to get started - no local setup required!

### Step-by-Step:

1. **Fork this repository**
   - Go to: https://github.com/americaniron/IRON-CREATOR
   - Click the "Fork" button in the top right
   - Wait for the fork to complete

2. **Get your API keys**
   - At minimum, get a Replicate API key (free tier available): https://replicate.com/account/api-tokens
   - Optionally, get keys for other services (see API Keys section in README_STREAMLIT.md)

3. **Deploy to Streamlit Cloud**
   - Visit: https://share.streamlit.io
   - Click "Sign in" and authorize with GitHub
   - Click "New app"
   - Select your forked repository
   - Branch: `main` or `copilot/build-streamlit-ai-video-app`
   - Main file path: `app.py`
   - Click "Advanced settings"
   - In the "Secrets" section, add:
     ```toml
     REPLICATE_API_KEY = "your-replicate-token-here"
     ```
   - Click "Deploy"

4. **Wait for deployment**
   - First deployment takes 2-3 minutes
   - You'll get a URL like: `https://your-app-name.streamlit.app`

5. **Start generating videos!**
   - Open your app URL
   - Select "Flux.1-schnell + SVD" (works with just Replicate key)
   - Enter a prompt like "A sunset over mountains"
   - Set duration to 10 seconds
   - Choose 720p resolution
   - Click "Generate Video"
   - Wait 2-5 minutes for generation

## 💻 Option 2: Run Locally

Perfect for development and testing.

### Step-by-Step:

1. **Clone the repository**
   ```bash
   git clone https://github.com/americaniron/IRON-CREATOR.git
   cd IRON-CREATOR
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure secrets**
   ```bash
   cp .streamlit/secrets.toml.template .streamlit/secrets.toml
   ```
   
   Edit `.streamlit/secrets.toml` and add your API keys:
   ```toml
   REPLICATE_API_KEY = "your-replicate-token-here"
   # Add other keys as needed
   ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

6. **Open in browser**
   - Automatically opens at: http://localhost:8501
   - Or manually visit that URL

## 🎨 Your First Video

Let's generate your first AI video!

### Example 1: Simple Scene (Fastest - 2-3 minutes)
- **Model**: Flux.1-schnell + SVD
- **Prompt**: "A peaceful lake surrounded by pine trees at sunrise"
- **Duration**: 10 seconds
- **Resolution**: 720p
- **Click**: Generate Video

### Example 2: Action Scene (Medium - 3-5 minutes)
- **Model**: Luma Dream Machine (Ray-2) [requires Luma API key]
- **Prompt**: "A sports car racing through a neon-lit city at night, cinematic"
- **Duration**: 15 seconds
- **Resolution**: 1080p
- **Click**: Generate Video

### Example 3: Abstract/Artistic (Medium - 3-5 minutes)
- **Model**: Flux.1-dev + SVD
- **Prompt**: "Swirling galaxy of colors and light, abstract art style"
- **Duration**: 20 seconds
- **Resolution**: 720p
- **Click**: Generate Video

## 📱 Using the Interface

### Model Selection
- **Dropdown menu** at the top
- 14 models to choose from
- Each model has different strengths:
  - **Sora**: Highest quality, most realistic
  - **Runway**: Fast, professional results
  - **Luma**: Cinematic, smooth motion
  - **Flux + SVD**: Good for creative/artistic styles
  - **Kling/Pika**: Specialized effects

### Prompt Writing Tips
- Be specific and descriptive
- Include style keywords: "cinematic", "photorealistic", "artistic"
- Mention camera movements: "slow zoom in", "panning shot"
- Describe lighting: "golden hour", "studio lighting", "neon lights"
- Add mood: "peaceful", "energetic", "mysterious"

### Duration Selection
- **5-10 seconds**: Quick tests, faster generation
- **10-20 seconds**: Standard clips
- **20-60 seconds**: Longer sequences (takes more time)

### Resolution
- **720p**: Faster generation, smaller file size
- **1080p**: Higher quality, larger file size

## ⏱️ Generation Times

Typical wait times per model:
- **Flux + SVD**: 2-5 minutes
- **Luma Dream Machine**: 3-7 minutes
- **Runway Gen-3**: 2-4 minutes
- **Sora**: 5-10 minutes
- **Kling/Pika**: 4-8 minutes
- **Vidu**: 3-6 minutes

*Times vary based on server load and video length*

## 💰 API Costs

Approximate costs (as of 2024):
- **Replicate (Flux + SVD)**: ~$0.10-0.30 per video
- **Luma**: ~$0.50-1.00 per video
- **Runway**: ~$0.75-1.50 per video
- **OpenAI Sora**: ~$2.00-5.00 per video

*Check each provider's pricing page for current rates*

## ❓ Troubleshooting

### "API key not found"
- Check your secrets configuration
- Make sure key name matches exactly (case-sensitive)
- Verify the key is valid on the provider's website

### "Generation failed"
- Check your API credits/balance
- Try a shorter duration
- Try a simpler prompt
- Wait a moment and try again (rate limit)

### App is slow/frozen
- Video generation takes time - be patient!
- Check the spinner for status updates
- Don't refresh the page during generation

### Video won't play
- Try downloading the video
- Check if the URL is accessible
- Try a different browser
- Some formats may need VLC or other players

## 🎓 Advanced Usage

### Chaining Generations
1. Generate an image with Flux
2. Use that image in another model
3. Create variations and sequences

### Batch Generation
1. Generate multiple videos with different prompts
2. Compare results across models
3. Mix and match for best results

### Custom Workflows
1. Start with specific model for style
2. Refine with another model
3. Export and edit in video software

## 📚 Next Steps

- Explore all 14 models
- Try different prompt styles
- Experiment with durations and resolutions
- Share your creations!
- Contribute to the project on GitHub

## 🆘 Need Help?

- Read the full README: `README_STREAMLIT.md`
- Check API provider documentation
- Open an issue on GitHub
- Review example prompts above

---

**Happy generating! 🎬✨**
