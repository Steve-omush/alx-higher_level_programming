#!/usr/bin/python3
"""Defines a function."""
import json


def load_from_json_file(filename):
    """creates an object from json file. use loads."""
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
