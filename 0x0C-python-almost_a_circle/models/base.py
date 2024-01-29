#!/usr/bin/python3
"""Defines base class model."""
import json


class Base:
    """Base Class Model.

    base class for all tasks in the project.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes new Base Class.

        Args:
            id (int): Identity of new Base class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
