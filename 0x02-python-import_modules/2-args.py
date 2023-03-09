#!/usr/bin/python3
import sys


def print_args():
    args = sys.argv
    if (len(args) == 1):
        print("0 arguments.")
        return
    if (len(args) == 2):
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(args) - 1))

    for x in range(len(args)):
        if (x != 0):
            print("{:d}: {}".format(x, args[x]))


if __name__ == "__main__":
    print_args()
