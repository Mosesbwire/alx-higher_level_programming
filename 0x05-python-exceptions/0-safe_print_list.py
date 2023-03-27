#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        if (not isinstance(my_list, list)):
            raise TypeError

    except TypeError:
        print()
        return count

    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        print()
    except TypeError:
        print()
    print()
    return count
