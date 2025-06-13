# 🛡️ Phishing Detection System

This is a machine learning-powered web application designed to detect phishing URLs in real time. It helps users quickly assess whether a website is legitimate or malicious using a trained Random Forest model.

## 🚀 Features

- 🔍 Real-time phishing detection
- 📊 Confidence scores and probability charts
- 🧠 Machine learning powered classification
- 🧾 Detection history tracking per user
- 🔐 Admin dashboard to manage users and access
- 🖥️ User-friendly Streamlit interface

## 🧪 How It Works

1. User enters a URL.
2. The system extracts 87+ handcrafted features.
3. A trained Random Forest model classifies the URL.
4. Confidence scores and visualizations are displayed.
5. Logged-in users have their scans saved to history.

## 📦 Project Structure

```bash
project_detection_system/
├── app/                 # Streamlit app pages
├── data/                # CSV datasets
├── models/              # Trained ML model (random_forest_model.pkl)
├── scripts/             # Training scripts
├── utils/               # Helper modules (auth, features, db, etc.)
├── .streamlit/          # Streamlit config (secrets.toml)
├── tests/               # Dev testing scripts (optional)
├── requirements.txt     # Python dependencies
├── setup.sh             # Startup script for deployment (optional)
├── README.md            # Project overview (this file)
└── streamlit_app.py     # Main entry point
