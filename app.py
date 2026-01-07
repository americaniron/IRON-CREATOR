import streamlit as st
import time
import requests
import openai
import replicate
from typing import Optional, Dict, Any
import os

# Page configuration
st.set_page_config(
    page_title="AI Video Generator",
    page_icon="🎬",
    layout="wide"
)

# Title and description
st.title("🎬 AI Video Generator")
st.markdown("Generate stunning videos using state-of-the-art AI models")

# Model options
MODELS = [
    "Sora (OpenAI)",
    "Runway Gen-3 Alpha Turbo",
    "Luma Dream Machine (Ray-2)",
    "Kling AI",
    "Pika Labs",
    "Vidu AI",
    "Pony-like (Stable Video Diffusion)",
    "Flux.1-schnell + SVD",
    "Flux.1-dev + SVD",
    "Flux.1-pro + SVD",
    "Flux.1.1-pro + SVD",
    "Flux.2 + SVD",
    "Flux.2-max + SVD",
    "Flux Kontext + SVD"
]

# Replicate model IDs for Flux models
FLUX_MODELS = {
    "Flux.1-schnell + SVD": "black-forest-labs/flux-schnell",
    "Flux.1-dev + SVD": "black-forest-labs/flux-dev",
    "Flux.1-pro + SVD": "black-forest-labs/flux-1.1-pro",
    "Flux.1.1-pro + SVD": "black-forest-labs/flux-1.1-pro",
    "Flux.2 + SVD": "black-forest-labs/flux-1.1-pro",
    "Flux.2-max + SVD": "black-forest-labs/flux-1.1-pro",
    "Flux Kontext + SVD": "black-forest-labs/flux-dev"
}

SVD_MODEL = "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438"


def get_api_key(service: str) -> Optional[str]:
    """Get API key from Streamlit secrets"""
    key_map = {
        "openai": "OPENAI_API_KEY",
        "runway": "RUNWAY_API_KEY",
        "luma": "LUMA_API_KEY",
        "wavespeed": "WAVESPEED_API_KEY",
        "replicate": "REPLICATE_API_KEY",
        "vidu": "VIDU_API_KEY"
    }
    
    try:
        return st.secrets.get(key_map.get(service, service))
    except:
        return os.environ.get(key_map.get(service, service))


def generate_sora_video(prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Generate video using OpenAI Sora"""
    try:
        api_key = get_api_key("openai")
        if not api_key:
            st.error("OpenAI API key not found. Please set OPENAI_API_KEY in secrets.")
            return None
        
        client = openai.OpenAI(api_key=api_key)
        
        # Map resolution
        size = "1280x720" if resolution == "720p" else "1920x1080"
        
        with st.spinner("Creating video with Sora..."):
            response = client.videos.create(
                model="sora-2-pro",
                prompt=prompt,
                duration=duration,
                size=size
            )
            
            video_id = response.id
            
            # Poll for completion
            with st.spinner("Processing video... This may take a few minutes."):
                while True:
                    status = client.videos.retrieve(video_id)
                    if status.status == "completed":
                        return status.url
                    elif status.status == "failed":
                        st.error(f"Video generation failed: {status.error}")
                        return None
                    time.sleep(10)
    except Exception as e:
        st.error(f"Error generating Sora video: {str(e)}")
        return None


def generate_runway_video(prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Generate video using Runway Gen-3"""
    try:
        api_key = get_api_key("runway")
        if not api_key:
            st.error("Runway API key not found. Please set RUNWAY_API_KEY in secrets.")
            return None
        
        # Runway API endpoint
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        # Map resolution
        width = 1280 if resolution == "720p" else 1920
        height = 720 if resolution == "720p" else 1080
        
        with st.spinner("Creating video with Runway Gen-3..."):
            response = requests.post(
                "https://api.runwayml.com/v1/text_to_video",
                headers=headers,
                json={
                    "prompt": prompt,
                    "duration": duration,
                    "width": width,
                    "height": height,
                    "model": "gen3a_turbo"
                }
            )
            
            if response.status_code != 200:
                st.error(f"Runway API error: {response.text}")
                return None
            
            task_id = response.json().get("id")
            
            # Poll for completion
            with st.spinner("Processing video... This may take a few minutes."):
                while True:
                    status_response = requests.get(
                        f"https://api.runwayml.com/v1/tasks/{task_id}",
                        headers=headers
                    )
                    
                    if status_response.status_code == 200:
                        status_data = status_response.json()
                        if status_data.get("status") == "completed":
                            return status_data.get("output", {}).get("url")
                        elif status_data.get("status") == "failed":
                            st.error(f"Video generation failed: {status_data.get('error')}")
                            return None
                    time.sleep(10)
    except Exception as e:
        st.error(f"Error generating Runway video: {str(e)}")
        return None


def generate_luma_video(prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Generate video using Luma Dream Machine"""
    try:
        api_key = get_api_key("luma")
        if not api_key:
            st.error("Luma API key not found. Please set LUMA_API_KEY in secrets.")
            return None
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        with st.spinner("Creating video with Luma Dream Machine..."):
            response = requests.post(
                "https://api.lumalabs.ai/dream-machine/v1/generations",
                headers=headers,
                json={
                    "prompt": prompt,
                    "aspect_ratio": "16:9",
                    "model": "ray-2"
                }
            )
            
            if response.status_code != 201:
                st.error(f"Luma API error: {response.text}")
                return None
            
            generation_id = response.json().get("id")
            
            # Poll for completion
            with st.spinner("Processing video... This may take a few minutes."):
                while True:
                    status_response = requests.get(
                        f"https://api.lumalabs.ai/dream-machine/v1/generations/{generation_id}",
                        headers=headers
                    )
                    
                    if status_response.status_code == 200:
                        status_data = status_response.json()
                        state = status_data.get("state")
                        if state == "completed":
                            return status_data.get("assets", {}).get("video")
                        elif state == "failed":
                            st.error(f"Video generation failed: {status_data.get('failure_reason')}")
                            return None
                    time.sleep(10)
    except Exception as e:
        st.error(f"Error generating Luma video: {str(e)}")
        return None


def generate_kling_video(prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Generate video using Kling AI via wavespeed"""
    try:
        api_key = get_api_key("wavespeed")
        if not api_key:
            st.error("Wavespeed API key not found. Please set WAVESPEED_API_KEY in secrets.")
            return None
        
        # Set API key for wavespeed
        os.environ["WAVESPEED_API_KEY"] = api_key
        
        import wavespeed
        
        with st.spinner("Creating video with Kling AI..."):
            output = wavespeed.run(
                "bytedance/kling-2.0",
                input={
                    "prompt": prompt,
                    "duration": duration,
                    "aspect_ratio": "16:9"
                }
            )
            
            if isinstance(output, str):
                return output
            elif isinstance(output, dict) and "video" in output:
                return output["video"]
            else:
                st.error("Unexpected output format from Kling AI")
                return None
    except Exception as e:
        st.error(f"Error generating Kling video: {str(e)}")
        return None


def generate_pika_video(prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Generate video using Pika Labs via wavespeed"""
    try:
        api_key = get_api_key("wavespeed")
        if not api_key:
            st.error("Wavespeed API key not found. Please set WAVESPEED_API_KEY in secrets.")
            return None
        
        # Set API key for wavespeed
        os.environ["WAVESPEED_API_KEY"] = api_key
        
        import wavespeed
        
        with st.spinner("Creating video with Pika Labs..."):
            output = wavespeed.run(
                "pika/pika-1.5",
                input={
                    "prompt": prompt,
                    "duration": duration,
                    "aspect_ratio": "16:9"
                }
            )
            
            if isinstance(output, str):
                return output
            elif isinstance(output, dict) and "video" in output:
                return output["video"]
            else:
                st.error("Unexpected output format from Pika Labs")
                return None
    except Exception as e:
        st.error(f"Error generating Pika video: {str(e)}")
        return None


def generate_vidu_video(prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Generate video using Vidu AI"""
    try:
        api_key = get_api_key("vidu")
        if not api_key:
            st.error("Vidu API key not found. Please set VIDU_API_KEY in secrets.")
            return None
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        with st.spinner("Creating video with Vidu AI..."):
            response = requests.post(
                "https://pollo.ai/api/platform/generation/vidu/vidu-v2-0",
                headers=headers,
                json={
                    "prompt": prompt,
                    "duration": duration,
                    "resolution": resolution
                }
            )
            
            if response.status_code != 200:
                st.error(f"Vidu API error: {response.text}")
                return None
            
            task_id = response.json().get("id")
            
            # Poll for completion
            with st.spinner("Processing video... This may take a few minutes."):
                while True:
                    status_response = requests.get(
                        f"https://pollo.ai/api/platform/generation/{task_id}",
                        headers=headers
                    )
                    
                    if status_response.status_code == 200:
                        status_data = status_response.json()
                        if status_data.get("status") == "completed":
                            return status_data.get("video_url")
                        elif status_data.get("status") == "failed":
                            st.error(f"Video generation failed: {status_data.get('error')}")
                            return None
                    time.sleep(10)
    except Exception as e:
        st.error(f"Error generating Vidu video: {str(e)}")
        return None


def generate_svd_video(image_url: str, duration: int = 25) -> Optional[str]:
    """Generate video from image using Stable Video Diffusion"""
    try:
        api_key = get_api_key("replicate")
        if not api_key:
            st.error("Replicate API key not found. Please set REPLICATE_API_KEY in secrets.")
            return None
        
        # Set API token for replicate
        os.environ["REPLICATE_API_TOKEN"] = api_key
        
        with st.spinner("Converting image to video with Stable Video Diffusion..."):
            output = replicate.run(
                SVD_MODEL,
                input={
                    "input_image": image_url,
                    "frames_per_second": 6,
                    "motion_bucket_id": 127,
                    "cond_aug": 0.02
                }
            )
            
            if output:
                return output if isinstance(output, str) else output[0] if isinstance(output, list) else None
            return None
    except Exception as e:
        st.error(f"Error generating SVD video: {str(e)}")
        return None


def generate_flux_image(model_name: str, prompt: str) -> Optional[str]:
    """Generate image using Flux model on Replicate"""
    try:
        api_key = get_api_key("replicate")
        if not api_key:
            st.error("Replicate API key not found. Please set REPLICATE_API_KEY in secrets.")
            return None
        
        # Set API token for replicate
        os.environ["REPLICATE_API_TOKEN"] = api_key
        
        model_id = FLUX_MODELS.get(model_name, "black-forest-labs/flux-schnell")
        
        with st.spinner(f"Generating image with {model_name}..."):
            output = replicate.run(
                model_id,
                input={
                    "prompt": prompt,
                    "aspect_ratio": "16:9",
                    "output_format": "png",
                    "output_quality": 90
                }
            )
            
            if output:
                return output[0] if isinstance(output, list) else str(output)
            return None
    except Exception as e:
        st.error(f"Error generating Flux image: {str(e)}")
        return None


def generate_pony_svd_video(prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Generate video using Pony-like Stable Video Diffusion"""
    try:
        api_key = get_api_key("replicate")
        if not api_key:
            st.error("Replicate API key not found. Please set REPLICATE_API_KEY in secrets.")
            return None
        
        # Set API token for replicate
        os.environ["REPLICATE_API_TOKEN"] = api_key
        
        with st.spinner("Generating video with Stable Video Diffusion..."):
            output = replicate.run(
                SVD_MODEL,
                input={
                    "input_image": None,  # Will use default/random initialization
                    "frames_per_second": 6,
                    "motion_bucket_id": 127
                }
            )
            
            if output:
                return output if isinstance(output, str) else output[0] if isinstance(output, list) else None
            return None
    except Exception as e:
        st.error(f"Error generating Pony SVD video: {str(e)}")
        return None


def generate_flux_svd_video(model_name: str, prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Generate video by first creating image with Flux, then converting to video with SVD"""
    # First generate image with Flux
    image_url = generate_flux_image(model_name, prompt)
    
    if not image_url:
        st.error("Failed to generate image with Flux model")
        return None
    
    # Display the generated image
    st.image(image_url, caption="Generated Image", use_container_width=True)
    
    # Convert image to video with SVD
    video_url = generate_svd_video(image_url, duration)
    
    return video_url


def generate_video(model: str, prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Main function to generate video based on selected model"""
    
    if model == "Sora (OpenAI)":
        return generate_sora_video(prompt, duration, resolution)
    
    elif model == "Runway Gen-3 Alpha Turbo":
        return generate_runway_video(prompt, duration, resolution)
    
    elif model == "Luma Dream Machine (Ray-2)":
        return generate_luma_video(prompt, duration, resolution)
    
    elif model == "Kling AI":
        return generate_kling_video(prompt, duration, resolution)
    
    elif model == "Pika Labs":
        return generate_pika_video(prompt, duration, resolution)
    
    elif model == "Vidu AI":
        return generate_vidu_video(prompt, duration, resolution)
    
    elif model == "Pony-like (Stable Video Diffusion)":
        return generate_pony_svd_video(prompt, duration, resolution)
    
    elif model in FLUX_MODELS:
        return generate_flux_svd_video(model, prompt, duration, resolution)
    
    else:
        st.error(f"Model {model} not implemented")
        return None


# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("### API Key Status")
    
    # Check which API keys are configured
    api_keys_status = {
        "OpenAI": get_api_key("openai"),
        "Runway": get_api_key("runway"),
        "Luma": get_api_key("luma"),
        "Wavespeed": get_api_key("wavespeed"),
        "Replicate": get_api_key("replicate"),
        "Vidu": get_api_key("vidu")
    }
    
    for service, key in api_keys_status.items():
        status = "✅ Configured" if key else "❌ Missing"
        st.text(f"{service}: {status}")
    
    st.markdown("---")
    st.markdown("### About")
    st.info(
        "This app generates AI videos using various state-of-the-art models. "
        "Select a model, enter your prompt, and generate stunning videos!"
    )

# Main interface
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🎨 Generation Settings")
    
    # Model selection
    selected_model = st.selectbox(
        "Select AI Model",
        MODELS,
        help="Choose the AI model to generate your video"
    )
    
    # Text prompt
    prompt = st.text_area(
        "Video Prompt",
        height=100,
        placeholder="Describe the video you want to generate...",
        help="Enter a detailed description of the video you want to create"
    )

with col2:
    st.subheader("⚙️ Video Parameters")
    
    # Duration slider
    duration = st.slider(
        "Duration (seconds)",
        min_value=5,
        max_value=60,
        value=10,
        help="Select video duration"
    )
    
    # Resolution selection
    resolution = st.radio(
        "Resolution",
        ["720p", "1080p"],
        help="Choose video resolution"
    )

# Generate button
if st.button("🎬 Generate Video", type="primary", use_container_width=True):
    if not prompt:
        st.warning("⚠️ Please enter a prompt to generate a video.")
    else:
        # Generate video
        video_url = generate_video(selected_model, prompt, duration, resolution)
        
        if video_url:
            st.success("✅ Video generated successfully!")
            
            # Display video
            st.subheader("📹 Generated Video")
            st.video(video_url)
            
            # Download button
            st.markdown("---")
            st.markdown(f"### [⬇️ Download Video]({video_url})")
            st.markdown(f"Direct link: `{video_url}`")
        else:
            st.error("❌ Failed to generate video. Please check your API keys and try again.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Built with ❤️ using Streamlit | 
        <a href='https://github.com/americaniron/IRON-CREATOR'>GitHub</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
