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
        print("\033[1;32m3\033[0m. Renseigner les résultats des Matchs")
        print("\033[1;32m9\033[0m. Quitter le menu de gestion des tours")
        print("*" * 40)
        return input()

    @classmethod
    def afficher_tours_disponibles(cls, tournoi):
        print("")
        print("\033[1;32mTours disponibles où vous pouvez générer des matchs :\033[0m")
        print("----------------------------------------")
        print("\nTournoi en cours :", tournoi.nom)
        print("----------------------------------------")
        if not tournoi.liste_tours:
            print("Aucun tour n'a été créé pour ce tournoi.")
            return None

        for i, tour in enumerate(tournoi.liste_tours, start=1):
            if not tour.liste_matchs:
                statut_matchs = "\033[3;31mMatchs non générés\033[0m"
            else:
                statut_matchs = "\033[1;32mMatchs générés\033[0m"
            print(f"{i}. {tour.nom} ({statut_matchs})")

        while True:
            choix = input("Saisissez le numéro du tour : ")
            if choix.isdigit() and 1 <= int(choix) <= len(tournoi.liste_tours):
                return int(choix)
            else:
                print("Choix invalide. Veuillez saisir un numéro valide.")

    @classmethod
    def nouveau_tournoi(cls) -> tuple:
        print("")
        print("\033[1;32mInitialisation d'un nouveau tournoi -->\033[0m")
        nom = input("Nom du tournoi : ")
        lieu = input("Lieu du tournoi : ")
        date_debut = input("Date de début du tournoi : ")
        date_fin = input("Date de fin du tournoi : ")
        nombre_tours = input("Nombre de tours prévu : ")
        description = input("Description du tournoi : ")
        return nom, lieu, date_debut, date_fin, nombre_tours, description

    @classmethod
    def choix_2(cls) -> str:
        print("")
        print("Voulez vous créer un autre paire de joueurs ? : (o / n)")
        return input()

    @classmethod
    def nouveau_joueur(cls) -> str:
        print("")
        print("Création d'un joueur :")
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
        for i, tour in enumerate(tournoi.liste_tours):
            print(f"{tour.nom} - {tour.date_debut} : {tour.date_fin}")
            print("")
            if i < len(tournoi.liste_tours) - 1:
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
            if tour.liste_matchs:
                print("Matchs associés :")
                print("")
                for match in tour.liste_matchs:
                    print(f"-{match.joueur1.nom} {match.joueur1.prenom} vs {match.joueur2.nom} {match.joueur2.prenom}")
                    print("")
                print("-------------------------------")
            else:
                print("\033[3;31mAucun match n'a été enregistré pour ce tour\033[0m")
                print("")
                print("-------------------------------")
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

    @classmethod
    def afficher_matchs(cls, matchs):
        print("\nMatchs générés :")
        print("")
        for match in matchs:
            print(f"- {match.joueur1.nom} {match.joueur2.prenom} vs {match.joueur2.nom} {match.joueur2.prenom}")
            print("")

    @classmethod
    def demande_resultat_match(cls, nom_joueur, prenom_joueur):
        while True:
            score = input(f"Entrez le résultat pour le joueur {nom_joueur} {prenom_joueur} (g/p/n): ")
            if score.lower() in ["g", "p", "n"]:
                return score.lower()
            else:
                print("Veuillez entrer un résultat valide (g, p ou n).")

    @classmethod
    def afficher_classement_tournoi(cls, tournoi):
        print(f"Classement du tournoi : {tournoi.nom}")
        print("-----------------------")
        classement = tournoi.classement()

        if classement:
            for i, joueur in enumerate(classement, start=1):
                print(f"{i}. {joueur.nom} {joueur.prenom} ({joueur.score})")
        else:
            None

        print("-----------------------\n")
        choix = input("\033[1;32mTape entrée pour retour en arriére\033[0m.")
        return choix
