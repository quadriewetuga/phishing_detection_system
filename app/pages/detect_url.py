# app/pages/detect_url.py

import streamlit as st
import joblib
import os
import numpy as np
import sys

# Set Streamlit page config FIRST
st.set_page_config(page_title="Phishing Detection", layout="centered")

# Add root path to import from utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Import the exact feature extractor used during training
from utils.feature_engineering import extract_features

# Load trained model
MODEL_PATH = os.path.join("models", "random_forest_model.pkl")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()

# Page title
st.title("🔎 Phishing URL Detection")

# User input
url_input = st.text_input("Enter a URL to check:")

if st.button("Check URL"):
    if url_input.strip() == "":
        st.warning("Please enter a URL.")
    else:
        try:
            features_dict = extract_features(url_input)
            feature_array = np.array(list(features_dict.values())).reshape(1, -1)

            prediction = model.predict(feature_array)[0]

            if prediction == 1:
                st.error("🚨 The URL is **likely phishing**!")
            else:
                st.success("✅ The URL appears to be **legitimate**.")
        except Exception as e:
            st.error(f"❌ Error extracting features: {e}")
