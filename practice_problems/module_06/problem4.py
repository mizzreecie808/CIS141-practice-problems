# Module 06 - Problem #4
# Create a list of integers.
# Write code that counts how many numbers are positive and how many are negative,
# then print both counts.
numbers = [-12, 7, -3, 18, -25, -8, 14, -1, 5, -19, 10]


count_neg = 0
count_pos = 0

for num in numbers:
    if num >= 0:
        count_pos += 1
    else:
        count_neg += 1

print(f"Total negative numbers:\t{count_neg}")
print(f"Total positive numbers:\t{count_pos}")
print(f"Numbers in list:\t\t{len(numbers)}")
