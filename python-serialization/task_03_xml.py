#!/usr/bin/python3
"""
Module permettant de sérialiser et désérialiser un dictionnaire en XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary: dict, filename: str) -> None:
    """
    Sérialise un dictionnaire en XML et enregistre le résultat dans un fichier.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)
    tree = ET.ElementTree(root)
    with open(filename, "wb") as xml_file:
        tree.write(xml_file, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename: str) -> dict:
    """
    Désérialise un fichier XML et reconstruit un dictionnaire.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        dictionary = {child.tag: child.text for child in root}

        print(f"Fichier '{filename}' désérialisé avec succès.")
        return dictionary

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{filename}' n'existe pas.")
    except ET.ParseError:
        print(f"Erreur : Le fichier '{filename}' n'est pas un XML valide.")

    return {}
