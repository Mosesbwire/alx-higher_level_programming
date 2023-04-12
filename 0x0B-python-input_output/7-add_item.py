#!/usr/bin/python3
"""
Module 7-add_item

This script reads data from file adds new data to file

"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    items_in_list = load_from_json_file(filename)
except FileNotFoundError:
    items_in_list = []


save_to_json_file(items_in_list + sys.argv[1:], filename)
