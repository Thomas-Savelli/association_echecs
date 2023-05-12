from datetime import date
from models.joueur import Joueur
from models.tournoi import Tournoi
from models.tour import Tour

# Création d'une liste contenant tout les joueurs initialisés
liste_joueurs = []
# création d'instance de Joueur
joueur1 = Joueur("Savelli", "Thomas", date(1992, 7, 16), "joueur1")
joueur2 = Joueur("Savelli", "Marc-André", date(1996, 5, 26), "joueur2")
joueur3 = Joueur("Cantet", "Agathe", date(1992, 4, 22), "joueur3")
joueur4 = Joueur("Cantet", "Antoine", date(1992, 4, 22), "joueur4")
joueur5 = Joueur("Buisson", "Antohny", date(1972, 2, 11), "joueur5")
joueur6 = Joueur("Rannou", "Juliette", date(1982, 9, 2), "joueur6")
joueur7 = Joueur("Monkey.D", "Luffy", date(1870, 2, 2), "joueur7")
joueur8 = Joueur("Kurusaki", "Ichigo", date(870, 1, 1), "joueur8")
joueur9 = Joueur("Uzumaki", "Naruto", date(1458, 9, 30), "joueur9")
joueur10 = Joueur("Dumbeldore", "Albus", date(1820, 6, 12), "joueur10")

liste_joueurs = [joueur1, joueur2, joueur3, joueur4, joueur5, joueur6]

# Création d'une liste contenant tout les tounois
liste_tournois = []
# Création tournoi
tournoi1 = Tournoi("Echéquier Dorée", "Salle des fêtes de L'Île-Rousse", date(2023, 5, 11),
                   date(2023, 5, 14), 4, "Tournoi d'inauguration de l'association d'échecs")
liste_tournois.append(tournoi1)

# Inscription des joueurs au tournoi_1
tournoi1.ajouter_joueur(joueur1)
tournoi1.ajouter_joueur(joueur2)
tournoi1.ajouter_joueur(joueur3)
tournoi1.ajouter_joueur(joueur4)
tournoi1.ajouter_joueur(joueur5)
tournoi1.ajouter_joueur(joueur6)

# Afficher tout les joueurs initialisés
for joueur in Joueur.afficher_joueurs_initialises():
    joueur.afficher_info()

# Création du premier tour
tour1 = Tour("tour 1", date(2023, 5, 11), date(2023, 5, 11),
             tournoi1.liste_joueurs)

# Création des matchs du premier tour
Tour.generate_matches(tour1)


# Renseigner les résultats des matchs du premier tour
tour1.liste_matchs[0].resultat_match(tour1.liste_matchs[0], 0, 1)
tour1.liste_matchs[0].resultat()

tour1.liste_matchs[1].resultat_match(tour1.liste_matchs[1], 1, 0)
tour1.liste_matchs[1].resultat()

tour1.liste_matchs[2].resultat_match(tour1.liste_matchs[2], 1, 0)
tour1.liste_matchs[2].resultat()

print("")
print("-------1 ER TOUR DU TOURNOI--------")
print("")
Tournoi.afficher_tournois(liste_tournois)
print("")
print("------------------------------------")
print("")

# Afficher les Matchs du premier tour
for match in tour1.liste_matchs:
    print(f"{match.joueur1.nom} {match.joueur1.prenom} - {match.joueur1.score} vs \
            {match.joueur2.nom} {match.joueur2.prenom} - {match.joueur1.score}")
print("")
print("------------------------------------")
print("")
tournoi1.classement()
print("")
print("------------------------------------")
print("")

# Création du second tour
tour2 = Tour("tour 2", date(2023, 5, 12), date(2023, 5, 12),
             tournoi1.liste_joueurs)

# Création des matchs du premier tour
Tour.generate_matches(tour2)


# Renseigner les résultats des matchs du premier tour
tour2.liste_matchs[0].resultat_match(tour2.liste_matchs[0], 1, 0)
tour2.liste_matchs[0].resultat()

tour2.liste_matchs[1].resultat_match(tour2.liste_matchs[1], 0, 1)
tour2.liste_matchs[1].resultat()

tour2.liste_matchs[2].resultat_match(tour2.liste_matchs[2], 0, 1)
tour2.liste_matchs[2].resultat()

print("-------2 EME TOUR DU TOURNOI--------")
print("")
Tournoi.afficher_tournois(liste_tournois)
print("")
print("------------------------------------")
print("")
# Afficher les Matchs du premier tour
for match in tour1.liste_matchs:
    print(f"{match.joueur1.nom} {match.joueur1.prenom} - {match.joueur1.score} vs \
          {match.joueur2.nom} {match.joueur2.prenom} - {match.joueur1.score}")
print("")
print("------------------------------------")
print("")
tournoi1.classement()
print("")
print("------------------------------------")
