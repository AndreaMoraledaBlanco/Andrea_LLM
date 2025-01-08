import streamlit as st
from generators.content_pipeline import ContentPipeline

def main():
    st.title("AI Content Generator")
    st.write("Generate platform-specific content using local AI models")
    
    # Sidebar for configurations
    st.sidebar.header("Content Settings")
    platform = st.sidebar.selectbox(
        "Platform",
        ["Blog", "Twitter", "Instagram"]
    )
    
    generate_image = st.sidebar.checkbox("Generate accompanying image")
    
    # Main content area
    topic = st.text_area("Topic", placeholder="Enter your topic...")
    audience = st.text_input("Target Audience", placeholder="e.g., professionals, teenagers...")
    tone = st.selectbox(
        "Content Tone",
        ["Professional", "Casual", "Educational", "Entertaining"]
    )
    
    if st.button("Generate Content"):
        if topic and audience:
            try:
                with st.spinner("Generating content..."):
                    pipeline = ContentPipeline()
                    content = pipeline.generate_content(
                        platform=platform.lower(),
                        topic=topic,
                        audience=audience,
                        tone=tone,
                        generate_image=generate_image
                    )
                    
                    # Display generated content
                    st.subheader("Generated Content")
                    st.text_area("Content", content["text"], height=300)
                    
                    if generate_image and "image" in content:
                        st.image(content["image"], caption="Generated Image")
                    
                    # Add download buttons
                    st.download_button(
                        "Download Content",
                        content["text"],
                        file_name=f"{platform.lower()}_content.txt"
                    )
            except Exception as e:
                st.error(f"Error generating content: {str(e)}")
        else:
            st.warning("Please fill in all required fields")

if __name__ == "__main__":
    main()