## **🧪 Exercice 5 – Liaison SQLModel & FastAPI + gestion des erreurs**

---

Maintenant que l'on a un SQLModel et un FastAPI fonctionnels, il est temps de les lier ensemble et de gérer les erreurs possibles.

### **🧩 <u>Partie 1 – Liaison entre FastAPI et SQLModel</u>**

Pour faciliter l’injection des dépendances et l’écriture de tests unitaires, nous allons **injecter la session SQLModel directement dans les endpoints** FastAPI.

* La fonction `get_session` ouvrira une session SQLModel et utilisera `yield` pour la maintenir ouverte le temps de l’opération.
* Chaque endpoint recevra la session via `Depends`.

```python
from fastapi import Depends
from sqlmodel import Session
from database import get_session

@app.get("/users/{user_id}")
async def get_user(user_id: int, session: Session = Depends(get_session)):
    ...
```

1. Créer la fonction `get_session` dans `src/database/session.py` qui :
   * ouvre une session SQLModel
   * la `yield` pour l’injection
   * ferme correctement la session après utilisation
2. Modifier vos endpoints FastAPI pour **injecter la session SQLModel** via `Depends(get_session)`.
3. Adapter vos fonctions de manipulation (CRUD) des utilisateurs pour **utiliser la session reçue en paramètre**.

### **🧩 <u>Partie 2 – Mapping des erreurs BDD vers des réponses API</u>**

Certaines opérations peuvent échouer. Nous allons gérer deux cas typiques :

1. **GET /users/{user_id}** : l’utilisateur demandé n’existe pas
2. **POST /users** : insertion échouée (ex : email déjà utilisé)

Pour chaque cas :

* Identifier l’erreur métier
* Associer un **code HTTP approprié**
* Définir un **message API clair et compréhensible**

> Exemple attendu pour GET inexistant :
> Code HTTP : `404`
> Message : `"Utilisateur non trouvé"`

> Exemple attendu pour POST avec email déjà utilisé :
> Code HTTP : `409`
> Message : `"Email déjà utilisé"`

<div style="page-break-after: always;"></div>
