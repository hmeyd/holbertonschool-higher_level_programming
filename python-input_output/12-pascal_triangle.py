#!/usr/bin/python3
"""
that returns a list of lists of integers
representing the Pascal s triangle of n
"""


def pascal_triangle(n):
    my_list = {}
    if n <= 0:
        my_list
    else:
        for i in range(n):
            for j in range(i):
                if j == 1 or j == i:
                    my_list[i][j] = 1
                else:
                    my_list[i][j] = my_list[i - 1][j - 1] + my_list[i - 1][j]
    return my_list
