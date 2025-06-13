import streamlit as st
from pymongo import MongoClient
from datetime import datetime, timezone

client = MongoClient(st.secrets["mongo"]["uri"])
db = client["phishing_app"]
collection = db["detection_history"]

# Dummy record
record = {
    "username": "quadri",
    "url": "http://example.com/test",
    "prediction": "Legitimate",
    "confidence": 98.7,
    "timestamp": datetime.now(timezone.utc)
}

collection.insert_one(record)

st.success("✅ Record inserted with timezone-aware UTC timestamp.")
