#!/usr/bin/python3
"""
Ce module fournit une fonction qui affiche un carré avec le caractère #
<size> est la longueur du côté du carré
et doit être un entier positif
"""


def print_square(size):
    """
    Affiche un carré de taille 'size' avec le caractère '#'.
    Arguments:
        size (int): La taille du côté du carré.

    Lève:
        TypeError: Si size n'est pas un entier.
        TypeError: Si size est un nombre à virgule flottante
        et est inférieur à 0.
        ValueError: Si size est inférieur à 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print('#' * size)
