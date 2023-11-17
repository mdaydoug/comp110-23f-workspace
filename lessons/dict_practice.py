"""Practice using Dictionaries."""

#  Create a new dictionary
ice_cream: dict[str, int] = {"chocolate": "12", "vanilla": "8", "strawberry": "5"}

#  Adding a key value pair
ice_cream["mint"] = 3
# print("Added mint:")

ice_cream["banana"] = 5

#  removing a key,value pair
ice_cream.pop("banana")
print("Removed banana:")

ice_cream.pop("mint")
print("Removed mint:")

print(f"There are {ice_cream['chocolate']} orders of chocolate")
# Updating a value
ice_cream["vanilla"] = 10
# ice_cream["vanilla"] += 2
print("After updating vanilla:")

# Print the length

#  Using "in" in a conditional
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint")
else:
    print("There are no orders of mint")

# Loop throguh dictionary and print out each flavor and number of orders
for flavor in ice_cream:
    # Print <flavor> has <number orders> of orders 
    print(f"{flavor} has {ice_cream[flavor]} orders.")

print(ice_cream)