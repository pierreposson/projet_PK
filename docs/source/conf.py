# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('C:/Users/Pierre/projet_PK/src'))
sys.path.insert(0, os.path.abspath('C:/Users/Pierre/projet_PK/tests'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Projet Pendule Simple'
copyright = '2024, Pierre Posson et Adrien Kiss'
author = 'Pierre Posson et Adrien Kiss'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Pour générer la documentation automatiquement à partir du code
    "sphinx.ext.viewcode",  # Pour afficher le code source des fonctions et classes dans la documentation
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
