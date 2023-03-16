#!/usr/bin/python3

def best_score(a_dictionary):
    key = ""
    val = 0

    if (not isinstance(a_dictionary, dict)):
        return
    if (len(list(a_dictionary)) == 0):
        return

    for k, v in a_dictionary.items():
        if (val < v):
            val = v
            key = k
        elif (val == v):
            key = None
    return key
