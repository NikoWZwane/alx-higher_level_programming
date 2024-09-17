#!/usr/bin/python3
"""Module that defines a Square class"""

class Square:
    """Class that defines a square by its size"""
    
    def __init__(self, size=0):
        """
        Initialize the square with a given size.
        
        Args:
            size (int): The size of one side of the square. Default is 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """area of square 
        Returns:
            the size of square
        """
        return self.__size ** 2
