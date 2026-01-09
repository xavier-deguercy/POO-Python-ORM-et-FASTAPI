
## **🧪 Exercice 6 – One-to-Many et Many-to-Many avec SQLModel**

---

Dans la continuité des exercices précédents, nous enrichissons le contexte de gestion des **utilisateurs** en ajoutant deux nouvelles entités :

1. **Relation One-to-Many**
   * Un **utilisateur** peut créer plusieurs **tickets**
   * Un **ticket** appartient à un seul **utilisateur**
2. **Relation Many-to-Many**
   * Un **ticket** peut être associé à plusieurs **étiquettes**
   * Une **étiquette** peut être associée à plusieurs **tickets**

<br>

### **🧩 <u>Partie 1 – Modélisation avec SQLModel</u>**

1. Créer les **schémas et modèles SQLModel** suivants :
   * `Ticket` : `id`, `titre`, `description`, `id_utilisateur`
   * `Tag` : `id`, `nom`
   * Une table d’association **Many-to-Many** `ticket_tag` entre `Ticket` et `Tag`
2. Définir correctement les relations :
   * `User` → `tickets` (**One-to-Many**)
   * `Ticket` ↔ `Tag` (**Many-to-Many**)
3. Ajouter les contraintes importantes :
   * clés primaires
   * règles de nullabilité adaptées
    * ...

> ⚠️ Pour les relations Many-to-Many, **seule la table d’association est attendue**.  
> Aucun schéma dédié n’est nécessaire.

<br>

### **🧩 <u>Partie 2 – Concrétisation via l’API</u>**

1. Créer les **5 endpoints CRUD** pour :
   * les **tickets**
   * les **étiquettes (tags)**
2. Mettre en place la **logique métier** dans le dossier `src/services/` afin de :
   * gérer correctement les relations entre entités
   * inclure les données liées (utilisateur, étiquettes) dans les réponses lorsque cela est pertinent
3. Tester les endpoints à l’aide de **Swagger UI** afin de vérifier :
   * la création des relations
   * la récupération correcte des données liées
   * le bon fonctionnement global des relations One-to-Many et Many-to-Many