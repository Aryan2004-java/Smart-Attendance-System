import streamlit as st
import subprocess
import sqlite3
import pandas as pd
from db import reset_attendance, get_attendance

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart Attendance System",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("🤖 Smart Attendance System")
st.caption("Face Recognition • OpenCV • SQLite • Streamlit")

st.markdown("---")

# ---------------- DB STATS ----------------
conn = sqlite3.connect("database/attendance.db")
cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM users WHERE active=1")
total_users = cur.fetchone()[0]

cur.execute("""
    SELECT COUNT(DISTINCT user_id)
    FROM attendance
    WHERE DATE(timestamp) = DATE('now')
""")
today_present = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM attendance")
total_records = cur.fetchone()[0]

conn.close()

# ---------------- DASHBOARD CARDS ----------------
st.header("📊 Attendance Overview")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("👥 Total Users", total_users)

with c2:
    st.metric("✅ Present Today", today_present)

with c3:
    st.metric("📊 Total Records", total_records)

# ---------------- RESET BUTTON ----------------
if total_records > 0:
    if st.button("🧹 Reset ALL Attendance"):
        with st.spinner("Clearing attendance records..."):
            reset_attendance()
        st.success("Attendance records cleared successfully!")
        st.rerun()
else:
    st.info("📭 No attendance data to reset.")

# ---------------- ATTENDANCE CONTROL ----------------
st.markdown("---")
st.header("🎥 Attendance Control")

if st.button("▶️ Start Attendance", disabled=(total_users == 0)):
    st.info("Starting camera... Press Q to stop.")
    subprocess.run(["python", "main.py"])

if total_users == 0:
    st.warning("⚠️ No users registered. Please register a user first.")

# ---------------- REGISTER USER ----------------
st.markdown("---")
st.header("➕ Register New User")

name = st.text_input("Enter user name")

if st.button("📸 Register User"):
    if name.strip() == "":
        st.warning("Please enter a valid name.")
    else:
        with st.spinner("Capturing face & training model..."):
            subprocess.run(["python", "register.py", name])
        st.success(f"User '{name}' registered successfully!")
        st.rerun()

# ---------------- ATTENDANCE RECORDS ----------------
st.markdown("---")
st.header("📋 Attendance Records")

records = get_attendance()

if len(records) == 0:
    st.info("📭 No attendance records found. Start attendance to see data here.")
else:
    df = pd.DataFrame(records, columns=["Name", "Timestamp"])
    df["Date"] = pd.to_datetime(df["Timestamp"]).dt.date

    # ---- FILTERS ----
    f1, f2, f3 = st.columns(3)

    with f1:
        selected_date = st.date_input("📅 Filter by date", value=None)

    with f2:
        show_today = st.checkbox("⏱️ Show only today")

    with f3:
        users = ["All"] + sorted(df["Name"].unique().tolist())
        selected_user = st.selectbox("👤 Filter by user", users)

    # ---- APPLY FILTERS ----
    if selected_date:
        df = df[df["Date"] == selected_date]

    if show_today:
        today = pd.to_datetime("today").date()
        df = df[df["Date"] == today]

    if selected_user != "All":
        df = df[df["Name"] == selected_user]

    # ---- TABLE ----
    st.dataframe(df, use_container_width=True)

    # ---- DOWNLOAD ----
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇️ Download Attendance CSV",
        csv,
        "attendance.csv",
        "text/csv"
    )
