#!/usr/bin/python3
"""
This module contains one function: add_integer(a, b)
The module was created as a Holberton School project on Python
add_integer(a, b): Return a + b
"""


def add_integer(a, b):
    """
    Return int(a) + int(b)
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
