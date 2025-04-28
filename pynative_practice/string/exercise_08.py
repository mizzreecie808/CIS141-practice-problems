# https://pynative.com/python-string-exercise/
# Exercise 8: Find all occurrences of a substring in a given string
# by ignoring case
s1 = "Welcome to USA. usa awesome, isn't it?"
s2 = "USA"

# make both strings lower
s1_lower = s1.lower()
s2_lower = s2.lower()

count = s1_lower.count(s2_lower)

print(f"The {s2} count is: {count}")
