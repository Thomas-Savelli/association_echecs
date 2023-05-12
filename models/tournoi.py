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
        # Permet d'ajouter un joueur au tournoi
        self.liste_joueurs.append(joueur)

    def afficher_joueurs(self):
        joueurs_tri = sorted(self.liste_joueurs, key=lambda joueur: joueur.nom)
        for joueur in joueurs_tri:
            print(joueur.afficher_info())

    def classement(self):
        # Permet d'afficher le classement des joueurs dans le tournoi
        classement_joueur = sorted(self.liste_joueurs,
                                   key=lambda j: j.score, reverse=True)
        print("Classement :")
        for i, joueur in enumerate(classement_joueur, start=1):
            print(f"{i}. {joueur.nom} {joueur.prenom} ({joueur.score})")

    def afficher_tournois(liste_tournois):
        # Affiche la liste de tous les tournois ainsi que leurs informations
        for tournoi in liste_tournois:
            print(f"Nom : {tournoi.nom}\nLieu : {tournoi.lieu}\
                  \nDate : {tournoi.date_debut} - {tournoi.date_fin}\
                  \nNombre de tours : {tournoi.nombre_tours}\
                  \nDescription : {tournoi.description}\n")
