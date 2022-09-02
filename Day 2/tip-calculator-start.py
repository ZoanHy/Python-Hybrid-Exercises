
print("Welcome to the tip calculator.\n")
total_bill = float(input("What was the total bill? $"))
percentage_tip = float(input(
    "What percentage tip would you like to give? 10, 12, or 15? ")) / 100
people = int(input("How many people to split the bill? "))

each_person_pay = round((total_bill * (1.0 + percentage_tip)/ people),2)
print(
    f"Each person should pay: ${each_person_pay}")
