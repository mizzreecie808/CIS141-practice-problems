# ChatGPT 🔁 Basic List Operations Exercises
# Exercise 1 - Accessing List ItemsView
# Print the first and last items in the list using indexing
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])  # First item
print(fruits[-1]) # Last item

# Exercise 2 - Appending to a List
# Append "green" and "yellow" to the list and print it
colors = ["red", "blue"]
colors.append("green")
colors.append("yellow")
print(colors)

# Exercise 3 - Deleting an items
# Delete "rabbit" from the list using the del statement
# Print the updated list
animals = ["cat", "dog", "rabbit", "hamster"]
del animals[2]
print(animals)

# Exercise 4 - Using pop()
numbers = [10, 20, 30, 40, 50]
# Use pop() to remove the last item and print the result
# Then use pop(1) to remove the second item
last_item = numbers.pop()
second_item = numbers.pop(1)
print(f"Popped last item: {last_item}")
print(f"Popped second item: {second_item}")

# Exercise 5 - Index Replacement
# Replace "Tokyo" with "Berlin"
cities = ["New York", "Paris", "Tokyo", "London"]
cities[2] = "Berlin"
print(cities)

# Exercise 6 - Create a List from InputDevice
# Ask the user to input 3 of their favorite foods and store them in a list.
# Then print the list.
# foods = []
# for i in range(3):
#     food = input(f"Enter favorite food #{i + 1}: ")
#     foods.append(food)
# print(foods)

# Exercise 7 - Combine Two Lists
# Combine them into one list and print the result.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# for i in range(len(list2)):
#     list1.append(list2[i])
# print(list1)

# Alternative 1 (cleaner)
combined = list1 + list2
print(combined)

# Alternative 2 (in-place)
list1.extend(list2)
print(list1)

# Exercise 8 - Find the Length of a List
# Print how many books are in the list using len()
books = ["1984", "Moby Dick", "Hamlet"]
print(len(books))

# Exercise 9 - Check if an Item is in the List
# Check if "drill" is in the list and print a message accordingly
tools = ["hammer", "screwdriver", "wrench"]
if "drill" in tools:
    print("Drill in list of tools.")
else:
    print("Drill is not in list of tools")

# Exercise 10 - Remove All Items Using a Loop
# Use a while loop and pop() to remove all elements one by one
# Print the list after each pop
letters = ["a", "b", "c", "d"]

while len(letters) > 0:
    letters.pop()
    print(letters)


