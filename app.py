import streamlit as st
import time
import requests
import os
from typing import Optional, Dict, Any

# Configure page
st.set_page_config(
    page_title="AI Video Generator",
    page_icon="🎬",
    layout="wide"
)

# Title and description
st.title("🎬 AI Video Generation Studio")
st.markdown("Generate videos using state-of-the-art AI models")

# Model definitions
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

# Flux model IDs for Replicate
FLUX_MODELS = {
    "Flux.1-schnell + SVD": "black-forest-labs/flux-schnell",
    "Flux.1-dev + SVD": "black-forest-labs/flux-dev",
    "Flux.1-pro + SVD": "black-forest-labs/flux-1.1-pro",
    "Flux.1.1-pro + SVD": "black-forest-labs/flux-1.1-pro",
    "Flux.2 + SVD": "black-forest-labs/flux-1.1-pro",  # Using 1.1 as placeholder
    "Flux.2-max + SVD": "black-forest-labs/flux-1.1-pro",  # Using 1.1 as placeholder
    "Flux Kontext + SVD": "black-forest-labs/flux-1.1-pro"  # Using 1.1 as placeholder
}

SVD_MODEL = "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438"


def get_api_key(service: str) -> Optional[str]:
    """Get API key from Streamlit secrets"""
    key_map = {
        "openai": "OPENAI_API_KEY",
        "runway": "RUNWAY_API_KEY",
        "luma": "LUMA_API_KEY",
        "wavespeed": "WAVESPEED_API_KEY",
        "vidu": "VIDU_API_KEY",
        "replicate": "REPLICATE_API_TOKEN"
    }
    
    try:
        key = st.secrets.get(key_map.get(service, ""))
        return key if key else None
    except (KeyError, AttributeError):
        return None


def generate_sora_video(prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Generate video using Sora (OpenAI)"""
    try:
        import openai
        
        api_key = get_api_key("openai")
        if not api_key:
            st.error("OpenAI API key not found. Please set OPENAI_API_KEY in secrets.")
            return None
        
        client = openai.OpenAI(api_key=api_key)
        
        # Map resolution to format
        size = "1920x1080" if resolution == "1080p" else "1280x720"
        
        with st.spinner("Creating video with Sora..."):
            # Create video generation request
            response = client.videos.create(
                model="sora-2-pro",
                prompt=prompt,
                size=size,
                duration=duration
            )
            
            video_id = response.id
            
            # Poll for completion
            st.info(f"Video generation started (ID: {video_id}). Polling for completion...")
            
            while True:
                status = client.videos.retrieve(video_id)
                
                if status.status == "completed":
                    return status.url
                elif status.status == "failed":
                    st.error(f"Video generation failed: {status.error}")
                    return None
                
                time.sleep(10)
                st.info(f"Status: {status.status}... (checking again in 10s)")
                
    except Exception as e:
        st.error(f"Error generating video with Sora: {str(e)}")
        return None


def generate_runway_video(prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Generate video using Runway Gen-3 Alpha Turbo
    
    Note: This is a placeholder implementation. The actual Runway API may differ.
    Update the endpoint and request format based on official Runway API documentation.
    """
    try:
        api_key = get_api_key("runway")
        if not api_key:
            st.error("Runway API key not found. Please set RUNWAY_API_KEY in secrets.")
            return None
        
        # Note: This is a placeholder implementation
        # Actual Runway API may differ - verify with official documentation
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        with st.spinner("Creating video with Runway..."):
            # Create task - endpoint may need to be updated
            response = requests.post(
                "https://api.runwayml.com/v1/text-to-video",
                headers=headers,
                json={
                    "prompt": prompt,
                    "duration": duration,
                    "resolution": resolution
                }
            )
            
            if response.status_code != 200:
                st.error(f"Runway API error: {response.text}")
                return None
            
            task_id = response.json().get("id")
            
            # Poll for completion
            st.info(f"Video generation started (ID: {task_id}). Polling for completion...")
            
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
                        st.error(f"Video generation failed")
                        return None
                
                time.sleep(10)
                st.info("Checking status... (every 10s)")
                
    except Exception as e:
        st.error(f"Error generating video with Runway: {str(e)}")
        return None


def generate_luma_video(prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Generate video using Luma Dream Machine (Ray-2)"""
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
            # Create generation
            response = requests.post(
                "https://api.lumalabs.ai/dream-machine/v1/generations",
                headers=headers,
                json={
                    "prompt": prompt,
                    "aspect_ratio": "16:9",
                    "loop": False
                }
            )
            
            if response.status_code != 200:
                st.error(f"Luma API error: {response.text}")
                return None
            
            generation_id = response.json().get("id")
            
            # Poll for completion
            st.info(f"Video generation started (ID: {generation_id}). Polling for completion...")
            
            while True:
                status_response = requests.get(
                    f"https://api.lumalabs.ai/dream-machine/v1/generations/{generation_id}",
                    headers=headers
                )
                
                if status_response.status_code == 200:
                    status_data = status_response.json()
                    
                    if status_data.get("state") == "completed":
                        return status_data.get("assets", {}).get("video")
                    elif status_data.get("state") == "failed":
                        st.error(f"Video generation failed")
                        return None
                
                time.sleep(10)
                st.info("Checking status... (every 10s)")
                
    except Exception as e:
        st.error(f"Error generating video with Luma: {str(e)}")
        return None


def generate_kling_video(prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Generate video using Kling AI"""
    try:
        import replicate
        
        api_key = get_api_key("replicate")
        if not api_key:
            st.error("Replicate API key not found. Please set REPLICATE_API_TOKEN in secrets.")
            return None
        
        os.environ["REPLICATE_API_TOKEN"] = api_key
        
        with st.spinner("Creating video with Kling AI..."):
            # Note: Using a placeholder model since exact Kling model on Replicate may vary
            output = replicate.run(
                "lucataco/kling:d55e8d8babc8a7657e7b0cc2ac2ee4b8e0ff63c2f37bfbb7e7f6367e888f3e57",
                input={
                    "prompt": prompt,
                    "duration": str(duration)
                }
            )
            
            if output:
                return output if isinstance(output, str) else str(output)
            return None
            
    except Exception as e:
        st.error(f"Error generating video with Kling AI: {str(e)}")
        return None


def generate_pika_video(prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Generate video using Pika Labs"""
    try:
        import replicate
        
        api_key = get_api_key("replicate")
        if not api_key:
            st.error("Replicate API key not found. Please set REPLICATE_API_TOKEN in secrets.")
            return None
        
        os.environ["REPLICATE_API_TOKEN"] = api_key
        
        with st.spinner("Creating video with Pika Labs..."):
            # Note: Using a placeholder model since exact Pika model on Replicate may vary
            output = replicate.run(
                "lucataco/animate-diff:1531004ee4c98e4f57c26f6e03d3d0cde9c6c6d9b8e1c0e3f0e8f7e6d5c4b3a2",
                input={
                    "prompt": prompt,
                }
            )
            
            if output:
                return output if isinstance(output, str) else str(output)
            return None
            
    except Exception as e:
        st.error(f"Error generating video with Pika Labs: {str(e)}")
        return None


def generate_vidu_video(prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Generate video using Vidu AI
    
    Note: This is a placeholder implementation. The actual Vidu AI API may differ.
    Update the endpoint and request format based on official Vidu/Pollo.ai API documentation.
    """
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
            # Create generation - endpoint may need to be updated
            response = requests.post(
                "https://pollo.ai/api/platform/generation/vidu/vidu-v2-0",
                headers=headers,
                json={
                    "prompt": prompt,
                    "duration": duration
                }
            )
            
            if response.status_code != 200:
                st.error(f"Vidu API error: {response.text}")
                return None
            
            generation_id = response.json().get("id")
            
            # Poll for completion
            st.info(f"Video generation started (ID: {generation_id}). Polling for completion...")
            
            while True:
                status_response = requests.get(
                    f"https://pollo.ai/api/platform/generation/{generation_id}",
                    headers=headers
                )
                
                if status_response.status_code == 200:
                    status_data = status_response.json()
                    
                    if status_data.get("status") == "completed":
                        return status_data.get("video_url")
                    elif status_data.get("status") == "failed":
                        st.error(f"Video generation failed")
                        return None
                
                time.sleep(10)
                st.info("Checking status... (every 10s)")
                
    except Exception as e:
        st.error(f"Error generating video with Vidu AI: {str(e)}")
        return None


def generate_svd_video(prompt: str, duration: int, resolution: str, image_url: Optional[str] = None) -> Optional[str]:
    """Generate video using Stable Video Diffusion"""
    try:
        import replicate
        
        api_key = get_api_key("replicate")
        if not api_key:
            st.error("Replicate API key not found. Please set REPLICATE_API_TOKEN in secrets.")
            return None
        
        os.environ["REPLICATE_API_TOKEN"] = api_key
        
        with st.spinner("Creating video with Stable Video Diffusion..."):
            # If no image provided, generate one first
            if not image_url:
                st.info("No image provided, generating from prompt first...")
                image_output = replicate.run(
                    "black-forest-labs/flux-schnell",
                    input={"prompt": prompt}
                )
                if image_output:
                    image_url = image_output[0] if isinstance(image_output, list) else image_output
            
            if not image_url:
                st.error("Failed to generate initial image")
                return None
            
            # Generate video from image
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
                return output if isinstance(output, str) else str(output)
            return None
            
    except Exception as e:
        st.error(f"Error generating video with SVD: {str(e)}")
        return None


def generate_flux_svd_video(prompt: str, duration: int, resolution: str, model_name: str) -> Optional[str]:
    """Generate video using Flux + SVD pipeline"""
    try:
        import replicate
        
        api_key = get_api_key("replicate")
        if not api_key:
            st.error("Replicate API key not found. Please set REPLICATE_API_TOKEN in secrets.")
            return None
        
        os.environ["REPLICATE_API_TOKEN"] = api_key
        
        flux_model = FLUX_MODELS.get(model_name)
        
        with st.spinner(f"Step 1/2: Generating image with {model_name.split(' + ')[0]}..."):
            # Generate image with Flux
            image_output = replicate.run(
                flux_model,
                input={"prompt": prompt}
            )
            
            if not image_output:
                st.error("Failed to generate image with Flux")
                return None
            
            image_url = image_output[0] if isinstance(image_output, list) else image_output
            st.success(f"Image generated successfully!")
            st.image(image_url, caption="Generated image", use_column_width=True)
        
        with st.spinner("Step 2/2: Converting image to video with SVD..."):
            # Generate video from image
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
                return output if isinstance(output, str) else str(output)
            return None
            
    except Exception as e:
        st.error(f"Error generating video with {model_name}: {str(e)}")
        return None


def generate_video(model: str, prompt: str, duration: int, resolution: str) -> Optional[str]:
    """Main video generation dispatcher"""
    
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
        return generate_svd_video(prompt, duration, resolution)
    elif model in FLUX_MODELS:
        return generate_flux_svd_video(prompt, duration, resolution, model)
    else:
        st.error(f"Unknown model: {model}")
        return None


# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Model selection
    selected_model = st.selectbox(
        "Select Model",
        MODELS,
        help="Choose the AI model for video generation"
    )
    
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
        help="Select output video resolution"
    )
    
    st.markdown("---")
    st.markdown("### 💡 Tips")
    st.markdown("- Be specific in your prompts")
    st.markdown("- Longer videos may take more time")
    st.markdown("- Some models work better for certain content")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Video Prompt")
    prompt = st.text_area(
        "Enter your video description",
        height=150,
        placeholder="Describe the video you want to generate...\n\nExample: A serene lake at sunset with mountains in the background, birds flying across the sky, gentle ripples on the water surface",
        help="Provide a detailed description of the video you want to generate"
    )
    
    generate_button = st.button("🎬 Generate Video", type="primary", use_container_width=True)

with col2:
    st.subheader("ℹ️ Model Info")
    
    model_info = {
        "Sora (OpenAI)": "State-of-the-art video generation from OpenAI",
        "Runway Gen-3 Alpha Turbo": "Fast, high-quality video generation",
        "Luma Dream Machine (Ray-2)": "Dream-like, artistic video creation",
        "Kling AI": "Advanced AI video synthesis",
        "Pika Labs": "Creative video generation with unique style",
        "Vidu AI": "High-quality text-to-video model",
        "Pony-like (Stable Video Diffusion)": "Image-to-video using SVD",
        "Flux.1-schnell + SVD": "Fast Flux image → video pipeline",
        "Flux.1-dev + SVD": "Development Flux → video pipeline",
        "Flux.1-pro + SVD": "Professional Flux → video pipeline",
        "Flux.1.1-pro + SVD": "Enhanced pro Flux → video pipeline",
        "Flux.2 + SVD": "Latest Flux → video pipeline",
        "Flux.2-max + SVD": "Maximum quality Flux → video pipeline",
        "Flux Kontext + SVD": "Context-aware Flux → video pipeline"
    }
    
    st.info(model_info.get(selected_model, "Select a model to see info"))

# Video generation and display
if generate_button:
    if not prompt:
        st.error("⚠️ Please enter a prompt for video generation")
    else:
        st.markdown("---")
        st.subheader("🎥 Generated Video")
        
        # Generate video
        video_url = generate_video(selected_model, prompt, duration, resolution)
        
        if video_url:
            st.success("✅ Video generated successfully!")
            
            # Display video
            try:
                st.video(video_url)
            except Exception as e:
                st.warning(f"Could not embed video, but here's the URL: {video_url}")
            
            # Download link
            st.markdown(f"[⬇️ Download Video]({video_url})")
            
            # Additional info
            with st.expander("📊 Generation Details"):
                st.write(f"**Model:** {selected_model}")
                st.write(f"**Prompt:** {prompt}")
                st.write(f"**Duration:** {duration} seconds")
                st.write(f"**Resolution:** {resolution}")
                st.write(f"**Video URL:** {video_url}")
        else:
            st.error("❌ Video generation failed. Please check your API keys and try again.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Made with ❤️ using Streamlit | Support multiple AI video models</p>
        <p>⚠️ API keys required for each service. See README for setup instructions.</p>
    </div>
    """,
    unsafe_allow_html=True
)
