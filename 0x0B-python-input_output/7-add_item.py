#!/usr/bin/python3
"""Defines a function."""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item_to_list(item_list, args):
    """add items to as arguments."""
    item_list.extend(args)


def main():
    filename = "add_item.json"

    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    add_item_to_list(items, sys.argv[1:])
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
