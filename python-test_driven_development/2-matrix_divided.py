#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.
    Args:
        matrix (list of lists): A list of lists of integers or floats.
        div (int or float): The divisor.
    Returns:
        list of lists: A new matrix with all elements divided by div,
                       rounded to 2 decimal places.
    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(msg)
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
    return [[round(element / div, 2) for element in row] for row in matrix]
