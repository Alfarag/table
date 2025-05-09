import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sensor & Performance Tables", layout="centered")
st.title("📋 Tables from Hybrid AI Leak Detection Manuscript")

st.markdown("### 📑 Table 1: Sensor Specifications")

# Table 1: Sensor Specs
table1 = pd.DataFrame({
    "Sensor": ["Methane (CH₄)", "Vibration (MEMS)", "Thermal Camera"],
    "Model": ["Figaro TGS2611", "ADXL345", "FLIR Lepton 3.5"],
    "Specification": ["1–500 ppm sensitivity", "±16g range", "160×120 resolution"],
    "Sampling Rate": ["10 Hz", "1 kHz", "5 Hz"]
})
st.table(table1)

st.markdown("---")
st.markdown("### 📊 Table 2: Performance Metrics Comparison")

# Table 2: Performance Metrics
table2 = pd.DataFrame({
    "Model": ["Threshold-based", "Hybrid (Ours)"],
    "Accuracy (%)": [80.1, 97.2],
    "False Positives (%)": [10.3, 1.5],
    "Latency (s)": [0.5, 1.8],
    "Power (W)": [3.2, 9.5]
})
st.table(table2)
