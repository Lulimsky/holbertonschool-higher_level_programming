#!/usr/bin/python3
"""Define a class Square"""


class Square:

    def __init__(self, size=0):
        """Instantiation size attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square"""
        return self.__size ** 2
