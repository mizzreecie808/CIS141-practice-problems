# Reading - Exercises:
# https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Decisions

# Exercise 1

# name = "Cerise"

# if name == "Cerise":
#     print("That is a nice name")
# elif name == "John Cleese" or name == "Michael Palin":
#     print(f"{name} - this is how I feel about you")
# else:
#     print("You have a nice name.")

# Exercise 2
# number = 7
# guess = -1
# count = 0

# print("Guess the number!")
# while guess != number:
#     guess = int(input("Is it... "))
#     count += 1
#     if guess == number:
#         print("Hooray! You guessed it right!")
#     elif guess < number:
#         print("It's bigger...")
#     elif guess > number:
#         print("It's not so big.")

# if count > 3:
#     print("That must have been complicated")
# else:
#     print("Good job!")

# Exercise 3
num1, num2 = 15, 99

if num1 + num2 > 100:
    print("That is a big number!")
