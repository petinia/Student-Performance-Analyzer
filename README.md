# Student Performance Analyzer

**Développé par : TATY MASSANGA PETINIA MICHELLE** *Projet réalisé en autonomie complète*


## Présentation et Objectifs
Ce projet n'est pas une simple liste d'étudiants. C'est une application de gestion conçue avec une **rigueur professionnelle**. L'objectif était de créer un logiciel capable de traiter des données scolaires de manière fluide, avec une interface graphique moderne et une sauvegarde réelle.

## Structure du Projet (Arborescence)

Student_Performance_Analyzer/
│
├── main.py                # Point d'entrée unique (Lanceur de l'application)
├── README.md              # Documentation technique
│
├── data/                  # Couche de stockage 
│   └── student.json       # Base de données au format JSON
│
├── models/                # Objets métiers (POO)
│   └── student.py         # Classe "Student" : Définit les attributs et méthodes d'un élève
│
├── services/              # Logique et Intelligence 
│   ├── data_manager.py    # Gestion CRUD (Ajout, Modification, Suppression) et Sauvegarde
│   └── analysis.py        # Algorithmes de calculs statistiques et moyennes
│
└── ui/                    # Interface Utilisateur (GUI)
    └── interface.py       # Design, couleurs, onglets et gestion des événements Tkinter

## Architecture Technique et Modularité (Le point fort)

Pour ce projet, j'ai refusé de mettre tout le code dans un seul fichier. J'ai choisi une **Structuration Modulaire** pour séparer les responsabilités. Cela permet une meilleure maintenance et une lecture du code beaucoup plus claire.



### Détail de l'arborescence :
* **`main.py`** : C'est le chef d'orchestre. Il initialise les composants et lance l'application.
* **`models/student.py`** : Contient la **Classe Student**. C'est ici que j'utilise la **Programmation Orientée Objet (POO)**. Chaque étudiant est un objet autonome qui possède ses propres attributs (nom, notes) et ses propres méthodes (calcul de moyenne).
* **`services/data_manager.py`** : C'est le gestionnaire de données. Il contient toute la logique de manipulation de la liste (Ajout, Modification, Suppression). Séparer ce fichier permet de modifier la logique de gestion sans toucher à l'interface.
* **`services/analysis.py`** : Ce fichier est dédié aux algorithmes statistiques. Il calcule les moyennes de classe et identifie les majors de promotion.
* **`data/student.json`** : Le dossier de stockage permanent. Les données y sont écrites en format JSON pour ne jamais être perdues.
* **`ui/interface.py`** : Ce fichier gère l'intégralité de la **Vue**. Les couleurs, les polices, et la disposition des boutons sont isolées ici pour ne pas polluer la logique métier.

---

## Concepts Avancés implémentés

### 1. Programmation Orientée Objet (POO)
J'ai séparé les entités en **Classes**. Cela permet de créer des "moules" réutilisables. Par exemple, si demain je veux ajouter une date de naissance ou un matricule à un étudiant, je modifie seulement la classe `Student` et tout le reste de l'application s'adapte automatiquement.

### 2. Persistance des Données (Fin de la mémoire vive)
Contrairement aux projets débutants qui perdent tout à la fermeture, j'ai implémenté la **persistance**. 
- **Sérialisation** : Transformation des objets Python en format JSON pour l'écriture.
- **Désérialisation** : Rechargement des données du fichier JSON vers l'interface au démarrage du logiciel.

### 3. Gestion Robuste des Erreurs et UX
- **Validation de saisie** : L'application vérifie que les notes sont bien des nombres avant de valider.
- **Feedback visuel** : Utilisation de boîtes de dialogue (messagebox) pour confirmer les actions .
- **Navigation par onglets** : Pour éviter de surcharger l'utilisateur, les fonctionnalités sont réparties de manière ergonomique.

---

## Guide d'Utilisation Professionnel

1.  **Lancement** : `python main.py`.
2.  **Flux de travail** :
    * Saisir les informations dans le formulaire de gauche.
    * Utiliser **AJOUTER** pour créer une nouvelle entrée.
    * Sélectionner un nom dans la liste pour charger ses données automatiquement dans les champs.
    * Utiliser **MODIFIER** pour mettre à jour ou **SUPPRIMER** pour nettoyer la base.
3.  **Consultation** : Cliquer sur les onglets "ANALYSE" pour voir les performances globales en temps réel.

---

##  Évolutions prévues
* Implémentation de graphiques dynamiques pour visualiser la progression des élèves.
* Tri automatique : Classer les élèves par ordre alphabétique dès l'ajout pour une meilleure lisibilité.

