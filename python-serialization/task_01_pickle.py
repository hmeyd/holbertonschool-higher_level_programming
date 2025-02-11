#!/usr/bin/python3
"""
serialize and deserialize custom Python
objects using the pickle module
"""
import pickle


class CustomObject:
    """This class should have the following attributes"""
    def __init__(self, name: str, age: int, is_student: bool):
        """fuction qui initialise le valeur"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet sous un format structuré.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """serialize"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """deserialize"""
        with open(filename, "rb") as f:
            return pickle.load(f)
