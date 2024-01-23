#!/usr/bin/python3

"""Define a function that prints lines."""


def text_indentation(text):
    """Prnts a text into string.

    Args:
        text (str): input string into text.

    Raises:
        TypeError: when input text is not string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuation_chars:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line.strip():
        print(current_line.strip(), end='')
