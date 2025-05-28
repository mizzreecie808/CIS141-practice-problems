# Scope (Local vs. global)
# https://www.youtube.com/watch?v=EzG5Vh9L_Qs
# Scope refers to area of a program where a particular variable can be accessed
# Pass by value: Pass an argument to a function. Sends a copy of that value, so
# changes made to that parameter inside the function do not affect original variable.
# Pass by Reference: Pass an argument to a function. Sends a reference to the
# original variable, therefore modifying parameter inside function changes the
# variable since they both point to the same memory location

# x = 10 #global variable
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

# numbers = [1, 2, 3]
# modify_list(numbers)
# print(numbers)

# https://www.youtube.com/watch?v=38uGbVYICwg
# First indent is global
# Nonlocal
# x = 1
# def foo():
#     searches for variables local first, then global
#     if you use global keyword, it will change
#     global x
#     x = 2
#     y = 12
#     print(f"foo sees x equal to {x}")
#     print(f"foo sees y equal to {y}")
# foo()
# print(f"global sees x equal to {x}")

x = 1
def outer():
    x = 2
    def inner():
        # changes the nonlocal variable x, one step above, not the global
        nonlocal x
        x = 3
        print(f"inner sees x equal to {x}")
        return
    inner()
    print(f"outer sees x equal to {x}")
    return

outer()
print(f"global sees x equal to {x}")
