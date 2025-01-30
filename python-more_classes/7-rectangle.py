#!/usr/bin/python3
"""
Ce module fournit une classe Rectangle pour représenter des rectangles.
La classe Rectangle permet de manipuler et de calculer des
propriétés des rectangles.
"""


class Rectangle:
    """
    Une classe qui définit un rectangle.

    Attributs de classe :
        number_of_instances (int) : Nombre d'instances existantes de Rectangle.
        print_symbol (any) : Symbole utilisé pour représenter le rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise un rectangle avec une largeur et une hauteur.

        Args:
            width (int): La largeur du rectangle (par défaut 0).
            height (int): La hauteur du rectangle (par défaut 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter pour l'attribut privé `__width`."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter pour l'attribut privé `__width` avec des vérifications."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter pour l'attribut privé `__height`."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter pour l'attribut privé `__height` avec des vérifications."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcule et retourne l'aire du rectangle."""
        return self.__height * self.__width

    def perimeter(self):
        """Calcule et retourne le périmètre du rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        Affiche le rectangle avec des caractères `#`.
        Si la largeur ou la hauteur est 0, la méthode n'affiche rien.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = []
        for _ in range(self.__height):
            rectangle_str.append(str(self.print_symbol)* self.__width)
        return "\n".join(rectangle_str)

    def __repr__(self):
        """
        Retourne une chaîne de caractères permettant de recréer
        une instance identique.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Affiche un message lorsqu'une instance de Rectangle est supprimée.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
