#!/usr/bin/python3
"""
Ce module fournit une classe Square pour représenter des carrés.
La classe Square permet de manipuler et de calculer des propriétés des carrés.
"""


class Square:

    """
    Une classe qui définit un carré.

    Attributs :
        oject has non attribute 'size'.
    """
    def __init__(self, size=0):

        self.__size = size

    @property
    def size(self):
        """
        Getter pour l'attribut privé `__size`.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for i in range(self.__size):
                    print("#", end="")
            print()
