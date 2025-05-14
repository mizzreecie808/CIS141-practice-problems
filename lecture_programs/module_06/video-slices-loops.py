# Slicing and Looping thru Lists
# https://www.youtube.com/watch?v=8JWMAasAFVQ

# Slicing - never includes the ending index (not inclusive)
shopping_list = ["potatoes","grapes","cuties","eggs","bread","mushrooms"]
# print(shopping_list[1:3]) # grapes, cuties - start and end
# print(shopping_list[:3]) # potatoes grapes, cuties - just the end
# print(shopping_list[3:]) # eggs, bread, mushrooms - only the start
# print(shopping_list[0:5:2]) # every other element on list

# Looping
# For ... in loop
# for element in shopping_list:
#     print(element)

# Using range() when you need indices
# for i in range(len(shopping_list)): # 0, 1, 2, 3, 4, 5
#     print(f"shopping_list[{i}] = {shopping_list[i]}")

# Exercise
names = ["Alice", "Bob", "Charlie"]
# loop that goes through each persons name and creates a greeting to them
for name in names:
    print(f"Greetings {name}, Have a Wonderful Day!")

for name in range(len(names)):
    print(f"Greetings {names[name]}, Have a Great Day!")
