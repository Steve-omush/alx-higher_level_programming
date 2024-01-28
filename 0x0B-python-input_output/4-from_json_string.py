#!/usr/bin/python3
"""Function load."""
import json


def from_json_string(my_str):
    """Loads a string to Python."""
    return json.loads(my_str)
