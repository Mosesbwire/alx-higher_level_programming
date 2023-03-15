#!/usr/bin/python3

def best_score(a_dictionary):
    key = ""
    val = 0

    if (not isinstance(a_dictionary, dict)):
        return

    for k, v in a_dictionary.items():
        if (val < v):
            val = v
            key = k
        if (val == v):
            key = None
    return key
