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

money = 0
while True:
    option = input("What would you like? (espresso/latte/cappuccino): ")
    if option == "off":
        break
    elif option == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")  
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif option == "espresso" or option == "latte" or option == "cappuccino":
        drink = MENU[option]
        ingredients = drink['ingredients']
        if ingredients['water'] > resources['water']:
            print("Sorry there is not enough water.")
        elif not option == 'espresso' and ingredients['milk'] > resources['milk']:
            print("Sorry there is not enough milk.")
        elif ingredients['coffee'] > resources['coffee']:
            print("Sorry there is not enough coffee.")
        else:
            print("Please insert coins.")
            money += 0.25 * float(input("How many quarters? "))
            money += 0.10 * float(input("How many dimes? "))
            money += 0.05 * float(input("How many nickels? "))
            money += 0.01 * float(input("How many pennies? "))
            if money >= drink['cost']:
                resources['water'] -= ingredients['water']
                if not option == 'espresso':
                    resources['milk'] -= ingredients['milk']
                resources['coffee'] -= ingredients['coffee']
                print(f"Here is ${round(money - drink['cost'], 2)} in change.")
                money = drink['cost']
                print(f"Here is your {option} ☕️ Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
