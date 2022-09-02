import os
import random
from unicodedata import name
from art import logo, vs
from game_data import data

os.system("cls")


        
def compare_followers(person_a, person_b):
    if person_a["follower_count"] > person_b["follower_count"]:
        return True
    elif person_a["follower_count"] < person_b["follower_count"]:
        return False

def detail_information(person):
    return f"{person['name']}, a {person['description']}, from {person['country']}"
    
def higher_lower_play(): 
    
    total_scores = 0
    check_play = True
    while check_play:
        os.system("cls")
        print(logo)
        if total_scores != 0:
            print(f"You're right! Current score: {total_scores}")
            person_a = person_b
        else:
            person_a = random.choice(data)
        
        person_b = random.choice(data)

        if person_a == person_b:
            while person_a == person_b:
                person_b = random.choice(data)

        
        print(f"Compare A: {detail_information(person_a)}")
        print(vs)
        print(f"Against B: {detail_information(person_b)}")

        choice_person = input("Who has more followers? Type 'A' or 'B': ")
        
        if (compare_followers(person_a, person_b) and choice_person == 'A') or (not compare_followers(person_a, person_b) and choice_person == 'B'):
            check_play = True
            total_scores+=1
        else:
            check_play = False
            print(f"Sorry, that's wrong. Final score: {total_scores}")
    
higher_lower_play()




