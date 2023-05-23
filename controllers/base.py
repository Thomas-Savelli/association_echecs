from models.tournoi import Tournoi
from models.joueur import Joueur
from models.tour import Tour
from models.match import Match
from views.esthetiqueview import Esthetique
import json
import os


class Controller:
    def __init__(self, view):
        self.view = view
        self.tournoi = None
        self.tour = None

    def start(self):
        while True:
            Esthetique.afficher_banniere()
            choix = self.view.menu_principal()

            if choix == "1":
                self.creer_tournoi()
                self.creer_joueur()
                while True:
                    choix_2 = self.view.choix_2()
                    if choix_2 == "o":
                        self.creer_joueur()
                    else:
                        break

                self.creer_tour()
                nom_fichier = self.tournoi.nom.replace(" ", "_") + ".json"
                self.sauvegarder_tournoi(self.tournoi, nom_fichier)
            elif choix == "2":
                dossier_tournois = "data_tournois"
                if not os.path.exists(dossier_tournois) or not os.listdir(dossier_tournois):
                    print("Le dossier de sauvegarde des tournois n'existe pas ou est vide.")
                    continue  # Retourne au début de la boucle while

                liste_fichiers = self.liste_fichiers_tournois()
                self.view.afficher_liste_fichiers(liste_fichiers)
                nom_fichier = self.view.demander_nom_fichier()
                if nom_fichier:
                    chemin_fichier = self.chemin_fichier_tournoi(nom_fichier)
                    tournoi = self.charger_tournoi(chemin_fichier)
                    while True:
                        os.system("cls")
                        Esthetique.afficher_banniere()
                        choix = self.view.menu_gestion_tournoi(tournoi.nom)
                        if choix == "1":
                            choix = self.view.afficher_informations_tournoi(tournoi)
                            if choix != "":
                                None
                            else:
                                continue
                        elif choix == "2":
                            choix = self.view.afficher_informations_joueurs(tournoi)
                            if choix != "":
                                None
                            else:
                                continue
                        elif choix == "3":
                            while True:
                                os.system("cls")
                                Esthetique.afficher_banniere()
                                choix = self.view.sous_menu_tours(tournoi.nom)
                                if choix == "1":
                                    self.view.afficher_informations_tours(tournoi)
                                    if choix != "":
                                        None
                                    else:
                                        continue
                                elif choix == "2":
                                    while True:
                                        Esthetique.afficher_banniere()
                                        choix_action = self.view.afficher_tours_disponibles(tournoi)
                                        if choix_action == "1":
                                            resultat_action = self.generer_match_tour(tournoi)
                                            if resultat_action == "retour_menu":
                                                break
                                elif choix == "9":
                                    break
                        elif choix == "4":
                            print("Affiche le classement du tournoi")
                        elif choix == "9":
                            os.system("cls")
                            break
            elif choix == "9":
                print("Au revoir !")
                break
            else:
                None

    def creer_tournoi(self):
        """creer un tournoi et le stocker dans self.tournoi"""
        while True:
            infos_tournoi = self.view.nouveau_tournoi()
            if all(infos_tournoi):
                break
            else:
                print("")
                print("Erreur de Saisie :")
                print("Veuillez entrée toutes les informations.")

        tournoi = Tournoi(*infos_tournoi)
        self.tournoi = tournoi

    def creer_joueur(self):
        """Creer une paire de joueurs pour le tournoi et les stockent dans self.joueur
        puis ajout des joueurs à la liste des joueurs"""
        while True:
            infos_joueur1 = self.view.nouveau_joueur()
            if all(infos_joueur1):
                joueur1 = Joueur(*infos_joueur1)
                self.tournoi.ajouter_joueur(joueur1)
            else:
                print("")
                print("Erreur de Saisie :")
                print("Veuillez entrer toutes les informations.")
                continue

            infos_joueur2 = self.view.nouveau_joueur()
            if all(infos_joueur2):
                joueur2 = Joueur(*infos_joueur2)
                self.tournoi.ajouter_joueur(joueur2)
            else:
                print("Veuillez entrer toutes les informations.")
                continue

            if len(self.tournoi.liste_joueurs) % 2 == 0:
                break
            else:
                print("Le nombre de joueurs doit être pair. Veuillez saisir les joueurs deux par deux.")

    def creer_tour(self):
        """creer les tours du tournoi"""
        if self.tournoi.liste_joueurs is None:
            print("Aucun joueur n'a été créé ...")

        nombre_tours = self.tournoi.nombre_tours
        if nombre_tours <= 0:
            print("Le nombre de tours du tournoi doit être supérieur à zéro ...")

        for tour_index in range(1, nombre_tours + 1):
            print(f"Création du tour {tour_index}")

            while True:
                infos_tour = self.view.nouveau_tour()
                if all(infos_tour):
                    break
                else:
                    print("")
                    print("Erreur de Saisie :")
                    print("Veuillez entrer toutes les informations.")
            tour_index = Tour(*infos_tour)
            self.tournoi.liste_tours.append(tour_index)

    def creer_matchs(self):
        self.tournoi.generer_match()

    def sauvegarder_tournoi(self, tournoi, nom_fichier):
        # Converti les objects en dictionnaires
        joueurs_data = [joueur.to_dict() for joueur in tournoi.liste_joueurs]
        tours_data = [tour.to_dict() for tour in tournoi.liste_tours]
        matchs_data = [match.to_dict() for match in tournoi.liste_matchs]

        # Crée le dictionnaire des données du tournoi
        tournoi_data = {
            "nom": tournoi.nom,
            "lieu": tournoi.lieu,
            "date_debut": tournoi.date_debut,
            "date_fin": tournoi.date_fin,
            "nombre_tours": tournoi.nombre_tours,
            "description": tournoi.description,
            "joueurs": joueurs_data,
            "tours": tours_data,
            "matchs": matchs_data,
        }

        # Crée le dossier pour les tournois s'il n'existe pas
        dossier_tournoi = "data_tournois"
        if not os.path.exists(dossier_tournoi):
            os.mkdir(dossier_tournoi)

        # Crée le chemin complet du fichier
        chemin_fichier = os.path.join(dossier_tournoi, nom_fichier)

        # Ecrit les données du tournoi dans le fichier JSON
        with open(chemin_fichier, "w") as fichier:
            json.dump(tournoi_data, fichier, indent=4)

    def charger_tournoi(self, mon_fichier):
        chemin_fichier = os.path.join(mon_fichier)
        print("chemin du fichier : ", chemin_fichier)
        if not os.path.exists(chemin_fichier):
            print("Le fichier spécifié n'existe pas.")
            return None

        with open(chemin_fichier, "r") as fichier:
            tournoi_data = json.load(fichier)
        # Charger les attributs du tournoi à partir du fichier JSON
            nom = tournoi_data.get("nom")
            lieu = tournoi_data.get("lieu")
            date_debut = tournoi_data.get("date_debut")
            date_fin = tournoi_data.get("date_fin")

        # Créer un objet Tournoi avec les attributs chargés
        tournoi = Tournoi(nom=nom, lieu=lieu, date_debut=date_debut, date_fin=date_fin)

        # Création des objets Joueur à partir des données fichier
        joueurs = []
        joueurs_data = tournoi_data.get("joueurs", [])
        for joueur_data in joueurs_data:
            joueur = Joueur(**joueur_data)
            joueurs.append(joueur)

        # Création des objets Tour à partir des données fichier
        tours = []
        tours_data = tournoi_data.get("tours", [])
        for tour_data in tours_data:
            tour = Tour(**tour_data)
            tours.append(tour)

        # Création des objets Match à partir des données fichier
        matchs = []
        matchs_data = tournoi_data.get("matchs", [])
        for match_data in matchs_data:
            joueur1_data = match_data.get("joueur1", {})
            joueur1 = Joueur(**joueur1_data)
            joueur2_data = match_data.get("joueur2", {})
            joueur2 = Joueur(**joueur2_data)
            score1 = match_data.get("score1", 0)
            score2 = match_data.get("score2", 0)
            match = Match(joueur1, joueur2, score1, score2)
            matchs.append(match)

        # Création d'un objet Tournoi à partir des données chargées
        tournoi.liste_joueurs = joueurs
        tournoi.liste_tours = tours
        tournoi.liste_matchs = matchs

        return tournoi

    def liste_fichiers_tournois(self):
        fichiers = []
        for nom_fichier in os.listdir("data_tournois"):
            if nom_fichier.endswith(".json"):
                fichiers.append(nom_fichier)
        return fichiers

    def chemin_fichier_tournoi(self, nom_fichier):
        return os.path.join("data_tournois", nom_fichier)

    def generer_match_tour(cls, tournoi) -> str:
        choix_tour = cls.view.afficher_tours_disponibles(tournoi)
        tour_selectionne = tournoi.liste_tours[choix_tour - 1]

        if tour_selectionne.matchs:
            choix_action = cls.view.afficher_matchs_existants(tour_selectionne)

            if choix_action == "1":
                cls.view.afficher_matchs_tour(tour_selectionne)
            elif choix_action == "2":
                return "retour_menu"
            else:
                print("Choix invalide. Veuillez réessayer.")
        else:
            tour_selectionne.generer_match()
            print(f"Les matchs ont été générés pour le tour '{tour_selectionne.nom}'.")

        return "continuer"
