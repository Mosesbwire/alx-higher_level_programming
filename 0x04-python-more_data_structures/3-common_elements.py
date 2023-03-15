#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_list = set_1 & set_2
    return list(common_list)


if __name__ == "__main__":
    common_elements(set(), set())
