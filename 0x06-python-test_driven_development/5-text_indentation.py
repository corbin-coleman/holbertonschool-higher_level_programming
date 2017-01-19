#!/usr/bin/python3

"""
The ``Indentation`` module

This module contains a function to print two new lines after thes characters:
'?', '.', ':'
There should be no extra whitespace at the beginning or the end of the line
"""


def text_indentation(text):
    """
    Print out the given text before a '?', '.', or ':' character followed
    by two new lines
    """
    if not text or not isinstance(text, str) or len(text) < 0:
        raise TypeError("text must be a string")
    new = "".join([let if let not in "?.:" else let + "\n\n" for let in text])
    print ("\n".join([words.strip() for words in new.split("\n")]), end="")
