
from fastapi import FastAPI
from .models.user import User, UserPost, UserPatch

app = FastAPI() 

@app.post("/users/")
def create_user(new_user: UserPost): # body
   # UserPost.model_dump(new_user)
   return {
      "user": new_user
   }

@app.get("/health")
async def health_check(): 
   return {"status": "ok"}

@app.get("/users")
def get_all_users():
   return {"resultat": []}

# query parameter ?active=False
@app.get("/users/{user_id}")
def get_user_by_id(user_id: int, active: bool):
   return {
      "id_mon_user": user_id,
      "active": active
   }