#!/usr/bin/python3
"""
Module définissant une classe VerboseList qui hérite de list.
Elle affiche des messages à chaque modification de la liste.
"""


class VerboseList(list):
    """
    Classe qui hérite de list et affiche des messages
    lorsqu'on ajoute ou supprime des éléments.
    """

    def append(self, item):
        """
        Ajoute un élément à la liste et affiche un message.

        Args:
            item: L'élément à ajouter.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Étend la liste avec plusieurs éléments et affiche un message.

        Args:
            iterable: Un iterable contenant les éléments à ajouter.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

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
            print(f"Removed [{item}] from the list.")

    def pop(self, index=-1):
        """
        Supprime et retourne l'élément à l'index donné et affiche un message.

        Args:
            index (int, optional): L'index de l'élément à supprimer.
                                   Par défaut, supprime le dernier élément.

        Returns:
            L'élément supprimé.

        Raises:
            IndexError: Si la liste est vide ou si l'index est hors limites.
        """
        if len(self) == 0:
            print("Error: Cannot pop from an empty list.")
            return None
