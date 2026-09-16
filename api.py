from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.6-flash",  # ← Modèle le plus récent et rapide
    contents="Explique-moi les réseaux de neurones en une phrase"
)

print(response.text)