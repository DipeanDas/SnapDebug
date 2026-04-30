import streamlit as st
from gemini_client import analyze_input
from utils import validate_input

# --- Page Config ---
st.set_page_config(
    page_title="SnapDebug",
    layout="centered",
    page_icon="🐞"
)

# --- Custom CSS ---
st.markdown("""
<style>

/* Background */
body {
    background-color: #0f172a;
    color: white;
}

/* Title */
.title {
    font-size: 3.8rem;
    font-weight: 800;
    background: linear-gradient(90deg, #00f5a0, #00d9f5, #4facfe);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem;
    text-shadow: 0 0 20px rgba(0, 217, 245, 0.4);
    text-align: center;
}

/* Caption */
.caption {
    font-size: 1.3rem;
    color: #cbd5f5;
    margin-bottom: 1.5rem;
    text-align: center;
}

/* Card */
.card {
    background-color: #111827;
    padding: 22px;
    border-radius: 14px;
    box-shadow: 0 6px 25px rgba(0,0,0,0.4);
    margin-top: 20px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #00f5a0, #00d9f5);
    color: black;
    border: none;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: 600;
    width: 100%;
}

/* Expander title */
.streamlit-expanderHeader {
    font-size: 1.2rem;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# --- Main Header ---
st.markdown('<div class="title">SnapDebug</div>', unsafe_allow_html=True)
st.markdown('<div class="caption">Upload code or snap of code and let AI debug it for you!</div>', unsafe_allow_html=True)


# =========================
# 🔹 Sidebar (Inputs)
# =========================
st.sidebar.header("⚙️ Controls")

input_mode = st.sidebar.radio(
    "Input Type",
    ["Upload Screenshot", "Paste Code/Error"]
)

uploaded_file = None
pasted_text = None

if input_mode == "Upload Screenshot":
    uploaded_file = st.sidebar.file_uploader(
        "Upload screenshot",
        type=["png", "jpg", "jpeg"]
    )
    if uploaded_file:
        st.sidebar.divider()
        st.sidebar.markdown("### 🖼️ Preview")
        st.sidebar.image(uploaded_file, width="stretch")
else:
    pasted_text = st.sidebar.text_area(
        "Paste code / error",
        height=150
    )

language = st.sidebar.selectbox(
    "Language",
    ["Auto", "Python", "C++", "JavaScript", "Java"]
)

mode = st.sidebar.radio(
    "Response Type",
    ["Hints", "Solution"]
)

debug_btn = st.sidebar.button("Debug Now!")


# =========================
# 🔹 Result Section
# =========================
if debug_btn:

    if not validate_input(uploaded_file, pasted_text):
        st.error("Provide an image or paste code.")
    else:
        with st.spinner("Analyzing your error..."):

            result = analyze_input(
                uploaded_file,
                pasted_text,
                language,
                mode
            )

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Debug Result")

        sections = result.split("###")

        for sec in sections:
            if sec.strip():
                title, *content = sec.split("\n")
                content_text = "\n".join(content)

                with st.expander(title.strip(), expanded=True):

                    # Detect Code section
                    if "code" in title.lower():
                        st.code(content_text, language="python")

                        
                        st.download_button(
                            label="Copy Code",
                            data=content_text,
                            file_name="fixed_code.py",
                            mime="text/plain"
                        )
                    else:
                        st.markdown(content_text)

        st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<style>
.footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: #0f172a;
    text-align: center;
    padding: 10px;
    font-size: 0.9rem;
    color: #94a3b8;
    border-top: 1px solid #1f2937;
}
</style>

<div class="footer">
    App by Dipean Dasgupta | Powered by Google Gemini API
</div>
""", unsafe_allow_html=True)