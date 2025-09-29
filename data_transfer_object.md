# Data Transfer Object (DTO)

Le pattern DTO est proposé en convention avec le bon usage des classes FastAPI/Pydantic pour séparer les préoccupations entre :
- Les données stockées en BDD
- Les données reçues en input (API INPUT)
- Les données exposées en output (API OUTPUT)

Les avantages de cette architecture sont une bonne pratique FastAPI recommandée pour les APIs robustes :
- Sécurité : Contrôle précis des données exposées/acceptées
- Flexibilité : Adaptation des régles de validation selon le contexte
- Evolution : Séparation des contrats API (input/output) / structure BDD
- Clarté : Intention explicite de chaque modèle selon son usage

## Les données stockées en BDD

Le principe est de créer une base avec les attributs métiers définis à la création d'une instance, utilisés à la lecture.<br>
La base est ensuite complétée avec une classe qui en hérite pour définir toutes les attributs techniques, les clés (P/K), champs datetime (création, update, etc.) & techniques (champs booléen, enums).

### Le modèle fondamental : TableBase (BaseSQLModel)
Il contient :
- **les attributs métiers essentiels** partagés entre création et lecture
- **les validateurs métier critiques**

### L'entité de base : Table (TableBase)
Il hérite de TableBase et ajoute **les attributs techniques (ID, statut, relations, datetime)**

## Les données reçues en Input

