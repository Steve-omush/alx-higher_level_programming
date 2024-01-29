#!/usr/bin/python3
"""Defines Class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Creates an instance of Square Class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size(width and height)."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square's attributes."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """Return the dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
