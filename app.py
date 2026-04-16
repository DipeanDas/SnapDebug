import streamlit as st
from gemini_client import analyze_image
from utils import validate_input

st.title("SnapDebug")
st.markdown("Upload snap of code erros and let AI debug it for you")

uploaded_file = st.file_uploader(
    "Upload error screenshot",
    type=["png", "jpg", "jpeg"]
)

mode = st.radio(
    "Choose response type:",
    ["Hints", "Solution with code"]
)

debug_btn = st.button("Debug Code")

if debug_btn:

    if not validate_input(uploaded_file, mode):
        st.error("Please upload an image and select an option.")
    else:
        with st.spinner("Analyzing error..."):

            image_bytes = uploaded_file.read()

            result = analyze_image(
                image_bytes,
                uploaded_file.type,
                mode
            )

            st.markdown("## Debug Result")
            st.markdown(result)