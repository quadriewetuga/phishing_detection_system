import streamlit as st
from utils.predictor import predict_url

st.set_page_config(page_title="Phishing Detection System", layout="centered")
st.title("Phishing Detection System")

st.write("Enter a URL below to check if it's legitimate or a phishing attempt.")

url_input = st.text_input("🔗 Enter URL")

if st.button("Check URL"):
    if url_input.strip() == "":
        st.warning("Please enter a valid URL.")
    else:
        prediction = predict_url(url_input)  # make sure this function is defined correctly
        if prediction == 1:
            st.error("This URL is likely a phishing attempt.")
        else:
            st.success("This URL appears to be safe.")
