#!/usr/bin/python3

"""Define a class"""


class BaseGeometry:
    """This is a class with 2 methods"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate name and value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class for rectangle"""
    def __init__(self, width, height):
        """Instantiate Rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Print the result"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """Calculate the area"""
        return self.__height * self.__width


class Square(Rectangle):
    """Square Class"""
    def __init__(self, size):
        """innit method for square class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
