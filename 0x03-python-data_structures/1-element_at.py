#!/usr/bin/python3

def element_at(my_list, idx):
    length = len(my_list)
    if (length == 0):
        return None

    if (idx < 0 or idx >= length):
        return None
    return my_list[idx]


if __name__ == "__main__":
    element_at([], 0)
