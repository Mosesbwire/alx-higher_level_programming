#!/usr/bin/python3

from calculator_1 import div, mul, sub, add
a = 10
b = 5


def calculations():
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:.0f}".format(a, b, div(a, b)))


if __name__ == "__main__":
    calculations()
