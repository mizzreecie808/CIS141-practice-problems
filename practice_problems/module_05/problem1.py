# Problem #1
# Prompt the user for a positive integer n.
# Use a while loop to sum all the integers from 1 up to n.
# Print the final sum.

n = int(input("Enter any positive integer: "))
sum = 0
count = 1

while count <= n:
    sum += count
    count += 1
print(f"Sum of all integers from 1 to {n} = {sum}")
