# More Practice Problems
# https://www.youtube.com/watch?v=ZyWbdMeN3oA

# Problem 1: Write a while loop that sums numbers from 1 to 50.
# counter = 1
# total = 0

# while counter < 51:
#     total += counter
#     print(f"counter = {counter}; sum = {total}")
#     counter += 1
# print(f"sum = {total}")

# Problem 2: Write a for loop that prints the even numbers from 1 to 20,
# but skip printing 10 using continue.
# for i in range(1, 21):
#     if i % 2 != 0 or i == 10:
#         continue
#     print(f"i = {i}")

# Problem 3: Write a program that creates a pyramid of asterisks (stars)
# For each row in the pyramid, you use one loop to print the required number
# of spaces and another loop to print the required number of asterisks.
# Output should look like:
#    *      Row 1: 4 spaces, 1 asterisk
#   ***     Row 2: 3 spaces, 3 asterisks
#  *****    Row 3: 2 spaces, 5 asterisks
# *******   Row 4: 1 space,  7 asterisks
#*********  Row 5: 0 spaces, 9 asterisks

row = 3

for i in range(row):                # 0, 1, 2, 3, 4
    # loop for creating spaces
    for j in range(row - 1 - i):
        print(" ", end = "")
    # loop for creating asterisks
    for k in range(1 + (2 * i)):
        print("*", end = "")
    # print new line
    print()
