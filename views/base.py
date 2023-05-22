import os


class View:
    @classmethod
    def menu_principal(cls) -> str:
        print("")
        print("Menu Principal")
        print("")
        print("1 - Créer un nouveau tournoi")
        print("2 - Charger un tournoi")
        print("3- Quitter le programme")
        print("")
        return input()

    @classmethod
    def nouveau_tournoi(cls) -> tuple:
        print("Initialisation d'un nouveau tournoi -->")
        nom = input("Nom du tournoi : ")
        lieu = input("Lieu du tournoi : ")
        date_debut = input("Date de début du tournoi : ")
        date_fin = input("Date de fin du tournoi : ")
        nombre_tours = input("Nombre de tours prévu : ")
        description = input("Description dutournoi : ")
        return nom, lieu, date_debut, date_fin, nombre_tours, description

    @classmethod
    def choix_2(cls) -> str:
        print("Voulez vous créer un autre paire de joueurs ? : (o / n)")
        return input()

    @classmethod
    def nouveau_joueur(cls) -> str:
        print("Veuillez créer une paire de joueurs -->")
        id = input("Id du joueur : ")
        nom = input("Nom du Joueur : ")
        prenom = input("Prenom du joueur : ")
        date_naissance = input("Date de naissance du joueur : ")
        return id, nom, prenom, date_naissance

    @classmethod
    def afficher_informations_tournoi(cls, tournoi) -> str:
        print("")
        print("------------------------------")
        print("")
        print("Informations sur le tournoi :")
        print(tournoi)
        print("------------------------------")
        print("")
        print("Joueurs du tournoi : ")
        print("")
        for joueur in tournoi.liste_joueurs:
            print(f"{joueur.id} - {joueur.nom} {joueur.prenom} {joueur.date_naissance} {joueur.score}")
            print("")
        print("------------------------------")
        print("")
        for tour in tournoi.liste_tours:
            print(f"{tour.nom} - {tour.date_debut} : {tour.date_fin}")
            print("")
            print(f"Matchs du {tour.nom} : ")
            print("")
            for match in tournoi.liste_matchs:
                if match.score1 is None or match.score2 is None:
                    print(f"{match.joueur1.nom} {match.joueur1.prenom} VS {match.joueur2.nom}\
                          {match.joueur2.prenom} : Non joué")
                else:
                    print(f"{match.joueur1.nom} {match.joueur1.prenom} VS {match.joueur2.nom} {match.joueur2.prenom} :\
                          {match.score1} - {match.score2}")
                print("")
            print("------------------------------")

    @classmethod
    def nouveau_tour(cls) -> str:
        nom = input("Nom du tour : ")
        date_debut = input("Date de début du tour : ")
        date_fin = input("Date de fin du tour : ")
        return nom, date_debut, date_fin

    @classmethod
    def afficher_liste_fichiers(cls, liste_fichiers):
        if len(liste_fichiers) == 0:
            print("Aucun tournoi n'est enregistré")
        else:
            print("Voici les tournois disponibles :")
            for i, fichier in enumerate(liste_fichiers):
                print(f"{i+1}. {fichier}")

    @classmethod
    def demander_nom_fichier(cls) -> str:
        liste_fichiers = os.listdir("data_tournois")

        # Demande à l'utilisateur de selctionner un fichier
        choix = input("Veuillez choisir un tournoi en entrant son numéro : ")
        if choix.isdigit() and int(choix) in range(1, len(liste_fichiers) + 1):
            nom_fichier = liste_fichiers[int(choix) - 1]
            return nom_fichier
        else:
            print("Choix invalide.")
            return None
