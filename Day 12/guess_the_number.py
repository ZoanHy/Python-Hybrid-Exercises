import os
import random
from art import logo

os.system("cls")

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

number_random = random.randint(1, 100) 
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

def set_difficulty():
    # global temps
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        return EASY_LEVEL_TURNS
        # temps = EASY_LEVEL_TURNS
    else:
        # temps = HARD_LEVEL_TURNS
        return HARD_LEVEL_TURNS

def check_answer(guess_num, number_random):
    if guess_num > number_random:
        print("Too high.")
    elif guess_num < number_random:
        print("Too low.")
    else:
        print(f"You got it! The answer was {number_random}")
    
def guess_the_number_game():
    temps = set_difficulty()

    guess_num = 0
    while temps > 0 and guess_num != number_random:
        print(f"You have {temps} attemps remaining to guess the number.")
        guess_num = int(input("Make a guess: "))
        check_answer(guess_num, number_random)
        temps -= 1
        if temps == 0:
            print("You've run out of guesses. You lose")
            return
        elif number_random != guess_num:
            print("Guess again")

guess_the_number_game()

    