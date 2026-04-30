def validate_input(uploaded_file, pasted_text):
    if uploaded_file is None and (pasted_text is None or pasted_text.strip() == ""):
        return False
    return True