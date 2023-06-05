class Match:
    """La classe "Match" permet de stocker
    les informations d'un match du tournoi """
    def __init__(self, joueur1, joueur2, score1=0, score2=0):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score1 = score1
        self.score2 = score2

    def to_dict(self):
        """permet de convertir les données en dictionnaire
        car JSON ne peut pas représenter directement les objets
        personnalisés"""
        return {
            "joueur1": self.joueur1.to_dict(),
            "joueur2": self.joueur2.to_dict(),
            "score1": self.score1,
            "score2": self.score2
        }

    def renseigner_resultat_match(self, score1, score2):
        # Permet de renseigner le resultat d'un match
        self.score1 = score1
        self.score2 = score2
