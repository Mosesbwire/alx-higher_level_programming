#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    if (length == 0):
        t = (0, None)
        return t
    t = (length, sentence[0])
    return t


if __name__ == "__main__":
    multiple_returns("word")
