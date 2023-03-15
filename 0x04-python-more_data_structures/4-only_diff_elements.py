#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff_list = set_1 ^ set_2
    return list(diff_list)


if __name__ == "__main__":
    only_diff_elements(set(), set())
