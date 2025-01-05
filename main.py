#A shopping cart program that adds items / prices to a list and prints the total.

#The list of available items in the store
ITEM_DICT = {"surfboard" : 399,
             "wetsuit" : 249,
             "sweater" : 99,
             "fin" : 49,
             "wax" : 14,
             "sticker" : 5}
cart = []
total_cost = []

#Define main user input
def main_prompt():
    item = input("Please input the item you would like to purchase: ").strip().lower()
    return item  #Returns Item for following functions

#Define function that validates if Item is in DICT
def validate_item(item):
    if item in ITEM_DICT:
        return True    #True will then lead to: add_item
    if item not in ITEM_DICT:
        print("That is not a valid item. Please try again.")
        return False

#Define function that appends item to cart + total cost
def add_item(item):
    if True:
        cart.append(item)
        total_cost.append(ITEM_DICT[item])
        print(f"The {item} is ${ITEM_DICT[item]} and has been added to your cart!")

#Define function that prompts another purchase
def continue_prompt():
    while True:
        choice = input("Would you like to add another item? (yes/no): ").lower()
        if choice == "no":
            return False
        elif choice == "yes":
            return True
        else:   #Catches user input error
            print("Sorry, please choose YES or NO.")

#define function that prints the final cart
def final_cart():
    print("-----FINAL CART-----")
    if not cart:
        print("Your cart is empty")
    else:
        for item in cart:
            print(f"{item.upper()} : ${ITEM_DICT[item]}")
        print(f"Total cost: ${sum(total_cost)}")
        print("Thanks for shopping with us!")

#Define main program loop
def main():

    continue_shopping = True

#Prints all available items
    print("Welcome to SC's Surf Shop!")
    print("--------------------------")
    print("AVAILABLE ITEMS:")
    for item, price in ITEM_DICT.items():
        print(f"{item.capitalize()}: ${price}")
    print("--------------------------")

#While loop that loops until the User breaks the program with: "no"
    while continue_shopping:
        item = main_prompt()

        if validate_item(item):
            add_item(item)
            continue_shopping = continue_prompt()
    final_cart()


if __name__ == "__main__":
    main()