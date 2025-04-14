'''
Module #2 Problem #4
Create a program that:
Prompts the user for their birth year
Displays a message that says
"You are ___ old". Use an f-string in your solution to this problem.
'''

birth_year = input("What is your birth year? ")
age = 2025 - int(birth_year)

# f-string to print solution
print(f"You are {age} years old.")
