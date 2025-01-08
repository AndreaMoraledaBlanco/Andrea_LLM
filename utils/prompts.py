from langchain.prompts import PromptTemplate

class PromptTemplates:
    BLOG_TEMPLATE = PromptTemplate(
        input_variables=["topic", "audience", "tone"],
        template="""Write a detailed blog post about {topic} for {audience}.
        Tone: {tone}
        Include:
        - Engaging headline
        - Introduction
        - 3-4 main sections
        - Conclusion with call-to-action
        - Suggested SEO keywords
        Make it informative and engaging while maintaining appropriate tone."""
    )
    
    TWITTER_TEMPLATE = PromptTemplate(
        input_variables=["topic", "audience"],
        template="""Generate 3-5 engaging tweets about {topic} for {audience}.
        Requirements:
        - Each tweet under 280 characters
        - Include relevant hashtags
        - Make it engaging and shareable
        - Create a coherent thread narrative"""
    )
    
    INSTAGRAM_TEMPLATE = PromptTemplate(
        input_variables=["topic", "audience"],
        template="""Create an Instagram post about {topic} for {audience}.
        Include:
        - Attention-grabbing first line
        - Engaging story or information
        - Call-to-action
        - 5-10 relevant hashtags
        Make it visual and engaging."""
    )