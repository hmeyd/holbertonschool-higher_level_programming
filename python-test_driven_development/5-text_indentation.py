#!/usr/bin/python3
"""
Ce module fournit une fonction qui affiche un texte
avec 2 nouvelles lignes après chacun de ces caractères : ., ? et :
<text> doit être une chaîne de caractères.
Il ne doit y avoir aucun espace au début ou à la fin de chaque ligne imprimée.
"""


def text_indentation(text):
    """
    Affiche le texte avec 2 nouvelles lignes après
    chaque occurrence de '.', '?', ou ':'.

    Arguments:
        text (str): Le texte à afficher.

    Lève:
        TypeError: Si text n'est pas une chaîne de caractères.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ['.', '?', ':']
    i = 0
    while i < len(text):
        char = text[i]

        # Ignorer les espaces en début de ligne
        if char == ' ' and (i == 0 or text[i - 1] in delimiters):
            i += 1
            continue

        print(char, end="")
        if char in delimiters:
            print("\n")
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
