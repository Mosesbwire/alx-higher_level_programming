#!/usr/bin/python3

def uniq_add(my_list=[]):
    if (not isinstance(my_list, list) or len(my_list) == 0):
        return
    result = 0
    for x in set(my_list):
        result += x
    return result


if __name__ == "__main__":
    uniq_add()
