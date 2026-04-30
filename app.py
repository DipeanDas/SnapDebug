import streamlit as st
from gemini_client import analyze_input
from utils import validate_input

st.set_page_config(page_title="SnapDebug", layout="centered")

st.title("SnapDebug")
st.caption("Upload code or snap of code and let AI debug it for you")

# --- Input Mode ---
input_mode = st.radio(
    "Choose input type:",
    ["Upload Screenshot", "Paste Code/Error"]
)

uploaded_file = None
pasted_text = None

if input_mode == "Upload Screenshot":
    uploaded_file = st.file_uploader(
        "Upload error screenshot",
        type=["png", "jpg", "jpeg"]
    )
else:
    pasted_text = st.text_area(
        "Paste your code / error here",
        height=200
    )

# --- Context ---
language = st.selectbox(
    "Language (optional):",
    ["Auto", "Python", "C++", "JavaScript", "Java"]
)

mode = st.radio(
    "Response type:",
    ["Hints", "Solution"]
)

debug_btn = st.button("Debug")

# --- Action ---
if debug_btn:

    if not validate_input(uploaded_file, pasted_text):
        st.error("Provide an image or paste code.")
    else:
        with st.spinner("Analyzing..."):

            result = analyze_input(
                uploaded_file,
                pasted_text,
                language,
                mode
            )

        st.divider()
        st.subheader("Result")

        # Expecting structured response
        sections = result.split("###")

        for sec in sections:
            if sec.strip():
                title, *content = sec.split("\n")
                with st.expander(title.strip(), expanded=True):
                    st.markdown("\n".join(content))