import os


class View:
    @classmethod
    def menu_principal(cls) -> str:
        print("")
        print("*" * 40)
        print("           MENU PRINCIPAL           ")
        print("*" * 40)
        print("")
        print("\033[1;32m1\033[0m. Créer un nouveau tournoi")
        print("\033[1;32m2\033[0m. Charger un tournoi")
        print("\033[1;32m9\033[0m. Quitter le programme")
        print("")
        return input()

    @classmethod
    def menu_gestion_tournoi(cls, tournoi) -> str:
        """Affiche le menu de gestion du tournoi"""
        print("*" * 40)
        print("            GESTION DU TOURNOI           ")
        print("*" * 40)
        print(f"Tournoi en cours : \033[1;32m{tournoi}\033[0m")
        print("-" * 40)
        print("\033[1;32m1\033[0m. Afficher les informations du tournoi")
        print("\033[1;32m2\033[0m. Afficher la liste des joueurs du tournoi")
        print("\033[1;32m3\033[0m. Gérer les tours du tournoi")
        print("\033[1;32m4\033[0m. Afficher le classement du tournoi")
        print("\033[1;32m9\033[0m. Quitter le menu de gestion de tournoi")
        print("*" * 40)
        return input()

    @classmethod
    def sous_menu_tours(cls, tournoi) -> str:
        """Affiche le menu de gestion des tours"""
        """Affiche le menu de gestion du tournoi"""
        print("*" * 40)
        print("       GESTION DES TOURS DU TOURNOI    ")
        print("*" * 40)
        print(f"Tournoi en cours : \033[1;32m{tournoi}\033[0m")
        print("-" * 40)
        print("\033[1;32m1\033[0m. Afficher les tours du tournoi")
        print("\033[1;32m2\033[0m. Générer des matchs pour un tour")
        print("\033[1;32m9\033[0m. Quitter le menu de gestion des tours")
        print("*" * 40)
        return input()

    @classmethod
    def afficher_tours_disponibles(cls, tournoi) -> str:
        print("*" * 40)
        print("       GESTION DES TOURS DU TOURNOI    ")
        print("*" * 40)
        print(f"Tournoi en cours : \033[1;32m{tournoi}\033[0m")
        print("-" * 40)
        print("Veuillez selectionner le tour où vous souhaitez générer des matchs :")

        # Afficher les options de sélection des tours disponibles
        for i, tour in enumerate(tournoi.liste_tours, start=1):
            print(f"{i+1}. {tour.nom}")

        choix = input("Saisissez le numéro du tour : ")
        return int(choix)

    @classmethod
    def afficher_matchs_existants(cls, tour):
        print(f"Les matchs ont déjà été générés pour le tour '{tour.nom}'. Que souhaitez-vous faire ?")
        print("1. Afficher les matchs existants")
        print("2. Revenir au menu principal")

        choix_action = input("Saisissez votre choix : ")
        return choix_action

    @classmethod
    def afficher_matchs_tour(cls, tour):
        print(f"Matchs du tour '{tour.nom}':")
        for match in tour.matchs:
            print(match)

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
        print("\033[1;32mInformations sur le tournoi :\033[0m")
        print(tournoi)
        print("------------------------------")
        print("")
        print("\033[1;32mNombre de Joueurs inscrient au tournoi : \033[0m" + str(len(tournoi.liste_joueurs))
              + " joueurs")
        print("")
        print("------------------------------")
        print("")
        print("\033[1;32mInformations sur les tours du tournoi : \033[0m")
        print("")
        for tour in tournoi.liste_tours:
            print(f"{tour.nom} - {tour.date_debut} : {tour.date_fin}")
            print("")
            # print(f"Matchs du {tour.nom} : ")
            # print("")
            # for match in tournoi.liste_matchs:
            #     if match.score1 is None or match.score2 is None:
            #         print(f"{match.joueur1.nom} {match.joueur1.prenom} VS {match.joueur2.nom}\
            #               {match.joueur2.prenom} : Non joué")
            #     else:
            #         print(f"{match.joueur1.nom} {match.joueur1.prenom} VS\
            # {match.joueur2.nom} {match.joueur2.prenom} :\
            #               {match.score1} - {match.score2}")
            #     print("")
            print("------------------------------")
        choix = input("\033[1;32mTape entrée pour retour en arriére\033[0m.")
        return choix

    @classmethod
    def afficher_informations_joueurs(cls, tournoi):
        print("")
        print("\033[1;32mInformations sur les Joueurs inscrient au tournoi : \033[0m")
        print("")
        for joueur in tournoi.liste_joueurs:
            print(f"{joueur.id} - {joueur.nom} {joueur.prenom} - {joueur.date_naissance} - Score : {joueur.score}")
        print("")
        choix = input("\033[1;32mTape entrée pour retour en arriére\033[0m.")
        return choix

    @classmethod
    def afficher_informations_tours(cls, tournoi):
        print("")
        print("\033[1;32mInformations sur les tours du tournoi : \033[0m")
        print("")
        for tour in tournoi.liste_tours:
            print(f"{tour.nom} - {tour.date_debut} : {tour.date_fin}")
            print("")
            if tournoi.liste_matchs:
                print("Matchs associés :")
                for match in tournoi.liste_matchs:
                    print(f"- {match.joueur1.nom} vs {match.joueur2.nom}")
            else:
                print("Aucun match n'a été enregistré pour ce tour")
                print("")
        choix = input("\033[1;32mTape entrée pour retour en arriére\033[0m.")
        return choix

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
            print("------------------------------------")
            print("")
            print("\033[1;32mVoici les tournois disponibles :\033[0m")
            print("")
            for i, fichier in enumerate(liste_fichiers):
                print(f"{i+1}. {fichier}")
            print("")

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
