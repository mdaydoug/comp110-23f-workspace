"""Things I'll be importing."""


def addition(x: int, y: int):
    """Make function that returns the sum of values."""
    return x + y


my_variable: str = "Hello!"

if __name__ == "__main__":
    print("This should only print when running my_functions")
else:
    print("my_functions is being imported")


def f(x: int) -> int:
    """Return x and demonstrates importance of order in function definition."""
    return x
    x *= 2
    print(x)


y: int = f(3)