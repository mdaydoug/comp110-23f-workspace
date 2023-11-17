"""Combining two lists into a dictionary."""

__author__ = "730660951"


def zip(x: list[str], y: list[int]) -> dict[str, int]:
    """Combines the lists using a while loop."""
    temp: dict[str, int] = {}
    if len(x) != len(y):
        return temp
    i: int = 0
    while len(x) > i:
        temp[x[i]] = y[i]
        i += 1
    return temp