#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Square instance with private size attribute"""
    def __init__(self, size):
        self.size = size

    """Retrive size"""
    @property
    def size(self):
        return (self.__size)

    """Set size"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
