from machine import MENU
from machine import resources

machine_active = True
instance_resources = resources
instance_money = 0

def print_current_resources():
    print(f"Water: {instance_resources['water']}ml")
    print(f"Milk: {instance_resources['milk']}ml")
    print(f"Coffee: {instance_resources['coffee']}ml")
    print(f"Money: ${instance_money}")


def check_resource_availability(instance_resources, menu_item_ingredients):
    resource_availability = True
    for resource in menu_item_ingredients:
        if instance_resources[resource] < menu_item_ingredients[resource]:
            print(f"Sorry there is not enough {resource}")
            resource_availability = False
            break
    return resource_availability


def update_resources(instance_resources,menu_item_ingredients):
    for resource in menu_item_ingredients:
        resource_withdrawal = menu_item_ingredients[resource]
        instance_resources[resource] = instance_resources[resource] - resource_withdrawal
    return instance_resources


def sum_coins_inserted(quarters, dimes, nickles, pennies):
    total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    return total


while machine_active:
    instruction = input("  What would you like? (espresso/latte/cappuccino):  ").lower()
    if instruction == "off":
        machine_active = False
    elif instruction == "report":
        print_current_resources()
    elif instruction == "espresso" or instruction == "latte" or instruction == "cappuccino":
        if check_resource_availability(instance_resources, MENU[instruction]['ingredients']) == True:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            money_added = sum_coins_inserted(quarters, dimes, nickles, pennies)
            money_required = MENU[instruction]['cost']
            if money_added < money_required:
                print("Not enough money")
            else:
                money_change = money_added - money_required
                instance_money += money_required
                instance_resources = update_resources(instance_resources, MENU[instruction]['ingredients'])
                print(f"Here is ${money_change} in change")
                print(f"Here is your {instruction} ☕ Enjoy!")