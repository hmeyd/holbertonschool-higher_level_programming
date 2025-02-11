#!/usr/bin/python3
"""
unction that returns the JSON representation of an object (string)
"""
import json


def from_json_string(my_obj):
    """Convertit une chaîne JSON en objet Python."""
    return json.dumps(my_obj)
