# Chat 🧪 No-Input Dictionary Practice Problems
# 1. Fruit Stock Checker 🍎🍌🍊🥝
# Print all fruit names, Print Total stock, Print fruits with stock < 5
fruit_stock = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "kiwi": 2
}

def fruit_checker(fruit_dict):
    low_stock = {}
    max_fruit = ("", 0)
    total_stock = sum(fruit_stock.values())
    stock_status = {}

    # iterate through keys and values using .items()
    for fruit, qty in fruit_dict.items():
        if qty == 0:
            stock_status[fruit] = "Out of Stock"
        elif 1 <= qty < 5:
            low_stock[fruit] = qty
            stock_status[fruit] = "Low Stock"
        else:
            stock_status[fruit] = "In Stock"

    for fruit, qty in fruit_dict.items():
        if qty > max_fruit[1]:
            max_fruit = (fruit, qty)

    # this sorts it then converts it back to a dictionary
    sorted_dict = dict(sorted(fruit_dict.items(), key=lambda item: item[1]))

    print("🍎📊 Fruit Inventory Report 📊🍎")
    print("=" * 35)
    print(f"{'Fruit':<10} {'Qty':<5} {'Status':<15}")
    print("-" * 35)
    for fruit in sorted_dict:
        qty = fruit_dict[fruit]
        status = stock_status[fruit]
        print(f"{fruit:<10} {qty:<5} {status:<15}")
    print("=" * 35)
    print(f"Total Fruit:\t{total_stock}")
    print(f"Max Fruit:\t{max_fruit[0]} ({max_fruit[1]})")
    print(f"Low Stock:\t{low_stock}")

    return low_stock, max_fruit, total_stock, sorted_dict

fruit_checker(fruit_stock)
