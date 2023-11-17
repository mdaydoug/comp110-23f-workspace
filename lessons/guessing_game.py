"""Program that loops until correct number is guesses."""

# from random import randint
# In initial example we generated a random number importing randint
# For this example we changed value of secret: int = 5 instead of int = randint

secret: int = 5
guess: int = int(input("Guess a number between 1 and 10: "))
number_of_tries: int = 0
max_tries: int = 3 


while (guess != secret) and (number_of_tries < (max_tries - 1)):
    print("Wrong, bitch!")
    # If guess is out of bounds, let them know
    if (guess < 1) or (guess > 10):
        print("That's not between 1 and 10!")
    # If guess is too low, tell them
    if guess < secret:
        print("Too low!")
    # If guess is too high, tell them
    elif guess > secret:
        print("Too high!")
    # Ask for a different guess
    guess = int(input("Guess again: "))
    number_of_tries += 1
# If I've reached this point, guess == secret
if guess == secret:
    print("You guessed right, bitch!")
else: 
    print("You lose. :( ")
