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


# ---------- cette partie est hors cadre (squelette minimal) ----------

# 5) Contenu minimal des fichiers
@"
.venv/
__pycache__/
*.pyc
.env
.pytest_cache/
"@ | Set-Content -Encoding utf8 .gitignore

@"
# Exemple de configuration
# SQLite:
DATABASE_URL=sqlite:///./app.db

# Exemple MySQL (PyMySQL) :
# DATABASE_URL=mysql+pymysql://user:password@localhost:3306/dbname
"@ | Set-Content -Encoding utf8 .env

@"
from fastapi import FastAPI

app = FastAPI(title="Mon API Utilisateurs")

@app.get("/health")
def health():
    return {"status": "ok"}
"@ | Set-Content -Encoding utf8 src\main.py

@"
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}
"@ | Set-Content -Encoding utf8 tests\test_health.py

@"
# $ProjectName

API REST Utilisateurs - FastAPI + SQLModel

## Installation
1) python -m venv .venv
2) activer le venv
3) pip install -r requirements.txt

## Lancer
uvicorn src.main:app --reload
"@ | Set-Content -Encoding utf8 README.md


# 6) Vérifications rapides
Write-Host "`n✅ Vérif imports..."
python -c "import fastapi, sqlmodel, uvicorn, dotenv; print('OK: fastapi/sqlmodel/uvicorn/dotenv')"
python -c "import pymysql; print('OK: pymysql')"

Write-Host "`n✅ Setup terminé."
Write-Host "➡️ Lancer l'API : uvicorn src.main:app --reload"
Write-Host "➡️ Tester : http://127.0.0.1:8000/health"
Write-Host "➡️ Lancer les tests : pytest"
