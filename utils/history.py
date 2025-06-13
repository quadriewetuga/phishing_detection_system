import streamlit as st
from pymongo import MongoClient
from datetime import datetime, timezone

# MongoDB setup
client = MongoClient(st.secrets["mongo"]["uri"])
db = client["phishing_app"]  # Use the same DB name as in auth.py
collection = db["detection_history"]

def save_detection_history(username, url, prediction_label, confidence):
    record = {
        "username": username,
        "url": url,
        "prediction": prediction_label,
        "confidence": confidence,
        "timestamp": datetime.now(timezone.utc)
    }
    collection.insert_one(record)

def get_user_history(username):
    return list(collection.find({"username": username}).sort("timestamp", -1))

