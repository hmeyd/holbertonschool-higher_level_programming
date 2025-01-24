#!/usr/bin/python3
"""
Ce module fournit une fonction qui affiche
"Mon nom est <prénom> <nom de famille>"
où <prénom> et <nom de famille> doivent être des chaînes de caractères.
"""


def say_my_name(first_name, last_name=""):
    """
    Affiche 'Mon nom est <first_name> <last_name>'

    Arguments:
        first_name (str): Le prénom.
        last_name (str, optionnel): Le nom de famille.
    Par défaut, une chaîne vide.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
