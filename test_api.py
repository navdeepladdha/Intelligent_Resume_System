import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load variables from .env (if present)
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
print("API key loaded:", bool(api_key))
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY is not set")

# Configure Gemini
genai.configure(api_key=api_key)

# Use a model that we KNOW exists from your list
MODEL_NAME = "models/gemini-2.5-flash"

print(f"Using model: {MODEL_NAME}")

model = genai.GenerativeModel(MODEL_NAME)

response = model.generate_content("Hello! Give me one short sentence so I can test the API.")
print("\nModel response:\n")
print(response.text)
