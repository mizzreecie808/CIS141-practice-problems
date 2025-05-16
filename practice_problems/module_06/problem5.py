# Module 06 - Problem #5
# Create a list of integers.
# Use a loop to build a new list where each element is the square
# of the corresponding element in the original list.
# Print the new list.
numbers = [3, 12, 7, 18, 5, 14, 9, 1, 20, 6]
square_nums = []

i = 0
while len(square_nums) < len(numbers):
    square_nums.append(numbers[i] ** 2)
    i += 1

print(numbers)
print(square_nums)

