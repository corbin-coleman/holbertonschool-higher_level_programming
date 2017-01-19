#!/usr/bin/python3
"""
This is the Name module

This module contains a simple function to print out a first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Return nothing
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    try:
        print("My name is {} {}".format(first_name, last_name))
    except Exception as e:
        print(e)
