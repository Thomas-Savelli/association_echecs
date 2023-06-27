class Joueur:
    """La classe "Joueur" permet de stocker les informations des joueurs"""
    def __init__(self, id, nom, prenom, date_naissance, score=0):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.score = score

    def __repr__(self):
        return f"{self.id} {self.nom} {self.prenom} - {self.date_naissance} - score: {self.score}"

    def to_dict(self):
        """permet de convertir les données en dictionnaire
        car JSON ne peut pas représenter directement les objets
        personnalisés"""
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "date_naissance": self.date_naissance,
            "score": self.score
        }

    def gagne(self):
        self.score += 1

    def egalise(self):
        self.score += 0.5

    def perd(self):
        pass

    def resultat(self, score1, score2):
        if score1 > score2:
            self.gagne()
        elif score1 < score2:
            self.perd()
        else:
            self.egalise()
