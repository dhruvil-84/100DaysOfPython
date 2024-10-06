from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

is_machine_on = True
while is_machine_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").strip().lower()
    if choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif choice == "off":
        is_machine_on = False
    elif choice == "cappuccino" or choice == "latte" or choice == "espresso":
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)
    else:
        print(f"please choose {menu.get_items()}.")