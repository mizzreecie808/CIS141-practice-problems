# https://pynative.com/python-string-exercise/
# Exercise 2: Append new string in the middle of a given string
str1 = "Ault"
str2 = "Kelly"

middle = int(len(str1) / 2)
str3 = str1[:middle] + str2 + str1[middle:]
print(str3)

def append_middle(s1, s2):
    print(f"Original Strings are: \"{s1}\" and \"{s2}\"")

    mid = int(len(s1) / 2)

    result = s1[:mid] + s2 + s1[mid:]
    print(f"After appending new string in the middle: {result}")

append_middle(str1, str2)
