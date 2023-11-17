"""File to define Bear class."""


class Bear:
    """Defines my Bear Class."""
    
    age: int
    hunger_score: int

    def __init__(self):
        """Constructor."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Monitors age and hungerscore of bears as time passes."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Updates Bear hungerscore."""
        self.hunger_score += num_fish
        return None