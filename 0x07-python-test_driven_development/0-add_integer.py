#!/usr/bin/python3
"""
    Add two numbers, int or float
"""

def add_integer(a, b=98):
    """ takes two parameters,
        return sum
    """

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")

    return a + b
