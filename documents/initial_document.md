# ZeroPaper
Application web d'archivage

*Bouchakour, Bienfait, Le Corff, Poidvin, Sergent*

## Introduction
Dans le cadre du cours d'*Introduction aux systèmes d'information* et de *Développement Web* nous avons décidé, en accord avec les professeurs, de réaliser un projet en commun entre les deux cours, possédant des aspects qui permettent une évaluation dans ces derniers.

Nous nous tournons donc vers un sujet proposé par M. Djerroud.

## Sujet
Dans le cadre d’un projet Zéro Papier, l’EFREI souhaite développer une application
d’archivage documents. L’application doit permettre de sauvegarder des documents
divers en PDF, Image,… dans une base de données.

Des méta-données doivent être ajoutées pour chaque document afin de l’identifier
avec précision par exemple (Type, Nom document, description, date ...). Pour faciliter
la recherche.

Les documents sont classés par type, l’utilisateur doit pouvoir créer des types au
besoin.

L’application doit implémenter les fonctionnalités suivantes :
1. Authentification
2. Gestion des utilisateurs (Création, modification et suppression)
3. Statistiques : Nombre de documents par type etc.
4. Fonction de recherche
5. Impression

---

**NB** : nous avons décider de garder le sujet tel quel sans y ajouter de compléxité ou de profondeur supplémentaire afin de nous concentrer sur d'autres aspect de la gestion du projet:
- Gestion des versions / repo **GitHub** propre
- Mise en place pipeline **CI/CD** automatisé dans GitHub
- Gestion de projet avec les outils adéquats
- Déploiement dans des conteneurs **Docker**

## Répartition des tâches
- Front : Erwann
- Back & intégration : Hugo & PL
- Tests : Meo & PL
- CI/CD : Younes

## Technologies
### Front
Pas de technologies particulières retenues, développement classique avec HTML, CSS, JS, utilisation de Bootstrap (ou autre librairie CSS).

### Back
Développement en Python en utilisant le framework **[Django](https://www.djangoproject.com/)**, de part l'expérience d'un membre sur la techno et l'envie pour les autres de se former dessus. Permettra un développement plutôt rapide et formateur.

*PS : le framework fonctionne de la même manière que Symfony sur le principe.*

### Tests
Utilisation de **[unittest](https://docs.python.org/3/library/unittest.html)**, inclu dans la librairie standard de Python.

### CI/CD & deploiement
Utilisation de **Docker** pour conteneuriser l'application afin de faciliter son déploiement et éviter les problèmes de dépendances.

Utilisation de **[GitHub action](https://github.com/features/actions)** permettant de réaliser des pipelines de déploiement. Le but étant de valider les tests pour ensuite lancer le déploiement de l'image Docker sur le serveur.

Utilsation d'un Raspberry Pi ou bien d'un cloud provider comme serveur pour le déploiement.

Utilisation de **[Caddy2](https://caddyserver.com/v2)** pour utiliser un chiffrage TLS et un DNS (nom de domaine).

### Gestion du projet
Utilisation de **[Trello](https://trello.com/)** pour l'organisation des tâches.

Utilisation de **[GitHub](https://github.com/)** pour noter les bugs et les fonctionnalité à implémenter (*issues*).

## Détails techniques
### Utilisation GitHub

Nous utiliserons GitHub de la manière suivante.
- `master` : branche de production
- `dev` : branche de développement
- `feature/<feature name>` : une branche pour chaque nouvelle feature. Elles seront merge sur la branche `dev`.

Le workflow devrait se faire donc de la manière suivante.

Nouvelle fonctionnalité :

1. Développement d'une fonctionnalité sur une branche `feature/`
2. Ouverture d'une pull request (merge request) vers `dev`
3. Validation par les membres du projet, système de review permettant d'assurer la qualité du code **ET** pipeline de tests OK
4. Merge de la branche vers `dev`

Déploiement en production :
1. Ouverture d'une pull request (merge request) vers `master`
2. Validation par les membres du projet, intégrations nécessaires **ET** pipeline de déploiement OK
3. Merge de la branche vers `master`
4. Pipeline master assurant le déploiement sur le serveur
