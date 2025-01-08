from .text_generator import TextGenerator
from utils.image_generator import ImageGenerator

class ContentPipeline:
    def __init__(self):
        self.text_generator = TextGenerator()
        self.image_generator = ImageGenerator()
    
    def generate_content(self, platform: str, topic: str, audience: str, 
                        tone: str = "professional", generate_image: bool = False):
        content = {
            "text": self.text_generator.generate(platform, topic, audience, tone)
        }
        
        if generate_image:
            image_prompt = f"High quality image representing {topic} for {platform} platform"
            content["image"] = self.image_generator.generate(image_prompt)
        
        return content
