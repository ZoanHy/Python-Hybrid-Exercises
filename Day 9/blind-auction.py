import os
os.system("cls")

from art import logo

print(logo)

bid_person = {} 

def find_highest_bidder(array_bids):
    highest_bidder = 0
    name_winner = ""
    for bidder in array_bids:
        bid_num = array_bids[bidder]
        if bid_num > highest_bidder:
            highest_bidder = bid_num
            name_winner = bidder
    print(f"The winner is {name_winner} with a bid of ${highest_bidder}")

check_bid = False
while not check_bid:
    name = input("What is your name? ")
    bid_price = float(input("What is your bid? $ "))
    bid_person[name] = bid_price
    countinue_bid = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if countinue_bid == "no":
        os.system("cls")
        check_bid = True
        find_highest_bidder(bid_person)
    else:
        os.system("cls")
        check_bid = False


