# More Practice Problems

# Problem 1: Write a while loop that sums numbers from 1 to 50.
#counter = 1
#sum = 0
#while counter <= 50:
#    sum += counter
    #print("counter = ", counter, "; sum = ", sum)
#    counter += 1
#print(sum)

# Problem 2: Write a for loop that prints the even numbers from 1 to 20, but skip printing 10 using continue.
#for i in range(1,21): #1 ... 20
#    if i == 10:
#        continue
#    if i % 2 == 0: #Really awesome way to test if number is even
#        print(i)


# Problem 3: Write a program that creates a pyramid of asterisks (stars) to the console.
# For each row in the pyramid, you use one loop to print the required number of spaces and another loop to
# print the required number of asterisks.
# Output should look like:
#    *      Row 1: 4 spaces, 1 asterisk
#   ***     Row 2: 3 spaces, 3 asterisks
#  *****    Row 3: 2 spaces, 5 asterisks
# *******   Row 4: 1 space,  7 asterisks
#*********  Row 5: 0 spaces, 9 asterisks

row = 3
for i in range(row): #0,1,2,3,4
    # Loop for creating spaces
    for _ in range(row - 1 - i):
        print("_", end="")
    # Loop for creating asterisks
    for _ in range(1 + (2 * i)):
        print("*", end="")
    # Print a new line
    print("")
