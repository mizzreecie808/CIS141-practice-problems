# Accessing & Slicing Strings & Comparison
# https://www.youtube.com/watch?v=rAKkI-4Op1E

# Indexing, including out of range errors
str = "Olympic College Rangers"
print(str[10])

length = len(str) - 1
print(str[length])

# Slicing & Stepping - Substring
# Choose starting number and the ending number + 1
slice = str[0:7]
print(slice)

slice2 = str[:7]
print(slice2)

end = str[16:]
print(end)

stepping = str[::3] #prints every nth character
print(stepping)

# String Comparison
print("olympic" == "olympic") # True
print("Olympic" == "olympic") # False
print("Olympic" != "olympic") # True
