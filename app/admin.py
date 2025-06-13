import streamlit as st
from pymongo import MongoClient
from datetime import datetime
import pandas as pd

# Mongo connection
MONGO_URI = st.secrets["mongo"]["uri"]
client = MongoClient(MONGO_URI)
db = client["phishing_app"]

def render_admin_page():
    #Defensive check to prevent session crash
    if "username" not in st.session_state:
        st.error("Something went wrong. Please log in again.")
        st.stop()

    username = st.session_state["username"]

    # Auto-promote certain users to admin
    if username in ["eniola", "mumsy", "testing"]:
        db.users.update_one(
            {"username": username},
            {"$set": {"is_admin": True}}
        )

    # Check if user has admin rights
    user = db.users.find_one({"username": username})
    if not user or not user.get("is_admin", False):
        st.error("🚫 Access Denied: You do not have admin privileges.")
        st.stop()

    # Admin Access Granted
    st.title("Admin Dashboard")

    # ---Stats Overview ---
    users = list(db.users.find({}, {"_id": 0}))
    history = list(db.detection_history.find({}, {"_id": 0}))

    total_users = len(users)
    total_scans = len(history)
    phishing_count = sum(1 for item in history if item.get("prediction", "").lower() == "phishing")
    legitimate_count = total_scans - phishing_count

    st.markdown("### 📊 Overview")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👥 Total Users", total_users)
    col2.metric("🕵️ Total Scans", total_scans)
    col3.metric("⚠️ Phishing URLs", phishing_count)
    col4.metric("✅ Legitimate URLs", legitimate_count)

    # --- Tabbed Data Views ---
    tabs = st.tabs(["👥 Registered Users", "🕵️ Global URL Scans"])

    # --- Registered Users Tab ---
    with tabs[0]:
        st.subheader("👥 All Registered Users")
        cleaned_users = []
        for user in users:
            username = user.get("username", "")
            email = user.get("email", "")

            # Detect and swap if email & username are flipped
            if "@" in username and not "@" in email:
                username, email = email, username

            cleaned_users.append({
                "Username": username if username else "N/A",
                "Email": email if email else "N/A"
            })

        if cleaned_users:
            user_df = pd.DataFrame(cleaned_users)
            st.dataframe(user_df, use_container_width=True, hide_index=False)
        else:
            st.info("No registered users found.")

            # --- Global Detection History Tab ---
    with tabs[1]:
        st.subheader("🕵️ All URL Scans (Global History)")
        if history:
            for entry in history:
                if isinstance(entry.get("timestamp"), datetime):
                    entry["timestamp"] = entry["timestamp"].strftime("%Y-%m-%d %H:%M:%S")

            df = pd.DataFrame(history)

            # Normalize prediction text for accuracy
            df["prediction"] = df["prediction"].str.capitalize()

            # Fix counts again just in case
            phishing_count = (df["prediction"] == "Phishing").sum()
            legitimate_count = (df["prediction"] == "Legitimate").sum()

            # Limit columns and rename
            display_df = df[["username", "url", "prediction", "confidence", "timestamp"]]
            display_df.columns = ["Username", "URL", "Prediction", "Confidence", "Timestamp"]

            st.dataframe(display_df, use_container_width=True, hide_index=False)
        else:
            st.info("No scan history available.")
