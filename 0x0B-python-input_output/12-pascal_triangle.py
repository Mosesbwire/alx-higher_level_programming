#!/usr/bin/python3
"""
Module 12-pascal_triangle

Contains function that calculates pascal's triangle
"""


def pascal_triangle(n):
    """Calculates the pascal triangle
    Args:
        n (int): number of triangles to produce
    Returns:
        list of lists of integers
    """

    if n == 0:
        return []

    my_list = []

    for x in range(n):
        row = []
        prev_row = []
        if len(my_list) != 0:
            prev_row = my_list[x - 1]
        for y in range(x + 1):
            num = 0
            if (y == 0 or y == len(prev_row)):
                num = 1
            else:
                num = prev_row[y] + prev_row[y - 1]

            row.append(num)
        my_list.append(row)
    return my_list
