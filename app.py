import streamlit as st

st.set_page_config(
    page_title="Smart Vitals Dashboard",
    layout="wide"
)

st.title("Smart Vitals Dashboard")

st.warning(
    "Educational prototype. Simulated data only. "
    "Not for clinical use."
)

st.header("Sample Patient: DEMO-001")

st.write("These are fictional readings, not real patient data.")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Heart rate", "75 bpm")
col2.metric("Blood oxygen (SpO2)", "98%")
col3.metric("Temperature", "36.8 °C")
col4.metric("Breathing rate", "14 breaths/min")

st.info(
    "First version: display sample readings. "
    "Alert rules and interactive controls will be added later."
)
