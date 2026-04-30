import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def analyze_input(uploaded_file, pasted_text, language, mode):
    from prompt_builder import build_prompt

    prompt = build_prompt(language, mode)

    contents = []

    # Text part
    if pasted_text:
        contents.append(pasted_text)
    else:
        contents.append(prompt)

    # Image part (FIXED)
    if uploaded_file:
        image_bytes = uploaded_file.read()

        image_part = types.Part.from_bytes(
            data=image_bytes,
            mime_type=uploaded_file.type
        )

        contents = [prompt, image_part]

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=contents
    )

    return response.text