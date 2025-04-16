'''
Problem #2
Prompt the user for their name and their age.
Calculate their age next year.
Use string concatenation to print
"Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."
'''

# prompt user for name and age
name = input("What is your name?  ")
age = int(input("How old are you?  "))

# calculate their age next year
next_year = age + 1

# concatenation
statement = "Hello, " + name + "! you are " + str(age) + " years old. Next year, you will be " + str(next_year) + " years old."
print(statement)

# f-string allow variables to be embedded into expressions
print(f"Hello, {name}! You are {age} years old. Next year, you will be {next_year} years old.")

# .format() - not from course videos
result = "Hello, {}! You are {} years old. Next year, you will be {} years old.".format(name, age, next_year)
print(result)
