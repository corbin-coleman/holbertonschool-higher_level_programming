#!/usr/bin/python3
def remove_char_at(str, n):
    pos = 0
    newstr = ""
    for i in str:
        if pos == n:
            pos += 1
            continue
        newstr += i
        pos += 1
    return (newstr)
