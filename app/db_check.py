import streamlit as st
from pymongo import MongoClient

# Get Mongo URI from Streamlit secrets
MONGO_URI = st.secrets["mongo"]["uri"]
DB_NAME = "phishing_app"  # This is your actual DB name from the URI

def check_database():
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]

        st.title("🧪 MongoDB Structure Check")

        # Show all collections
        collections = db.list_collection_names()
        st.write("### 📂 Collections found:", collections)

        # Check sample from 'users'
        if 'users' in collections:
            st.write("### 👤 Sample user document:")
            st.json(db.users.find_one())
        else:
            st.warning("No 'users' collection found.")

        # Check sample from other collections (e.g., history, logs)
        for name in collections:
            if name != 'users':
                st.write(f"### 📜 Sample document from `{name}` collection:")
                st.json(db[name].find_one())
    except Exception as e:
        st.error(f"Failed to connect or fetch data: {e}")

check_database()
