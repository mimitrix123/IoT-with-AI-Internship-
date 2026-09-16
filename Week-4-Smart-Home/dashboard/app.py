"""Tiny real-time dashboard starter using Streamlit."""
import json
import streamlit as st

st.set_page_config(page_title="AI Smart Home", layout="wide")
st.title("🏠 AI Smart Home Dashboard")
st.caption("Prototype UI — connect this page to your MQTT/time-series backend in deployment.")

sample = {"temperature": 24.5, "motion": True, "light": 620, "sound": 72, "occupied": True}
cols = st.columns(5)
for col, (name, value) in zip(cols, sample.items()):
    col.metric(name.replace("_", " ").title(), str(value))

st.subheader("AI recommendations")
if sample["occupied"]:
    st.info("Occupancy detected. Optimize lighting/HVAC while preserving comfort.")
else:
    st.success("No occupancy predicted. Consider eco mode for idle devices.")
