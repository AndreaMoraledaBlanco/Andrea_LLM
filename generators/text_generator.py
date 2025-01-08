from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from utils.prompts import PromptTemplates
import logging

class TextGenerator:
    def __init__(self, model_name="llama2"):
        try:
            self.llm = Ollama(model=model_name)
            self.templates = PromptTemplates()
        except Exception as e:
            logging.error(f"Error initializing TextGenerator: {e}")
            raise
    
    def get_template(self, platform: str) -> PromptTemplate:
        templates = {
            "blog": self.templates.BLOG_TEMPLATE,
            "twitter": self.templates.TWITTER_TEMPLATE,
            "instagram": self.templates.INSTAGRAM_TEMPLATE
        }
        return templates.get(platform.lower())
    
    def generate(self, platform: str, topic: str, audience: str, tone: str = "professional") -> str:
        template = self.get_template(platform)
        if not template:
            raise ValueError(f"Unsupported platform: {platform}")
        
        chain = LLMChain(llm=self.llm, prompt=template)
        try:
            result = chain.run(topic=topic, audience=audience, tone=tone)
            return result
        except Exception as e:
            logging.error(f"Error generating content: {e}")
            raise