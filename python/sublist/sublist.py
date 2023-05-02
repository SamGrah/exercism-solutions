"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'is a sublist'
SUPERLIST = 'is a superlist' 
EQUAL = 'is equal' 
UNEQUAL = 'is unequal' 


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_sublist(list_two, list_one):
        return SUPERLIST
    
    return UNEQUAL


def is_sublist(first: list, second: list) -> bool:
    first_len = len(first)
    second_len = len(second)
    
    for second_idx in range(second_len):
        sublist_begin = second_idx
        sublist_end = second_idx + first_len
        sublist = second[sublist_begin:sublist_end]
       
        if (sublist_end - 1) >= second_len: # exhausted all sublists
            return False
        if first == sublist:
            return True
    return False 
