#!/usr/bin/python3
"""
serialize and deserialize custom Python
objects using the pickle module
"""
import pickle


class CustomObject:
    """This class should have the following attributes"""
    def __init__(self, first_name, last_name, age):
        """fuction qui initialise le valeur"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def serialize(self, filename):
        """serialize"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """deserialize"""
        with open(filename, "rb") as f:
            return pickle.load(f)
