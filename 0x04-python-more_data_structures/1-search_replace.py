#!/usr/bin/python3

def swap(initial_num, replace, search):

    if (initial_num == search):
        return replace
    return initial_num


def search_replace(my_list, search, replace):

    if (not isinstance(my_list, list)):
        return
    if (len(my_list) == 0):
        return my_list

    new_list = map(
        swap,
        my_list,
        [replace] *
        len(my_list),
        [search] *
        len(my_list))

    return list(new_list)


if __name__ == "__main__":
    search_replace([], 0, 0)
    swap(0, 0)
