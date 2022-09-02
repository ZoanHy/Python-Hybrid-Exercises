from unittest import result


print("Welcome to the Love Calculator")
your_name = input("What is your name? ").lower()
destiny_name = input("What is your destiny name? ").lower()

concat_name = your_name + destiny_name
total_true = concat_name.count("t") + concat_name.count("r") + concat_name.count("u") + concat_name.count("e") 
total_love = concat_name.count("l") + concat_name.count("o") + concat_name.count("v") + concat_name.count("e") 

score = str(total_true) + str(total_true)
result = int(score             )
if result < 10 or result > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")