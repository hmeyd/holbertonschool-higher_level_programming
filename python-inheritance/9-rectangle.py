#!/usr/bin/python3
"""
A class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""

# Importation de BaseGeometry depuis 7-base_geometry.py
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance.
        """
        """Validation des valeurs"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        """ Attributs privés"""
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a formatted string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height
