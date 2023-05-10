import random
from models.match import Match


class Tour:
    """La classe "Tour" permet de stocker
    les informations d'un tour du tournoi"""
    def __init__(self, nom, date_debut, date_fin, joueurs):
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.liste_matchs = []
        self.joueurs = joueurs

    def generate_matches(self):
        # Mélange des joueurs de façon aléatoire
        if self.nom == "Tour 1" or self.nom == "tour 1":
            random.shuffle(self.joueurs)

        # Tri des joueurs par nombre de points dans le tournoi
        self.joueurs.sort(key=lambda x: x.total_point, reverse=True)

        # Association des joueurs dans l'ordre sans matchs identiques
        jouee = set()

        # Sur l'intégralité des joueurs, selection de deux à la fois
        for i in range(0, len(self.joueurs), 2):
            """ Pour for qui va de 0 à la longueur de la liste self.joueurs en
            incrémentant de 2 à chaque fois (pour prendre deux joueurs à la
            fois). À chaque itération, on prend les deux joueurs joueur1
            et joueur2 à partir de leur index i et i+1 dans la liste
            self.joueurs."""
            joueur1 = self.joueurs[i]
            joueur2 = self.joueurs[i+1]
            while (joueur1, joueur2) in jouee or (joueur2, joueur1) in jouee:
                """Dans la boucle while, on vérifie si la paire de joueurs
                (joueur1, joueur2) ou (joueur2, joueur1) a déjà été jouée
                (jouee). Si c'est le cas, on passe à la paire suivante
                (i est incrémenté de 2) jusqu'à ce qu'on trouve une paire
                de joueurs qui n'a pas encore été jouée."""
                i += 2
                joueur1 = self.joueurs[i]
                joueur2 = self.joueurs[i+1]

            """Une fois que la paire de joueurs est trouvée,
            on l'ajoute à jouee pour éviter de la réutiliser
            et on crée un objet Match avec les joueurs
            joueur1 et joueur2. Enfin, on ajoute cet objet Match
            à la liste self.matches qui contiendra
            tous les matchs du tour."""
            jouee.add((joueur1, joueur2))
            match = Match(joueur1, joueur2)
            self.liste_matchs.append(match)

        # Retourne la liste des matchs
        return self.liste_matchs
