import os
os.system("cls")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_text = ""
    for character in text:
        index = alphabet.index(character)
        if(index + shift) < len(alphabet) - 1:
            new_character = alphabet[index + shift]
        else:
            new_character = alphabet[index + shift - len(alphabet) - 1]
        encrypted_text+=new_character
    print(encrypted_text)

def decrypt(text, shift):
    deencrypted_text = ""
    for character in text:
        index = alphabet.index(character)
        if(index - shift) >= 0:
            new_character = alphabet[index - shift]
        else:
            new_character = alphabet[index - shift + len(alphabet) + 1]
        deencrypted_text+=new_character
    print(deencrypted_text)
if direction == "encode":
    encrypt(text=text, shift=shift)
else:
    decrypt(text=text, shift=shift)