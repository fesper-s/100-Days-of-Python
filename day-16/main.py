from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    option = input(f"What would you like? ({menu.get_items()}): ")
    if option == "off":
        break
    elif option == "report":
        coffee_maker.report()
        money_machine.report()
    elif option in menu.get_items():
        drink = menu.find_drink(option)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)
