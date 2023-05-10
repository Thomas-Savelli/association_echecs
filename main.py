from datetime import date
from models.joueur import Joueur
from models.tournoi import Tournoi
from models.tour import Tour
from models.match import Match

# création d'instance de joueur
joueur1 = Joueur("Savelli", "Thomas", date(1992, 7, 16))
joueur2 = Joueur("Savelli", "Marc-André", date(1996, 5, 26))
joueur3 = Joueur("Cantet", "Agathe", date(1992, 4, 22))
joueur4 = Joueur("Cantet", "Antoine", date(1992, 4, 22))


# Création tournoi
tournoi1 = Tournoi("Echequier dorée", "L'Île-Rousse", date(2022, 5, 9),
                   date(2022, 5, 9), "4 tours", "Tournois Espoir Haute-Corse")

# Ajout des joueurs au Tournoi Echequier dorée
tournoi1.ajouter_joueur(joueur1)
tournoi1.ajouter_joueur(joueur2)
tournoi1.ajouter_joueur(joueur3)
tournoi1.ajouter_joueur(joueur4)

# Création d'un Tour pour le tournoi
tour = Tour("Round 1", date(2022, 6, 1), date(2022, 6, 3),
            tournoi1.liste_joueurs)

# Générer les paires de matchs pour le tour
tour.generate_matches()

# Afficher les matchs générés pour le tour
for match in tour.liste_matchs:
    print(f"{match.joueur1.nom} {match.joueur1.prenom} vs. \
            {match.joueur2.nom} {match.joueur2.prenom}")

# Rentrer les resultats des matchs du premier tour
tour.liste_matchs[0].resultat_match(tour.liste_matchs[0], 1, 0)
tour.liste_matchs[0].resultat()

tour.liste_matchs[1].resultat_match(tour.liste_matchs[1], 0.5, 0.5)
tour.liste_matchs[1].resultat()

tournoi1.classement()
