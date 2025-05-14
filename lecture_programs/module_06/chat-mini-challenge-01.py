# ChatGPT 🧠 Mini Challenge #1: Backpack Inventory
# Create an empty list called backpack.
# Ask the user to add 3 items to their backpack using input() and append().
# Print the contents of the backpack.
# Ask the user what item they want to remove from the backpack.
# If it’s in the list, remove it using pop() or remove().
# If it’s not in the list, print a message that it wasn't found.
# Finally, empty the backpack using a while loop and print the contents
# after each removal.
backpack = []
for i in range(3):
    item = input(f"Item #{i + 1}: ")
    backpack.append(item)
print(backpack)

remove_item = input("What would you like to remove: ")

if remove_item in backpack:
    backpack.remove(remove_item)
    print("Current backpack contents:", backpack)
else:
    print("Item not in backpack")

while len(backpack) > 0:
    pop_item = backpack.pop()
    print(f"{pop_item} was removed from backpack")

if not backpack:
    print("Backpack is now empty!")
