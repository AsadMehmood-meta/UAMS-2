from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_KEY")

if not api_key:
    raise ValueError("GEMINI_KEY not found. Make sure it's defined in .env file.")

gemini = genai.Client(api_key=os.getenv("GEMINI_KEY"))

response = gemini.models.generate_content(
    model="gemini-2.5-flash", contents="tell me about rest api"
)
print(response.text)
