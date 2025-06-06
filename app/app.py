# app/app.py
import streamlit as st
import os
import sys

# Add the root directory to sys.path so we can import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import auth

#Set page config FIRST
st.set_page_config(page_title="Phishing Detection System", layout="centered")

# Initialize session state
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# ------------------ Login / Signup ------------------ #
if not st.session_state["authenticated"]:
    st.title("🛡️ Phishing Detection System")

    #Side-by-side radio for action selection
    col1, col2 = st.columns([1, 5])
    with col1:
        st.write("**Action**")
    with col2:
        action = st.radio("", ["Login", "Sign Up"], horizontal=True)

    #Dynamic heading
    if action == "Login":
        st.header("🔐 Login to your account")
    else:
        st.header("🆕 Create a new account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if action == "Sign Up":
        if st.button("Sign Up"):
            success, msg = auth.signup_user(username, password)
            if success:
                st.success(msg)
            else:
                st.error(msg)

    elif action == "Login":
        if st.button("Login"):
            success, msg = auth.login_user(username, password)
            if success:
                st.success(msg)
                st.session_state["authenticated"] = True
                st.session_state["username"] = username
                st.rerun()  #Updated method
            else:
                st.error(msg)

# ------------------ Main App Interface ------------------ #
else:
    st.sidebar.title("🔍 Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Detect URL", "Logout"])

    if page == "Home":
        st.title("🏠 Welcome")
        st.markdown(f"Hello, **{st.session_state['username']}**! 👋")
        st.markdown("Use the sidebar to navigate to the URL detection system.")

    elif page == "Detect URL":
        st.title("🔎 Phishing URL Detection")
        st.markdown("Coming soon: Enter a URL to check if it's phishing or legitimate.")

    elif page == "Logout":
        st.session_state["authenticated"] = False
        st.session_state["username"] = ""
        st.success("You have been logged out.")
        st.rerun()  #Updated method
