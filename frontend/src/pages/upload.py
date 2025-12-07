"""
Upload and analysis page
"""

import streamlit as st
from src.utils.api_client import APIClient


def render():
    """Render upload page"""

    st.title("📤 Upload & Analyze X-ray")

    # Upload section
    uploaded_file = st.file_uploader(
        "Upload Chest X-ray Image",
        type=["jpg", "jpeg", "png"],
        help="Supported formats: JPG, PNG (max 10MB)"
    )

    if uploaded_file:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Original Image")
            st.image(uploaded_file, use_column_width=True)

        with col2:
            st.markdown("### Analysis Results")

            # Options
            with st.expander("⚙️ Analysis Options"):
                threshold = st.slider(
                    "Detection Threshold",
                    min_value=0.0,
                    max_value=1.0,
                    value=0.5,
                    step=0.05
                )

                show_bbox = st.checkbox("Show Bounding Boxes", value=True)
                patient_id = st.text_input("Patient ID (optional)")

            # Analyze button
            if st.button("🔍 Analyze", type="primary", use_container_width=True):
                with st.spinner("Analyzing..."):
                    # TODO: Call API
                    st.success("Analysis completed!")

                    # Display results
                    st.markdown("#### Detected Conditions")

                    # Sample results
                    results = [
                        {"disease": "Pneumonia", "probability": 0.85, "positive": True},
                        {"disease": "Cardiomegaly", "probability": 0.65, "positive": True},
                        {"disease": "Effusion", "probability": 0.35, "positive": False},
                    ]

                    for result in results:
                        if result["positive"]:
                            st.warning(
                                f"⚠️ **{result['disease']}**: {result['probability']:.2%} confidence"
                            )

                    # Metrics
                    st.markdown("#### Summary")
                    metric_col1, metric_col2, metric_col3 = st.columns(3)

                    with metric_col1:
                        st.metric("Conditions Detected", "2")

                    with metric_col2:
                        st.metric("Avg Confidence", "75%")

                    with metric_col3:
                        st.metric("Risk Level", "Medium")

                    # Download report
                    st.download_button(
                        "📄 Download Report",
                        data="Sample report content",
                        file_name="xray_report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
