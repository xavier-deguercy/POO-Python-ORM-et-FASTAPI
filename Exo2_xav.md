## **🧪 Exercice 2 – Mise en place de l’environnement projet**

---

### **🧩 <u>Partie 1 – Création de l’environnement</u>**

1. Créer et activer un environnement virtuel Python dédié au projet.
2. Installer les dépendances nécessaires :
   * FastAPI, SQLModel, Uvicorn (serveur ASGI)
   * Toute autre bibliothèque utile (ex : pymysql, python-dotenv, etc.)
3. Figer les dépendances dans un fichier `requirements.txt`.
4. Mettre en place une structure de projet claire et organisée.
   ```bash
   mon-projet-api/
   ├── src/              # code source de l'application
   │   ├── main.py       # point d'entrée de l'application
   │   ├── models/       # models et schémas SQLModel
   │   ├── repositories/ # logique de manipulation des models
   │   ├── services/     # logique métier
   │   ├── routes/       # endpoints FastAPI
   │   ├── conf/         # gestion de la configuration (Ex: .env, bdd, etc.)
   │   └── utils/        # fonctions utilitaires
   ├── tests/
   │   ├── conftest.py   # configuration des tests unitaires
   │   └── test_*.py     # tests unitaires d'un model jusqu'à l'endpoint
   ├── .env              # variables d'environnement (ex : BDD credentials)  
   ├── requirements.txt  # liste des dépendances
   └── README.md         # documentation du projet
   ```

<br>






### ------ -------- ------ ###
### ------ Reponses ------ ###
### ------ -------- ------ ###

```
# 0) Création structure projet
$ProjectName = "mon-projet-api"
$ProjectPath = Join-Path (Get-Location) $ProjectName

New-Item -ItemType Directory -Force -Path $ProjectPath | Out-Null
Set-Location $ProjectPath

New-Item -ItemType Directory -Force -Path `
  "src",
  "src\models",
  "src\repositories",
  "src\services",
  "src\routes",
  "src\conf",
  "src\utils",
  "tests" | Out-Null

New-Item -ItemType File -Force -Path `
  ".env",
  "requirements.txt",
  "README.md",
  ".gitignore",
  "src\__init__.py",
  "src\models\__init__.py",
  "src\repositories\__init__.py",
  "src\services\__init__.py",
  "src\routes\__init__.py",
  "src\conf\__init__.py",
  "src\utils\__init__.py",
  "src\main.py",
  "tests\conftest.py",
  "tests\test_health.py" | Out-Null


# 1) Créer et activer un environnement virtuel Python dédié au projet
python -m venv .venv

# Activation (PowerShell / VSCode sous Windows)
try {
  .\.venv\Scripts\Activate.ps1
} catch {
  # Si l’activation est bloquée, je débloque seulement pour ce terminal
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
  .\.venv\Scripts\Activate.ps1
}

# Recommandé : pip à jour
python -m pip install --upgrade pip


# 2) Installer les dépendances nécessaires
# FastAPI, SQLModel, Uvicorn + libs utiles
pip install fastapi sqlmodel "uvicorn[standard]" python-dotenv pymysql

# (utile pour tes tests)
pip install pytest httpx

# (option) Après clonage, pour réinstaller :
# pip install -r requirements.txt


# 3) Figer les dépendances dans requirements.txt
pip freeze > requirements.txt

```












### **🧩 <u>Partie 2 – MVP</u>**

1. Un endpoint FastAPI `/health` dans `src/main.py` qui retourne un succes avec le message `"status": "ok"`.
   
   
   ```python
   from fastapi import FastAPI
   app = FastAPI()
   @app.get("/health")
   async def health_check():
      return {"status": "ok"}


   ```
2. Lancer l’application avec Uvicorn et vérifier que l’endpoint fonctionne : `uvicorn src.main:app --reload`
3. Accéder à l’interface Swagger via l’URL `/docs` et vérifier que l’endpoint `/health` y est bien listé.  
   [http://localhost:8000/docs](http://localhost:8000/docs)

<div style="page-break-after: always;"></div>



PS .\POO-Python-ORM-et-FASTAPI> cd .\mon-projet-api\
PS .\POO-Python-ORM-et-FASTAPI\mon-projet-api> .\.venv\Scripts\activate
(.venv) PS C:\Users\xavie\Dropbox\projet_perso_xavier\POO-Python-ORM-et-FASTAPI\mon-projet-api> uvicorn src.main:app --reload