#!/usr/bin/python3
"""Defines base class model."""


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
