#!/usr/bin/python3
""""Defines a class-checking function
"""


def is_same_class(obj, a_class):
    """Checks IF object is exactly an instance of the specified class
    Returns:
        True if the object is exactly an instance of the specified clasS
        otherwise False
    """
    return True if type(obj) is a_class else False
