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
    new_text = ""

    for char in text:
        new_text += char
        if char in delimiters:
            print(new_text.strip())
            new_text = ""
    if new_text:
        print(new_text.strip())
