#!/usr/bin/python3
"""
Module permettant de convertir un fichier CSV en JSON.
"""
import csv
import json


def convert_csv_to_json(csv_filename: str) -> bool:
    """
    Convertit un fichier CSV en fichier JSON.
    """
    try:
        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            data = list(csv.DictReader(csv_file))
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except FileNotFoundError:
        return False
