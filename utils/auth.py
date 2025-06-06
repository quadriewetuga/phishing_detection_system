# utils/auth.py

import hashlib
from pymongo import MongoClient
import streamlit as st

# Secure MongoDB connection using secrets
MONGO_URI = st.secrets["mongo"]["uri"]
DB_NAME = "phishing_app"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
users_collection = db["users"]

def hash_password(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def signup_user(username, password):
    """Registers a new user if the username doesn't already exist."""
    if users_collection.find_one({"username": username}):
        return False, "Username already exists"

    hashed_pw = hash_password(password)
    users_collection.insert_one({"username": username, "password": hashed_pw})
    return True, "Signup successful"

def login_user(username, password):
    """Authenticates an existing user."""
    user = users_collection.find_one({"username": username})
    if not user:
        return False, "User not found"

    hashed_pw = hash_password(password)
    if hashed_pw == user["password"]:
        return True, "Login successful"
    return False, "Incorrect password"
