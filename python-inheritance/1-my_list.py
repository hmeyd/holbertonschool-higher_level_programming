#!/usr/bin/python3
class MyList(list):
    """Classe qui hérite de list et ajoute une méthode
    pour afficher une liste triée.
    """

    def print_sorted(self):
        """Affiche la liste triée sans modifier la liste originale.
        """
        print(sorted(self))
