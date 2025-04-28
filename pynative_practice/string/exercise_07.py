# https://pynative.com/python-string-exercise/
# Exercise 7: String characters balance Test
# Are all letters in s1 in s2
s1 = "Ynx"
s2 = "PYnative"

# set flag
flag = True

# iterate string
for char in s1:
    if char in s2:
        continue
    else:
        flag = False

print(flag)
