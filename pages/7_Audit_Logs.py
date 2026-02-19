import streamlit as st
from database.db_connection import get_connection

st.header("📜 Audit Logs")

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT action, user_name, result, created_at FROM audit_logs ORDER BY created_at DESC;")
logs = cursor.fetchall()

conn.close()

st.dataframe(logs)
