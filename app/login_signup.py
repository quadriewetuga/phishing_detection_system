import streamlit as st
from utils import auth

def show_login_signup():
    st.markdown("## Phishing Detection System")

    if "show_signup" not in st.session_state:
        st.session_state.show_signup = False

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login", key="login_btn_toggle"):
            st.session_state.show_signup = False
    with col2:
        if st.button("Sign Up", key="signup_btn_toggle"):
            st.session_state.show_signup = True

    st.markdown("---")

    if st.session_state.show_signup:
        show_signup()
    else:
        show_login()

def show_login():
    st.markdown("### Login")
    identifier = st.text_input("Username or Email", placeholder="Username or email", key="login_identifier")
    password = st.text_input("Password", type="password", placeholder="Enter your password", key="login_password")

    if st.button("Login", key="login_btn_submit"):
        if not identifier or not password:
            st.error("Please fill in all fields.")
            return

        success, message, username = auth.login_user_flexible(identifier, password)
        if success:
            st.session_state.logged_in = True
            st.session_state.username = username #the key to admin.py 
            st.session_state.user = username
            st.session_state.page = "Home"
            st.rerun()  # Trigger rerun
        else:
            st.error(message)

def show_signup():
    st.markdown("### Create a New Account")
    email = st.text_input("Email", placeholder="Enter your email address", key="signup_email")
    username = st.text_input("Username", placeholder="Choose a unique username", key="signup_username")
    password = st.text_input("Password", type="password", placeholder="Create a secure password", key="signup_password")

    if st.button("Sign Up", key="signup_btn_submit"):
        if not email or not username or not password:
            st.error("Please fill in all fields.")
            return

        success, message = auth.register_user(email, username, password)
        if success:
            st.success(message + " Please log in.")
            st.session_state.show_signup = False
        else:
            st.error(message)
