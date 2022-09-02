import os
from art import logo
os.system("cls")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    caesar_text = ""
    if shift > len(alphabet):
        shift = shift % 26
    for character in text:
        if character in alphabet:
            index = alphabet.index(character)
        if (direction == "encode"): 
            if(index + shift) <= len(alphabet) - 1:
                new_character = alphabet[index + shift]
            else:
                new_character = alphabet[index + shift - len(alphabet)]
            caesar_text+=new_character
        else:
            if(index - shift) >= 0:
                new_character = alphabet[index - shift]
            else:
                new_character = alphabet[index - shift + len(alphabet)]
            caesar_text+=new_character  
    print(caesar_text)

print(logo)
check = True
while check:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text=text, shift=shift, direction=direction)
    choice = input("Do you want to restart the cipher program? Type 'yes' or 'no'\n").lower()
    if choice == "yes":
        check = True
    else:
        check = False

    
