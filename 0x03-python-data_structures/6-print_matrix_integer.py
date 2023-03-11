#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if (len(matrix[x]) > 0):
                val = matrix[x][y]
                if (y == len(matrix[x]) - 1):
                    print("{:d}".format(val), end="")
                else:
                    print("{:d} ".format(val), end="")
        print()


if __name__ == "__main__":
    print_matrix_integer()
