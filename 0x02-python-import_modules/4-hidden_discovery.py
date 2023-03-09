#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    hidden_list = dir(hidden_4)
    for i in range(len(hidden_list)):
        if (hidden_list[i][0] != "_"):
            print(f"{hidden_list[i]}")
