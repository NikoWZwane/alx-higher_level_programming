#!/usr/bin/python3
"""Class representing a square"""

class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialize the square with a given size"""
        self.__size = size  # Use the property setter

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
        """prints hash tag"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
