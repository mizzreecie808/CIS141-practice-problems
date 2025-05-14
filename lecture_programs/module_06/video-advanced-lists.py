# Advanced List Operations
# https://www.youtube.com/watch?v=f8785kimbL4
numbers = [5, 2, 9, 1, 8, 4, 3, 2, 7, 3]
edibles = ["broccoli","apple","lettuce","cucumber","tomato","raspberry","onion","dill","basil"]

# .sort() - changes list in place MUTATES the existing list
# numbers.sort()  # ascending
# print(numbers)
# numbers.sort(reverse = True)
# print(numbers)  # decending
# edibles.sort()  # alphabetical
# print(edibles)

# sorted() - leaves original list unchanged, returns new list
# if you want the old list and a new list
# sorted_numbers = sorted(numbers)
# print(numbers)
# print(sorted_numbers)

# .reverse() - changes list in place MUTATES the existing list
# print(numbers)
# numbers.reverse()
# print(numbers)
# print(edibles)
# edibles.sort()
# print(edibles)
# edibles.reverse()
# print(edibles)

# min(), max(), sum() - Standalone function, must past variable in
# print(f"min = {min(numbers)}")
# print(f"max = {max(numbers)}")
# print(f"sum = {sum(numbers)}")

# .index() - index searching
tom = edibles.index("cauliflower")
print(tom)
