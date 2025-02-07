#!/usr/bin/python3
"""
Cet itérateur garde une trace du nombre d'éléments parcourus.
"""


class CountedIterator:
    """
    Classe qui étend la fonctionnalité des itérateurs en comptant
    le nombre d'éléments parcourus.
    """

    def __init__(self, iterable):
        """
        Initialise l'itérateur avec un objet iterable.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Rend l'objet itérable.
        """
        return self

    def __next__(self):
        """
        Récupère l'élément suivant et incrémente le compteur.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("Aucun élément restant dans l'itérateur.")

    def get_count(self):
        """
        Retourne le nombre d'éléments parcourus.
        """
        return self.count
