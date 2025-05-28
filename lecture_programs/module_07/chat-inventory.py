# ChatGPT 🧠 Coding Challenge: Inventory Restocker
inventory = {
    "apple": 4,
    "banana": 12,
    "orange": 9,
    "grapes": 2
}


def print_key(inventory):
    # iterates through keys
    for key in inventory:
        print(key)

def print_value(inventory):
    # iterates through values
    for value in inventory.values():
        print(value)

def print_pairs(invetory):
    # iterates through key-value pairs
    for key, value in inventory.items():
        print(f"Key: {key}, Value: {value}")

def print_inventory(inventory):
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def restock_items(inventory):
    print("--Before Stocking--")
    print_inventory(inventory)
    for item, quantity in inventory.items():
        if inventory[item] < 10:
            inventory[item] = 10
    print("--After Stocking--")
    print_inventory(inventory)
    return inventory





restock_items(inventory)
