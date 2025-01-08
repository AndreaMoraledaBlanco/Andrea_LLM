from diffusers import StableDiffusionPipeline
import torch

class ImageGenerator:
    def __init__(self):
        self.model_id = "runwayml/stable-diffusion-v1-5"
        self.pipe = StableDiffusionPipeline.from_pretrained(
            self.model_id,
            torch_dtype=torch.float16
        ).to("cuda" if torch.cuda.is_available() else "cpu")
    
    def generate(self, prompt: str):
        try:
            image = self.pipe(prompt).images[0]
            return image
        except Exception as e:
            logging.error(f"Error generating image: {e}")
            raise