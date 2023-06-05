class Tour:
    """La classe "Tour" permet de stocker
    les informations d'un tour du tournoi"""
    def __init__(self, nom, date_debut, date_fin, matchs=None):
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.liste_matchs = matchs if matchs is not None else []

    def to_dict(self):
        """permet de convertir les données en dictionnaire
        car JSON ne peut pas représenter directement les objets
        personnalisés"""
        return {
            "nom": self.nom,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin,
            "matchs": [match.to_dict() for match in self.liste_matchs],
        }
