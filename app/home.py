# app/home.py
import streamlit as st

def render_home_page(username=None):
    st.title("Phishing Detection System")

    if username:
        st.markdown(f"<h3 style='color:#89CFF0;'>Welcome back, {username} 👋</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color:#89CFF0;'>Welcome to your cybersecurity dashboard 👋</h3>", unsafe_allow_html=True)

    st.markdown("""
        <div style='padding: 15px; border-radius: 10px; background-color: #1b263b; color: #e0f2f1; margin-top: 10px;'>
            <p>
                The internet is full of threats — phishing attacks being one of the most dangerous. These attacks trick users
                into revealing sensitive information like passwords, credit card numbers, and personal data. Our mission is to help
                you detect such attacks quickly and accurately.
            </p>
            <p>
                This Phishing Detection System uses a powerful machine learning model trained on real-world phishing and legitimate URLs.
                It's designed to identify subtle patterns that are often missed by traditional filters.
            </p>
            <p><strong>What this system offers you:</strong></p>
            <ul>
                <li>✅ Real-time phishing detection powered by advanced algorithms</li>
                <li>📈 Visual confidence reports to understand predictions</li>
                <li>🗂️ Track your history of scanned URLs</li>
                <li>🔐 Admin-level access control for added security</li>
            </ul>
            <p>
                Start using the detection dashboard to analyze suspicious URLs and protect your digital identity.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🚀 Ready to analyze a URL?")
    if st.button("Start Detection", key="start_detection_btn"):
        st.session_state.page = "Detection Dashboard"
        st.rerun()
