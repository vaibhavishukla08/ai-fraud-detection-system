import streamlit as st
import pandas as pd


st.header("📊 Threat Intelligence Dashboard")
st.divider()
st.subheader("📊 Threat Distribution Overview")
# conn = get_connection()
# cursor = conn.cursor()
# cursor.execute("SELECT severity, COUNT(*) FROM threat_scans GROUP BY severity")
# data = cursor.fetchall()
# conn.close()
data = [
    ("Low", 12),
    ("Medium", 8),
    ("High", 3)
]

st.caption("Real-time AI-based multi-channel threat monitoring system.")

df = pd.DataFrame(data, columns=["Severity", "Count"])

st.subheader("Threat Distribution")
st.bar_chart(df.set_index("Severity"))

high = df[df["Severity"] == "High"]["Count"].sum() if "High" in df["Severity"].values else 0

if high > 0:
    st.error("⚠ High-risk threats detected. Immediate attention required.")
else:
    st.success("✅ No high-risk threats currently.")
st.divider()
st.caption("© 2026 FinShield AI | Built for Barclays Innovation Challenge")
