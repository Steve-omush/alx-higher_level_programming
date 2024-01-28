#!/usr/bin/python3
"""Function that serializes."""
import json


def save_to_json_file(my_obj, filename):
    """Uses dump function to write."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
