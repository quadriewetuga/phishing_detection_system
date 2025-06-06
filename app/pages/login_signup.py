import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st

st.set_page_config(page_title="Phishing Detection System", layout="centered")

# App title
st.title("🛡️ Phishing Detection System")

# Side-by-side radio buttons with proper label
col1, col2 = st.columns([1, 5])
with col1:
    st.write("**Action**")
with col2:
    action = st.radio("Select Action", ["Login", "Sign Up"], horizontal=True, label_visibility="collapsed")

# Dynamic heading based on selected action
if action == "Login":
    st.header("🔐 Login to your account")
else:
    st.header("🆕 Create a new account")

# User input fields
username = st.text_input("Username", placeholder="Enter your Username")
password = st.text_input("Password", type="password", placeholder="Enter your Password")

# Handle login or signup
if action == "Sign Up":
    if st.button("Sign Up"):
        from utils import auth
        success, msg = auth.signup_user(username, password)
        if success:
            st.success(msg)
        else:
            st.error(msg)

elif action == "Login":
    if st.button("Login"):
        from utils import auth
        success, msg = auth.login_user(username, password)
        if success:
            st.success(msg)
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.rerun()
        else:
            st.error(msg)
