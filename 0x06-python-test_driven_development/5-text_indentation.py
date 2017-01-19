#!/usr/bin/python3

"""
The ``Indentation`` module

This module contains a function to print two new lines after thes characters:
'?', '.', ':'
There should be no extra whitespace at the beginning or the end of the line
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    for let in text:
        i = 0
        new_text += let
        string_to_print = ""
        if let in ['?', '.', ':']:
            while new_text[i] == ' ':
                i += 1
            while i != len(new_text):
                string_to_print += new_text[i]
                if new_text[i] in ['?', '.', ':']:
                    break
                i += 1
            print("{:s}\n".format(string_to_print))
            new_text = ""
