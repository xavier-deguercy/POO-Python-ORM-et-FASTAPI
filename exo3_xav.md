## **🧪 Exercice 3 – Développement de l’API REST avec FastAPI**

---

Ensuite, on va implémenter l’API REST conçue précédemment en utilisant FastAPI.

Voici un payload JSON typique utilisé pour créer un utilisateur :  
```json
{
  "email": "user@test.com",
  "full_name": "John Doe",
  "age": 32,
  "is_active": true
}
```

<br>

### **🧩 <u>Partie 1 – Analyse des données</u>**

> ⚠️ Cette partie réflexion est à réaliser **avant toute écriture de code**.

1. Identifier les champs qui doivent être stockés en base de données.
2. Pour chaque champ, indiquer :
   * le type de données **SQLModel** approprié
   * la clé primaire
   * les contraintes évidentes (unique, nullable, valeurs obligatoires, etc.)

<br>

### **🧩 <u>Partie 2 – API et sécurité des données</u>**

> ⚠️ Toujours sans code, réponse attendue sous forme de points

Expliquer quels **risques potentiels** (fonctionnels et/ou sécurité) peuvent exister si :
* l’API accède directement aux tables de la base de données
* ou exécute des requêtes SQL construites à partir des données reçues des clients

<br>

### **🧩 <u>Partie 3 – Modélisation avec SQLModel</u>**

1. Dans le dossier `src/models/`, créer un fichier `user.py`.

2. Ensuite, proposer un ou plusieurs **schémas SQLModel** adaptés à cette API, en distinguant si nécessaire
   * `UserBase` _(super-classe abstraite)_  
   Champs communs à tous les schémas
   * `UserCreate` _(sous-classe conrete de UserBase)_  
   Champs nécessaires à la création (ex : ajout d’un mot de passe)
   * `UserPatch` _(sous-classe conrete de UserBase)_  
   Champs utilisés pour la mise à jour (tous optionnels)
   * `User` _(sous-classe conrete de UserBase)_  
   Schéma complet correspondant à la table réelle en base de données

> ❌ Il n’est **pas nécessaire** de créer un schéma `UserDelete`.  
> Les schémas ne servent que si un payload est attendu (création, mise à jour, etc.)

> 💡 Il peut parfois être intéressant de faire un `UserGet` (sous-classe de UserBase).   
> Ce sera un équivalent au Schéma `User`, mais sans champs sensibles (ex : password)

<br>

### **🧩 <u>Partie 4 – Implémentation FastAPI</u>**

1. Dans le dossier `src/routes/`, créer un fichier `user_routes.py`.
2. Ensuite, implémenter les endpoints FastAPI définis dans l’exercice 1 Partie 2 :
   * les schémas SQLModel définis précédemment
   * une logique claire de séparation entre API et base de données
3. Pour finir, importer et inclure les routes dans `src/main.py` afin qu’elles soient accessibles.

<br>

> 📌 *Aucune gestion d’authentification, de pagination ou de permissions n’est demandée.*
> On mettra en place les retours HTTP appropriés (codes et messages) pour les cas de succès et d’erreurs courants (ex : utilisateur non trouvé) plus tard : Exercice 4.

<br>

### **🧩 <u>Partie 5 - Tester avec Swagger</u>**

Afin d'éviter les bug et la dette technique, il est important de tester morceau de code au fur et a mesure du développement.

Pour tester les endpoints, comme l'exercice 2, on utilisera l’interface Swagger auto-générée par FastAPI :
1. Lancer l’application FastAPI
2. Accéder à l’interface Swagger via l’URL `/docs`
3. Pour chaque endpoint implémenté :
   * Effectuer une requête de test (avec payload si nécessaire)
   * Vérifier que la réponse est conforme aux attentes

<br>

> 💡 Vous pouvez voir vos schémas tout en bas avec les champs obligatoires, optionnelles, les types des champs, leurs contraintes...

<div style="page-break-after: always;"></div>