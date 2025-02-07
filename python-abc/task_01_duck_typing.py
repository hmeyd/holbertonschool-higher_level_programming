#!/usr/bin/python3
""" Duck Typing """
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Classe abstraite
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
        self.__radius = abs(radius)

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
        self.width = width
        self.height = height

    def area(self):
        """Retourne l'aire du rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Retourne le périmètre du rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Fonction affichant l'aire et le périmètre d'une forme géométrique.

    Args:
        shape (Shape): Une instance d'une sous-classe de Shape.
    """
    print("Aire: {}".format(shape.area()))
    print("Périmètre:{}".format(shape.perimeter()))
