#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rect = Rectangle(5, 5)

print(my_rect.number_of_instances)
del my_rect
print(Rectangle.number_of_instances)
