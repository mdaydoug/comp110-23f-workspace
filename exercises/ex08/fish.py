"""File to define Fish class."""


class Fish:
    """Defines my Fish class."""

    age: int

    def __init__(self):
        """Constructor."""
        self.age = 0
        return None
    
    def one_day(self):
        """Monitors age and hungerscore of fish as time passes."""
        self.age += 1
        return None