from sqlmodel import Session
from ..conf.database import engine
from ..models.user import User, UserPatch


'''

def create_user():
    with Session(engine) as session:
        robin = User(full_name="Robin Dupont", email="robin.dupont@example.com")    # créer une instance de User
        session.add(robin)                                                          # ajouter l'utilisateur à la session
        session.commit()                                                            # valider la transaction

        '''

def create_user(full_name= "Robin Dupont", email= "robin.dupont@example.com"):
    with Session(engine) as session:
        robin = User(full_name=full_name, email=email)                              # créer une instance de User
        session.add(robin)                                                          # ajouter l'utilisateur à la session
        session.commit()   


def get_all_user()
    pass

# SELECT + FROM users

#WHERE full_name = "Robin Dupont" AND id = "robin.dupont@example.com"

def get_user_by_id(user_id: int):
    requete_preparere = select(User).where(User.full_name == "Robin Dupont" and User.id == user_id)  
    resultat = session.execute(requete_preparere).scalars().first()  
    return resultat


def patch_user_by_id(user_id: int, mod_user: UserPatch):
    pass

def delete_user_by_id(user_id: int):
    pass