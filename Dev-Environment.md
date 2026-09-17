# 🛠️ ENVIRONNEMENT DE DÉVELOPPEMENT - BILAN COMPLET

## Table des matières
1. [Python avec UV](#1-python-avec-uv)
2. [Environnement Virtuel](#2-environnement-virtuel)
3. [Installation des Packages](#3-installation-des-packages)
4. [Node.js avec PNPM](#4-nodejs-avec-pnpm)
5. [Rust](#5-rust)
6. [Julia](#6-julia)
7. [Configuration VS Code](#7-configuration-vs-code)
8. [Git et .gitignore](#8-git-et-gitignore)

---

## 1. PYTHON AVEC UV

### Qu'est-ce que `uv` ?
Gestionnaire de packages Python ultra-rapide qui remplace `pip` et `venv`.

### Installation
```powershell
# Télécharger depuis https://docs.astral.sh/uv/
# pip install uv

Verification:
uv --version


# ENVIRONNEMENT VIRTUEL
Pourquoi un ".venv ?"
#
Isoler les packages de chaque projet
Éviter les conflits entre projets
Reproductibilité

création d'un environnement virtuel
uv venv

###Activation du virtualenv###

Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\activate

###Désactivation du virtualenv###
deactivate ###

###Installation de packages###

# Installer
uv pip install numpy torch 

# Lister
uv pip list

# Désinstaller
uv pip uninstall numpy
```
#Vérification
import numpy as np
print(np.__version__)

# NODE.JS AVEC PNPM
Installation de Node.js
```powershell
winget install OpenJS.NodeJS.LTS
node --version
npm --version

#Installation de fnm (Fast Node Manager)
```powershell
winget install Schniz.fnm
# Fermer et rouvrir PowerShell
fnm install 22
fnm use 22
fnm default 22

#Installation de pnpm
```powershell
npm install -g pnpm
pnpm --version

#Rust
Installer Rust
winget install Rustlang.Rustup
#Vérification
rustc --version
cargo --version
Gestionnaire
cargo (inclus avec Rust)

#Julia
Installation
winget install JuliaLang.Julia
#Vérification   
julia --version

#CONFIGURATION VS CODE
Changer l'interpréteur Python
Ctrl + Shift + P
Taper Python: Select Interpreter
Choisir celui avec .venv

##CHEAT SHEET
````
# === PYTHON ===
uv venv                              # Créer le .venv
.\.venv\Scripts\activate             # Activer
uv pip install numpy                 # Installer package
python mon_script.py                 # Exécuter

# === NODE.JS ===
fnm install 22                       # Installer Node
fnm use 22                           # Utiliser
npm install -g pnpm                  # Installer pnpm

# === RUST ===
rustc --version                      # Vérifier
cargo --version                      # Vérifier

# === JULIA ===
julia --version                      # Vérifier

# === GIT ===
git add .
git commit -m "message"
git push origin my_progress

#🎯 RÈGLES D'OR
#Toujours activer le .venv avant d'installer des packages
#Toujours utiliser le Python du .venv pour exécuter les scripts
#Vérifier avec where python que le bon Python est utilisé
#Ne jamais commiter .env sur GitHub
#Redémarrer PowerShell après installation de fnm
