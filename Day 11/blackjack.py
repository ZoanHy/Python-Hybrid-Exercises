import imp
from locale import currency
import os
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_card = []
computer_card = []

def random_card():
    return random.choice(cards)

def calculator_score(list_card):
    total_scores = 0
    for score in list_card:
        total_scores += score
    if total_scores > 21 and check_have_ace(list_card):
        total_scores -= 10
    return total_scores

def check_have_blackjack(list_card):
    if 10 in list_card and 11 in list_card and len(list_card) == 2:
        return True
    return False

def check_have_ace(list_card):
    if 11 in list_card:
        return True
    return False
        
def print_final_result(user_card, computer_card):
    print(f"\tYour final hand: {user_card}, current score: {calculator_score(user_card)}")
    print(f"\tComputer's final hand: {computer_card}, final score: {calculator_score(computer_card)}")
    
def print_waiting_result(user_card, computer_card):
    print(f"\tYour cards: {user_card}, current score: {calculator_score(user_card)}")
    print(f"\tComputer's first card: {computer_card[0]}")
    
def comare_score(scores_user, scores_com):
    if scores_user == scores_com or (scores_com > 21 and scores_user > 21):
        print("You draw")
    elif scores_user > scores_com and scores_user <= 21:
        print("You win")
    else:
        print("You lose")
# user_card = [11, 1]
# computer_card = [10, 11]

#Start
game_black_jack = True

while game_black_jack:
    os.system("cls")
    print(logo)
    for i in range(2):
        user_card.append(random_card())
        computer_card.append(random_card())
    print_waiting_result(user_card, computer_card)
    
    if check_have_blackjack(user_card):
        print_final_result(user_card, computer_card)
        print("You win")
    elif check_have_blackjack(computer_card):
        print_final_result(user_card, computer_card)
        print("Lose, opponent has Blackjack")
    else:
        get_card = True
        scores_user = calculator_score(user_card)
        
        while scores_user > 21:
            if not check_have_ace(user_card):
                print("You lose")
            else:
                scores_user = calculator_score(user_card)
        
        get_card = True
        while get_card:
            choose_get_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choose_get_card == "y":
                user_card.append(random_card())
                print_waiting_result(user_card, computer_card)
            else:
                get_card = False        
        scores_com = calculator_score(computer_card)
            
        while scores_com < 17:
            computer_card.append(random.choice(cards))
            scores_com = calculator_score(computer_card)
            
        if scores_com > 21:
            print_final_result(user_card, computer_card)
            print("You win")
        else:
            print_final_result(user_card, computer_card)
            comare_score(scores_user, scores_com)
            
    continue_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if continue_game == 'y':
        game_black_jack = True
    else:
        game_black_jack = False