#!/usr/bin/python3

"""Define class Square."""


class Square:
    """Class with private size attribute."""
    def __init__(self, size):
        """Initializes a new sqaure instiannce.

        Args:
            size (int): Size of square.
        """
        self.__size = size
