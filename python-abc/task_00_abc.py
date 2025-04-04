#!/usr/bin/python3
"""
Module définissant une classe abstraite Animal et ses sous-classes Dog et Cat.
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe abstraite représentant un animal.
    Chaque sous-classe doit implémenter la méthode `sound()`.
    """

    @abstractmethod
    def sound(self):
        """
        Méthode abstraite qui doit être implémentée par toutes les sous-
        classes.
        Elle définira le son que fait l'animal.
        """
        pass


class Dog(Animal):
    """
    Classe Dog qui hérite de Animal.
    Elle implémente la méthode `sound()` pour retourner "Bark".
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    Classe Cat qui hérite de Animal.
    Elle implémente la méthode `sound()` pour retourner "Meow".
    """

    def sound(self):
        return "Meow"
