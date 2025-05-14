# ChatGPT 🔁 Basic List Operations Exercises
# Exercise 11 - Insert at a Specific Index
# animals = ["bear", "cat", "llama", "horse", "giraffe"]
# print(animals)
# animals.insert(2, "fox")
# print(animals)

# Exercise 12 - Count Occurrences
# fruits = ["apple", "banana", "apple", "cherry", "apple"]
# count = 0
# for fruit in fruits:
#     if fruit == "apple":
#         count += 1
# print(f"Count of apples = {count}")
# print(fruits.count("apple"))  # built-in count method

# Exercise 13 - Reverse a List
# colors = ["red", "green", "blue"]
# print(colors)
# colors.reverse()
# print(colors)
# colors[::-1]  # more advanced

# Exercise 14 - Sort Numbers
# numbers = [5, 3, 8, 1, 2]
# print(numbers)
# numbers.sort()
# print(numbers)
# nums_sort = sorted(numbers)   # keeps original list unchanged

# Exercise 15 - Loop and Double
# nums = [2, 4, 6, 8]
# doubled = [0] * len(nums)

# for i in range(len(nums)):
#     print(f"nums[{i}] = {nums[i]}")
#     doubled[i] = nums[i] * 2
# print(doubled)

# Exercise 16 - Find the Minimum
# temperatures = [72, 68, 75, 70, 66]
# min_temp = min(temperatures)
# print(min_temp)

# Exercise 17 - Find the Maximum
# scores = [85, 92, 78, 90]
# max_score = max(scores)
# print(max_score)

# Exercise 18 - Calculate the Sum
# prices = [10.99, 5.99, 3.49, 12.99]
# total = sum(prices)
# print(f"Total = ${total:.2f}")

# Exercise 19 - Find the Index of an Item
# fruits = ["apple", "banana", "cherry", "banana"]
# print(fruits.index("banana"))

# Exercise 20 - Combine Everything
numbers = [5, 3, 8, 1, 2]
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(numbers.index(max(numbers)))

