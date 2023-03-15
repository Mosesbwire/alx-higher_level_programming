#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []

    if (not isinstance(my_list, list) or len(my_list) == 0):
        return

    for x, y in enumerate(my_list):
        if (y != search):
            new_list.append(y)
        else:
            new_list.append(replace)
    return new_list


if __name__ == "__main__":
    search_replace([], 0, 0)
