#!/usr/bin/python3
"""
A class Square that inherits from Rectangle (9-rectangle.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (must be a positive integer).
        """
        self.integer_validator("size", size)  # Validation du size
        super().__init__(size, size)  # Appel du constructeur de Rectangle




s = Square(13)

print(s)
print(s.area())