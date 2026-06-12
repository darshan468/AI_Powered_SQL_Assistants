
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

with open("models.txt", "w") as f:
    try:
        f.write("Listing available models...\n")
        import google.generativeai as genai # redundant but just in case
        for m in genai.list_models():
            f.write(f"{m.name}\n")
    except Exception as e:
        f.write(f"Error listing models: {str(e)}\n")
