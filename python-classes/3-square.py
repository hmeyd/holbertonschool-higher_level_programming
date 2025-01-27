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

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2
