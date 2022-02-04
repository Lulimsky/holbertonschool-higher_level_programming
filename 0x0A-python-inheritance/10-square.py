#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle subclass which inherits
       from BaseGeometry class"""
    def __init__(self, size):
         """Instantiation function for size attribute
        Args:
            size (int): the size of the square
        """
        self.__size = self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)
