class Joueur:
    """La classe "Joueur" permet de stocker les informations des joueurs"""
    def __init__(self, id, nom, prenom, date_naissance):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.score = 0

    def __repr__(self):
        return f"{self.id} {self.nom} {self.prenom} - {self.date_naissance} - score: {self.score}"

    def gagne(self):
        self.score += 1

    def egalise(self):
        self.score += 0.5

    def perd(self):
        pass


if __name__ == '__main__':
    joueur = Joueur("qlizdj", "jean", "toto", "10/12/3434")
    print(joueur)
