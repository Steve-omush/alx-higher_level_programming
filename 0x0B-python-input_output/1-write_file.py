#!/usr/bin/python3
"""Defines a function that writes."""


def write_file(filename="", text=""):
    """Function that writes to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = file.write(text)
        return nb_characters
