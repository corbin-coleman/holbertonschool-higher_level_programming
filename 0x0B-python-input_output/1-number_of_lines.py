#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, 'r', encoding='utf-8') as my_file:
        line_count = 0
        for lines in my_file:
            line_count += 1
    return (line_count)
