#!/usr/bin/python3
"""
Module 100-singly_linked_list can be used to create a singly linked list
"""


class Node:
    """Represents node of a linked list. Holds the data of the list"""

    def __init__(self, data, next_node=None):
        """ initializes the object
        Args:
            data (int): integer
            next_node (Node): next node in the linked list
        """
        self.__data = data
        self.__next_node = next_node

        @property
        def data(self):
            """returns the data variable
            setter throws TypeError exception if argument is not int
            """
            return self.__data

        @data.setter
        def data(self, value):
            if type(value) is not int:
                raise TypeError("data must be an integer")
            else:
                self.__data = value

        @property
        def next_node(self):
            """returns the next_node
            setter throws TypeError if value is not a Node
            """
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            if type(value) is not Node:
                raise TypeError("next_node must be a node object")
            else:
                self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list"""

    def __init__(self):
        """initializes the object"""
        __head = None

    def sorted_insert(self, value):
        """inserts the a node in the list
        the nodes inserted in ascending order
        """
        new_node = Node(value)
        try:
            new_node.data(value)
        except TypeError:
            raise

        if self.__head is None:
            self.__head = new_node
            return
        current_node = self.__head

        try:
            while current_node is not None:
                if current_node.data <= value:
                    new_node.next_node(current_node)
                elif value > current_node.data and current_node.next_node is not None and current_node.next_node.data >= value:
                    new_node.next_node(current_node.next_node)
                    current_node.next_node(new_node)
                else:
                    current_node.next_node(new_node)

                current_node = current_node.next_node
        except TypeError:
            raise
