
---

##  LECON API AND KEYS API - BILAN COMPLET

```markdown
# 🔑 API AND KEYS API - BILAN COMPLET

## Table des matières
1. [Qu'est-ce qu'une Clé API](#1-quest-ce-quune-clé-api)
2. [Sécuriser les Clés API](#2-sécuriser-les-clés-api)
3. [Variables d'Environnement](#3-variables-denvironnement)
4. [SDK vs HTTP Brut](#4-sdk-vs-http-brut)
5. [Comprendre le JSON](#5-comprendre-le-json)
6. [Les Headers HTTP](#6-les-headers-http)
7. [Gestion des Erreurs](#7-gestion-des-erreurs)
8. [Obtenir une Clé API](#8-obtenir-une-clé-api)
9. [Documentations](#9-documentations)

---

## 1. QU'EST-CE QU'UNE CLÉ API

### Définition
Chaîne unique qui :
1. **Identifie** ton compte
2. **Autorise** tes requêtes
3. **Permet le suivi** de l'utilisation et la facturation

### Exemples
sk-ant-abc123... (Anthropic)
sk-proj-xyz789... (OpenAI)
AQ.Ab8RN6... (Google Gemini)

### Comment obtenir une clé API ?  

 Google Gemini (Gratuit)
 htpps://aistudio.google.com/app/apikey
 "Create API Key"
 Copier la clé
 .env: GOOGLE_API_KEY=ta_clé

OpenAI(Payant)
https://platform.openai.com/api-keys
"Create new secret key"
Copier la clé
.env:OPEN_AI_KEY=ta-clé

Anthropic (Payant)
https://console/anthropic/com
"Get API Keys"
"Create Key"
Copier immédiatement
.env:ANTHROPIC_API_KEY=ta-clé


### ⚠️ DANGER
Si quelqu'un vole ta clé → Il l'utilise à ta place → **TU SERAS FACTURÉ**

---

## 2. SÉCURISER LES CLÉS API

### Règle d'or
> **NE JAMAIS** mettre une clé API dans le code ou sur GitHub

### Méthode : Fichier .env

**1. Créer `.env`** (racine du projet)
```env
GOOGLE_API_KEY=AQ.Ab8RN6...
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-proj-...

Ajouter au .gitignore
.env
### Commiter .gitignore (pas .env)

git add .gitignore
git commit -m "🔒 Sécurisation des clés API"
git push

```VARIABLES D'ENVIRONNEMENT
 .env[Stocke la clé] (disque) → load_dotenv()[Charge dans Windows] → Windows (mémoire) → os.environ.get()[Récupère la clé] → Code

 Code complet
  from dotenv import load_dotenv
  import os

  load_dotenv()
  api_key = os.environ.get("GOOGLE_API_KEY")

##SDK VS HTTP BRUT
 Software Development Kit = Package qui simplifie l'utilisation d'une API

| Aspect| SDK |HTTP Brut
|Simplicité|Très simple| verbeux
|Contrôle|Limité| Total
|Débogage|Moins transparent|Tu vois tout

Exemple SDK (Google Gemini)
from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explique-moi les réseaux de neurones"
)

print(response.text)

Exemple HTTP Brut(Google Gemini)
from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.environ.get("GOOGLE_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={api_key}"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Explique-moi les réseaux de neurones"
                }
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()
    texte = data["candidates"][0]["content"]["parts"][0]["text"]
    print(texte)
else:
    print(f"Erreur {response.status_code}: {response.text}")

###COMPRENDRE LE JSON
Qu'est-ce que le JSON ?
JavaScript Object Notation = Format standard pour échanger des données entre les programmes
JSON est un format de données structurés
 Structure
 {
  "cle": "valeur",
  "liste": [1, 2, 3],
  "objet": {
    "sous-cle": "sous-valeur"
  }
} 
En Python
# Envoyer
data = {"texte": "ma question"}
requests.post(url, json=data)  # Transforme en JSON

# Recevoir
response = requests.get(url)
data = response.json()  # Transforme en dictionnaire Python

###LES HEADERS HTTP
Les headers HTTP sont des informations qui sont envoyées avec chaque requête HTTP_À quoi ça sert ?
Métadonnées de la requête (comme l'enveloppe d'une lettre)
 Exemple:
 headers = {
    "Content-Type": "application/json",  # "Je t'envoie du JSON"
    "Authorization": f"Bearer {api_key}"  # "Voici ma clé"
}

Où mettre la clé API ?
API | Emplacement
Gemini |URL:?key=TA_CLÉ
Anthropic |Headers : x-api-key: sk-ant-...
OpenAI | Headers : Authorization: Bearer sk-proj-...

###GESTION DES ERREURS
 Codes d'erreur courants
 Code|Signification|Cause
 200|Succès| - 
 400|Bad request|Format JSON incorrect
 401|Unauthorized|Clé API invalide
 403|Forbidden|Pas de permissions
 404|Not Found|Modèles inexistants
 429|Too Many Requests|Rate_limit trop de requêtes
 451|Unavailable For Legal Reasons|Pas de connexion
 500|Internal Server Error|Erreur interne du serveur
 502|Bad Gateway|Erreur de connexion au serveur
 503|Service Unavailable|Serveur indisponible       

###DOCUMENTATIONS
API |Documentation
Google Gemini|https://ai.google.dev/docs
Gemini Rest API|https://ai.google.dev/api/rest/v1beta/models/generateContent
OpenAI|https://platform.openai.com/docs
Anthropic|https://docs.anthropic.com
Mistral|https://docs.mistral.ai

CHEAT SHEET API

Avec SDK

from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Ta question"
)
print(response.text)

Avec HTTP Brut

import requests

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent"
params = {"key": os.environ.get("GOOGLE_API_KEY")}
data = {"contents": [{"parts": [{"text": "Ta question"}]}]}

response = requests.post(url, params=params, json=data)

if response.status_code == 200:
    print(response.json()["candidates"][0]["content"]["parts"][0]["text"])

🎯 RÈGLES D'OR
Toujours utiliser .env pour les clés API
Toujours ajouter .env à .gitignore
Ne jamais partager sa clé API
Toujours gérer les erreurs (try/except)
Consulter la documentation en cas de problème