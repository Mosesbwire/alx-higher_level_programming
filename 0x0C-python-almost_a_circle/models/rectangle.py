#!/usr/python3
"""
Explain module here

"""

from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """
        if id is not None:
            super().__init__(id)
        else:
            super().__init__()

        self.__width = None
        self.__height = None
        self.__x = None
        self.__y = None

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")

        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Calculates the area of a rectangle
        Returns:
            an int - area of rectangle
        Example usage:
            >>> rect = Rectangle(10, 20, 1, 5)
            >>> rect.area()
            200
        """
        return self.width * self.height

    def display(self):
        """ Display rectangle as a series of #
        Example usage:
            >>> rect = Rectangle(3, 3)
            >>> rect.display()
            ###
            ###
            ###
        """
        print("\n" * self.y +
              "\n".join(" " * self.x + "#" * self.width
                        for i in range(self.height)))

    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}"\
            .format(self.__class__.__name__, self.id, self.x, self.y,
                    self.width, self.height)

    def update(self, *args, **kwargs):
        """ updates the attributes of the rectangle """
        if not args:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    raise AttributeError("{} is not an instance variable"
                                         .format(key))
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            return

    def to_dictionary(self):
        """ returns a dictionary of the objects attributes """
        attr_dict = {'id': self.id, 'width': self.width,
                     'height': self.height, 'x': self.x, 'y': self.y}

        return attr_dict
