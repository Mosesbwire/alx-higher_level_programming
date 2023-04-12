#!/usr/bin/python3
read_file = __import__('0-read_file').read_file
write_file = __import__('1-write_file').write_file

"""task 0"""
read_file("README.md")

""" task 1 """
nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
