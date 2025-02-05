#!/usr/bin/python3
"""
a function that returns True if the object is exactly an
instance of the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """ Function to check if obj is an instance of a_class
    or its subclass """
    return isinstance(obj, a_class)
