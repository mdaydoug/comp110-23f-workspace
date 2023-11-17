"""EX04 List Utils!"""
__author__ = "730660951"


def all(list_ints: list[int], given: int) -> bool:
    """Returns True if all ints in list are the same as given!"""
    idx: int = 0
    matches: bool = False
    while len(list_ints) > idx:
        if list_ints[idx] == given:
            matches = True
        else:
            return False
        idx += 1
    return matches
    

def max(input: list[int]) -> int:
    """Returns largest int from a list of ints!"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    # Is my_max a global?
    my_max: int = input[0]
    while len(input) > idx:
        current_max: int = input[idx]
        if (current_max > my_max):
            my_max = current_max
        idx += 1
    return my_max


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Return true if every element at every index is equal!"""
    if len(list_1) != len(list_2):
        return False
    idx: int = 0
    while len(list_1) > idx:
        if list_1[idx] != list_2[idx]:
            return False
        idx += 1
    return True
