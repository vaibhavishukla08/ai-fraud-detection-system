import streamlit as st
from backend.prompt_attack_tester import test_prompt

st.header("🧪 Prompt Injection & Jailbreak Test Lab")

prompt = st.text_area("Enter prompt to test against AI model")

if st.button("Run Attack Simulation"):
    result = test_prompt(prompt)

    st.metric("Leak Risk Score", result["leak_risk"])
    st.write("### Findings")
    st.write(result["analysis"])
