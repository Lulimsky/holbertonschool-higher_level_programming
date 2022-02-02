#!/usr/bin/python3
"""Defines an object attribute lookup function."""
def lookup(obj):
    """Return attributes available in object
    Args:
        obj: object to search
    """

    return dir(obj)
