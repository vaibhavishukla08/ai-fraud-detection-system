import streamlit as st
from backend.email_detector import analyze_email

st.header("📧 AI-Generated Phishing Email Detector")

email_text = st.text_area("Paste email content here", height=250)

if st.button("Analyze Email"):

    result = analyze_email(email_text)

    st.subheader("🔍 Analysis Result")

    st.metric("Risk Score", result["risk_score"])
    st.metric("AI-Generated Probability", f"{result['confidence']}%")

    if result["severity"] == "High":
        st.error("🔴 HIGH RISK — Immediate action recommended")
    elif result["severity"] == "Medium":
        st.warning("🟡 MEDIUM RISK — Review advised")
    else:
        st.success("🟢 LOW RISK — No immediate threat")

    st.subheader("🧠 Explanation")
    st.write(result["explanation"])
