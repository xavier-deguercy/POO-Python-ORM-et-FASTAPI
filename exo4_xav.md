## **🧪 Exercice 4 – Mise en place de l’ORM avec SQLModel**

---

Maintenant que l’API REST de gestion des utilisateurs est en place avec FastAPI, on va intégrer SQLModel pour gérer la persistance des données.

> On gérera le lien entre les 2 dans le prochain exercice.

En vous basant sur schéma `User` qui est la vrai table effective en bdd, réaliser les tâches suivantes :

<br>

### **🧩 <u>Partie 1 – Compréhension du cycle de session</u>**

En pseudo-code, décrire les étapes nécessaires pour :
* Créer l’engine de connexion à la base de données
* Ouvrir une session SQLModel 
* Récupérer tous les utilisateurs
* Fermer proprement la session

> Le pseudo-code doit faire apparaître clairement ces différentes étapes et les étapes intermédiaires nécessaires  
> _(ex : exécution de la requête, récupération des résultats, etc.)_

<br>

### **🧩 <u>Partie 2 – Implémentation en Python</u>**

On va implémenter le pseudo-code précédent en Python, en suivant les bonnes pratiques.

1. Dans le dossier `src/conf/`, créer un fichier `setting.py` pour gérer la configuration de l’application.
   * Charger les variables d’environnement depuis le fichier `.env`
   * créer la chaîne de connexion à la base de données
   * ...
2. Dans le dossier `src/conf/`, créer un fichier `session.py`
   * Importe la chaine de connexion depuis `setting.py`
   * Crée l’engine SQLModel
   * ...
3. Dans le dossier `src/repositories/`, créer un fichier `user_repository.py`
   * Importe le model `User`
   * Importe l’engine SQLModel depuis `session.py`
   * Implémente le CRUD complet pour le modèle `User`
   * ...

> 💡 Pour tester votre code, vous pouvez importer `user_repository.py` dans le `src/main.py` et appeler les fonctions de manipulation des utilisateurs.

> 💡 N'oubliez pas le `sqlmodel.metadata.create_all(engine)` dans le main pour créer la table dans la bdd.

<div style="page-break-after: always;"></div>