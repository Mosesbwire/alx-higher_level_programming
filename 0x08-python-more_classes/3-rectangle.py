#!/usr/bin/python3

"""Used to create a rectangle"""


class Rectangle:
    """Represents a rectangle
    Args:
        width (int): width of a rectangle
        height (int): height of a rectangle
    """

    def __init__(self, width=0, height=0):

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__width = width
            self.__height = height

    @property
    def width(self):
        """gets the value of width
        Returns: width of rectangle
        setter throws ValueError if value is less than 0
        setter throws TypeError if value is not int
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the value of height
        Returns: height of rectangle
        setter throws ValueError if value is less than 0
        setter throws TypeError if value is not int
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculates area of a rectangle
        Returns: Area
        """
        return self.width * self.height

    def perimeter(self):
        """calculates perimeter of a rectangle
        Returns: perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        new_str = ""
        if self.width == 0 or self.height == 0:
            return " "

        for x in range(self.height):
            for y in range(self.width):
                new_str = new_str + "#"
            new_str = new_str + '\n'
        return new_str.rstrip()
