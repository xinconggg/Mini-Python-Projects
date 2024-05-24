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

def check_resources_sufficient(drink):
    drink_ingredients = drink["ingredients"]
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there's not enough {item}")
            return False
    return True

def check_money(drink, total_amt):
    change = 0
    profit = 0
    drink_cost = drink["cost"]
    if drink_cost > total_amt:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = round(total_amt - drink_cost, 2)
        profit += drink_cost
        print(f"Here's ${change} in change.")
        return profit
    
def minus_resources(drink):
    drink_ingredients = drink["ingredients"]
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    return resources[item]


def start_coffee_machine(MENU, resources):
    correct_input = False
    while not correct_input:
        choice = input("What would you like? (espresso / latte / cappuccino / **report** / **off**): ").lower()

        # If user wants to check the amount of resources left
        if choice == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")

        # If user wants to turn off the machine
        elif choice == 'off':
            correct_input = True

        # If user chooses a drink from menu
        elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
            drink = MENU[choice]
            resources_left = check_resources_sufficient(drink)
            # If there's sufficient ingredients
            if resources_left:
                print(f"The cost of {choice} is: {drink['cost']}")
                print("Please insert coins.")
                amt_in_quarters = int(input("How many quarters?: ")) * 0.25
                amt_in_dimes = int(input("How many dimes?: ")) * 0.1
                amt_in_nickles = int(input("How many nickles?: ")) * 0.05
                amt_in_pennies = int(input("How many pennies?: ")) * 0.01
                total_amt = amt_in_quarters + amt_in_dimes + amt_in_nickles + amt_in_pennies
                profit = check_money(drink, total_amt)
                if profit:
                    print(f"Here is your {choice} ☕! Enjoy!!")
                    minus_resources(drink)

start_coffee_machine(MENU, resources)