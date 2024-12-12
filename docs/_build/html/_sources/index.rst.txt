Pendule Simple Documentation
=============================

Bienvenue dans la documentation du projet **Pendule Simple**. Ce projet contient une implémentation Python d'une simulation et d'un outil d'analyse d'un pendule simple. Il respecte les bonnes pratiques de codage, inclut des tests complets et une documentation détaillée.

Badges
------

.. image:: https://img.shields.io/badge/Python-3.8%2B-blue.svg
    :target: https://www.python.org/
.. image:: https://img.shields.io/badge/coverage-100%25-green.svg
    :target: https://coveralls.io/github/nom-utilisateur/pendule-simple
.. image:: https://img.shields.io/badge/code%20style-black%20%2F%2F%20PEP%208-black.svg
    :target: https://black.readthedocs.io/en/stable/

Fonctionnalités
---------------

Le projet **Pendule Simple** inclut plusieurs fonctionnalités principales :

- **Simulation du Pendule Simple** : Calcul du mouvement d'un pendule simple en fonction des paramètres initiaux (longueur, angle, etc.).
- **Tests et Couverture** : Inclut des tests unitaires complets avec du coverage, afin de garantir le bon fonctionnement du projet.
- **Normes de Codage** : Le code respecte les standards **PEP 8**, vérifiés avec l'outil **black**.
- **Documentation** : Documentation détaillée générée avec **Sphinx**.
- **Badges** : Visualisation des badges pour la couverture des tests et le respect des normes de codage.

Prise en Main
-------------

### Prérequis

Avant d'installer le projet, assurez-vous que **Python 3.8** ou une version supérieure est installé sur votre machine. Vous pouvez vérifier votre version de Python avec la commande suivante :


D'accord ! Voici le fichier index.rst complet, prêt à être copié dans un seul fichier sans les sections Bash séparées. Ce fichier peut être directement utilisé dans votre projet Sphinx.

index.rst complet
rst
Copier le code
Pendule Simple Documentation
=============================

Bienvenue dans la documentation du projet **Pendule Simple**. Ce projet contient une implémentation Python d'une simulation et d'un outil d'analyse d'un pendule simple. Il respecte les bonnes pratiques de codage, inclut des tests complets et une documentation détaillée.


Fonctionnalités
---------------

Le projet **Pendule Simple** inclut plusieurs fonctionnalités principales :

- **Simulation du Pendule Simple** : Calcul du mouvement d'un pendule simple en fonction des paramètres initiaux (longueur, angle, etc.).
- **Tests et Couverture** : Inclut des tests unitaires complets avec du coverage, afin de garantir le bon fonctionnement du projet.
- **Normes de Codage** : Le code respecte les standards **PEP 8**, vérifiés avec l'outil **black**.
- **Documentation** : Documentation détaillée générée avec **Sphinx**, disponible ici.
- **Badges** : Visualisation des badges pour la couverture des tests et le respect des normes de codage.

Prise en Main
-------------

Prérequis
---------

Avant d'installer le projet, assurez-vous que **Python 3.8** ou une version supérieure est installé sur votre machine. Vous pouvez vérifier votre version de Python avec la commande suivante :

python --version

Installez ensuite les dépendances nécessaires à l'aide de la commande suivante :

pip install -r requirements.txt


Installation
------------

Pour installer le projet localement, utilisez **pip** en exécutant la commande suivante à partir du répertoire racine du projet :

pip install .


Utilisation
-----------

Pour exécuter le programme principal et simuler le pendule simple, vous pouvez utiliser la commande suivante (en supposant que le script principal s'appelle `pendule.py`) :

python main.py


Tests
-----


Les tests unitaires du projet sont situés dans le répertoire `tests/`. Vous pouvez exécuter tous les tests en utilisant **pytest** avec la commande suivante :

pytest --cov=src


Cette commande exécutera les tests et génèrera automatiquement un rapport de couverture.

Pour visualiser le rapport de couverture, utilisez la commande suivante :

coverage report

