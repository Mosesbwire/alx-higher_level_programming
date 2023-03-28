#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    div_list = []

    try:
        for i in range(list_length):
            a = my_list_1[i]
            b = my_list_2[i]
            try:
                res = a / b
                div_list.append(res)
            except ZeroDivisionError:
                print("division by 0")
                div_list.append(0)
            except TypeError:
                print("wrong type")
                div_list.append(0)
    except IndexError:
        if (len(my_list_1) == 0 or len(my_list_2) == 0):
            for i in range(list_length):
                print("out of range")
                div_list.append(0)
        else:
            print("out of range")
            div_list.append(0)
    finally:
        return div_list
