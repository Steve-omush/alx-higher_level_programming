#!/usr/bin/python3

"""Defines a function that adds integer."""


def add_integer(a, b=98):
    """Returns the integer addition of a and b.

    Args:
        a (int or float): First number.
        b (int or float): Second number. Default to 98.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
