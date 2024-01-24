#!/usr/bin/python3

"""Defines a function that returns True."""


def inherits_from(obj, a_class):
    """Object is an instance of a class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
