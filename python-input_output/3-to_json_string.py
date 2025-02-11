#!/usr/bin/python3
"""
Function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Convertit une chaîne JSON en objet Python."""
    return json.dumps(my_str)
