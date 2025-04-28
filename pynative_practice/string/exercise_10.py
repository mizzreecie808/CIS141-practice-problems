# https://pynative.com/python-string-exercise/
# Exercise 10: Write a program to count occurrences of all characters in string
s1 = "Mississippi"


def count_char(str):
    return {char:str.count(char) for char in str} #    must use {}

print(count_char(s1))

char_dict = dict()
for char in s1:
    count = s1.count(char)
    char_dict[char] = count
print("Result:", char_dict)
