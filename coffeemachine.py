from menuresources import menu, resources
import os


def machine():
    print(f"\nMENU\nespresso: ${menu['espresso']['cost']}0     latte: ${menu['latte']['cost']}0     cappuccino: ${menu['cappuccino']['cost']}0")
    while True:
        drink_choice = input("\nWhat would you like? Type '1' for espresso, '2' for latte, or '3' for cappuccino: ")
        if drink_choice == '1':
            drink_choice = "espresso"
            enough_ingredients(drink_choice)
            break
        elif drink_choice == '2':
            drink_choice = "latte"
            enough_ingredients(drink_choice)
            break
        elif drink_choice == '3':
            drink_choice = "cappuccino"
            enough_ingredients(drink_choice)
            break
        elif drink_choice == 'report':
            print(f"\nWater: {resources['water']}mL\nMilk: {resources['milk']}mL\nCoffee: {resources['coffee']}g")
            machine()
            break
        elif drink_choice == 'off':
            exit()
        else:
            print("\nIncorrect response - please try again.")
    print("\nPlease insert coins.")
    while True:
        try:
            num_quarters = int(input("How many quarters?: "))
        except ValueError:
            print("\nIncorrect input - please try again.")
        else:
            break
    while True:
        try:
            num_dimes = int(input("How many dimes?: "))
        except ValueError:
            print("\nIncorrect input - please try again.")
        else:
            break
    while True:
        try:
            num_nickels = int(input("How many nickels?: "))
        except ValueError:
            print("\nIncorrect input - please try again.")
        else:
            break
    while True:
        try:
            num_pennies = int(input("How many pennies?: "))
        except ValueError:
            print("\nIncorrect input - please try again.")
        else:
            break
    money_amount = change_value(num_quarters, num_dimes, num_nickels, num_pennies)
    change = enough_money(money_amount, drink_choice)
    resources["water"] -= menu[drink_choice]["ingredients"]["water"]
    resources["milk"] -= menu[drink_choice]["ingredients"]["milk"]
    resources["coffee"] -= menu[drink_choice]["ingredients"]["coffee"]
    change = "{:0.2f}".format(change)
    print(f"\nHere is ${change} in change. Here is your {drink_choice}. Enjoy!")
    machine()


def enough_ingredients(drink_choice):
    """Take drink ordered and see if machine has enough ingredients"""
    if resources["water"] < menu[drink_choice]["ingredients"]["water"]:
        print("\nSorry, there is not enough water.")
        machine()
    elif resources["milk"] < menu[drink_choice]["ingredients"]["milk"]:
        print("\nSorry, there is not enough milk.")
        machine()
    elif resources["coffee"] < menu[drink_choice]["ingredients"]["coffee"]:
        print("\nSorry, there is not enough coffee.")
        machine()
    else:
        return 

def enough_money(money_amount, drink_choice):
    """Takes coins given and see if it's enough to buy coffee"""
    if money_amount >= menu[drink_choice]["cost"]:
        change_returned = money_amount - menu[drink_choice]["cost"]
        return change_returned
    else:
        print("\nSorry, that's not enough money. Money refunded.")
        machine()


def change_value(num_quarters, num_dimes, num_nickels, num_pennies):
    quarters = num_quarters * 0.25
    dimes = num_dimes * 0.1
    nickels = num_nickels * 0.05
    pennies = num_pennies * 0.01
    sum_change = quarters + dimes + nickels + pennies
    return sum_change

machine()
