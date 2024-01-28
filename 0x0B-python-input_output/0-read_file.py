#!/usr/bin/python3
"""Defines a function that opens a file."""


def read_file(filename=""):
    """The function isused to open and read a file."""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
