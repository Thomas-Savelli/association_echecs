import random

from models.match import Match
from models.tour import Tour


class Tournoi:
    """La classe "Tournoi" permet de stocker les informations du tournoi """
    def __init__(self, nom, lieu, date_debut, date_fin,
                 nombre_tours=4, description=''):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_tours = int(nombre_tours)
        self.liste_tours = []
        self.liste_joueurs = []
        # self.liste_matchs = []
        self.description = description

    def ajouter_joueur(self, joueur):
        # Permet d'ajouter un joueur au tournoi
        self.liste_joueurs.append(joueur)

    def afficher_joueurs(self):
        # Permet d'afficher les joueurs du tournoi par ordre alphabétique
        joueurs_tri = sorted(self.liste_joueurs, key=lambda joueur: joueur.nom)
        for joueur in joueurs_tri:
            print(joueur)

    def classement(self):
        # Permet d'afficher le classement des joueurs dans le tournoi
        classement_joueur = sorted(self.liste_joueurs,
                                   key=lambda j: j.score, reverse=True)
        print("Classement :")
        for i, joueur in enumerate(classement_joueur, start=1):
            print(f"{i}. {joueur.nom} {joueur.prenom} ({joueur.score})")

    def __repr__(self):
        return f"Nom : {self.nom}\nLieu : {self.lieu}\
                \nDate : {self.date_debut} - {self.date_fin}\
                \nNombre de tours : {self.nombre_tours}\
                \nDescription : {self.description}\n"

    def generer_match(self, tour_selectionne):
        """
        Cette méthode génère les matchs pour un tour spécifique.
        Chaque joueur doit jouer une fois par tour, donc nous avons besoin de
        diviser la liste des joueurs en paires. Pour les tours suivant le premier,
        les matchs doivent être générés en fonction des scores des joueurs.
        """
        # Assurez-vous que la liste des joueurs est paire
        if len(self.liste_joueurs) % 2 != 0:
            print("Le nombre de joueurs doit être pair pour générer des matchs.")
            return

        # Générer les matchs pour le tour
        matchs = []

        if tour_selectionne == 0:
            # Pour le premier tour, simplement mélanger les joueurs et les diviser en paires
            joueurs = self.liste_joueurs[:]
            random.shuffle(joueurs)

            while joueurs:
                joueur1 = joueurs.pop(0)
                joueur2 = joueurs.pop(0)
                match = Match(joueur1, joueur2)
                matchs.append(match)
        else:
            # Pour les tours suivants, les matchs doivent être générés en fonction des scores des joueurs
            joueurs = sorted(self.liste_joueurs, key=lambda x: x.score, reverse=True)
            while joueurs:
                joueur1 = joueurs.pop(0)
                joueur2 = None
                for joueur in joueurs:
                    # Vérifier si ces deux joueurs ont déjà joué ensemble
                    if not any((m.joueur1 == joueur1 and m.joueur2 == joueur or m.joueur2 == joueur1 and m.joueur1 == joueur) for m in tour_selectionne.liste_matchs):
                        joueur2 = joueur
                        break
                if not joueur2:
                    print(f"Impossible de trouver un adversaire pour le joueur {joueur1.nom} qui n'est pas déjà joué avec.")
                    return
                joueurs.remove(joueur2)
                match = Match(joueur1, joueur2)
                matchs.append(match)

        # Retourner la liste des matchs pour le tour spécifique
        return matchs


if __name__ == '__main__':
    tournoi1 = Tournoi("tournoi echec", "ile rousse", "11/11/2023", "12/11/2023", "4", "zzzzzzzzzzzzzzzzzz")
    print(tournoi1)
    Tournoi.generer_match(tournoi1)
    tour1 = Tour("tour1", "11/11/2023", "11/11/2023")
    tour2 = Tour("tou21", "12/11/2023", "12/11/2023")
    print(tournoi1.liste_tours)
