"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730660951"

word_used: str = input("Enter a 5-character word: ")

if len(word_used) != 5:
    print("Error: Word must contain 5 characters")
    exit()   

character: str = input("Enter a single character: ")

if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

num_of_matches: int = 0
print("Searching for " + character + " in " + word_used)

if str(word_used[0]) == character:
    print(character + " found at index 0")
    num_of_matches = num_of_matches + 1
if str(word_used[1]) == character:
    print(character + " found at index 1")
    num_of_matches = num_of_matches + 1
if str(word_used[2]) == character:
    print(character + " found at index 2")
    num_of_matches = num_of_matches + 1
if str(word_used[3]) == character:
    print(character + " found at index 3")
    num_of_matches = num_of_matches + 1
if str(word_used[4]) == character:
    print(character + " found at index 4")
    num_of_matches += num_of_matches
if int(num_of_matches) > 1:
    print(str(num_of_matches) + " instances of " + character + " found in " + word_used)
if int(num_of_matches) == 1:
    print(str(num_of_matches) + " instance of " + character + " found in " + word_used)
if int(num_of_matches) == 0:
    print("No instances of " + character + " found in " + word_used)