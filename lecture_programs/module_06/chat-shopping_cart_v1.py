# ChatGPT 🛍️ Shopping Cart Simulator - Version #1
# Show menu - Add, Remove, View Cart, Checkout/Quit
# Basic

menu = """🛒 Shopping Cart Menu:
 1️⃣  Add Item
 2️⃣  Remove Item
 3️⃣  View Cart
 4️⃣  Checkout 🧾
 Choose and option: """
cart = ["apple", "banana", "cherry"]

while True:
    action = input(menu)

    if action == "1":
        add_item = input(" Item to add: ")
        if add_item in cart:
            print(f" ❌ {add_item} already in cart.")
        else:
            cart.append(add_item)
            print(f" ✅ Added {add_item} to your cart.")

    elif action == "2":
        remove_item = input(" Item to remove: ")
        if remove_item in cart:
            cart.remove(remove_item)
            print(f" ✅ Removed {remove_item} from cart.")
        else:
            print(" ❌ That item is not in your cart.")
    elif action == "3":
        if not cart:
            print("🧺 Your cart is empty.")
        else:
            # use enumerate to print each item in a list
            print("🧺 Your cart contains:")
            for i, item in enumerate(cart):
                print(f"  {i+1}. {item}")
    elif action == "4":
        if not cart:
            print("🛒 Your cart is empty! Nothing to checkout.")
        else:
            print("\n🧾 Time to checkout! Here's your final cart:")
            for i, item in enumerate(cart):
                print(f"  {i+1}. {item}")
            print("🛍️ Thank you for shopping with us!")
            break
    else:
        print("Incorrect Choice")



