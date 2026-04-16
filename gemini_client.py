import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def analyze_image(image_bytes, mime_type, mode):
    from prompt_builder import build_prompt

    prompt = build_prompt(mode)

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            prompt,
            {
                "mime_type": mime_type,
                "data": image_bytes
            }
        ]
    )

    return response.text