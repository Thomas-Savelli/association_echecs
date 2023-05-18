class Tour:
    """La classe "Tour" permet de stocker
    les informations d'un tour du tournoi"""
    def __init__(self, nom, date_debut, date_fin):
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = date_fin

    def to_dict(self):
        """permet de convertir les données en dictionnaire
        car JSON ne peut pas représenter directement les objets
        personnalisés"""
        return {
            "nom": self.nom,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin
        }
