#!/usr/bin/python3
"""Defines a function."""


def append_write(filename="", text=""):
    """Appends at the end of a file."""
    with open(filename, 'a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
        return nb_characters_added
