#!/usr/bin/python3
"""Class representing a square"""

class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """initiating the object"""
        self.__size = size
        """Initialize the square with a given size"""
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
        """returns the area of square"""
        return (self.__size * self.__size)
