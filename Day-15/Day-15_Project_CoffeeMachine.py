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
    "money": 0
}

def generate_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}\n")

def check(ingredients):
    can_make = True
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            can_make = False
    if can_make == False:
        print("")
    return can_make

def deduct(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]

def money_section(cost):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ").strip())
    dimes = int(input("How many dimes?: ").strip())
    nickels = int(input("How many nickels?: ").strip())
    pennies = int(input("How many pennies?: ").strip())
    dollar = round((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01), 2)
    if dollar >= cost:
        resources["money"] += cost
        return round(dollar - cost, 2)
    else:
        return -1

is_machine_on = True
while is_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
    if choice == "report":
        generate_report()
    elif choice == "off":
        is_machine_on = False
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check(MENU[choice]["ingredients"]):
            val = money_section(cost = MENU[choice]["cost"])
            if val > 0:
                deduct(MENU[choice]["ingredients"])
                print(f"Here is ${val} in change.\nHere is your {choice} coffee. Enjoy!\n")
            elif val == 0:
                deduct(MENU[choice]["ingredients"])
                print(f"Here is your {choice} coffee. Enjoy!\n")
            else:
                print("Sorry that's not enough money. Money refunded.\n")
    else:
        print("please choose espresso/latte/cappuccino.\n")