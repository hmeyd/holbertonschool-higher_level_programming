#!/usr/bin/python3
"""
that returns a list of lists of integers
representing the Pascal s triangle of n
"""


def pascal_triangle(n):
    """Si n <= 0, retourne une liste vide"""
    my_list = []
    if n <= 0:
        my_list
    else:
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = my_list[i - 1][j - 1] + my_list[i - 1][j]
            my_list.append(row)
    return my_list
