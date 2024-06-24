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
    },
}

total_money = 0  # initializing the profit to 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_enough_resource(order_item):
    """This function will return true if there are sufficient resources or false if there are not enough resources."""
    for item in order_item:
        if order_item[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins():
    """Takes coins as input and returns the total amount."""
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    total = quarters + dimes + nickles + pennies
    return total


def deduct_items(resources, order_item):
    """This func will take resources as input and update the resources"""
    for item in order_item:
        resources[item] -= order_item[item]


def order():
    """This function will process the order"""
    order = input("What do you want to order? (espresso/latte/cappuccino): ")
    order_item = MENU[order]["ingredients"]
    if not is_enough_resource(order_item):
        return
    else:
        money = process_coins()
        price = MENU[order]["cost"]
        if money >= price:
            return_money = round(money - price, 2)
            deduct_items(resources, order_item)  # reformat the resources
            print(f"Here is ${return_money} in change.")
            print(f"Here is your {order} ☕️. Enjoy!")
            global total_money
            total_money += price # counts the total profit
        else:
            print(f"Sorry that's not enough money. Money refunded.")


def coffee_machine():
    """This function will run the coffee machine."""
    while True:
        # This loop will continue until the user power off the machine
        instruction = input("Kindly give an instruction: ").lower()
        if instruction == "off":
            return
        elif instruction == "order":
            order()
        elif instruction == "report":
            print(f"Water: {resources["water"]}ml")
            print(f"Milk: {resources["milk"]}ml")
            print(f"Coffee: {resources["coffee"]}g")
            print(f"Money: ${total_money}")
        else:
            print("Invalid instruction! Try again.")


coffee_machine()