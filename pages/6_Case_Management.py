import streamlit as st
from database.db_connection import get_connection

st.header("📁 Case Management")

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT case_id, status FROM cases ORDER BY created_at DESC;")
cases = cursor.fetchall()

for case in cases:
    case_id, status = case

    col1, col2 = st.columns([1,2])

    col1.write(f"Case #{case_id}")

    new_status = col2.selectbox(
        "Update Status",
        ["Open", "Investigating", "Resolved"],
        index=["Open","Investigating","Resolved"].index(status),
        key=case_id
    )

    if new_status != status:
        cursor.execute("UPDATE cases SET status=%s WHERE case_id=%s", (new_status, case_id))
        conn.commit()

conn.close()
