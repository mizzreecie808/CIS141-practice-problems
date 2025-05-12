# Reading - Count to 10, While Loops
# https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Count_to_10

# print to 10
# a = 0
# while a < 10:
#     a += 1
#     print(a)

# calculator
# user_input = 1
# total = 0
# print("Enter numbers to add to the sum.")
# print("Enter 0 to quit.")

# while user_input !=0:
#     print(f"Current Sum: {total}")
#     user_input = float(input("Number: "))
#     total += user_input
# print(f"Total Sum: {total}")

# Fibonacci sequence method 1
# 0 1 1 2 3 5 8 13 21 34
# a = 0
# b = 1
# count = 0
# max_count = 20

# while count < max_count:
#     count += 1
#     print(a, end = " ") # this keeps from creating a new line
#     old_a = a           # we need to keep track of "a" since we change it
#     a = b
#     b += old_a
# print() # adds empty new line

# Fibonacci sequence method 2
# a = 0
# b = 1
# count = 0
# max_count = 10  # only half the amount needed

# while count < max_count:
#     count += 1
#     print(a, b, end = " ") # this keeps from creating a new line
#     a += b
#     b += a
# print() # adds empty new line

# Fibonacci sequence method 3
# a = 0
# b = 1
# count = 0
# max_count = 20

# while count < max_count:
#     count += 1
#     old_a = a
#     a += b
#     b = old_a
#     print(old_a, end = " ")
# print()

# Enter password
password = str()

while password != "unicorn":
    password = input("Password: ")
print("Welcome in")
