"""Summing the elements of a list using different groups!"""
__author__ = "730660951"


def w_sum(vals: list[float]) -> float:
    """Returns sum of all of the elements of list using while loop."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum 


def f_sum(vals: list[float]) -> float:
    """Returns sum of all elements of list using a for loop."""
    sum: float = 0.0
    for elem in vals:
        sum += elem 
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Returns sum of all elements of list using a for range loop."""
    sum: float = 0.0
    for elem in range(0, len(vals)):
        sum += vals[elem]
    return sum
