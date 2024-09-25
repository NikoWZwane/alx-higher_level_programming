#!/usr/bin/python3
"""class Rectangle"""
class Rectangle:
    """A class to represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes the Rectangle with width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """instance method that returns the rectangle area"""
        area = self.width * self.height
        return area
    
    def perimeter(self):
        """Public instance method that returns the rectangle perimeter"""
        rect_perimeter = 2 * (self.width + self.height)
        return rect_perimeter
    
    def __str__(self):
        """Returns a string representation of rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width for _ in range(self.height)]) 
