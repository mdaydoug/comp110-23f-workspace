"""Practice Writing Functions (in-class) 9/26/23."""

# Write a miimic function: input a string and return same string back to you


def mimic(my_words: str) -> str:
    """Given the string my_words, output the same string."""
    return my_words


# Calling it:
mimic("Hello")
print(mimic("Hello"))


my_words: str = "Hello"
response: str = mimic(my_words)

# Print displays value in terminal
# Return outputs within the program


def mimic_letter(my_word: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx."""
    if letter_idx >= len(my_word):
        return "Index too high"
    # If we made it here, that means the letter_idx is valid
    return my_word[letter_idx]


xs: str = "123"
ys: str = "45"

x_idx: int = 0 
while x_idx < len(xs):
    y_idx: int = 0
    while y_idx < len(ys):
        print(f"({xs[x_idx]}, {ys[y_idx]})")
        y_idx += 1
    x_idx += 1