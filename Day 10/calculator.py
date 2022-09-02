import os
from art import logo
os.system("cls")

#Calculator
# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def sub(n1, n2):
    return n1 - n2

# Multiply
def mul(n1, n2):
    return n1 * n2

#Divide
def div(n1, n2):
    return n1 / n2

calcultor_dictionary = {
    "+" : add,
    "-": sub,
    "*": mul,
    "/": div
}

# function = calcultor_dictionary["+"]
# print(function(2,3))

def calculation():
    print(logo)
    num1 = float(input("What's the first number? "))
    for symbol in calcultor_dictionary:
        print(symbol)
    check = True
    # answer_final = num1
    while check:
        # temp = answer_final
        choose_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number? "))
        cal_function = calcultor_dictionary[choose_symbol]
        answer_final = cal_function(num1, num2)
        print(f"{num1} {choose_symbol} {num2} = {answer_final}")
        choice = input(f"Type 'y' to continue calculating with {answer_final}, or type 'n' to exit.: ").lower()
        if choice == "y":
            check = True
            num1 = answer_final
        else:
            check = False

# print(f"{num1} {choose_symbol} {num2} = {fist_answer}")

# choose_symbol = input("Pick another operation: ")
# num3 = int(input("What's the next number? "))
# cal_function = calcultor_dictionary[choose_symbol]
# result_final = cal_function(fist_answer, num3)

