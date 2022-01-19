#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """create Square instance with private size attribute"""
    def __init__(self, size=0):
        self.size = size

    """retrieve size"""
    @property
    def size(self):
        return self.__size

    """set size"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Returns the current square area"""
    def area(self):
        return self.__size ** 2
