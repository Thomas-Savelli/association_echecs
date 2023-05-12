from models.tournoi import Tournoi


class Controller:
    def __init__(self, view):
        self.view = view
        self.tournoi = None
    
    def start(self):
        while True:
            choix = self.view.menu_principal()
            if choix == "1":
                print("super on démarre")
                self.creer_tournoi()
            else:
                print("aurevoir !")
                break

    def creer_tournoi(self):
        """creer un tournoi et le stocker dans self.tournoi"""
        infos_tournoi = self.view.nouveau_tournoi()
        tournoi = Tournoi()
        
        self.tournoi = tournoi
