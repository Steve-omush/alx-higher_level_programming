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

    @staticmethod
    def from_json_string(json_string):
        """Converts String to Dictionaries."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Runs instances when created."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
       """The method loads to file."""
       filename = cls.__name__ + ".json"
       try:
           with open(filename, "r") as file:
               json_data = file.read()
               dictionaries = cls.from_json_string(json_data)
               instances = [cls.create(**d) for d in dictionaries]
               return instances
       except FileNotFoundError:
           return []
