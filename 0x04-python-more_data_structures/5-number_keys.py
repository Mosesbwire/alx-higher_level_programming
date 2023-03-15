#!/usr/bin/python3

def number_keys(a_dictionary):
    if (not isinstance(a_dictionary, dict)):
        return
    return len(list(a_dictionary))


if __name__ == "__main__":
    number_keys({})
