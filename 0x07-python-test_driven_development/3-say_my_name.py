#!/usr/bin/python3
"""
prints to text output to stdout

"""


def say_my_name(first_name, last_name):
    """ prints string with args first_name and last_name
        Args:
            first_name (string): string representation of a name
            last_name (string): string representation of a name
        Raises:
            TypeError: if first_name or last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    say_my_name("Moses", "Bwire")
