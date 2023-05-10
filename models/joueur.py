class Joueur:
    """La classe "Joueur" permet de stocker les informations des joueurs"""
    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.score = 0

    def afficher_info(self):
        print(f"{self.prenom} {self.nom}, né(e) le {self.date_naissance} - \
                 {self.score}")
