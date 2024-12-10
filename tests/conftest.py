import sys
import os

# Ajoutez le répertoire 'src' à sys.path pour que Python puisse le trouver
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
