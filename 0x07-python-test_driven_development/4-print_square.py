#!/usr/bin/python3

"""Define a function that prints square."""


def print_square(size):
    """Function that prints square.

    Args:
        size (int): size or number of the suares.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
