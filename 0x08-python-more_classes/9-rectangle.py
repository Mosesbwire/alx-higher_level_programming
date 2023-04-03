#!/usr/bin/python3

"""Used to create a rectangle"""


class Rectangle:
    """Represents a rectangle
    Args:
        width (int): width of a rectangle
        height (int): height of a rectangle
        number_of_instances (int): keeps count of objects created
        print_symbol (string): used to print the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

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
            Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Determines which rect has a larger area
        Args:
            rect_1 (Rectangle): instance of Rectangle
            rect_2 (Rectangle): instance of Rectangle
        Returns:
            rect_1 if area of rect_1 == area of rect_2
            rect with bigger area
        """

        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (rect_1.area() == rect_2.area()):
            return rect_1

        if (rect_1.area() > rect_2.area()):
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

    def __str__(self):
        new_str = ""
        if self.width == 0 or self.height == 0:
            return " "

        for x in range(self.height):
            for y in range(self.width):
                new_str = new_str + Rectangle.print_symbol
            new_str = new_str + '\n'
        return new_str.rstrip()

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        else:
            Rectangle.number_of_instances = 0
