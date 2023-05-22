
class Esthetique:
    @staticmethod
    def afficher_banniere():
        banniere = """
==================================================
|                                                |
|          GESTION DE TOURNOI - PROGRAMME         |
|                                                |
==================================================
"""
        print("\033[1;34m" + banniere + "\033[0m")
