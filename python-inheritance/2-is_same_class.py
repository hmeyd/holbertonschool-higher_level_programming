#!/usr/bin/python3
"""
a function that returns True if the object is exactly an
instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """ Function to check if an object is exactly an instance of a class """
    return type(obj) is a_class
