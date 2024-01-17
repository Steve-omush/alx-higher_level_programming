#!/usr/bin/python3

"""Define Class Square."""


class Square:
    """Square class with private size attribute and area method."""
    def __init__(self, size=0):
        """Initialize a new Square class instance.

        Args:
            size (int): size of square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns area of square."""
        return self.__size ** 2
