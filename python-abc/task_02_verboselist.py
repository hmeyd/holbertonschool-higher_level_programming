#!/usr/bin/python3
"""
Module définissant une classe VerboseList qui hérite de list.
Elle affiche des messages à chaque modification de la liste.
"""


class VerboseList(list):
    """
    Classe qui hérite de list
    """

    def append(self, item):
        """
        Ajoute un élément à la liste et affiche un message.

        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """
        Étend la liste avec plusieurs éléments et affiche un message.

        Args:
            iterable: Un iterable contenant les éléments à ajouter.
        """
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """
        Supprime un élément de la liste et affiche un message.

        Args:
            item: L'élément à supprimer.

        Raises:
            ValueError: Si l'élément n'existe pas dans la liste.
        """
        if item not in self:
            print(f"Error: Item [{item}] not found in the list.")
        else:
            super().remove(item)
            print("Removed [{}] from the list.".format(item))

    def pop(self, item=-1):
        if not (-len(self) <= item < len(self)):
            raise IndexError("index out of range")
        print("Popped [{}] from the list.".format(self[item]))
        return super().pop(item)
