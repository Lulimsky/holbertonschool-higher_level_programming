#!/usr/bin/python3
"""This module is from the class Base """


class Base:
    """Class descrption """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
