#!/usr/bin/python3
"""
 function that creates an Object from a “JSON file"
"""
import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object represented by the JSON content.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
