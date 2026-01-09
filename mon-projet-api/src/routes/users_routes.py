from ..models.user import User, UserPost, UserPatch
from fastapi import APIRouter

users_routeur = APIRouter()

@users_routeur.get("/users")                                       # endpoint pour récupérer tous les utilisateurs
def get_all_users() -> list[User]:                       # fonction pour récupérer tous les utilisateurs 
   return {"resultat": []}                               # retourne une liste vide pour l'instant

# query parameter ?active=False
@users_routeur.get("/users/{user_id}")                             # endpoint pour récupérer un utilisateur par son ID
def get_user_by_id(
    user_id: int, 
    active: bool):
   return {
      "id_mon_user": user_id,                            # id de l'utilisateur
      "active": active                                   # statut actif ou inactif, querry permet de faire des filtres
   }

@users_routeur.post("/users/")                                     # endpoint pour créer un utilisateur
def create_user(new_user: UserPost):                     # réceptionne un UserPost en entrée
   return {
      "Résultat": new_user
   }                                                     # retourne le nouvel utilisateur créé

### ---- pathuser

@users_routeur.patch("/users/{user_id}")
def patch_user_by_id(
    user_id: int,
    mod_user:UserPatch):
      return{
          "user_id" : user_id,
          "mod_user" : mod_user   

      }


### ----- delete_user


@users_routeur.delete("/users/{user_id}")
def delete_user_by_id(
    user_id: int
):
    return{
        "user_id" : user_id

    }