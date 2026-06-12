import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

try:
    print("Testing with gemini-pro...")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Hi")
    print("Success (gemini-pro):", response.text)
except Exception as e:
    print("Error (gemini-pro):", str(e))

try:
    print("\nListing available models...")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print("Error listing models:", str(e))
