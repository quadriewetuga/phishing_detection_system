import streamlit as st

def render_about_page():
    st.title("About Phishing Detection System")

    with st.expander("📌 Project Overview", expanded=True):
        st.markdown("""
        The **Phishing Detection System** is a smart web-based application designed to help users identify and avoid phishing websites in real-time.  
        By analyzing the structure and characteristics of a given URL, the system uses machine learning to determine whether the link is **legitimate or potentially malicious**.

        This system empowers everyday users with the ability to detect threats **before** clicking harmful links — making the web safer, one URL at a time.
        """)

    with st.expander("🚨 Problem Statement & Motivation"):
        st.markdown("""
        Phishing attacks are among the most common and dangerous threats on the internet today.  
        Cybercriminals use deceptive links to trick users into revealing sensitive information such as passwords, credit card numbers, or personal data.

        Despite growing awareness, many users still struggle to recognize phishing URLs.  
        Traditional security tools may miss new or cleverly disguised threats — especially when attacks evolve rapidly.

        This project was developed to **bridge that gap** by giving users a fast, reliable tool to analyze URLs and protect themselves from being deceived.
        """)

    with st.expander("🎯 Objectives"):
        st.markdown("""
        The main objectives of this phishing detection system are:

        - 🔎 **Accurately detect** whether a URL is phishing or legitimate using machine learning.
        - ⚡ **Provide real-time feedback** to users in a simple, user-friendly interface.
        - 📁 **Allow registered users** to track their detection history.
        - 🔐 **Ensure user privacy and secure handling** of scanned URLs and login credentials.
        - 🌐 **Make phishing detection accessible** even to non-technical users.
        """)

    with st.expander("🛠️ How to Use the Web App"):
        st.markdown("""
        Using this phishing detection system is simple and straightforward. Follow these steps:

        1. **Create an Account / Log In**  
           Sign up with a secure password or log in to your existing account to access the full features.

        2. **Navigate to the Detection Dashboard**  
           Use the sidebar or the “Start Detection” button on the Home page to go to the detection section.

        3. **Enter a URL**  
           Paste the URL you want to check in the input box.

        4. **Run the Detection**  
           Click the **Detect** button. The system will analyze the URL using a machine learning model.

        5. **View the Result**  
           See whether the URL is marked as **Phishing** or **Legitimate** — along with a confidence score and helpful visual indicators.

        6. **Track Your History**  
           Logged-in users can revisit the **History** page to view a list of all previously scanned URLs and their results.

        🔒 All user data is handled securely and kept private.
        """)

    with st.expander("🧠 How It Works (Architecture Overview)"):
        st.markdown("""
        When a user enters a URL for analysis, the system follows these major steps:

        1. **URL Feature Extraction**  
           The system breaks down the URL into various characteristics — such as structure, length, number of symbols, presence of suspicious keywords, etc.

        2. **Prediction Using Trained Model**  
           These features are passed to a pre-trained machine learning model that evaluates them and predicts whether the URL is **phishing** or **legitimate**.

        3. **Confidence Scoring**  
           The system also provides a **confidence score** to show how sure it is about the prediction — giving users more context.

        4. **Result Presentation**  
           Results are shown instantly with clear color indicators, text output, and a visual confidence chart.

        5. **User Activity Logging**  
           For registered users, the system stores scanned URLs and predictions to allow review in the **History** section.

        This behind-the-scenes flow enables the system to make quick and accurate decisions with minimal user effort.
        """)

    with st.expander("📊 Model Summary"):
        st.markdown("""
        The phishing detection system is powered by a supervised machine learning model trained on a large dataset of phishing and legitimate URLs.

        - The model analyzes over **80 unique features** extracted from each URL.
        - These features capture everything from URL structure to suspicious patterns and behavior indicators.
        - The model was trained on thousands of examples to learn the difference between phishing and safe URLs.

        During training, the system achieved high accuracy and generalization, making it effective even against new or unseen threats.

        ⚠️ The model continuously evolves as more data is added and can be updated to stay effective over time.
        """)

    with st.expander("⚠️ Limitations"):
        st.markdown("""
        While the phishing detection system is highly effective, it’s important to understand its current limitations:

        - 🧠 **Model Bias**: The system's predictions are only as good as the data it was trained on. Some edge cases may be misclassified.
        - 🌐 **URL-Only Analysis**: The detection is based purely on URL characteristics — it does not analyze the actual content of the website.
        - ⌛ **Static Updates**: The model does not yet learn in real-time. Regular retraining is required to keep it up-to-date with new phishing trends.
        - 📶 **Internet Dependency**: The app requires an internet connection to work, especially for user authentication and backend processing.

        Despite these limitations, the system provides a powerful layer of protection and education for users against phishing threats.
        """)
