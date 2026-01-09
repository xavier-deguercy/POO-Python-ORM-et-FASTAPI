from sqlmodel import Field, SQLModel

class UserBase(SQLModel):
   full_name: str
   email: str
   age: int | None = None
   is_active: bool = True
   
# Schéma POST
class UserPost(UserBase):
   pass

# Schéma PATCH
class UserPatch(UserBase):
   full_name: str | None = None
   email: str | None = None
   
# model
class User(UserBase, table=True):
   id: int | None = Field(default=None, primary_key=True)