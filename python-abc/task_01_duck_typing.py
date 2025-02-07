#!/usr/bin/python3
"""
Module définissant une classe abstraite Shape et ses sous-classes
Circle et Rectangle.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Classe abstraite représentant une forme géométrique.
    Les sous-classes doivent implémenter les méthodes
    `area()` et `perimeter()`.
    """

    @abstractmethod
    def area(self):
        """Méthode abstraite pour calculer l'aire de la forme."""
        pass

    @abstractmethod
    def perimeter(self):
        """Méthode abstraite pour calculer le périmètre de la forme."""
        pass


class Circle(Shape):
    """
    Classe représentant un cercle, héritant de Shape.
    """

    def __init__(self, radius):
        """
        Initialise un cercle avec un rayon donné.

        Args:
            radius (float): Le rayon du cercle (doit être positif).
        """
        if radius <= 0:
            raise ValueError("Le rayon doit être un nombre positif")
        self.__radius = radius

    def area(self):
        """Retourne l'aire du cercle."""
        return math.pi * self.__radius ** 2

    def perimeter(self):
        """Retourne le périmètre du cercle."""
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    Classe représentant un rectangle, héritant de Shape.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec une largeur et une hauteur.

        Args:
            width (float): La largeur du rectangle (doit être positive).
            height (float): La hauteur du rectangle (doit être positive).
        """
        if width <= 0 or height <= 0:
            raise ValueError("La largeur et la h doivent être es n positifs")
        self.__width = width
        self.__height = height

    def area(self):
        """Retourne l'aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre du rectangle."""
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    Fonction affichant l'aire et le périmètre d'une forme géométrique.

    Args:
        shape (Shape): Une instance d'une sous-classe de Shape.
    """
    print(f"Aire: {shape.area()}")
    print(f"Périmètre: {shape.perimeter()}")
