#!/usr/bin/python3
"""
Module définissant une classe FlyingFish qui hérite de Fish et Bird.
Ce module explore l'héritage multiple et le MRO (Method Resolution Order).
"""


class Fish:
    """
    Classe représentant un poisson.
    """

    def swim(self):
        """Affiche un message indiquant que le poisson nage."""
        print("The fish is swimming.")

    def habitat(self):
        """Affiche l'habitat du poisson."""
        print("The fish lives in water.")


class Bird:
    """
    Classe représentant un oiseau.
    """

    def fly(self):
        """Affiche un message indiquant que l'oiseau vole."""
        print("The bird is flying.")

    def habitat(self):
        """Affiche l'habitat de l'oiseau."""
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    """
    Classe représentant un poisson volant.
    Hérite des classes Fish et Bird.
    """

    def fly(self):
        """Redéfinit la méthode fly pour un poisson volant."""
        print("The flying fish is soaring!")

    def swim(self):
        """Redéfinit la méthode swim pour un poisson volant."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Redéfinit la méthode habitat pour un poisson volant."""
        print("The flying fish lives both in water and the sky!")
