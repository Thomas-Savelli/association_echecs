class Joueur:
    """La classe "Joueur" permet de stocker les informations des joueurs"""
    def __init__(self, nom, prenom, date_naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.total_point = 0

    def __str__(self):
        return f"{self.prenom} {self.nom}, né(e) le {self.date_naissance}"
