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

units = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}


def report():
    for resource in resources:
        print(f"{resource}: {resources[resource]}{units[resource]}")
    print(f"Money: ${money}")


def resources_ok(menu_item):
    needed_ingredients = MENU[menu_item]["ingredients"]
    for resource in needed_ingredients:
        available = resources[resource]
        needed = needed_ingredients[resource]
        if available < needed:
            print(f"Sorry, there is no enough {resource}")
            return False
    for resource in needed_ingredients:
        needed = needed_ingredients[resource]
        resources[resource] -= needed
    return True


def money_ok(menu_item):
    print("Please, insert coins.")
    q = int(input("How many quarters?"))
    d = int(input("How many dimes?"))
    n = int(input("How many nickles?"))
    p = int(input("How many pennies?"))
    gived = q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01
    needed = MENU[menu_item]["cost"]
    if gived > needed:
        print(f"Here is you $ {round(gived - needed, 2)} in change.")
        return True
    elif gived == needed:
        print(f"Money Ok")
        return True
    else:
        print(f"You give ${gived}, but ${needed} needed. Money refunded.")
        return False


def make_coffee(menu_item):
    global money
    if not money_ok(menu_item):
        return
    if not resources_ok(menu_item):
        return
    money += MENU[menu_item]["cost"]
    print(f"Here is your {menu_item}.☕ Enjoy!")


def ask_question():
    is_continue = True
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if answer == "espresso":
        make_coffee("espresso")
    elif answer == "latte":
        make_coffee("latte")
    elif answer == "cappuccino":
        make_coffee("cappuccino")
    elif answer == "off":
        is_continue = False
    elif answer == "report":
        report()
    return is_continue


on = True
money = 0
while on:
    on = ask_question()
