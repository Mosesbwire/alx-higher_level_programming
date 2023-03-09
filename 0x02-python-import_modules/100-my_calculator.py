#!/usr/bin/python3
import calculator_1 as calc
import sys


def calculate():
    args = sys.argv
    exit_val = 0
    if (len(args) != 4):
        exit_val = 1
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    else:
        a = int(args[1])
        b = int(args[3])
        operator = args[2]

        if (operator == "+"):
            print(f"{a} {operator} {b} = {calc.add(a, b)}")

        elif (operator == "*"):
            print(f"{a} {operator} {b} = {calc.mul(a, b)}")

        elif (operator == "-"):
            print(f"{a} {operator} {b} = {calc.sub(a, b)}")

        elif (operator == "/"):
            print(f"{a} {operator} {b} = {calc.div(a, b)}")

        else:
            exit_val = 1
            print("Unknown operator. Available operators: +, -, * and /")
    return exit_val


if __name__ == "__main__":
    exit = calculate()
    sys.exit(exit)
