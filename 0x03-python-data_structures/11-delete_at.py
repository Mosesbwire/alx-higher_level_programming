#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    length = len(my_list)

    if (length == 0 or idx < 0 or idx >= length):
        return my_list

    del my_list[idx]
    return my_list


if __name__ == "__main__":
    delete_at()
