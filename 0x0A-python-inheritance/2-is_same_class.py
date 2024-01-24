#!/usr/bin/python3

"""Define method that returns true if type."""


def is_same_class(obj, a_class):
    """Returns true is object

    Args:
        obj (int, float): object to get the type.
        a_class (int, float): the desired class.
    """
    return type(obj) is a_class
