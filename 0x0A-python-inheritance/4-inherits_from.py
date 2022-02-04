#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Determine whether obj is an instances of a subclass of a_class
    Args:
        obj: instance to check
        a_class: class to check
    Returns:
        True if obj is instance of subclass of a_class, else False
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
