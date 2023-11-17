"""File to define River class."""
__author__ = "730660951"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """This is my class to define my River."""
    
    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        for x in range(num_bears):
            self.bears.append(Bear())
        for x in range(num_fish):
            self.fish.append(Fish())
        return None

    def bears_eating(self):
        """Bears eating increases hunger score and removes fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """If hunger_score < 0, remove Bear from river."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears
        return None

    def check_ages(self):
        """If the Bears or fish are too old, they should be removed."""
        new_fish: list[Fish] = []
        new_bears: list[Bear] = []
        for x in self.fish:
            if x.age <= 3:
                new_fish.append(x)
        self.fish = new_fish
        for y in self.bears:
            if y.age <= 5:
                new_bears.append(y)
        self.bears = new_bears
        return None
    
    def remove_fish(self, amount: int):
        """Removes amount many Fish from the River."""
        while amount > 0:
            amount -= 1
            self.fish.pop(0)
        return None

    def repopulate_fish(self):
        """Create offspring to repopulate the numb_fish in the river."""
        n = len(self.fish)
        for i in range((n // 2) * 4):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Create offspring to repopulate the num_bears in the river."""
        n = len(self.bears)
        for i in range(n // 2):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Visualizes the river."""
        view: str = f"~~~ Day {self.day}: ~~~\n"
        view += f"Fish population: {len(self.fish)}\n"
        view += f"Bear population: {len(self.bears)}"
        print(view)
        return None
    
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Call one_river_day() 7 times."""
        for x in range(0, 7):
            self.one_river_day()
        return None