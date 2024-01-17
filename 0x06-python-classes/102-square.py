#!/usr/bin/python3

class Square:
    """Square class with private size attribute and method"""
    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (number, optional): The size of the square. Defaults to 0.
        """
        self.size = size  # Using the setter to perform validation

    @property
    def size(self):
        """Getter method to retrieve the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size.

        Args:
            value (number): The new value for the size attribute.

        Raises:
            TypeError: If the value is not a number.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparator based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparator based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparator based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparator based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparator based on area."""
        return self.area() >= other.area()
