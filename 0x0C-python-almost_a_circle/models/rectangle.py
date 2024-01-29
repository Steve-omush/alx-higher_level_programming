#!/usr/bin/python3
"""Defines Class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Getters methods for Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.validate_value("width", value)
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.validate_value("height", value)
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x atrribute."""
        self.validate_value("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for x attribute."""
        self.validate_value("y", value)
        self.__y = value

    def validate_value(self, attr_name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr_name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(attr_name))
