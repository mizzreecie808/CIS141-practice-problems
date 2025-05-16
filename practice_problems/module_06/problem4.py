# Module 06 - Problem #4
# Create a list of integers.
# Write code that counts how many numbers are positive and how many are negative,
# then print both counts.
numbers = [23, 49, 91, 16, 37, 62, 75, 83, 54, 9]

count_odd = 0
count_even = 0

for num in numbers:
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"Total odd numbers:\t{count_odd}")
print(f"Total even numbers:\t{count_even}")
