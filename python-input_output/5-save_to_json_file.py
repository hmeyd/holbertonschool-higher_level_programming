#!/usr/bin/python3
"""
Function that writes an Object to a text file
"""
import json


def save_to_json_file(my_obj, filename):
    """ function """
    with open(filename, "w", encoding="utf-8") as f:
        jason = json.dumps(my_obj)
        return f.write(jason)
