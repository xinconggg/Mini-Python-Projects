#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
print("Welcome to Number Guessing game!")
print("I'm thinking of a number between 1 and 100.")

def get_difficulty_level():
    correct_input = False
    while not correct_input:
        difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()

        if difficulty_level == 'easy':
            print("You have 10 attempts to guess the number.")
            lives = 10
            return lives

        elif difficulty_level == 'hard':
            print("You have 5 attempts to guess the number.")
            lives = 5
            return lives

        else:
            print("Please type only 'easy' or 'hard': ")

def play_game(lives):
    number_to_guess = random.randint(1,100)
    while lives > 0:
        guess_number = int(input("Make a guess: "))
        if guess_number < number_to_guess:
            print("Too low.")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number.")

        elif guess_number > number_to_guess:
            print("Too high.")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number.")

        else:
            print(f"You got it! The answer was {number_to_guess}.")
            break
            
    if lives == 0:
        print(f"You ran out of guesses, the number was {number_to_guess}. Thank you for Playing!")

lives = get_difficulty_level()
play_game(lives)