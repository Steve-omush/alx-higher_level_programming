#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for item in my_list:
        if item not in new_list:
            sum += item
            new_list.append(item)
    return sum
