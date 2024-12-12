# Projet Python : Pendule Simple

Ce dépôt contient une implémentation en Python d'une simulation et d'un outil d'analyse d'un pendule simple. Le projet respecte les bonnes pratiques de codage, inclut des tests complets et une documentation détaillée.

## Fonctionnalités

- **Simulation du Pendule Simple** : Calcul du mouvement d'un pendule simple en fonction des paramètres initiaux (longueur, angle, etc.).
- **Tests et Couverture** : Inclut des tests unitaires complets avec du coverage.
- **Normes de Codage** : Le code respecte les standards PEP 8, vérifiés avec `black`.
- **Documentation** : Documentation détaillée générée avec Sphinx, disponible [ici](https://pierreposson.github.io/projet_PK).
- **Badge** : Ajout des badges

## Prise en Main

### Prérequis

Assurez-vous que Python 3.8 ou une version supérieure est installé. Installez les dépendances nécessaires :

pip install -r requirements.txt

### Installation

Installez le projet localement avec pip :

Copier le code
pip install .

### Utilisation
Exécutez le programme principal pour simuler un pendule simple

### Tests
Les tests unitaires se trouvent dans le répertoire tests/. Exécutez les tests avec pytest :

Copier le code
pytest --cov=src

Un rapport de couverture est généré automatiquement. Pour visualiser le rapport de couverture :
Copier le code
coverage report

### Documentation
La documentation du projet est générée avec Sphinx et hébergée sur GitHub Pages. Seulement après avoir essayer et recommencer de nombreuses fois, nous avons seulement réussi à obtenir une génération partielle de notre documenttion avec Sphinx.

### Actions GitHub
Ce dépôt inclut un workflow qui :

Exécute les tests avec pytest.
Vérifie la qualité du code avec black.
Garantit une couverture de code à 100%.

### Badge 
![Couverture des Tests](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Black](https://img.shields.io/badge/code%20style-black%20%2F%2F%20PEP%208-black.svg)

