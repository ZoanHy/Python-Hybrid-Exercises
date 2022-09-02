
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

player_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[player_choice])

com_choice = random.randint(0, 2)
print(f"Computer chose: ")
print(game_images[com_choice])

if player_choice == com_choice:
    print("You draw")
elif player_choice == 0 and com_choice == 2:
    print("You win")
elif com_choice > player_choice:
    print("You loss")
elif player_choice > com_choice:
    print("You win")
elif player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number! You loss")
elif com_choice == 0 and player_choice == 2:
    print("You loss")
