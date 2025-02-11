#!/usr/bin/python3
"""une fonction que serialiser et deserialise """
import json


def serialize_and_save_to_file(data, filename):
    
    with open(filename, "r", encoding="utf-8") as f:
        json.dumps(f, data)
    pass

def load_and_deserialize(filename):
     with open(filename, "r", encoding="utf-8") as f:
        return json.__dict__
