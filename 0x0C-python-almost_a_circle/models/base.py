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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        json_string = "[]"

        if list_objs is not None:
            json_string = cls.to_json_string([obj.to_dictionary()
                                             for obj in list_objs])

        with open(filename, 'w') as file:
            file.write(json_string)
