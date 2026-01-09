from sqlmodel import Session
from ..conf.database import engine
from ..models.user import User


'''

def create_user():
    with Session(engine) as session:
        robin = User(full_name="Robin Dupont", email="robin.dupont@example.com")    # créer une instance de User
        session.add(robin)                                                          # ajouter l'utilisateur à la session
        session.commit()                                                            # valider la transaction

        '''

def create_user(full_name= "xx", email= "xx@xx.com"):
    with Session(engine) as session:
        robin = User(full_name=full_name, email=email)                              # créer une instance de User
        session.add(robin)                                                          # ajouter l'utilisateur à la session
        session.commit()   