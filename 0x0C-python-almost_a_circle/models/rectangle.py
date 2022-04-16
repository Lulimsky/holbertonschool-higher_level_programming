#!/usr/bin/python3
"""This module is from the class Rectangle """

from models.base import Base


class Rectangle(Base):
    """ Rectangle declaretion"""
    def __init__(self, width, height, x=0, y=0, id=None):

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
