#!/usr/bin/python3
"""
<<<<<<< HEAD
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
=======
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
>>>>>>> db5bea9c8b8e30f61e5621714b0bff9e787118ef
