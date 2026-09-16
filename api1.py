from dotenv import load_dotenv
import os
import requests
import json

# Charger la clé API
load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")

# URL de l'API Gemini
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={api_key}"

# Les en-têtes (headers)
headers = {
    "Content-Type": "application/json"
}

# Le corps de la requête (payload)
payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Explique-moi les réseaux de neurones en une phrase"
                }
            ]
        }
    ]
}

# Envoyer la requête POST
response = requests.post(url, headers=headers, json=payload)

# Vérifier si ça a marché
if response.status_code == 200:
    # Parser la réponse JSON
    data = response.json()
    # Extraire le texte
    texte = data["candidates"][0]["content"]["parts"][0]["text"]
    print(texte)
else:
    print(f"Erreur {response.status_code}: {response.text}")