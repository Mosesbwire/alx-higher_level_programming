#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if (not isinstance(a_dictionary, dict)):
        return
    sorted_list = sorted(list(a_dictionary))

    for key in sorted_list:
        print("{:s}: {}".format(key, a_dictionary[key]))


if __name__ == "__main__":
    print_sorted_dictioanry({})
