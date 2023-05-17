from models.tournoi import Tournoi
from models.joueur import Joueur
from models.tour import Tour


class Controller:
    def __init__(self, view):
        self.view = view
        self.tournoi = None
        self.tour = None

    def start(self):
        while True:
            choix = self.view.menu_principal()

            if choix == "1":
                self.creer_tournoi()
                self.creer_joueur()
                while True:
                    choix_2 = self.view.choix_2()
                    if choix_2 == "o":
                        self.creer_joueur()
                    else:
                        # print("Merci, vos données ont été enregistrées ! ")
                        break

                self.creer_tour()

            elif choix == "2":
                self.view.afficher_informations_tournoi(self.tournoi, self.tournoi.liste_joueurs,
                                                        self.tournoi.liste_tours)

            else:
                print("aurevoir !")
                break

    def creer_tournoi(self):
        """creer un tournoi et le stocker dans self.tournoi"""
        infos_tournoi = self.view.nouveau_tournoi()
        tournoi = Tournoi(*infos_tournoi)
        self.tournoi = tournoi

    def creer_joueur(self):
        """Creer joueur pour le tournoi et le stocker dans self.joueur
        puis ajout du joueur à la liste des joueurs"""
        infos_joueur = self.view.nouveau_joueur()
        joueur = Joueur(*infos_joueur)
        self.tournoi.ajouter_joueur(joueur)

    def creer_tour(self):
        """creer les tours du tournoi"""
        if self.tournoi is None:
            print("Aucun tournoi n'a été créé ...")
            return
        if self.tournoi.liste_joueurs is None:
            print("Aucun joueur n'a été créé ...")

        nombre_tours = self.tournoi.nombre_tours
        if nombre_tours <= 0:
            print("Le nombre de tours du tournoi doit être supérieur à zéro ...")

        for tour_index in range(1, nombre_tours + 1):
            print(f"Création du tour {tour_index}")

            infos_tour = self.view.nouveau_tour()
            tour_index = Tour(*infos_tour)
            self.tournoi.liste_tours.append(tour_index)
