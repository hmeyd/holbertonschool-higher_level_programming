#!/usr/bin/python3
"""
Module that contains the function read_file.
"""


def read_file(filename=""):
    """
    Reads a UTF-8 text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to be read.
    Default is an empty string.

    Returns:
        None
    """
    with open(filename, "r") as f:
        for line in f:
            print(line.strip)
