#!/usr/bin/python3
"""
a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
    raises an Exception
    """
    def area(self):
        """Method that raises an Exception"""
        if self:
            raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raise a TypeError exception"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
