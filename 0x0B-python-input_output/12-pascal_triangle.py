#!/usr/bin/python3
"""
Module for pascal_triangle method.
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """
    rows = [[1 for x in range(y + 1)] for y in range(n)]
    for n in range(n):
        for y in range(n - 1):
            rows[n][y + 1] = sum(rows[n - 1][y:y + 2])
    return rows
