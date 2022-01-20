#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square attributes"""
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square"""
        self.size = size
        self.position = position

    def area(self):
        """square's area calcutations"""
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(["#" for l in range(self.__size)]))

    @property
    def position(self):
        """position of the square"""
        return self.__position

#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a size of the square
        __position (tuple): position of the square in 2D space
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes the square
        Args:
            size (int): size of a side of the square
            position (tuple): positoin of the square in 2D space
        Returns:
            None
        """
        self.size = size
        self.position = position

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square


    @position.setter
    def position(self, value):
        ''' method that sets the position of the square
        '''
        if isinstance(value, tuple) is False or len(value) != 2 or \
           type(value[0]) != int or type(value[1]) != int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        ''' method that returns area of the square
        '''
        return self.__size * self.__size

    def __str__(self):
        ''' printable representation of square
        '''
        toprint = ''
        if self.__size == 0:
            return toprint
        for a in range((self.__position)[1]):
            toprint = toprint + '\n'
        for i in range(self.__size):
            for b in range((self.__position)[0]):
                toprint = toprint + ' '
            for j in range(self.size):
                toprint = toprint + '#'
            toprint = toprint + '\n'
        return toprint[:-1]

    def my_print(self):
        ''' method that prints the square
        '''
        print (self)
