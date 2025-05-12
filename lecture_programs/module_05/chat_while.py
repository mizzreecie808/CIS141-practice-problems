# ChatGPT ✅ Beginner Exercises for while Loops

# Exercise 1
# n = 0
# while n < 10:
#     n += 1
#     print(n)

# Exercise 2
# n = 2
# while n <= 20:
#     print(n)
#     n += 2

# Exercise 3
# password = "123abc"
# user = input("Enter your password: ")

# while user != password:
#     user = input("Enter your password: ")
# print("You entered the correct password!")

# Exercise 4
# answer = 7
# guess = int(input("Guess a number between 1-10:\n"))

# while guess != answer:
#     print("Sorry, wrong number")
#     guess = int(input("Guess a number between 1-10:\n"))
# print(f"Correct! The answer was {answer}")

# Exercise 5
# import time
# n = 10
# while n > 0:
#     print(n)
#     time.sleep(0.5)
#     n -= 1
# print("Blast off!")

# Exercise 6
# num = "0"
# sum = 0
# print("Enter a number and type (stop) when done")

# while num.lower() != "stop":
#     sum += int(num)
#     num = input("Number: ")
# print(sum)

# total = 0

# while True:
#     user_input = input("Enter a number (or type 'stop' to finish):\t")

#     if user_input.lower() == "stop":
#         break

    #Convert the input to a number
#     try:
#         number = float(user_input)
#         total += number
#     except ValueError:
#         print("That's not a valid number. Try again.")

# print("Total:", total)

# Exercise 7
# import random

# while True:
    # Generate two random numbers between 1 and 10
#     num1 = random.randint(1, 10)
#     num2 = random.randint(1, 10)

    # Ask the question
#     answer = input(f"What is {num1} x {num2}? (type 'exit' to quit)\t")

    # Exit if user types 'exit'
#     if answer.lower() == "exit":
#         print("Thanks for playing!")
#         break

    # Check if the answer is correct
#     try:
#         if int(answer) == num1 * num2:
#             print("Correct!\n")
#         else:
#             print(f"Wrong. The answer was {num1 * num2}.\n")
#     except ValueError:
#         print("Please enter a number or type 'exit' to quit.\n")

# Exercise 8
# while True:
    # As the user if they want to continue
    # only ask once at the top of the loop
#     user_input = input("Do you want to continue?\n")

#     if user_input.lower() == "yes":
        # use continue to go back to the top of the loop
#         continue
#     elif user_input.lower() == "no":
#         print("Goodbye")
#         break
#     else:
#         print("Please answer yes or no")

# Exercise 9
# num = 50
# while num >= 0:
#     print(num)
#     num -= 5

# Exercise 10
# secret = "banana"
# count = 0

# while True:
#     user_input = input("What is the secret word? ")
#     count += 1

#     if user_input.lower() == secret:
#         print(f"You guessed {secret} in {count} guesses. Good job!")
#         break
#     else:
#         print("Try again")
#         continue

# Exercise 11
# total = 0
# print("Enter numbers, type '0' to sum the positive numbers")

# while True:
#     num = float(input("Enter a number: "))

#     if num > 0:
#         total += num
#     elif num < 0:
#         continue
#     else:
#         print(f"The sum of all positive numbers = {total}")
#         break

# Exercise 12
# password = "letmein"
# count = 0

# while True:
#     user_input = input("Enter the password: ")
#     count += 1

#     if user_input == password:
#         print("Access granted")
#         break
#     elif count >= 3:
#         print("Access denied!")
#         break

# Exercise 13
num = 1
count = 0

while num < 1000:
    num *= 2
    count += 1
    print(num)
print(f"It took {count} times for the number to go over 1000")

