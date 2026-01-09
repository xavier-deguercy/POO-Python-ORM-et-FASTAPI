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

### ------ Reponses ------ ###


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

### ------  1) Endpoints REST proposés (CRUD)

Je modélise la ressource **Utilisateur** via la collection `/users` et un utilisateur unique via `/users/{id}`.

---

### ------ Créer un utilisateur
- **Méthode HTTP :** `POST`
- **URL :** `/users`
- **Codes attendus :**
  - `201 Created` : utilisateur créé (souvent avec `Location: /users/{id}`)
  - `204 No Content` : **non recommandé** pour une création (plutôt utilisé quand on ne renvoie aucun contenu, mais en création REST on attend généralement `201`)
  - `401 Unauthorized` : non authentifié (si l’API exige une authentification)
  - `403 Forbidden` : authentifié mais non autorisé (ex : seul un admin peut créer)
  - `400 Bad Request` : JSON invalide / champs manquants / validation KO
  - `409 Conflict` : conflit (ex : email déjà utilisé)
  - `415 Unsupported Media Type` : mauvais `Content-Type` (ex : pas `application/json`)


---

### ------ Récupérer tous les utilisateurs
- **Méthode HTTP :** `GET`
- **URL :** `/users`
- **Codes attendus :**
  - `200 OK` : liste des utilisateurs retournée (y compris liste vide `[]`)
  - `204 No Content` : aucun utilisateur à retourner (réponse sans corps) *(si choisi dans la convention du projet)*
  - `400 Bad Request` : paramètres de requête invalides (ex : pagination/tri)
  - `401 Unauthorized` : pas authentifié (si l’API est protégée)
  - `403 Forbidden` : authentifié mais pas les droits

---

### ------ Récupérer un utilisateur unique
- **Méthode HTTP :** `GET`
- **URL :** `/users/{id}`
- **Codes attendus :**
  - `200 OK` : utilisateur trouvé (retourne le JSON de l’utilisateur)
  - `400 Bad Request` : id invalide / mal formé (ex : attendu un entier mais reçu "abc")
  - `401 Unauthorized` : pas authentifié (si l’API nécessite une connexion/token)
  - `403 Forbidden` : authentifié mais pas autorisé (droits insuffisants)
  - `404 Not Found` : utilisateur inexistant (id valide mais aucun utilisateur correspondant)

---

### ------  Mettre à jour un utilisateur
Je privilégie `PATCH` pour une mise à jour partielle.

- **Méthode HTTP :** `PATCH`
- **URL :** `/users/{id}`
- **Codes attendus :**
  - `200 OK` : utilisateur mis à jour (si je renvoie l’objet)
  - `204 No Content` : mise à jour OK (si je ne renvoie pas de corps)
  - `400 Bad Request` : données invalides
  - `404 Not Found` : utilisateur inexistant
  - `409 Conflict` : conflit (ex : email déjà utilisé)

> Alternative possible : `PUT /users/{id}` pour un remplacement complet.

---

### ------ Supprimer un utilisateur
- **Méthode HTTP :** `DELETE`
- **URL :** `/users/{id}`
- **Codes attendus :**
  - `204 No Content` : suppression réussie
  - `404 Not Found` : utilisateur inexistant

---

### ------  2) Récapitulatif rapide

- `POST /users` → `201` (erreurs `400/409/415`)
- `GET /users` → `200` (erreur possible `400`)
- `GET /users/{id}` → `200` (erreurs `404/400`)
- `PATCH /users/{id}` → `200` ou `204` (erreurs `400/404/409`)
- `DELETE /users/{id}` → `204` (erreur `404`)

---

#### ------ 3) Exemple de payload JSON (création)

```json
payload complet
{
  "firstName": "Xavier", 
  "lastName": "Deguercy",
  "email": "xavier.deguercy@gmail.com",
  "age" :,
  "is_active" : ,
}
payload minimal
{  
  "firstName": "Xavier", 
  "lastName": "Deguercy",
  "email": "xavier.deguercy@gmail.com",

}
