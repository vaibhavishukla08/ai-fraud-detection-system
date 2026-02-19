import streamlit as st
from backend.website_analyzer import analyze_website

st.header("🌐 Website Phishing & Spoofing Detector")

url = st.text_input("Enter website URL")

if st.button("Check Website"):
    result = analyze_website(url)

    st.metric("Trust Score", result["trust_score"])
    st.write("### Indicators Detected")
    for i in result["indicators"]:
        st.warning(i)
