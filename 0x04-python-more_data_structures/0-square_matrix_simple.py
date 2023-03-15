#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_list = []

    if (not isinstance(matrix, list) or len(matrix) == 0):
        return

    for x in matrix:
        if isinstance(x, list) and len(x) > 0:
            result = [y**2 for y in x]
            squared_list.append(result)
    return squared_list


if __name__ == "__main__":
    square_matrix_simple([])
