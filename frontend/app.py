"""
MedVision AI - Streamlit Dashboard
Main application entry point
"""

import streamlit as st
from src.pages import home, upload, history, analytics

st.set_page_config(
    page_title="MedVision AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)


def main():
    """Main application"""

    # Sidebar navigation
    with st.sidebar:
        st.image("public/logo.png", width=200) if st.sidebar else None
        st.title("🏥 MedVision AI")
        st.markdown("---")

        page = st.radio(
            "Navigation",
            ["🏠 Home", "📤 Upload & Analyze", "📊 History", "📈 Analytics"],
            label_visibility="collapsed"
        )

        st.markdown("---")
        st.markdown("""
        ### About
        AI-powered chest X-ray analysis system for automated disease detection.

        **Supported Conditions:**
        - Pneumonia
        - Tuberculosis
        - COVID-19
        - And 11 more pathologies
        """)

    # Route to pages
    if page == "🏠 Home":
        home.render()
    elif page == "📤 Upload & Analyze":
        upload.render()
    elif page == "📊 History":
        history.render()
    elif page == "📈 Analytics":
        analytics.render()


if __name__ == "__main__":
    main()
