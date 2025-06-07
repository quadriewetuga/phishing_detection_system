import joblib
import numpy as np
import pandas as pd
from scripts.feature_engineering import extract_features  # adjust if path differs

# Load your model (adjust the path if needed)
model = joblib.load("models/random_forest_model.pkl")

def predict_url(url: str) -> int:
    # Extract features from the URL
    features_df = extract_features([url])  # make sure it returns a DataFrame
    features_array = features_df.values  # convert to NumPy array if needed
    prediction = model.predict(features_array)
    return int(prediction[0])  # Return 0 (legit) or 1 (phishing)
