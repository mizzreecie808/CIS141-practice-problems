# Scope (Local vs. global)
# https://www.youtube.com/watch?v=EzG5Vh9L_Qs

x = 10 #global variable
def my_function():
    x = 5   # local variable, only accessed in this function
    y = 2   # local variable, only accessed in this function
#     print(f"Inside function\t x = {x}")

# my_function()
# print(f"Outside function\t x = {x}")
# print(y) <--- error, only defined in function

# Pass by Value (immutable objects: int, float, str)
def modify(n):
    n = 10  # This creates a new local variable 'n'
    print(f"Inside function:\t{n}")

num = 5
# modify(num)
# print(f"Outside function:\t{num}")  # Still 5, because int are immutable

# Pass by Reference (mutable objects: list, dictionaries)
def modify_list(lst):
    lst.append(4)   # Modifies original list

numbers = [1, 2, 3]
modify_list(numbers)
print(numbers)
