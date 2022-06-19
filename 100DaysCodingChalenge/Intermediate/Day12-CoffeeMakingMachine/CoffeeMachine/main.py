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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_transaction_successful(money_received,drink_cost):
    """Return True when the payment is accepted, or False of money is insufficient"""
    if money_received>=drink_cost:
        change= round(money_received-drink_cost,2)
        print(f"Here is {change} in change")
        global profit
        profit +=drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded")
        return False

def is_resource_sufficient(order_ingredient):
    """Return True when order can be made, False if ingredients are insufficient.."""
    for item in order_ingredient:
        if order_ingredient[item]>resources[item]:
            print(f"Sorry there is not enough {item} available")
            return False
    return True

def process_coins():
    """Return the total calculted from the coin inserted..."""
    print("Please insert coins.")
    total=int(input("How many quaters?"))*0.25
    total += int(input("How many dine?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total

def make_coffee(drink_name,order_ingredient):
     """Deduct the required ingregient from dthe resources."""
     for item in order_ingredient:
         resources[item] -= order_ingredient[item]
     print(f"Here is your {drink_name}coffee! Have a great day!")

is_on=True
while is_on:
    # TODO: 1. Promt the user about their requirement
    choice= input("What would you like? (espresso/latte/cappuccino):")
    # TODO: 2. We should turn off the machine by entering "off" to the prompt
    if choice =="off":
        is_on=False
# TODO: 3. Print report of all the coffee machine resources on "report" to the promp
    elif choice=="report":
        print(f"water:{resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money:${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])

