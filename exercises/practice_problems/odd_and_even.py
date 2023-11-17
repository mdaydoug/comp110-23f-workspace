"""Practice Writing Functions for QZ02."""

def odd_and_even(x: list[int]) -> list[int]:
    """Returns list of odd elements with an even index."""
    i: int = 0
    y: list[int] = []

    while i < len(x):
        if x[i] % 2 == 1 and i % 2 == 0:
            y.append(x[i])
        i += 1
    return y