# ChatGPT
# 1) 📄 print shopping list
def show_list(name):
    print("🛒 Shopping List:")
    with open(name, "r") as file:
        for line in file:
            print(line.strip())

# 2) ➕ add items
def add_items(name, items):
    with open(name, "a") as file:
        for item in items:
            file.write(f"{item}\n")
    print("➕ Items added to shopping list!")

# 3) 🔤 sort items alphabetically
def sort_file(name):
    with open(name, "r") as file:
        items = [line.strip() for line in file]

    items.sort()

    with open(name, "w") as file:
        for item in items:
            file.write(f"{item}\n")

    print("🔤 Shopping list sorted!")
    with open(name, "r") as file:
        for line in file:
            print(line.strip())

# 4) ✅ remove duplicates
def duplicate_remover(name):
    with open(name, "r") as file:
        items = [line.strip() for line in file]

    # remove duplicates: to keep original order, use dictionary
    items = list(dict.fromkeys(items))

    with open(name, "w") as file:
        for item in items:
            file.write(f"{item}\n")

    print("✅ Duplicates removed!")
    with open(name, "r") as file:
        for line in file:
            print(line.strip())

# 5) ❌ delete items
def delete_item(name, remove_item):
    with open(name, "r") as file:
        items = [line.strip() for line in file]

    if remove_item in items:
        items.remove(remove_item)
        print(f"❌ Removed: {remove_item}")
    else:
        print(f"{remove_item.capitalize()} not found.")

    with open(name, "w") as file:
        for item in items:
            file.write(f"{item}\n")

def main():
    file_name = "shopping_list.txt"

    while True:
        print("\n🛒 Shopping List Manager")
        print("1. Show list")
        print("2. Add items")
        print("3. Sort list")
        print("4. Remove duplicates")
        print("5. Delete an item")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_list(file_name)
        elif choice == "2":
            items_to_add = ["cheese", "juice", "chicken"]
            add_items(file_name, items_to_add)
        elif choice == "3":
            sort_file(file_name)
        elif choice == "4":
            duplicate_remover(file_name)
        elif choice == "5":
            remove_this = "eggs"
            delete_item(file_name, remove_this)
        elif choice == "6":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
