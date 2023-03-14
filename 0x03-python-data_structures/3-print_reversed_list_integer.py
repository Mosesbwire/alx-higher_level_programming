#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if (my_list is None):
        return

    length = len(my_list)
    n_length = (length + 1) * -1

    if (length == 0):
        return

    for i in range(-1, n_length, -1):
        print("{:d}".format(my_list[i]))


if __name__ == "__main__":
    print_reversed_list_integer([])
