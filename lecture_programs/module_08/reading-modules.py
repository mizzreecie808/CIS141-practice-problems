# Reading - Using Modules
# https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Using_Modules

# import calendar
# year = int(input("Type in the year number: "))
# calendar.prcal(year)

# infinite output as seconds pass
# from time import time, ctime
# prev_time = ""
# while True:
#     the_time = ctime(time())
#     if prev_time != the_time:
#         print("The time is:", ctime(time()))
#         prev_time = the_time

# Plays the guessing game higher or lower
# import random
# pc_number = random.randint(0, 99)
# guess = -1
# print(pc_number)

# print("Guess the number!")
# while guess != pc_number:
#     guess = int(input("Is it... "))

#     if guess == pc_number:
#         print("Hooray! You guessed it right!")
#     elif guess < pc_number:
#         print("It's bigger...")
#     elif guess > pc_number:
#         print("It's not so big.")

import greetings

statement = greetings.say_hello("Cerise")
print(statement)
