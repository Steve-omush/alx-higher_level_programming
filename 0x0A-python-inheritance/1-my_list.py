#!/usr/bin/python3

"""Define class MyliST."""


class MyList(list):
    """Inherits from list class."""
    def __init__(self):
        """Instantiate the class."""
        super().__init__()

    def print_sorted(self):
        """Print the sorted list."""
        print(sorted(self))
