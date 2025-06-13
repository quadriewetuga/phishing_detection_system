# utils/db.py

import streamlit as st
from pymongo import MongoClient

def get_db():
    mongo_uri = st.secrets["mongo"]["uri"]
    client = MongoClient(mongo_uri)
    return client["phishing_app"]  # ✅ Corrected DB name
