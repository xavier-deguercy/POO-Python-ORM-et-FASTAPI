from fastapi import FastAPI                              # importer FastAPI pour créer l'application
from .routes.users_routes import users_routeur           # importer le routeur des utilisateurs
from .conf.database import engine                        # importer l'engine de la base de données
from sqlmodel import SQLModel                            # importer SQLModel pour la gestion des modèles et des tables
from .models.user import User                            # importer le model User pour créer les tables dans la base de données


from .repositories.user_repository import create_user    # importer la fonction create_user du repository utilisateur



app = FastAPI()                                          # instance de l'application FastAPI
app.include_router(users_routeur)

SQLModel.metadata.create_all(engine)                     # création des tables dans la base de données


@app.get("/health")                                      # endpoint de vérification de l'état de santé de l'API. on ne sais pas si elle fonctionne ou pas 
                                                         # (on peut mettre de bot pour verifier si ca fonctionne encore)
async def health_check():                                # async car opération non bloquante
   return {"status": "ok"}                               # retourne un statut "ok" si l'API est en bonne santé


create_user()
   