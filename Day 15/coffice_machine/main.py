import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COIN_QUARTER = 0.25
COIN_DIME = 0.1
COIN_NICKLES = 0.05
COIN_PENNY = 0.01


def check_resources(flavors):
    array_flavors_lack = []
    for key in resources:
        if key in flavors["ingredients"]:
            if flavors["ingredients"][key] > resources[key]:
                array_flavors_lack.append(key)
    return array_flavors_lack


def check_coin(coin_flavors, coin_customer):
    return coin_customer - coin_flavors


def process_coin():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * COIN_QUARTER
    total += int(input("how many dimes?: ")) * COIN_DIME
    total += int(input("how many nickles?: ")) * COIN_NICKLES
    total += int(input("how many pennies?: ")) * COIN_PENNY
    return total


def coffee_machine():
    off_coffee_machine = False
    total_money = 0
    while not off_coffee_machine:
        customer_choose = input(" What would you like? (espresso/latte/cappuccino): ").lower()
        if customer_choose == "report":
            print(f"Water {resources['water']}ml")
            print(f"Milk {resources['milk']}ml")
            print(f"Coffee {resources['coffee']}g")
            print(f"Money: ${total_money}")
        elif customer_choose == 'off':
            off_coffee_machine = True
        else:
            flavor = MENU[customer_choose]
            length_array_lack = len(check_resources(flavor))
            if length_array_lack == 0:
                total_coin = process_coin()
                result_coin = check_coin(flavor['cost'], total_coin)
                for key in flavor["ingredients"]:
                    resources[key] -= flavor["ingredients"][key]
                if result_coin >= 0:
                    total_money += flavor['cost']
                    print(f"Here is ${round(result_coin, 2)} in change.")
                    print(f"Here is your {customer_choose}. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded")
            else:
                for item in check_resources(flavor):
                    print(f"Sorry there is not enough {item}.")


coffee_machine()
