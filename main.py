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


# TODO: Print report
def report(water, coffee, milk, money):
    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")


# TODO: Process coins
def calculate(q, d, n, p):
    total = 0.25 * q + 0.1 * d + 0.05 * n + 0.01 * p
    return float(total)


# TODO: Check resources sufficient
# TODO: Check transaction successful
is_sufficient = False
def sufficient(choice, water, coffee, milk, money):
    if MENU[choice]["ingredients"]["water"] > water:
        print("Sorry there is not enough water.")
        is_sufficient = False
    elif MENU[choice]["ingredients"]["coffee"] > coffee:
        print("Sorry there is not enough coffee.")
        is_sufficient = False
    elif MENU[choice]["ingredients"]["water"] > milk:
        print("Sorry there is not enough milk.")
        is_sufficient = False
    else:
        is_sufficient = True
        quarter = int(input("Please insert coins. \nHow many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickle = int(input("How many nickles?: "))
        penny = int(input("How many pennies?: "))
        inserted_coin = calculate(quarter, dime, nickle, penny)
        change = inserted_coin - MENU[choice]["cost"]
        if change < 0:
            print("Sorry that's not enough money. Money refunded.")
            is_sufficient = False
        else:
            print(f"Here is ${round(change, 2)} in change.")
            print(f"Here is your {choice} ☕️. Enjoy!")
    return is_sufficient

# TODO: Prompt user by asking "What would you like?"
# TODO: Turn off the CM be entering "off" to the prompt
# TODO: Make coffee
should_continue = True
money = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
while should_continue:
    choice = input("What would like? (espresso/latte/cappuccino): ")
    if choice == "off":
        should_continue = False
    elif choice == "report":
        report(water, coffee, milk, money)
    elif sufficient(choice, water, coffee, milk, money) == True:
        money += MENU[choice]["cost"]
        water -= MENU[choice]["ingredients"]["water"]
        if(choice != "espresso"):
            milk -= MENU[choice]["ingredients"]["milk"]
        coffee -= MENU[choice]["ingredients"]["coffee"]


