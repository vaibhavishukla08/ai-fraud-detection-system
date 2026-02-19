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

    status_options = ["Open", "Investigating", "Resolved"]

    new_status = col2.selectbox(
        "Update Status",
        status_options,
        index=status_options.index(row["Status"]),
        key=row["Case ID"]
    )

    if new_status != row["Status"]:
        st.success(f"Status updated to {new_status} (Demo Mode)")
