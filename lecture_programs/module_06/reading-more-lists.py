# Reading - More on Lists
# https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/More_on_Lists

some_numbers = ["zero", "one", "two", "three", "four", "five"]

# Accessing lists Forward
# for i in range(len(some_numbers)):
#     print(f"somenumbers[{i}] = {some_numbers[i]}")

# Accessing lists Backward
# Use range with Negative Step
# for i in range(len(some_numbers) - 1, -1, -1):
#     print(f"somenumbers[{-i}] = {some_numbers[i]}")

things = [0, 'Fred', 2, 'S.P.A.M.', 'Stocking', 42, "Jack", "Jill"]
# print("---Slicing---")
# print("things[first_index:last_index] - excludes last_index")
# print(things[2:4])
# print(things[-4:-2])
# print(things[:2])
# print(things[-2:])
# print(things[:-5])

# Copying Lists
# b makes reference to a, so any modifications to b will modify a
a = [1, 2, 3]
# b = a
# print(a)
# print(b)
# b[1] = 10
# print(a)
# print(b)

# b is not a direct reference to a, it creates a new list called a * 2
# modifications to a will not affect b
# b = a * 2
# print(a)
# print(b)
# a[1] = 10
# print(a)
# print(b)

# creating an actual copy of a list
c = [4, 5, 6]
d = c[:]
print(c)
print(d)
d[1] = 10
print(c)
print(d)
