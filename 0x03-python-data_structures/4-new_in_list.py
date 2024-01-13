#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    modified_list = my_list.copy()

    for i in range(len(modified_list)):
        modified_list[idx] = element

    return modified_list
