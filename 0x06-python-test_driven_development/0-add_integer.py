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
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
