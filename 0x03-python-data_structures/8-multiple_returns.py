#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first_char = None
    for i in sentence:
        if length == 0:
            first_char = i
        length += 1
    return_tuple = (length, first_char)
    return (return_tuple)
