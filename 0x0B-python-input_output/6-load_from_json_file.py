#!/usr/bin/python3
"""
Module 6-load_from_json_file

"""

import json


def load_from_json_file(filename):
    with open(filename, encoding="utf-8") as f:
        json.load(f)
