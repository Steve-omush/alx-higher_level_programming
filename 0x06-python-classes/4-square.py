#!/usr/bin/python3

"""Define Class Square."""


class Square:
    """Square class with private ttribute, getter, setter, area method."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
        size (int): Size of square.
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size.

        Args:
            value (int): The new value for the size attribute

        Raises:
            TypeError: If the value is not an integr.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
