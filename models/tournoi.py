import random

from models.match import Match
from models.joueur import Joueur


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
        self.liste_matchs = []
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

    def generer_match(self):
        """generer un tour avec une liste de matchs et l'ajouter à la liste des tours"""
        # Cette méthode permet de générer les matchs du tour initialisé
        # Mélange des joueurs de façon aléatoire
        if self.nom == "Tour 1" or self.nom == "tour 1":
            random.shuffle(self.liste_joueurs)

        # Tri des joueurs par nombre de points dans le tournoi
        self.liste_joueurs.sort(key=lambda x: x.score, reverse=True)

        # Association des joueurs dans l'ordre sans matchs identiques
        jouee = set()

        # Sur l'intégralité des joueurs, selection de deux à la fois
        for i in range(0, len(self.liste_joueurs), 2):
            """ Pour for qui va de 0 à la longueur de la liste self.joueurs en
            incrémentant de 2 à chaque fois (pour prendre deux joueurs à la
            fois). À chaque itération, on prend les deux joueurs joueur1
            et joueur2 à partir de leur index i et i+1 dans la liste
            self.joueurs."""
            joueur1 = self.liste_joueurs[i]
            joueur2 = self.liste_joueurs[i+1]
            while (joueur1, joueur2) in jouee or (joueur2, joueur1) in jouee:
                """Dans la boucle while, on vérifie si la paire de joueurs
                (joueur1, joueur2) ou (joueur2, joueur1) a déjà été jouée
                (jouee). Si c'est le cas, on passe à la paire suivante
                (i est incrémenté de 2) jusqu'à ce qu'on trouve une paire
                de joueurs qui n'a pas encore été jouée."""
                i += 2
                joueur1 = self.liste_joueurs[i]
                joueur2 = self.liste_joueurs[i+1]

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

    def to_dict(self):
        """permet de convertir les données en dictionnaire
        car JSON ne peut pas représenter directement les objets
        personnalisés"""
        return {
            "nom": self.nom,
            "lieu": self.lieu,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
            "nombre_tour": self.nombre_tours,
            "liste_tours": [tour.to_dict() for tour in self.liste_tours],
            "liste_joueurs": [joueur.to_dict() for joueur in self.liste_joueurs],
            "liste_matchs": [match.to_dict() for match in self.liste_matchs],
            "description":  self.description
        }


if __name__ == '__main__':
    tournoi1 = Tournoi("Tournoi N1", "L'Ile-Rousse", "12/12/2023", "20/12/2023", "4",
                       "Tournoi d'inauguration du Club d'echecs d'ile rousse")

    print(tournoi1)

    joueur1 = Joueur("ST01", "Savelli", "Thomas", "16/07/1992")
    joueur2 = Joueur("AC01", "Cantet", "Agathe", "22/04/1992")
    joueur3 = Joueur("MM01", "Massoni", "Marc", "01/04/1988")
    joueur4 = Joueur("AC02", "Alfieri", "Cedric", "26/05/1978")

    tournoi1.ajouter_joueur(joueur1)
    tournoi1.ajouter_joueur(joueur2)
    tournoi1.ajouter_joueur(joueur3)
    tournoi1.ajouter_joueur(joueur4)

    tournoi1.afficher_joueurs()
