#!/usr/bin/python3

"""Defines class BaseGeometry."""


class BaseGeometry:
    """Class has 2 methods."""
    def area(self):
        """Raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this method validates value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
