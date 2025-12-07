"""
History page
"""

import streamlit as st
import pandas as pd


def render():
    """Render history page"""

    st.title("📊 Analysis History")

    # Filters
    col1, col2, col3 = st.columns(3)

    with col1:
        date_filter = st.date_input("Date Range", [])

    with col2:
        patient_filter = st.text_input("Patient ID")

    with col3:
        condition_filter = st.multiselect(
            "Detected Conditions",
            ["Pneumonia", "Cardiomegaly", "Effusion", "All"]
        )

    st.markdown("---")

    # Sample data
    data = pd.DataFrame({
        "ID": ["001", "002", "003"],
        "Date": ["2025-12-07", "2025-12-06", "2025-12-05"],
        "Patient ID": ["P001", "P002", "P001"],
        "Detected Conditions": [
            "Pneumonia, Cardiomegaly",
            "Effusion",
            "Pneumonia"
        ],
        "Confidence": ["85%", "72%", "90%"],
        "Risk Level": ["High", "Medium", "High"]
    })

    # Display table
    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )

    # Statistics
    st.markdown("---")
    st.markdown("### 📈 Statistics")

    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

    with stat_col1:
        st.metric("Total Analyses", "156")

    with stat_col2:
        st.metric("This Week", "23", delta="5")

    with stat_col3:
        st.metric("Avg Confidence", "82%")

    with stat_col4:
        st.metric("High Risk Cases", "12")
