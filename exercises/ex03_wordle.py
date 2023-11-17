"""EX03 - Structured Wordle!"""
__author__ = "730660951"


def contains_char(search_str: str, single_char: str) -> bool:
    """Returns True if the single character is found at any index in the first string."""
    assert len(single_char) == 1
    idx: int = 0
    # test each index of the first parameter to see if its equal to the second parameter
    while idx < len(search_str):
        if search_str[idx] == single_char:
            return True
        idx += 1
    return False


def emojified(search_str: str, secret: str) -> str:
    """Given guess and secret returns string with correct emoji."""
    assert len(search_str) == len(secret)
    emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    alt_idx: int = 0
    # Create while loop
    while alt_idx < len(search_str):
        if search_str[alt_idx] == secret[alt_idx]:
            emoji += GREEN_BOX
        elif ((contains_char(secret, search_str[alt_idx])) is True):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        alt_idx += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Prompts for guess until guess is of expected length."""
    correct_chars: str = input(f"Enter a {expected_length} character word: ")
    # Ensure guess is the same length as the secret word
    while expected_length != len(correct_chars):
        correct_chars = str(input(f"That wasn't {expected_length} chars! Try again: "))
    return correct_chars


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    num_of_guesses: int = 1
    max_guesses: int = 6
    secret: str = "codes"
    won: bool = False

    while (num_of_guesses <= max_guesses) and (won != True):
        # print current turn number
        print(f"=== Turn {num_of_guesses}/6 ===")
        # prompt guess using input_guess to get correct length
        guess: str = input_guess(len(secret))
        # Codify emoji results using emojified and print string
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {num_of_guesses}/6 turns!")
            won = True
        if num_of_guesses == max_guesses:
            print("X/6 - Sorry, try again tomorrow!")
        # need counter outside of if statements at the bottom of while loop
        num_of_guesses += 1


# the following allows us to run program as a module and make it possible for other modules to import and reuse functions
if __name__ == "__main__":
    main()