#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    control = 1
    try:
        control + value
        print("{:d}".format(value))
        return True
    except TypeError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
