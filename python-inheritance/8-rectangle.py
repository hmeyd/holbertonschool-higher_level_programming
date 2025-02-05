#!/usr/bin/python3
"""
a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class rectangle(BaseGeometry):
    """
    raises an Exception
    """
    def __init__(self, width, height):
        """validated by integer_validator"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
