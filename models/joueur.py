class Joueur:
    # Liste enregistrant tout les joueurs initialisés
    liste_joueurs_initilises = []
    """La classe "Joueur" permet de stocker les informations des joueurs"""
    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.score = 0
        Joueur.liste_joueurs_initilises.append(self)

    def afficher_info(self):
        # Affiche les infos d'un joueur
        print(f"{self.prenom} {self.nom} - {self.date_naissance} - score : {self.score}")

    @classmethod
    # Permet de prendre la classe en tant que premier argument plutôt que l'instance de la classe.
    def afficher_joueurs_initialises(cls):
        # Permet de retourner l'ensemble des joueurs initialisés
        return cls.liste_joueurs_initilises
