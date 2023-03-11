#!/usr/bin/python3

def no_c(my_string):
    new_list = []
    for w in my_string:
        if (w != 'C' and w != 'c'):
            new_list.append(w)

    new_str = ''.join(new_list)
    return new_str


if __name__ == "__main__":
    no_c("no str")
