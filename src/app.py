import streamlit as st
from PIL import Image
from pathlib import Path
import sys

# Add the parent directory to sys.path to import local modules
sys.path.append(str(Path(__file__).parent))

from models.object_detector import ObjectDetector
from utils.prompt_templates import PromptTemplates
from utils.llm_interface import LLMInterface

def initialize_session_state():
    """Initialize session state variables"""
    if 'detector' not in st.session_state:
        st.session_state.detector = ObjectDetector()
    if 'llm' not in st.session_state:
        st.session_state.llm = LLMInterface()
    if 'current_recommendations' not in st.session_state:
        st.session_state.current_recommendations = None

def main():
    # Page configuration
    st.set_page_config(
        page_title="GenAI Recommendation System",
        page_icon="🎨",
        layout="wide"
    )

    # Initialize session state
    initialize_session_state()

    # Main title
    st.title("🎨 GenAI Recommendation System")
    st.write("Get AI-powered recommendations for your space and style!")

    # Initialize components
    prompt_templates = PromptTemplates()

    # Sidebar
    with st.sidebar:
        st.header("Settings")
        
        # Category selection
        category = st.selectbox(
            "Select Category",
            options=["study_desk", "interior", "fashion"],
            format_func=lambda x: x.replace('_', ' ').title()
        )

        # Confidence threshold slider
        confidence_threshold = st.slider(
            "Detection Confidence Threshold",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
            step=0.05
        )
        st.session_state.detector.confidence_threshold = confidence_threshold

    # Main content area
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Upload Image")
        uploaded_file = st.file_uploader(
            "Choose an image...",
            type=['jpg', 'jpeg', 'png'],
            help="Upload an image for analysis"
        )

        if uploaded_file:
            # Display uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Process button
            if st.button("Generate Recommendations"):
                with st.spinner("Detecting objects..."):
                    # Detect objects
                    detected_objects = st.session_state.detector.detect_objects(image)

                    if detected_objects:
                        # Display detected objects
                        st.subheader("Detected Objects")
                        objects_text = ", ".join([
                            f"{obj['class']} ({obj['confidence']:.2f})"
                            for obj in detected_objects
                        ])
                        st.write(objects_text)

                        # Generate recommendations
                        with st.spinner("Generating recommendations..."):
                            template = prompt_templates.get_template(category)
                            if template:
                                prompt = template.format(objects=objects_text)
                                system_prompt = prompt_templates.get_system_prompt()
                                
                                # Debug information in expander
                                with st.expander("Debug Information", expanded=False):
                                    st.write("System Prompt:", system_prompt)
                                    st.write("Generated Prompt:", prompt)
                                
                                recommendations = st.session_state.llm.generate_recommendations(
                                    prompt,
                                    system_prompt
                                )
                                
                                if not recommendations.startswith("Error"):
                                    st.session_state.current_recommendations = recommendations
                                    st.success("Recommendations generated successfully!")
                                else:
                                    st.error(recommendations)
                            else:
                                st.error("Invalid category selected")
                    else:
                        st.warning("No objects detected in the image")

    with col2:
        st.subheader("Recommendations")
        if st.session_state.current_recommendations:
            st.markdown(st.session_state.current_recommendations)
        else:
            st.info("Upload an image and generate recommendations to see them here.")

    # Help section
    with st.expander("How to Use"):
        st.markdown("""
        1. **Select a Category**: Choose between Study Desk, Interior Design, or Fashion
        2. **Upload Image**: Upload a clear image related to your selected category
        3. **Adjust Settings**: Use the sidebar to adjust detection confidence if needed
        4. **Generate**: Click the 'Generate Recommendations' button
        5. **Review**: Review the detected objects and recommendations
        
        **Note**: For best results, ensure your image is well-lit and clearly shows the items you want analyzed.
        """)

    # Footer
    st.markdown("---")
    st.markdown(
        "Made with ❤️ using Streamlit | "
        "Powered by YOLOv8 and Gemma 2B"
    )

if __name__ == "__main__":
    main()