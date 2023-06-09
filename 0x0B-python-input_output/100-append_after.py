#!/usr/bin/python3
"""
Module for append_after method.
"""


def append_after(filename="", search_string="", new_string=""):
    '''Method for inserting text after search string.'''
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
        x = 0
        while x < len(lines):
            if search_string in lines[x]:
                lines[x:x + 1] = [lines[x], new_string]
                x += 1
            x += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
