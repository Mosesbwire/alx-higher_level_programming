#!/usr/bin/python3
"""
Square module
Represents a square

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor """
        if id is not None:
            super().__init__(size, size, x, y, id)
        else:
            super().__init__(size, size, x, y)

    def __str__(self):
        """ called when print/ str is used on the object """
        return "[{}] ({}) {}/{} - {}"\
            .format(self.__class__.__name__, self.id, self.x, self.y,
                    self.width)

    @property
    def size(self):
        """ getter method for size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates the attributes of the instance """
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
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            return

    def to_dictionary(self):
        """ returns a dictionary of the objects attributes """
        attr_dict = super().to_dictionary()
        attr_dict.pop('width', None)
        attr_dict.pop('height', None)
        attr_dict['size'] = self.size
        return attr_dict
