#!/usr/bin/python3
"""
Module that contains the function write_file.
"""


def write_file(filename="", text=""):
    """
    write a text UTF-8 text file.

    Args:
        filename (str): The name of the file to be write.
    Default is an empty string.

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.write(text), end="")
