import streamlit as st
import openai
import os

st.title("Legal Document Analyzer")

openai.api_key = os.getenv("OPENAI_API_KEY")

text = st.text_area("Paste a section of your legal document")

if text:
    prompt = f"Summarize this legal document section in plain English and highlight any vague or risky terms:\n\n{text}"
    with st.spinner("Analyzing document..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.success(response.choices[0].message["content"])
