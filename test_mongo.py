import streamlit as st
from pymongo import MongoClient

client = MongoClient(st.secrets["mongo"]["uri"])
db = client["phishing_app"]

try:
    print("Collections:", db.list_collection_names())
    print("Connection: ✅ Success")
except Exception as e:
    print("❌ Connection failed:", e)
