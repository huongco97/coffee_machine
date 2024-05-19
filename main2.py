MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
def report(water, milk, coffee, money):
    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")
def calculate(q, d, n, p):
    money = 0.25*q + 0.1*d + 0.05*n + 0.01*p
    return money

def check(drink):
    if MENU[drink]['ingredients']['water'] > water:
        print("Sorry there was not enough water.")
        return False
    elif MENU[drink]['ingredients']['milk'] > milk:
        print("Sorry there was not enough milk.")
        return False
    elif MENU[drink]['ingredients']['coffee'] > coffee:
        print("Sorry there was not enough coffee.")
        return False
    return True
#     elif MENU[drink]['cost'] > money:
#         print("Not enough money.")
#         should_continue = False

should_continue = True
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0
while should_continue:
    drink = input("What would you like? espresso/latte/cappuccino ")
    if drink == 'off':
        should_continue = False
    elif drink == 'report':
        report(water, milk, coffee, money)
    else:
        if check(drink):
            print("Please insert coins.\n")
            q = int(input("How many quarters? "))
            d = int(input("How many dimes? "))
            n = int(input("How many nickles? "))
            p = int(input("How many pennies? "))
            added = calculate(q,d,n,p)
            if added >= MENU[drink]['cost']:
                money += added
                change = money - MENU[drink]['cost']
                print(f"Here is ${round(change,2)} in change.\nHere is your {drink}. Enjoy!")
                water = water - MENU[drink]['ingredients']['water']
                milk = milk - MENU[drink]['ingredients']['milk']
                coffee = coffee - MENU[drink]['ingredients']['coffee']
                money = round(money-MENU[drink]['cost'],1)
            else:
                print("Sorry that's not enough money. Money refunded")
                money += added
