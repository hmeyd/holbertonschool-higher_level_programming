#!/usr/bin/python3
"""
Ce module fournit une classe Rectangle pour représenter des Rectangle.
La classe Rectangle permet de manipuler et de calculer des propriétés
des Rectangle.
"""


class Rectangle:

    """
    Une classe qui définit un Rectangle.

    Attributs :
        Aucun pour le moment (c'est un exemple minimal).
    """
    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height

    @property
    def width(self):
        """
            Getter pour l'attribut privé `__width`.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter pour l'attribut privé `__width` avec des vérifications.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter pour l'attribut privé `__height`.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter pour l'attribut privé `__height` avec des vérifications.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
