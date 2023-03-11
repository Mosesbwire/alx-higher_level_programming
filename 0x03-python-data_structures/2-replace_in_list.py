#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if (idx < 0 or idx >= length):
        return my_list
    my_list[idx] = element
    return my_list


if __name__ == "__main__":
    replace_in_list([], 0, 0)
