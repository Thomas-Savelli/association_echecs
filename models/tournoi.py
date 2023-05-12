class Tournoi:
    """La classe "Tournoi" permet de stocker les informations du tournoi """
    def __init__(self, nom, lieu, date_debut, date_fin,
                 nombre_tours=4, description=''):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nombre_tours = nombre_tours
        self.liste_tours = []
        self.liste_joueurs = []
        self.description = description

    def ajouter_joueur(self, joueur):
        # Permet d'ajouter un joueur au tournoi
        self.liste_joueurs.append(joueur)

    def afficher_joueurs(self):
        # Permet d'afficher les joueurs du tournoi par ordre alphabétique
        joueurs_tri = sorted(self.liste_joueurs, key=lambda joueur: joueur.nom)
        for joueur in joueurs_tri:
            print(joueur)

    def classement(self):
        # Permet d'afficher le classement des joueurs dans le tournoi
        classement_joueur = sorted(self.liste_joueurs,
                                   key=lambda j: j.score, reverse=True)
        print("Classement :")
        for i, joueur in enumerate(classement_joueur, start=1):
            print(f"{i}. {joueur.nom} {joueur.prenom} ({joueur.score})")

    def __repr__(self):
        return f"Nom : {self.nom}\nLieu : {self.lieu}\
                \nDate : {self.date_debut} - {self.date_fin}\
                \nNombre de tours : {self.nombre_tours}\
                \nDescription : {self.description}\n"

    def generer_tour(self)
        """generer un tour avec une liste de matchs et l'ajouter à la liste des tours"""