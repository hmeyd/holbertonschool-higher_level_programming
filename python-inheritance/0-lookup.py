#!/usr/bin/python3
"""
Ce module fournit une fonction pour retourner la liste des
attributs et méthodes d'un objet.
"""


def lookup(obj):
    """
    Retourne la liste des attributs et méthodes d'un objet.

    :param obj: L'objet à inspecter
    :return: Une liste des attributs et méthodes de l'objet
    """
    return dir(obj)
