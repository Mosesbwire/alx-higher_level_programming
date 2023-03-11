#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = []
    length = len(my_list)

    if (idx < 0 or idx >= length):
        return my_list

    for i in range(length):
        new_list.append(my_list[i])

    new_list[idx] = element
    return new_list


if __name__ == "__main__":
    new_in_list([], 0, 0)
