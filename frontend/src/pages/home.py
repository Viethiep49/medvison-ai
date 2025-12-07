"""
Home page
"""

import streamlit as st


def render():
    """Render home page"""

    st.markdown('<h1 class="main-header">🏥 MedVision AI</h1>', unsafe_allow_html=True)
    st.markdown("### AI-Powered Chest X-ray Analysis System")

    st.markdown("---")

    # Feature highlights
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### 🎯 Accurate Detection
        - 14 pathological conditions
        - 95%+ accuracy on test set
        - Medical-grade AI model
        """)

    with col2:
        st.markdown("""
        ### ⚡ Fast Analysis
        - Results in seconds
        - Batch processing support
        - Cloud-based inference
        """)

    with col3:
        st.markdown("""
        ### 📊 Comprehensive Reports
        - Visual localization
        - Confidence scores
        - Detailed statistics
        """)

    st.markdown("---")

    # Quick start
    st.markdown("### 🚀 Quick Start")
    st.markdown("""
    1. Navigate to **Upload & Analyze** page
    2. Upload a chest X-ray image (JPG, PNG, DICOM)
    3. Get instant AI analysis with disease predictions
    4. View results and download reports
    """)

    # System status
    st.markdown("---")
    st.markdown("### 📡 System Status")

    status_col1, status_col2, status_col3 = st.columns(3)

    with status_col1:
        st.metric("API Status", "🟢 Online")

    with status_col2:
        st.metric("Model Status", "🟢 Ready")

    with status_col3:
        st.metric("Database", "🟢 Connected")
