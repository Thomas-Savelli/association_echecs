class Tournoi:
    """La classe "Tournoi" permet de stocker les informations du tournoi """
    def __init__(self, nom, lieu, date_debut, date_fin,
                 nombre_tours=4, description=''):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_tours = nombre_tours
        self.numero_tour_actuel = 1
        self.liste_tours = []
        self.liste_joueurs = []
        self.description = description

    def ajouter_joueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def afficher_joueurs(self):
        for joueur in self.liste_joueurs:
            print(joueur.nom, joueur.prenom)
