# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 16:51:09 2025

@author: AFTAB MOMIN
"""

import pickle 
import streamlit as st

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app setup
st.set_page_config(page_title="NLP Text Classifier", layout="centered")
st.title("📝 NLP Text Classifier (TF-IDF + Naive Bayes)")


# User input
text_input = st.text_area("Enter your text here:")

if st.button("Predict"):
    if text_input.strip() == "":
        st.warning("⚠️ Please enter some text.")
    else:
        # Predict using the pipeline
     prediction = model.predict([text_input])[0]

     # Map numeric prediction to label
     label_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
     sentiment = label_map.get(prediction, "Unknown")

     st.success(f"💬 Predicted Sentiment: **{sentiment}**")