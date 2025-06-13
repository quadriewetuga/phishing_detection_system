import streamlit as st
from pymongo import MongoClient

# Mongo connection
MONGO_URI = st.secrets["mongo"]["uri"]
client = MongoClient(MONGO_URI)
db = client["phishing_app"]

st.title("🧪 MongoDB Data Viewer")

# Show collections
collections = db.list_collection_names()
st.write("📂 Collections found:", collections)

# View users collection
if "users" in collections:
    st.subheader("👥 Users Collection")
    users = list(db.users.find({}, {"_id": 0}))  # Hides _id field
    if users:
        st.json(users)
    else:
        st.info("No users found.")
else:
    st.warning("No 'users' collection found.")

# View history collection
if "history" in collections:
    st.subheader("📜 History Collection")
    history = list(db.history.find({}, {"_id": 0}))
    if history:
        st.json(history)
    else:
        st.info("No history entries found.")
else:
    st.warning("No 'history' collection found.")
