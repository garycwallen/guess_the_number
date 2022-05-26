# Built-in package that imports random numbers
import random

# Guessing a random number from the computer
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
            
    print(f"Yay, congrats. You have guessed the number {random_number} correctly!")

# Having the computer guess a number we have
## Providing input to the computer whether they're High, Low, or Correct.
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low 
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)?? ").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Yay! The computer guessed your number, {guess}, correctly!")

# Change to guess to play the user guessing game
# TODO: Make dynamic to select which game you'd like to play
computer_guess(1000)