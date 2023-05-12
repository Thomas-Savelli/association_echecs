class Match:
    """La classe "Match" permet de stocker
    les informations d'un match du tournoi """
    def __init__(self, joueur1, joueur2, score1=0, score2=0):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.score1 = score1
        self.score2 = score2

    def resultat(self):
        # Permet de mettre à jour le score des joueurs
        if self.score1 > self.score2:
            self.joueur1.score += 1
        elif self.score1 < self.score2:
            self.joueur2.score += 1
        else:
            self.joueur1.score += 0.5
            self.joueur2.score += 0.5

    def resultat_match(self, match, score1, score2):
        # Permet de renseigner le resultat d'un match
        match.score1 = score1
        match.score2 = score2
