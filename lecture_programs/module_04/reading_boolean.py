# Reading - Boolean Expressions
# https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Boolean_Expressions

name = "john"
guess = input("What is my name? ")
count = 0

while count < 3 and name != guess.lower():
    print("You are wrong!")
    guess = input("What is my name? ")
    count += 1

if guess.lower() != name:
    print("You are wrong!")
    print("You ran out of chances")
else:
    print(f"Yes! my name is {name}!")
