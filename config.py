from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODELS = {
    "text": "llama2",  # Using Ollama's Llama2
    "image": "stable-diffusion"  # Local Stable Diffusion
}
