#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if (not isinstance(a_dictionary, dict)):
        return

    a_dictionary[key] = value
    return a_dictionary


if __name__ == "__main__":
    update_dictionary({}, 'key', 'value')
