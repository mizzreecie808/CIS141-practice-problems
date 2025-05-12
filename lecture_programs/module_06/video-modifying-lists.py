# Modifying Lists
# https://www.youtube.com/watch?v=DBiSYuLMlwY

# ADDING ELEMENTS
# Appending (adds element to END of list)
# my_list = [1, 2, 3]
# print(my_list)
# my_list.append(4)
# print(my_list)

# Insert (inserts an element at a specific position)
# my_list.insert(1, 1.5)
# print(my_list)

# REMOVING ELEMENTS
# Remove (removes the first occurrence of a specific value)
# new_list = [1, 2, 3, "a", "b", "c"]
# print(new_list)
# new_list.remove(2)
# print(new_list)

# Pop (removes an element by index (defaults to last index))
# new_list.pop()
# print(new_list)
# new_list.pop(3)
# print(new_list)

# Del keyword (removes an element at a specific index or a slice)
# del new_list[0]
# print(new_list)
# del new_list[0:3]
# print(new_list)

# CHANGING EXISTING ELEMENTS
# Re-assigning elements by index
ls = ["Olympic","College","Rangers"]
print(ls)
ls[2] = "Warriors"
print(ls)