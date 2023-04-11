#!/usr/bin/python3
"""
Extends the list class

"""


class MyList(list):
    """ extends the list class

    """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
