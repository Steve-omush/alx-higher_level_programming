#!/usr/bin/python3

"""Define Class Square."""


class Square:
    """Square class with private attribute and three methods."""
    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): size of square.
        """
        self.size = size

    @property
    def size(self):
        """Get method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size.

        Args:
            value (int): va;ue for size attribute.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns area of square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
