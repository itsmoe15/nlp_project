import streamlit as st
import os
from newsclassifier import Classifier

model = Classifier()

st.set_page_config(
    page_title="News Topic Classifier",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("📰 News Classifier")

tab_text, tab_pdf = st.tabs(["📝 Text", "📄 PDF"])

with tab_text:
    text = st.text_area("Enter text to classify", height=200)
    if st.button("Predict Text", key="text"):
        with st.spinner("Classifying text…"):
            label, scores = model.predict(text)
        st.markdown(f"### 🔍 Predicted Category: **{label}**")
        st.markdown("#### 📊 Also Related to:")
        for cat, score in sorted(scores.items(), key=lambda x: x[1], reverse=True)[1:4]:
            st.write(f"- **{cat}**: {score*100:.4f}%")

with tab_pdf:
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
    if pdf_file and st.button("Predict PDF", key="pdf"):
        tmp_path = pdf_file.name
        with open(tmp_path, "wb") as f:
            f.write(pdf_file.getbuffer())
        with st.spinner("Extracting text & classifying…"):
            label, scores = model.predict_from_pdf(tmp_path)
        os.remove(tmp_path)
        st.markdown(f"### 🔍 Predicted Category: **{label}**")
        st.markdown("#### 📊 Also Related to:")
        for cat, score in sorted(scores.items(), key=lambda x: x[1], reverse=True)[1:4]:
            st.write(f"- **{cat}**: {score*100:.4f}%")
