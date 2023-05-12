import os
import json


class GestionData:
    """Gére les sauvegardes et chargements des Data enregistrées"""
    def sauvegarde(self, donnees):
        # Création (si inexistant) du dossier data_tournois
        if not os.path.exists("data_tournois"):
            os.mkdir("data_tournois")

        with open(f"{self.nom}", "w") as f:
            json.dump(donnees, f)

    def charger(self):
        with open(f"{self.nom}", "r") as f:
            donnees = json.load(f)
        return donnees
