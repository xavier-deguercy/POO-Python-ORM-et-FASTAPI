from fastapi import FastAPI
from .routes.users_routes import users_routeur



app = FastAPI()                                          # instance de l'application FastAPI
app.include_router(users_routeur)


@app.get("/health")                                      # endpoint de vérification de l'état de santé de l'API. on ne sais pas si elle fonctionne ou pas 
                                                         # (on peut mettre de bot pour verifier si ca fonctionne encore)
async def health_check():                                # async car opération non bloquante
   return {"status": "ok"}                               # retourne un statut "ok" si l'API est en bonne santé


