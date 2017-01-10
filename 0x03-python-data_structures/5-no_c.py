#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    a = 0
    for char in my_string:
        if char == 'c' or char == 'C':
            a += 1
        else:
            new_str += char
    return (new_str)
