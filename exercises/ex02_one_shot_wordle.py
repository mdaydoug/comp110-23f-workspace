"""EX02 - One-Shot-Wordle - Loops!"""

__author__ = "730660951"

secret_word: str = ("python")
guess_word: str = input(f"What is your {len(secret_word)}-letter guess? ")
num_of_guesses: int = 0
max_guesses: int = 1

while (guess_word != secret_word) and (num_of_guesses < max_guesses):
    # Ensure guess is the same length as the secret word
    if len(guess_word) != len(secret_word):
        guess_word = str(input(f"That was not {len(secret_word)} letters! Try again: "))
    # Need a way to quit after one wrong guess with the correct length as the secret word
    if len(guess_word) == len(secret_word):
        num_of_guesses += 1

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

idx: int = 0
emoji: str = ""

# Establish boolean variable to keep track of guessed character
# Keep track of alternate indices of the secret with counter
character: bool = False
alt_idx: int = 0

while idx < len(secret_word):
    # When the indicies of guess and secret match, concatenate green emoji to string
    if guess_word[idx] == secret_word[idx]:
        emoji += GREEN_BOX
    else:
        # Test for any characters in the secret word that are in the incorrect index
        while (not character and alt_idx < len(secret_word)):
            if secret_word[alt_idx] == guess_word[idx]:
                character = True
            else:
                alt_idx += 1
        # A True bool tells us there are present characters of the secret word in the wrong index
        if (character):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    # Reset bool and alternate index to be ran through the while loop again
    character = False
    alt_idx = 0
    idx += 1
print(emoji)

if guess_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon! ")
