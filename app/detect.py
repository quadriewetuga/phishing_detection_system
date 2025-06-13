import streamlit as st
import plotly.graph_objects as go
from utils.predictor import predict_url  # This should return (label, confidence)

def show_confidence_donut(confidence):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence * 100,
        number={'suffix': "%", 'font': {'size': 48, 'color': "#00ffff"}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#00ffff"},
            'bar': {'color': "#00ffff"},
            'bgcolor': "#0a0f24",
            'borderwidth': 2,
            'bordercolor': "#00ffff",
            'steps': [
                {'range': [0, 50], 'color': "#240a0a"},
                {'range': [50, 100], 'color': "#0a1f24"}
            ],
            'threshold': {
                'line': {'color': "#ff4b4b", 'width': 4},
                'thickness': 0.75,
                'value': confidence * 100
            }
        }
    ))
    fig.update_layout(
        paper_bgcolor="#0a0f24",
        height=400,
        margin=dict(t=0, b=0, l=0, r=0),
    )
    st.plotly_chart(fig, use_container_width=True)


def render_detection_page():
    st.markdown("<h1 style='color: #00ffff;'>🔎 URL Phishing Detection</h1>", unsafe_allow_html=True)
    st.write("Enter a URL below to check if it's legitimate or a phishing attempt.")

    url_input = st.text_input("🔗 Enter URL")

    if st.button("Check URL"):
        if url_input.strip() == "":
            st.warning("Please enter a valid URL.")
        else:
            label, confidence = predict_url(url_input)  # Make sure this returns (label, confidence)

            if label == 1:
                st.error("🚨 This URL is likely a phishing attempt.")
            else:
                st.success("✅ This URL appears to be safe.")

            st.markdown(f"<h4 style='color: cyan;'>Confidence Score</h4>", unsafe_allow_html=True)
            show_confidence_donut(confidence)
