# Practice Problems with Booleans
# https://www.youtube.com/watch?v=o5AXVDb28Sk

# What do the folwing Boolean expressions evalute to:
# (5 > 3) and (2 == 2) # True & True = True

# ("apple" == "pie") or (24 > 6) # False & True = True

# not (-6 < 0) # not True = False

# Write an if-else that checks if a number is positive or negative
# Step 1 - Get input from user
# num = int(input("What number would you like to check?: "))

# Step 2 - Check if number is positive (greater than 0)
# Step 2a - if number is positive, print positive message
# if num > 0:
#     print(f"{num} is a positive number")

# Step 2b - if number is negative, print negative message
# else:
#     print(f"{num} is a negative number")

# Write a program that asks for a persons age & drivers license b4 alcohol
# Step 1 - Request users age
age = int(input("How old are you? "))
# Step 2 - Request whether user has driver license
license = input("Do you have a driver's license (Yes/No)? ")

if (age >= 21) and (license.lower() == "yes"):
    print("You are over 21 and have a license")
else:
    print("You cannot get alcohol")
