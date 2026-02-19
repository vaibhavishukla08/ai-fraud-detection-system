import streamlit as st
import pandas as pd

st.header("📜 Audit Logs")

# Demo data (cloud-safe)
logs = [
    {"Action": "Email Scan", "User": "Vaibhavi", "Result": "High"},
    {"Action": "Website Check", "User": "Vaibhavi", "Result": "Medium"},
    {"Action": "Deepfake Detection", "User": "Vaibhavi", "Result": "Low"},
]

df = pd.DataFrame(logs)

st.table(df)
