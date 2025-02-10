#!/usr/bin/python3
"""
Module that contains the function write_file.
"""


def append_write(filename="", text=""):
    """
    Writes a text in a UTF-8 text file.

    Args:
        filename (str): The name of the file to be written.
        text (str): The content to add in the file.

    Returns:
        nombre of caracters
    """
    count = 0
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
