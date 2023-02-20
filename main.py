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

# print(resources.get("water"))
# resources.update({"water": "50"})
# print(resources.get("water"))

money=0

# TODO 3: Print report.
def Print_report():
    """Print The Inventory report"""
    global money
    print("Water: "+str(resources.get("water"))+"ml")
    print("Milk: " + str(resources.get("milk"))+"ml")
    print("Coffee: " + str(resources.get("coffee"))+"ml")
    print("Money: $" + str(money))


# TODO 4: Check resources sufficient.
def Check_resource(type):
    """ TYPE is a espresso/latte/cappuccino. And It check the Inventory """
    if(type.lower()=="espresso"):

        coffee=MENU.get("espresso").get("ingredients").get("coffee")
        water=MENU.get("espresso").get("ingredients").get("water")
        # print("I am in: "+ str(coffee)+"  "+str(water))

        if coffee <= resources.get("coffee") and water <= resources.get("water"):
            return True
        else: return False

    elif (type.lower()=="latte"):

        coffee = MENU.get("latte").get("ingredients").get("coffee")
        water = MENU.get("latte").get("ingredients").get("water")
        milk = MENU.get("latte").get("ingredients").get("milk")

        if coffee <= resources.get("coffee") and water <= resources.get("water") and milk <= resources.get("milk"):
            return True
        else:
            return False

    elif (type.lower() == "cappuccino"):

        coffee = MENU.get("cappuccino").get("ingredients").get("coffee")
        water = MENU.get("cappuccino").get("ingredients").get("water")
        milk = MENU.get("cappuccino").get("ingredients").get("milk")

        if coffee <= resources.get("coffee") and water <= resources.get("water") and milk <= resources.get("milk"):
            return True
        else:
            return False

# TODO 5: Process coins
def Process_coins():
    """Coin convert in Doller"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    total_money =  (0.25 * quarters) + (0.1 * dimes)  + (0.05 * nickles) + (0.01 * pennies)
    return total_money

# TODO 6: Check transaction successful

def Check_transaction(orderType,pay):
    price=MENU.get(orderType).get("cost")
    if pay >= price :
        return True
    else:
        return False



# TODO 7: Make Coffee.

def Make_Coffee(order_type,change_amt):

    global money
    if order_type.lower() != "espresso":

        coffee = resources.get("coffee")-MENU.get(order_type).get("ingredients").get("coffee")
        water = resources.get("water")-MENU.get(order_type).get("ingredients").get("water")
        milk = resources.get("milk")-MENU.get(order_type).get("ingredients").get("milk")
        money+=MENU.get(order_type).get("cost")

        resources.update({"water": water,"coffee": coffee, "milk": milk})
    else:
        coffee = resources.get("coffee") - MENU.get(order_type).get("ingredients").get("coffee")
        water = resources.get("water") - MENU.get(order_type).get("ingredients").get("water")
        #milk = resources.get("milk") - MENU.get(order_type).get("ingredients").get("milk")
        money += MENU.get(order_type).get("cost")

        resources.update({"water": water, "coffee": coffee})


    print(f"Here is ${change_amt} in change.")
    print(f"Here is your {order_type} ☕️. Enjoy!")

# TODO Get Price
def refund(orderType,pay):
    refnd=round(pay-MENU.get(orderType).get("cost"),2)
    return refnd

# TODO 1:  asking from user

while True:
    user_choise=input("  What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choise == "espresso" or user_choise == "latte" or user_choise == "cappuccino":
        if Check_resource(user_choise):

            pay_amount= Process_coins()
            if Check_transaction(user_choise,pay_amount):

                    change_amt=refund(user_choise,pay_amount)
                    Make_Coffee(user_choise,change_amt)


            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough water.")


    elif user_choise == "off":
        exit()

    elif user_choise == "report":
        Print_report()

    else: print("Wrong Input")




