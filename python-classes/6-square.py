#!/usr/bin/python3
"""
Ce module fournit une classe Square pour représenter des carrés.
La classe Square permet de manipuler et de calculer des propriétés des carrés.
"""


class Square:
    """
    Une classe qui définit un carré avec une taille et une position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise un carré avec une taille et une position optionnelles.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter pour l'attribut privé `__size`.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter pour l'attribut privé `__size` avec des vérifications.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter pour l'attribut privé `__position`.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter pour l'attribut privé `__position` avec des vérifications.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Retourne l'aire du carré.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Affiche le carré avec le caractère # en prenant en compte la position.
        """
        if self.__size == 0:
            print("")
            return

        # Imprime les lignes vides pour la position verticale
        for _ in range(self.__position[1]):
            print("")

        # Imprime les lignes du carré avec le décalage horizontal
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
