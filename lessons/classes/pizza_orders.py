"""Instantiating A Class."""

"""
This is where we instantiate the class we defined in classes.py.
In other words, we're creating objects that belong to that class.
"""

# Import the class
# from <file_name>.<module_name>.<class_name> import <class_name>
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) # Constructor

# # access/set/update attribute values
# # my_pizza.size = "large"
# my_pizza.size = "large" # can be defined in argument with init
# my_pizza.toppings = 10
# my_pizza.gluten_free = True
my_pizza.toppings += 2 # can be used to update values

print("Size: ")
print(my_pizza.size)
print(my_pizza.toppings)

# print("my_pizza:")
# print(my_pizza) # address or location in memory where we store it (doesn't make sense)
# print(Pizza) # says that pizza is in the classes lessons folder in file called pizza

# Make Sals_pizza size medium, 5 toppings, NOT GF
sals_pizza: Pizza = Pizza("medium", 5, False)

def price(input_pizza: Pizza) -> float:
    """Compute the price of a pizza."""
    if input_pizza == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += 0.75 * input_pizza.toppings
    if input_pizza.gluten_free:
        cost += 1.00
    return cost

# Calling function
print(price(my_pizza))
print(price(sals_pizza))

# Calling method (whatever comes before period is self)
print(my_pizza.price())
print(sals_pizza.price())

"""
Usually make function a method and define prices within method.
It is made to specifically work on pizza object.
"""

my_pizza.add_toppings(3)
print(my_pizza.toppings)
print(my_pizza.price())

my_second_pizza: Pizza = my_pizza.add_toppings_new_order(2)
print(my_second_pizza.toppings)
print(my_pizza.toppings)