#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
The matrix must be a list of lists of integers or floats.
Each row of the matrix must be of the same size.
"div" must be a number (integer or float) but not 0.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.
    Args:
        matrix (list of lists): A list of lists of integers or floats.
        div (int or float): The divisor.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    rows_check = []
    for row in matrix:
        if not isinstance(row, list):
            rows_check.append(False)
        else:
            rows_check.append(True)
    if not all(rows_check):
        raise TypeError(msg)
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for i in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), i)))
    return new_matrix
