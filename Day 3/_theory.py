#_Control Flow with if else and Conditional Operators

# print("Welcome to the rollerccoaster")
height = int(input("What is your height in cm? "))

# if height > 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, You have to grow taller before you can ride.")
    
#_Nested if statements and elif statements
bill = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets aare $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo taken? y or n. ")
    if(wants_photo == "y"):
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry, You have to grow taller before you can ride.")
    
#_Multiple If Statements in Succession

#_Logical Operators