## **🧪 Exercice 1 – Analyse et conception d’une API REST Utilisateurs**

---

Tout d'abord, on va réfléchir à la conception d’une API REST simple pour gérer des utilisateurs.

<br>

### **🧩 <u>Partie 1 – Analyse critique d’une API</u>**

On vous fournit les endpoints `User` d’une API REST existante :

```
POST /getUser                       # Post sert a la creation de donnée
GET /deleteUser?id=12               # pour supprimer on utilise DELETE pas get
POST /updateUser                    # pour update on utilise PATCH
```

Identifier et expliquer brièvement pourquoi ces endpoints ne respectent pas les bonnes pratiques REST.

Les points suivants doivent notamment être abordés :
* l’utilisation des méthodes HTTP
* la structure des URLs
* la sémantique REST (ressources vs actions)
* le caractère complet ou incomplet des endpoints proposés

<br>

### ------ -------- ------ ###
### ------ Reponses ------ ###
### ------ -------- ------ ###



### ------ Notes ------ ###
POST /users                         # créer
GET /users                          # lister
GET /users/{id}                     # lire
PATCH /users/{id}                   # modifier 
DELETE /users/{id}                  # supprimer


### ------ Problèmes dans l’API fournie ------ ###


POST /getUser                       
#                                   # Post sert a la creation de donnée
#                                   # si je veux faire un get user, je ne le remat pas dans le nom
GET /deleteUser?id=12               
#                                   # GET doit être "safe" (sans effet de bord) : il ne doit jamais supprimer.
#                                   # La suppression se fait avec DELETE.
#                                   # En REST, l’identifiant est plutôt dans le chemin : /users/{id}.
POST /updateUser                    
#                                   # Pour une mise à jour, on utilise plutôt PATCH (partielle) ou PUT (complète).
#                                   #L’URL doit cibler la ressource : /users/{id}.


### ------ corectifs ------ ###


# POST /getUser remplacé par
GET /users/{id}                     # ou GET /users pour une liste
# GET /deleteUser?id=12
DELETE /users/12                    # 
# POST /updateUser
PATCH /users/{id}                   #


















<br>

### **🧩 <u>Partie 2 – Refonte et conception d’une API REST</u>**

Vous devez maintenant **reconcevoir cette API REST correctement** pour gérer des **utilisateurs**.

1. Proposer les endpoints REST permettant de :
   * créer un utilisateur
   * récupérer tous les utilisateurs
   * récupérer un utilisateur unique
   * mettre à jour un utilisateur
   * supprimer un utilisateur
2. Pour chaque endpoint, préciser :
   * la méthode HTTP
   * l’URL
   * le(s) code(s) HTTP attendu (succès/erreur)
3. Donner un exemple de payload JSON utilisé pour la création d’un utilisateur.

<br>



### ------ reposes ------ ###
### ------ 🧩 Partie 2 – Refonte et conception d’une API REST (Utilisateurs)

### ------ 1) Endpoints REST proposés (CRUD)

Je modélise la ressource **Utilisateur** via la collection `/users` et un utilisateur unique via `/users/{id}`.

---

### ------ Créer un utilisateur
- **Méthode HTTP :** `POST`
- **URL :** `/users`
- **Codes attendus :**
  - `201 Created` : utilisateur créé (souvent avec `Location: /users/{id}`)
  - `400 Bad Request` : mauvais format (JSON invalide, types incohérents, etc.)
  - `401 Unauthorized` : pas connecté
  - `403 Forbidden` : pas les droits
  - `409 Conflict` : utilisateur déjà créé (ex : email déjà existant)
  - `422 Unprocessable Entity` : JSON bien formé mais validation échoue (champs obligatoires vides, email invalide, contraintes métier)
  - `415 Unsupported Media Type` : mauvais `Content-Type` (ex : pas `application/json`)

> **Note :** `204 No Content` n’est pas attendu ici pour une création. Une création REST retourne généralement `201 Created`.

---

### ------ Récupérer tous les utilisateurs
- **Méthode HTTP :** `GET`
- **URL :** `/users`
- **Codes attendus :**
  - `200 OK` : liste des utilisateurs retournée (y compris liste vide `[]`)
  - `204 No Content` : aucun utilisateur à retourner (réponse sans corps)
  - `400 Bad Request` : paramètres de requête invalides (ex : pagination/tri)
  - `401 Unauthorized` : pas connecté
  - `403 Forbidden` : pas les droits
  - ~~`404 Not Found`~~ : non attendu sur la collection `/users` (la ressource existe, même si elle est vide)

> **Note (200 [] vs 204) :** les deux conventions existent.  
> - `200` renvoie un corps (ex : `[]`).  
> - `204` renvoie **zéro** corps.

---

### ------ Récupérer un utilisateur unique
- **Méthode HTTP :** `GET`
- **URL :** `/users/{id}`
- **Codes attendus :**
  - `200 OK` : utilisateur trouvé (retourne le JSON)
  - `400 Bad Request` : id invalide / mal formé
  - `401 Unauthorized` : pas connecté
  - `403 Forbidden` : pas les droits
  - `404 Not Found` : utilisateur inexistant

> **Note (400 vs 404) :**  
> - `400` : l’id n’a pas le bon format.  
> - `404` : l’id est valide mais aucune ressource ne correspond.

---

### ------ Mettre à jour un utilisateur
Je privilégie `PATCH` pour une mise à jour partielle.

- **Méthode HTTP :** `PATCH`
- **URL :** `/users/{id}`
- **Codes attendus :**
  - `200 OK` : utilisateur mis à jour
  - `400 Bad Request` : mauvais format
  - `401 Unauthorized` : pas connecté
  - `403 Forbidden` : pas les droits
  - `404 Not Found` : utilisateur inexistant
  - `409 Conflict` : conflit (ex : email déjà existant)
  - `422 Unprocessable Entity` : validation échoue (valeurs non conformes aux règles)

> **Note :** `201 Created` est plutôt associé à `PUT` dans certains cas (si on “crée/remplace” via l’URL). Ici, en `PATCH`, on attend `200 OK`.

---

### ------ Supprimer un utilisateur
- **Méthode HTTP :** `DELETE`
- **URL :** `/users/{id}`
- **Codes attendus :**
  - `200 OK` : suppression réussie (si l’API renvoie un message/JSON)
  - `204 No Content` : suppression réussie (sans corps)
  - `400 Bad Request` : id invalide / mal formé
  - `401 Unauthorized` : pas connecté
  - `403 Forbidden` : pas les droits
  - `404 Not Found` : utilisateur inexistant

---

### ------ 2) Récapitulatif rapide

- `POST /users` → `201` (erreurs `400/401/403/409/422/415`)
- `GET /users` → `200` ou `204` (erreurs `400/401/403`)
- `GET /users/{id}` → `200` (erreurs `400/401/403/404`)
- `PATCH /users/{id}` → `200` (erreurs `400/401/403/404/409/422`)
- `DELETE /users/{id}` → `200` ou `204` (erreurs `400/401/403/404`)

---

#### ------ 3) Exemple de payload JSON (création)

> **Contrainte projet :** `email` et `full_name` obligatoires. `age` et `is_active` optionnels.

**Payload complet :**
```json
{
  "email": "xavier.deguercy@gmail.com",
  "full_name": "Xavier Deguercy",
  "age": 39,
  "is_active": true
}

payload minimal
{
  "email": "xavier.deguercy@gmail.com",
  "full_name": "Xavier Deguercy"
}

