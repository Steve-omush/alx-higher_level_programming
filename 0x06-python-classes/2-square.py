#!/usr/bin/python3

"""Define Class Square."""


class Square:
    """Square class with a private size attribute."""

    def __init__(self, size=0):
        """Initializes a new Square Instance.

        Args:
            size (int): Size of square. Default is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
