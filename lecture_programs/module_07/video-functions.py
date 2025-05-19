# FUNCTIONS
# https://www.youtube.com/watch?v=Pt58lz0fUYw
# Input goes in, output comes out

# Defining a function, reusable
def greet(name):
    print(f"Hello, {name}")
    return f"Hello, {name}"

# Calling a function
# greet("Lindsey")
# greet("Sean")
# greet("Kevin")

# Return Values
greeting = greet("Lindsey")
print(greeting)

# Math function
def add(num1, num2):
    return num1 + num2

output = add(5, 6)
print(output)
