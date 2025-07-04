import streamlit as st

# MUST be the very first Streamlit command
st.set_page_config(
    page_title="Phishing Detection System",
    layout="centered"
)

from app import login_signup, home, about, history, admin, dashboard
from utils.db import get_db  # Imported here to access MongoDB

# --- Session state defaults ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "user" not in st.session_state:
    st.session_state.user = "Guest"

# --- Sidebar navigation ---
def render_sidebar():
    with st.sidebar:
        st.markdown("## 🧭 Navigation")

        # Navigation buttons
        nav_options = ["Home", "Detection Dashboard", "History", "About", "Admin Page"]
        current = st.session_state.page if st.session_state.page in nav_options else "Home"

        for page in nav_options:
            if st.button(page, use_container_width=True, key=f"nav_{page}"):
                st.session_state.page = page
                st.rerun()

        # Profile section stays below navigation
        with st.expander("👤 Profile Options"):
            st.markdown(f"Hey👋, **{st.session_state.user}**")
            if st.button("Logout", key="logout_btn", use_container_width=True):
                st.session_state.clear()
                st.rerun()

# --- App routing ---
if st.session_state.logged_in:
    render_sidebar()

    if st.session_state.page == "Home":
        home.render_home_page(username=st.session_state.user)

    elif st.session_state.page == "Detection Dashboard":
        dashboard.render_dashboard()

    elif st.session_state.page == "History":
        history.render_history_page()

    elif st.session_state.page == "About":
        about.render_about_page()

    elif st.session_state.page == "Admin Page":
        admin.render_admin_page()

else:
    login_signup.show_login_signup()
