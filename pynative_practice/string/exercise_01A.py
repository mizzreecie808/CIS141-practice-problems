'''
Exercise 1A:
Create a string made of the first, middle and last character
'''
str = "Pynative"
result = str[0]
print(result)

middle = int(len(str) / 2)
result = result + str[middle]
print(result)

last = len(str) - 1
result = result + str[last]
print(result)
