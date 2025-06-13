import streamlit as st
from datetime import datetime
import pandas as pd
from utils.db import get_db  # ✅ Ensure DB is imported here

def render_history_page():
    st.title("Detection History")

    username = st.session_state.user  # ✅ Uses correct session key
    st.info(f"Logged in as: **{username}**")

    db = get_db()
    history_collection = db["detection_history"]

    # Fetch records for the current user, newest first
    history_records = list(history_collection.find({"username": username}).sort("timestamp", -1))

    if not history_records:
        st.info("No detection record found.")
        return

    # Convert records to DataFrame
    data = []
    for record in history_records:
        timestamp = record.get("timestamp")
        if isinstance(timestamp, datetime):
            formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        else:
            formatted_time = "N/A"

        data.append({
            "URL": record.get("url", "N/A"),
            "Prediction": record.get("prediction", "N/A"),
            "Confidence (%)": round(record.get("confidence", 0.0), 2),
            "Timestamp": formatted_time
        })

    df = pd.DataFrame(data)

    # --- Filter section ---
    with st.expander("🔍 Filter Options", expanded=True):
        search_url = st.text_input("Search by URL keyword")
        prediction_filter = st.selectbox("Filter by Prediction", ["All", "Phishing", "Legitimate"])

        if search_url:
            df = df[df["URL"].str.contains(search_url, case=False)]

        if prediction_filter != "All":
            df = df[df["Prediction"] == prediction_filter]

    # Display the table
    st.dataframe(df, use_container_width=True)
