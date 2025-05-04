"""
Main UI for the application using Streamlit.

Used the streamlit command: `streamlit run src/app.py` to run the app.
"""

import streamlit as st
from model import llm_resit_ocr


def main():
    st.title("Receipt Analyzer")
    col1, col2 = st.columns(2)
    
    with col1:
        st.text("Upload your receipt image here:")
        uploaded_file = st.file_uploader("Choose an image...", 
                                         type=["jpg", "jpeg", "png"])
        
        # read image as bytes
        if image_bytes := uploaded_file.read() if uploaded_file else None:
            st.image(image_bytes, caption="Uploaded Image")
        
    with col2:
        st.text("Receipt Content:")
        if image_bytes:
            receipt = llm_resit_ocr(image_bytes)
            st.json(receipt.model_dump())

main()