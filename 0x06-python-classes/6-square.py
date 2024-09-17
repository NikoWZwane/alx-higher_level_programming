#!/usr/bin/python3
"""Class representing a square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a given size and position"""
        self.size = size
        self.position = position

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if (not isinstance(value, tuple) or len(value) != 2 or 
                not all(isinstance(num, int) for num in value) or 
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with hash tags"""
        if self.__size == 0:
            print()
            return
        [print() for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for item in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()
