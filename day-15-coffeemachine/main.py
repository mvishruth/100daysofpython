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

profit = 0
resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
}


def report():
  water = resources["water"]
  milk = resources["milk"]
  coffee = resources["coffee"]
  print(f"Water : {water}ml")
  print(f"Milk : {milk}ml")
  print(f"coffee : {coffee}g")
  print(f"Money : ${profit}")


def check_resources(user_input):
  """Returns True when order can be made, False if ingredients are insufficient."""
  required = MENU[user_input]['ingredients']
  for key in resources:
    if resources[key] > required[key]:
      flg = True
    else:
      flg = False
  return flg


def insert_coins(user_input):
  print("Please insert Coins:")
  coins = int(input("How many quarters:")) * .25
  coins += int(input("How many dimes:")) * .10
  coins += int(input("How many nickles:")) * .05
  coins += int(input("How many pennies:")) * .01
  return coins


def is_transaction_successfull(user_input, coins):
  """Returns True when payment  is received, False when payment are insufficient"""
  global profit
  cost = MENU[user_input]['cost']
  change = coins - cost
  if coins >= cost:
    print(f"here is your ${change} in change")
    profit += cost
    return True
  else:
    return False


def make_coffee(drink_name):
  """" deduct the resources in the machine """
  required = MENU[drink_name]['ingredients']
  for item in resources:
    resources[item] -= required[item]
  print(f"Here is your {drink_name} ☕️. Enjoy!")


# TODO 1 User Input promt shoud show everytme drink is dispensed

is_on = True


def main():

  #global profit
  while is_on == True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
      report()
    elif user_input == "off":
      print("Coffe Machine is now off.")
      exit(0)
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
      check_resources_flg = check_resources(user_input)
      if check_resources_flg == True:
        coins = insert_coins(user_input)
        transaction_success = is_transaction_successfull(user_input, coins)
        make_coffee(user_input)
    else:
      print("Sorry wrong option try again")


main()