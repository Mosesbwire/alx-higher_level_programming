#!/usr/bin/python3
""" Divides each element of a matrix"""


def matrix_divided(matrix, div):
    """
    divides every element of matrix with div
    Args:
        matrix (list): List of lists containig floats or integers
        div (int or float): number to divide matrix elements by
    Returns:
        matrix with result of dividing each element with div

    Raises:
        TypeError: if div is not a number or matrix is not a list of lists of int or floats
        ZeroDivisionError: if div is zero

    """
    a_list_len = 0
    new_matrix = []

    if type(matrix) is not list:
        raise TypeError("matrix must be a list")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if len(matrix) == 0:
        return []
    a_list_len = len(matrix[0])

    for a_list in matrix:
        if type(a_list) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if len(a_list) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if a_list_len != len(a_list):
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for element in a_list:
            if type(element) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            new_list.append(round(element / div, 2))
        new_matrix.append(new_list)

    return new_matrix


if __name__ == "__main__":
    matrix = [[30, 50, 20], [3, 9, 10], [1000, 5300, 77]]
    new_matrix = matrix_divided(matrix, 3)
    print("original {}".format(matrix))
    print("new {}".format(new_matrix))
