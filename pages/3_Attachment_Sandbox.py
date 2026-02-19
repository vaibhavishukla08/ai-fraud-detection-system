import streamlit as st
from backend.attachment_scanner import scan_file

st.header("📎 Attachment & Pharming Verification")

uploaded_file = st.file_uploader("Upload attachment")

if uploaded_file and st.button("Scan Attachment"):
    result = scan_file(uploaded_file)

    st.metric("Threat Level", result["threat_level"])
    st.write(result["behavior_summary"])
