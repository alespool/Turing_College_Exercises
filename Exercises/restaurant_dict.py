from typing import *

MENU = {
    'sandwich': 5,
    'pizza': 6,
    'salad': 8,
    'chicken': 7,
    'tea': 2,
    'beef': 9
}


def restaurant_orders(user: str, request: Optional[List[str]]) -> None:
    active = True
    total = 0

    while active:
        orders = [order.strip() for order in request.split(',')]
        for order in orders:

            if not order:  # if blank
                print("Invalid order: blank entry")
                continue

            price = MENU.get(order)
            if price is None:

                print(f"We don't offer {order} at this time, sorry!")
                continue
            else:
                print(f"The {order} costs {price}.")
                total += price

        print(f"Your total is now: {total}.")
        check = input("Do you want anything else? Please say 'Yes' or 'No' ")

        if check == 'Yes'.lower():
            request = input(f"What else would you like to order, {user}? ")
            continue

        elif check == 'No'.lower():
            print(f"Thank you for ordering!")
            print(f"The total is {total}.")
            active = False

        else:
            print("Invalid input. Please say 'Yes' or 'No'")
            print(f"The total is {total}.")

    return


user = input(f"Hi! What's your name? ")
request = input(f"What would you like to order, {user}? ")


test = restaurant_orders(user, request)
