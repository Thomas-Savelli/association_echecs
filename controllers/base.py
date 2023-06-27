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
                os.system("cls")
            elif choix == "2":
                dossier_tournois = "data_tournois"
                if not os.path.exists(dossier_tournois) or not os.listdir(dossier_tournois):
                    os.system("cls")
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
                                choix_sous_menu = self.view.sous_menu_tours(tournoi.nom)
                                if choix_sous_menu == "1":
                                    self.view.afficher_informations_tours(tournoi)
                                    if choix_sous_menu != "":
                                        None
                                    else:
                                        continue
                                elif choix_sous_menu == "2":
                                    while True:
                                        os.system("cls")
                                        Esthetique.afficher_banniere()
                                        tour_index = self.view.afficher_tours_disponibles(tournoi)
                                        if tour_index is None:
                                            break

                                        tour_selectionne = tournoi.liste_tours[tour_index - 1]
                                        if tour_selectionne.liste_matchs:
                                            print("\033[3;31mLes matchs ont déjà été générés pour ce tour.\033[0m")
                                        else:
                                            matchs = tournoi.generer_match(tour_selectionne)
                                            tour_selectionne.liste_matchs.extend(matchs)
                                            self.view.afficher_matchs(matchs)
                                            self.sauvegarder_tournoi(tournoi, nom_fichier)
                                            break

                                    self.sauvegarder_tournoi(tournoi, nom_fichier)
                                    continue
                                elif choix_sous_menu == "3":
                                    self.renseigner_resultats_matchs(tour_selectionne)
                                    self.sauvegarder_tournoi(tournoi, nom_fichier)
                                elif choix_sous_menu == "9":
                                    break
                        elif choix == "4":
                            self.view.afficher_classement_tournoi(tournoi)
                        elif choix == "9":
                            self.sauvegarder_tournoi(tournoi, nom_fichier)
                            os.system("cls")
                            break
                        else:
                            None
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
                os.system("cls")
                print("")
                print("\033[1;31mErreur de Saisie :\033[0m")
                print("\033[3;31mVeuillez entrer toutes les informations.\033[0m")

        tournoi = Tournoi(*infos_tournoi)
        self.tournoi = tournoi

    def creer_joueur(self):
        """Creer une paire de joueurs pour le tournoi et les stockent dans self.joueur
        puis ajout des joueurs à la liste des joueurs"""
        print("")
        print("\033[1;32mVeuillez créer une paire de joueurs -->\033[0m")
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
        if not self.tournoi.liste_joueurs:
            print("\033[3;31mAucun joueur n'a été créé ...\033[0m")

        nombre_tours = self.tournoi.nombre_tours
        if nombre_tours <= 0:
            print("\033[3;31mLe nombre de tours du tournoi doit être supérieur à zéro !\033[0m")

        for tour_index in range(1, nombre_tours + 1):
            print("")
            print(f"\033[1;32mCréation du tour {tour_index}\033[0m")

            while True:
                infos_tour = self.view.nouveau_tour()
                if all(infos_tour):
                    break
                else:
                    print("")
                    print("\033[1;31mErreur de Saisie :\033[0m")
                    print("\033[3;31mVeuillez entrer toutes les informations.\033[0m")
            nouveau_tour = Tour(*infos_tour)
            self.tournoi.liste_tours.append(nouveau_tour)

    def sauvegarder_tournoi(self, tournoi, nom_fichier):
        joueurs_data = []
        for joueur in tournoi.liste_joueurs:
            joueur_data = joueur.to_dict()
            joueurs_data.append(joueur_data)

        tours_data = []
        matchs_data = []

        for tour in tournoi.liste_tours:
            tour_data = tour.to_dict()
            tour_matchs_data = [match.to_dict() for match in tour.liste_matchs]
            tours_data.append({**tour_data, "matchs": tour_matchs_data})
            matchs_data.extend(tour_matchs_data)

        # Créer le dictionnaire des données du tournoi
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

        # Créer le dossier pour les tournois s'il n'existe pas
        dossier_tournoi = "data_tournois"
        if not os.path.exists(dossier_tournoi):
            os.mkdir(dossier_tournoi)

        # Créer le chemin complet du fichier
        chemin_fichier = os.path.join(dossier_tournoi, nom_fichier)

        # Écrire les données du tournoi dans le fichier JSON
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
        tours_data = tournoi_data.get("tours", [])
        for tour_data in tours_data:
            tour = Tour(**tour_data)

        # Charger les matchs à partir des données du tour
            tour.liste_matchs = []
            matchs_data = tour_data.get("matchs", [])
            for match_data in matchs_data:
                joueur1_data = match_data.get("joueur1", {})
                joueur1 = Joueur(**joueur1_data)
                joueur2_data = match_data.get("joueur2", {})
                joueur2 = Joueur(**joueur2_data)
                score1 = match_data.get("score1", 0)
                score2 = match_data.get("score2", 0)
                match = Match(joueur1, joueur2, score1, score2)
                tour.liste_matchs.append(match)

            # Ajouter le tour à la liste des tours du tournoi
            tournoi.liste_tours.append(tour)

        # Création d'un objet Tournoi à partir des données chargées
        tournoi.liste_joueurs = joueurs

        return tournoi

    def liste_fichiers_tournois(self):
        fichiers = []
        for nom_fichier in os.listdir("data_tournois"):
            if nom_fichier.endswith(".json"):
                fichiers.append(nom_fichier)
        return fichiers

    def chemin_fichier_tournoi(self, nom_fichier):
        return os.path.join("data_tournois", nom_fichier)

    def creation_matchs(self, tournoi):
        while True:
            tour_index = self.view.afficher_tours_disponibles(tournoi)
            if tour_index is None:
                return

            tour_selectionne = tournoi.liste_tours[tour_index - 1]
            if tour_selectionne.liste_matchs:
                print("Les matchs ont déjà été générés pour ce tour.")
            else:
                matchs = tournoi.generer_match(tour_selectionne)
                tour_selectionne.liste_matchs.extend(matchs)
                self.view.afficher_matchs(matchs)
                break

    def renseigner_resultats_matchs(self, tour):
        print(f"Renseigner les résultats des matchs pour le tour {tour.nom}")
        print("")

        for match in tour.liste_matchs:
            joueur1 = match.joueur1
            joueur2 = match.joueur2

            print(f"Match : {joueur1.nom} {joueur1.prenom} vs {joueur2.nom} {joueur2.prenom}")
            resultat_joueur1 = self.view.demande_resultat_match(joueur1.nom, joueur1.prenom)
            resultat_joueur2 = self.view.demande_resultat_match(joueur2.nom, joueur2.prenom)

            if self.valider_resultats(resultat_joueur1, resultat_joueur2):
                match.renseigner_resultat_match(resultat_joueur1, resultat_joueur2)
                joueur1.resultat(resultat_joueur2, resultat_joueur1)
                joueur2.resultat(resultat_joueur1, resultat_joueur2)
            else:
                print("Les résultats saisis ne sont pas valides. Veuillez réessayer.")

        print("\nLes résultats des matchs ont été renseignés avec succès.\n")

    def valider_resultats(self, resultat_joueur1, resultat_joueur2):
        if resultat_joueur1 == "g" and resultat_joueur2 == "p":
            return True
        elif resultat_joueur1 == "p" and resultat_joueur2 == "g":
            return True
        elif resultat_joueur1 == "n" and resultat_joueur2 == "n":
            return True
        else:
            return False
