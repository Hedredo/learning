var = __name__

import logging

# Créer un logger spécifique au module
logger = logging.getLogger(__name__)  
logger.setLevel(logging.DEBUG)  # Définir le niveau du logger

# Ajouter un handler pour afficher les logs dans la console
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

# Ajouter le handler au logger
logger.addHandler(handler)

# Test du logger
logger.debug("Le logger de script.py a été initialisé.")

def test_log():
    logger.info("La fonction test_log a été appelée.")

# Pour éviter que le script ne s'exécute lors de l'importation
if __name__ == "__main__":
    logger.info("Ce message s'affichera uniquement si le script est exécuté directement.")