# ChatGPT 🛍️ Shopping Cart Simulator - Version #2
# Show menu - Add, Remove, View Cart, Checkout/Quit
# Quantity Management
# Search for items
# .strip().lower() ensures that entires are treated the same
# cart.values() gives you all the items in the dictionary

menu = """🛒 Shopping Cart Menu:
 🔹 1 - Add Item
 🔹 2 - Remove Item
 🔹 3 - View Cart
 🔹 4 - Checkout 🧾
Choose an option: """

cart = {
    "apple": {"qty": 2, "price": 0.99},
    "milk": {"qty": 1, "price": 5.99},
    "banana": {"qty": 5, "price": 0.30},
    }

while True:
    action = input(menu)

    if action == "1":
        item = input("🔹 Item to add: ").strip().lower()

        try:
            qty = int(input("🔹 Quantity: "))
            price = float(input("🔹 Price per item: $"))
        except ValueError:
            print("⚠️ Please enter valid numbers.")
            continue

        if qty <= 0 or price <= 0:
            print("⚠️ Quantity and price must be greater than 0.")
            continue

        if item in cart:
            cart[item]["qty"] += qty # Increase the quantity
            cart[item]["price"] = price
            print(f" ✅ Updated {item}: {cart[item]['qty']} total at ${cart[item]['price']:.2f} each")
        else:
            cart[item] = {"qty": qty, "price": price}
            print(f" ✅ Added {qty} x {item} at ${price:.2f}.")

    elif action == "2":
        item = input(" Item to remove: ").strip().lower()

        if item not in cart:
            print(" ❌ That item is not in your cart.")
            continue

        try:
            qty = int(input(" Quantity: "))
        except ValueError:
            print("⚠️ Please enter a valid quantity.")
            continue

        if qty <=0:
            print("⚠️ Quantity must be greater than 0.")
            continue

        if qty >= cart[item]["qty"]:
            del cart[item]
            print(f"🗑️ Removed all of the {item} from your cart.")
        else:
            cart[item]["qty"] -= qty
            print(f"🗑️ Removed {qty} of {item}. You now have {cart[item]['qty']}.")

    elif action == "3":
        if not cart:
            print("🧺 Your cart is empty.")
            continue

        print("\n🛒✨ Your Shopping Cart ✨")
        print("━" * 50)
        print(f"{'No.':<4} {'Item':<14} {'Qty':>5} {'Price':>10} {'Total':>10}")
        print("━" * 50)

        for i, (item, info) in enumerate(cart.items(), start=1):
            qty = info["qty"]
            price = info["price"]
            total = qty * price
            print(f"{i:<4} {item.capitalize():<14} {qty:>5} {f'${price:.2f}':>10} {f'${total:.2f}':>10}")
        print("━" * 50)

    elif action == "4":
        if not cart:
            print("🧺 Your cart is empty.")
            continue

        total_items = sum(info["qty"] for info in cart.values())
        total_cost = sum(info["qty"] * info["price"] for info in cart.values())

        print("\n🧾✨ Checkout Summary ✨")
        print(f"🧮 Total Items: {total_items}")
        print("━"*50)
        print(f"🔢{'':<3} {'Item':<14} {'Qty':>5} {'Price':>10} {'Total':>10}")
        print("━"*50)

        for i, (item, info) in enumerate(cart.items(), start=1):
            qty = info["qty"]
            price = info["price"]
            total = qty * price
            print(f" {i:<4} {item.capitalize():<14} {qty:>5} {('$' + f'{price:.2f}'):>10} {('$' + f'{total:.2f}'):>10}")

        print("━"*50)
        print(f"🧾 Grand Total: {f'${total_cost:.2f}':>32}")
        print("🛍️ Thank you for shopping with us!")
        break
    else:
        print("Incorrect Choice")
