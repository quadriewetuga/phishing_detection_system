import streamlit as st
from pymongo import MongoClient
import hashlib

# Connect to MongoDB Atlas
client = MongoClient(st.secrets["mongo"]["uri"])
db = client["phishing_app"]
users_collection = db["users"]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login_user_flexible(identifier, password):
    """Login with either username or email."""
    hashed_pw = hash_password(password)
    user = users_collection.find_one({
        "$or": [{"username": identifier}, {"email": identifier}],
        "password": hashed_pw
    })
    if user:
        return True, "Login successful", user["username"]
    return False, "Invalid username/email or password"

def register_user(email, username, password):
    # Check if email already exists
    if users_collection.find_one({"email": email}):
        return False, "An account already exists with this email."

    # Check if username already exists
    if users_collection.find_one({"username": username}):
        return False, "Username is already taken."

    hashed_pw = hash_password(password)
    user_data = {
        "email": email,
        "username": username,
        "password": hashed_pw
    }

    users_collection.insert_one(user_data)
    return True, "User registered successfully"
