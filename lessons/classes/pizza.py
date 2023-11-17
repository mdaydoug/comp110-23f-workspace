"""Defining a Class!"""
from __future__ import annotations
"""
This line of code imports the types (classes) created later in the future of the file
This allows us to make our return type a Pizza later down in the file within our Pizza class definition.
"""


"""
Think of a class definition as a "roadmap" for objects that belong to the class.
You are defining the underlying structure every instance of this class will have.
"""


class Pizza:
    """This is my class to represent pizza."""

    # attributes
    # syntax <name> : <type>
    size: str
    toppings: int
    gluten_free: bool


    def __init__(self, size_input: str, toppings_input: int, gf_input: bool) -> None:
        """Constructor."""
        self.size = size_input
        self.toppings = toppings_input
        self.gluten_free = gf_input
        # returns self for you (don't need to specify return type)


    def price(self) -> float:
        """Defining Price function within class Pizza, only object is self."""
        if self == "large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += 0.75 * self.toppings
        if self.gluten_free:
            cost += 1.00
        return cost
    
    def add_toppings(self, num_toppings: int) -> int:
        """Update existing pizza order with num_toppings."""
        self.toppings += num_toppings

    # Create a new order and add new toppings to it


    def add_toppings_new_order(self, num_toppings: int) -> Pizza:
        """Make new pizza order using existing info."""
        new_pizza: Pizza = Pizza(self.size, self.toppings + num_toppings, self.gluten_free)
        return new_pizza
    
    def __str__(self) -> str:
        """The result when I call str()"""
        pizza_info: str = f"Pizza order: {self.toppings} toppings, size {self.size}, GF: {self.gluten_free}"
        return pizza_info

my_pizza: Pizza = Pizza("medium", 3, False)
print(str(my_pizza))
sals_pizza: Pizza = Pizza("large", 1, True)
print(str(sals_pizza))