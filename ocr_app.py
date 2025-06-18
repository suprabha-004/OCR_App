import streamlit as st
from PIL import Image
import pytesseract
import os

# Set Tesseract command path if on Windows
# Uncomment and edit the line below if needed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.set_page_config(page_title="Image to Text OCR", layout="centered")

st.title("📄 Image to Text Converter (OCR)")

st.markdown("Upload an image file, and we'll extract the text using Tesseract OCR.")

uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
 

    with st.spinner("Extracting text..."):
        extracted_text = pytesseract.image_to_string(image)

    st.success("Text extracted!")

    st.subheader("✍️ Editable Extracted Text")
    editable_text = st.text_area("You can edit the extracted text below:", value=extracted_text, height=300)

    if st.button("Download Text as .txt"):
        st.download_button(
            label="📥 Download",
            data=editable_text,
            file_name="extracted_text.txt",
            mime="text/plain"
        )
