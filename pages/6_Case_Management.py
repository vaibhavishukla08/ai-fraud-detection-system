import streamlit as st
import pandas as pd

st.header("📁 Case Management")

# Demo data (cloud-safe)
cases = [
    {"Case ID": 101, "Status": "Open"},
    {"Case ID": 102, "Status": "Investigating"},
    {"Case ID": 103, "Status": "Resolved"},
]

df = pd.DataFrame(cases)

for index, row in df.iterrows():
    col1, col2 = st.columns([1, 2])

    col1.write(f"Case #{row['Case ID']}")

    new_status = col2.selectbox(
        "Update Status",
        ["Open", "Investigating", "Resolved"],
        index=["Open", "Investigating", "Resolved"].index
    )