#!/usr/bin/python3

lookup = __import__('0-lookup').lookup

class ClassA(object):
    pass

class MyClass(object):
    my_attr = 3
    def my_meth(self):
        pass


print(lookup(MyClass))
