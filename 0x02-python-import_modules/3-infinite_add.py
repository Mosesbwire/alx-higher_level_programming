#!/usr/bin/python3
import sys


def add():
    args = sys.argv
    total = 0
    if (len(args) == 1):
        print(0)
        return
    for i in range(1, len(args)):
        total += int(args[i])
    print(total)


if __name__ == "__main__":
    add()
