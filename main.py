from art import logo
import random

# This is a function that generates a random int number between 1 and 100
def generate_random_number():
    return random.randrange(1,100,1)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = generate_random_number()
print(f"Pssst, the correct answer is {number}")

# Ask player for a difficulty level
level = ""
while level != "easy" and level != "hard":
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

# Save the number of rounds
rounds = 0
if level == "easy":
    rounds = 10
elif level == "hard":
    rounds = 5

print(f"You have {rounds} attempts remaining to guess the number.")

# Game main loop
while rounds > 0:
    guess = int(input("Make a guess: "))
    
    # Let's compare the guess with the number
    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    elif guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")

    # Update rounds
    rounds -= 1
    # Test if rounds > 0
    if rounds == 0:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again.")
        print(f"You have {rounds} attempts remaining to guess the number.")