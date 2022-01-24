#!/usr/bin/python3
"""
add_integer module
return: a + b
"""


def add_integer(a, b=98):

    if isinstance(a, float):
        a = int(a)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return int(a + b)
