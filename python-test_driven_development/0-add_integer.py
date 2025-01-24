#!/usr/bin/python3

"""
Module add_integer

Ajoute deux nombres entiers ou floats (convertis en entiers).
"""


def add_integer(a, b=98):

    """
    Ajoute deux entiers ou floats.

    Args:
        a (int, float): Premier nombre.
        b (int, float): Deuxième nombre (par défaut 98).

    Raises:
        TypeError: Si `a` ou `b` n'est ni un entier ni un float.

    Returns:
        int: La somme des deux nombres.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
