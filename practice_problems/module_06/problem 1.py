# Module 06 - Problem #1
# Create a list of integers (you get to pick!).
# Write code to iterate through the list and calculate the sum of all even numbers.
# Print the resulting sum.

numbers = [10, 34, 38, 11, 11, 45, 28, 17, 7, 9, 10, 30]
total_evens = 0

for num in numbers:
    if num % 2 == 0:
        total_evens += num
print(f"Sum of all even numbers = {total_evens}")
