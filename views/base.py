class View:
    @classmethod
    def menu_principal(cls) -> str:
        print("")
        print("Menu Principal")
        print("")
        print("1 - Démarrer un tournoi")
        print("2 - Informations sur le tournoi")
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
        print("Voulez vous créer un autre joueur ? : (o / n)")
        return input()

    @classmethod
    def nouveau_joueur(cls) -> str:
        print("Veuillez créer un joueur -->")
        id = input("Id du joueur : ")
        nom = input("Nom du Joueur : ")
        prenom = input("Prenom du joueur : ")
        date_naissance = input("Date de naissance du joueur : ")
        return id, nom, prenom, date_naissance

    @classmethod
    def afficher_informations_tournoi(cls, tournoi, joueurs, tours) -> str:
        print("")
        print("------------------------------")
        print("Informations sur le tournoi :")
        print(tournoi)
        print("------------------------------")
        print("")
        print("Joueurs du tournoi : ")
        print("")
        for joueur in joueurs:
            print(f"{joueur.id} - {joueur.nom} {joueur.prenom} {joueur.date_naissance} {joueur.score}")
            print("")
        print("------------------------------")
        print("")
        for tour in tours:
            print(f"{tour.nom} - {tour.date_debut} : {tour.date_fin}")

    @classmethod
    def afficher_informations_joueurs(cls, joueurs) -> str:
        print("Informations sur les joueurs : ")
        print("------------------------------")
        for joueur in joueurs:
            print(f"Id: {joueur.id}")
            print(f"Nom: {joueur.nom}")
            print(f"Prénom: {joueur.prenom}")
            print(f"Date de naissance: {joueur.date_naissance}")
            print(f"Score: {joueur.score}")
            print("------------------------------")

    @classmethod
    def nouveau_tour(cls) -> str:
        nom = input("Nom du tour : ")
        date_debut = input("Date de début du tour : ")
        date_fin = input("Date de fin du tour : ")
        return nom, date_debut, date_fin
