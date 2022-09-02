import os
import random
import hangman_art
from hangman_words import word_list

# += ~ extend: add more items
# append: add one item

os.system("cls")

# word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
lives = 6

print(hangman_art.logo)
# print(f'Pssst, the solution is {chosen_word}.')

blank = True

for _ in range(len(chosen_word)):
    # display.append("_")
    display += "_"

while blank:
    called_guess = input("Guess a letter: ").lower()
    if called_guess in display:
        print(f"You've already guessed {called_guess}")
        
    for index in range(len(chosen_word)):
        if chosen_word[index] == called_guess:
            display[index] = called_guess 
    if called_guess not in chosen_word:
        print(f"You guessed {called_guess}, that's not in the word. You lose a life")
        lives -= 1
        if(lives == 0):
            blank = False
            print("You lost")
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        blank = False
        print("You win")        
    print(hangman_art.stages[lives])
    