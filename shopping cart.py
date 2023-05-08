#Using Python and the skills we learned over the past week, 
#create a shopping cart program that will allow a user to add
#and remove items to a shopping cart. The cart should keep 
#track of the quantity and price of each item.  The user 
#should also be able to view the items that are currently in 
#their cart. The user should be able to continue to add to, 
#remove from, and view their cart until the user "quits" or 
#"checks out". When the user quits/checks out, the program 
# should display a receipt showing the items in the cart with 
# quantity and price and the total price.


# create a function that takes name and says "hello name welcome to Spensive Mart"
# create dictionary of groceries to choose from
# create an empty dictionary called shopping_cart
# create a function to add items to a shopping_cart
# create a funciton to view grocery items for sale
# create a function to keep track of quantity in shopping_cart
# create a function to remove items from shopping_cart affecting quantity
# create a function to print items and quantity in shopping_cart
# create a function to quit that removes all items and says thank you come again
# create a fucntion called checkout that prints entire list with tax included in sum
# create a while loop to reinsert all options until user checks out or quits



welcome = input('\nHello, welcome to Spensive Mart. What is your name?')
print(f"\nThank you for choosing Spensive Mart {welcome}. Please make a selction.\n")


item_prices={
    "beef": 14.99,
    "turkey": 12.99,
    "tomato": 2.99,
    "brussel sprouts": 6.99,
    "mini potatoes": 3.99,
    "brown eggs": 18.99,
    "milk": 6.99,
    "red onions": 8.99,
    "halibut": 129.99
}


shopping_cart = {}

def add(item, quantity):
    if item in item_prices:
        if item in shopping_cart:
            shopping_cart[item] += quantity
        else:
            shopping_cart[item] = quantity
        print(f"{quantity} {item} added to cart.")

def delete(item, quantity):
    if item in shopping_cart:
        del shopping_cart[item]
        print(f"{item} removed.")
    else:
        shopping_cart[item] -= quantity
        print(f"Removed {quantity} {item} from the shopping cart.")
            
def view():
    print("Items currently in the shopping cart:")
    for item, quantity in shopping_cart.items():
        price = item_prices[item]
        total_price = price * quantity
        print(f"{item} (Quantity: {quantity}, Price: ${price}, Total: ${total_price})")

def checkout():
    total_price = 0
    for item, quantity in shopping_cart.items():
        price = item_prices[item] 
        total_price += price * quantity + (price*.07)
        print(f"{item} (Quantity: {quantity}, Price: ${price}, Total: ${price * quantity})")
    print("Thank you for choosing Spensive Mart. Your total w/ tax is")
    print(f"Total: ${total_price}")
    shopping_cart.clear()


while True:
    print("1 ----- Add ------")
    print("2 ---- Delete -----")
    print("3 --- Your Cart ---")
    print("4 --- Checkout ----")
    print("5 ----- Quit ------\n")
    
    selection = input("Select a number:")
    
    if selection == "1":
        print(item_prices)
        item = input("\nWhich item would you like to add?:")
        quantity = int(input("\nHow many?:"))
        add(item, quantity)
    elif selection == "2":
        item = input("\nType the item to delete: ")
        quantity = int(input("\nEnter the quantity: "))
        delete(item, quantity)
    elif selection == "3":
        view()
    elif selection == "4":
        checkout()
        break
    elif selection == "5":
        print("\nThank you come again!")
        break
    