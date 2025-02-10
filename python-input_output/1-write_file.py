#!/usr/bin/python3
"""
Module that contains the function write_file.
"""


def write_file(filename="", text=""):
    """
    Writes a text in a UTF-8 text file.

    Args:
        filename (str): The name of the file to be written.
        text (str): The content to write in the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        print(f.write(text))
