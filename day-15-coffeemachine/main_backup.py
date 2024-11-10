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

currency =  {"quarters":  0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

# TODO: 1. Print report of all coffee machine resources
def print_report():
    #print(f"Water: {resources["water"]}")
    w = resources["water"]
    m = resources["milk"]
    c = resources["coffee"]
    print(f"Water: {w}ml")
    print(f"Milk: {m}ml")
    print(f"Coffee: {c}g")
    print(f"Money: ${money}")


def check_resources(ui):
    required = MENU[ui]['ingredients']
    for key in resources:
        if not resources[key] >= required[key]:
            return False
        else:
            return True
            #print(f"{resources[key]}, {required[key]}")

def process_coins():
    """Returns the total calculated from coins"""
    print("Please Insert Coins:")
    total = int(input("How many Quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.1
    total += int(input("How many nickles?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total

def check_transaction(ui):
    ingd = MENU[ui]["ingredients"]
    coffee_cost = MENU[ui]["cost"]
    usr_money = process_coins()
    if usr_money >= coffee_cost:
        global money
        money += coffee_cost
        change = usr_money - coffee_cost
        print(f"Here is ${change} dollars in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """deduct the resources in machine"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


def main():
    user_input = input("What would you like? (espresso/latte/cappuccino):")
    resource_flg = check_resources(user_input)
    while resource_flg == True:
        transaction_flg = check_transaction(user_input)
        if transaction_flg == True:
            make_coffee(user_input,MENU[user_input]["ingredients"])
    print_report()

main()
